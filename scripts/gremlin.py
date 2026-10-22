#!/usr/bin/env python3
"""
Chaos Gremlin - a tiny, stdlib-only silliness engine for Muse.

Summon it when a human needs a dramatic decision, a heroic excuse,
a bite-size side quest, an over-the-top compliment, or a fortune
that is almost certainly not legally binding.

Usage:
    python3 gremlin.py decide "tea" "coffee" "regret"
    python3 gremlin.py excuse --context work --severity dramatic
    python3 gremlin.py quest --minutes 10
    python3 gremlin.py compliment --name NAME --style pirate
    python3 gremlin.py fortune --mood cursed
    python3 gremlin.py --help

Add --seed 42 for reproducible chaos, and --format json when another
program (hello, Muse) wants to present the result itself.
"""

from __future__ import annotations

import argparse
import json
import random
import sys

# ---------------------------------------------------------------------------
# The sacred vaults of nonsense
# ---------------------------------------------------------------------------

DECISION_OPENINGS = [
    "The Gremlin Court is now in session. Please remove your serious hats.",
    "A tiny gavel bangs. Somewhere, a kazoo plays the national anthem of indecision.",
    "The options have been summoned. They look nervous. Good.",
    "Ancient ritual commenced: one part logic, nine parts vibes.",
]

DECISION_ARGUMENTS = [
    "it has undeniable main-character energy",
    "the vibes were, frankly, immaculate",
    "it would make a far better story at dinner",
    "future-you is already high-fiving present-you about it",
    "it is the option least likely to be haunted",
    "the gremlin jury deliberated for 0.4 seconds and felt things",
    "it sparkles in a way the others simply do not",
    "science cannot explain it, and the gremlin respects that",
]

DECISION_VERDICTS = [
    "Case closed. No appeals, unless snacks are offered.",
    "So it is written, so it shall be done, probably after a biscuit.",
    "The court advises committing fully and blaming the gremlin if needed.",
    "Go forth. Be decisive. Be slightly feral about it.",
]

EXCUSES = {
    "work": [
        "I was trapped in a meeting with my own calendar and it won",
        "my laptop staged a dramatic faint and required emotional support",
        "I attempted to be early and accidentally time-travelled past it",
        "a rogue update restarted everything, including my motivation",
        "I was abducted by a spreadsheet with no exit strategy",
    ],
    "social": [
        "my houseplant confessed it needed me and I could not abandon it",
        "I put on going-out clothes and my soul filed a formal objection",
        "the moon was in a mood and advised me, personally, to stay in",
        "I opened the front door, the weather looked at me, we both agreed no",
        "my social battery is not low, it is in another castle",
    ],
    "chores": [
        "the dishes have formed a union and negotiations are ongoing",
        "I cleaned in spirit, which the gremlin counts as cardio",
        "a spider has claimed that corner and legally it is theirs now",
        "I was about to start, then I remembered I am mortal and sat down",
        "the vacuum looked at me like I had disappointed its ancestors",
    ],
    "general": [
        "a wizard did it, and frankly I did not want to escalate",
        "Mercury is in retrograde, probably, and so am I",
        "I followed a tutorial and ended up in a different hobby entirely",
        "the gremlin ate my plan and left only this excellent excuse",
        "I was busy preventing a much worse, invisible disaster",
    ],
}

EXCUSE_SEVERITY = {
    "plausible": "Honestly? Fair enough.",
    "dramatic": "Delivered, ideally, while clutching the furniture for support.",
    "unhinged": "Say it with total confidence and do not break eye contact.",
}

QUESTS = [
    ("Find the oldest thing in your kitchen and give it a formal title",
     "Bonus point if you bow while naming it."),
    ("Rate five objects near you out of ten, out loud, like a wine critic",
     "Use the words 'notes of dust' at least once."),
    ("Walk to the furthest room and back as if you are on a catwalk",
     "No audience is not an excuse. The walls are watching."),
    ("Write a two-line epic poem about the nearest mug",
     "It must contain the word 'destiny'."),
    ("Balance a spoon on your nose or, failing that, on a table with intent",
     "Intent counts. The gremlin is lenient and easily impressed."),
    ("Compliment a piece of furniture as if it just won an award",
     "Thank it for its years of silent service."),
    ("Make the fanciest drink your kitchen allows and name it after yourself",
     "Serve it in the best glass. You are royalty now."),
    ("Find something blue and invent its tragic backstory in 30 seconds",
     "Keep it light. The blue thing has been through enough."),
    ("Do your next small task while narrating it like a nature documentary",
     "David Attenborough voice is encouraged but not required."),
    ("Pick a song and have a one-song dance break, seated dancing counts",
     "Commit to the chorus. That is where the magic lives."),
]

COMPLIMENTS = {
    "classic": [
        "{name}, you have the energy of someone who would survive a montage and look good doing it",
        "If competence had a face, {name}, it would ask you for tips",
        "{name}, you are proof that chaos and excellence can share a flat",
    ],
    "pirate": [
        "Arrr, {name}, ye be the treasure the map was too shy to mention",
        "Captain {name}, ships turn around just to salute ye",
        "{name}, even the sea calms down to listen when ye speak",
    ],
    "shakespeare": [
        "{name}, thou art more lovely and more temperate than this meeting",
        "O {name}, thy wit doth make the stars apply for lessons",
        "Good {name}, if charms were currency, thou wouldst own the realm",
    ],
    "hype": [
        "LET'S GO, {name}! Undefeated. Unmatched. Slightly intimidating to mediocrity itself",
        "{name} does not enter a room, the room levels up",
        "BREAKING: {name} continues to be an absolute problem for low expectations",
    ],
}

FORTUNES = {
    "blessed": [
        "A small good thing is on its way and it is bringing a friend",
        "You will soon be thanked for something you barely remember doing",
        "An excellent snack is closer than you think. Trust the process",
        "Someone is about to laugh at your joke at exactly the right volume",
    ],
    "cursed": [
        "You will step on something wet while wearing socks. Forewarned is forearmed",
        "A cable you need will be one centimetre too short. Breathe",
        "You shall say 'you too' when a waiter says 'enjoy your meal'. It will haunt you briefly",
        "Your next sneeze will be interrupted. The gremlin apologises in advance",
    ],
    "chaotic": [
        "You will make a decision so quickly it surprises even you, and it will work out",
        "Expect an unexpected compliment from an unexpected direction on an ordinary day",
        "A door you thought was locked was simply a push, not a pull. Metaphorically. Probably",
        "You will find money, a memory, or a really good pen in a pocket soon",
    ],
}


# ---------------------------------------------------------------------------
# Chaos, but make it a function
# ---------------------------------------------------------------------------

def pick(rng: random.Random, items):
    return rng.choice(items)


def do_decide(rng: random.Random, options: list[str]) -> dict:
    if len(options) < 2:
        raise SystemExit("decide needs at least two options to argue about.")
    winner = pick(rng, options)
    losers = [o for o in options if o != winner]
    argument = pick(rng, DECISION_ARGUMENTS)
    return {
        "mode": "decide",
        "title": pick(rng, DECISION_OPENINGS),
        "winner": winner,
        "body": f"The court finds in favour of '{winner}', because {argument}.",
        "extra": f"Honourable mentions to {', '.join(losers)} for showing up. "
                 + pick(rng, DECISION_VERDICTS),
    }


def do_excuse(rng: random.Random, context: str, severity: str) -> dict:
    excuse = pick(rng, EXCUSES[context])
    return {
        "mode": "excuse",
        "title": "Your heroic excuse, as certified by the gremlin",
        "winner": excuse,
        "body": f"Simply say: \"Sorry, {excuse}.\"",
        "extra": EXCUSE_SEVERITY[severity],
    }


def do_quest(rng: random.Random, minutes: int) -> dict:
    quest, bonus = pick(rng, QUESTS)
    return {
        "mode": "quest",
        "title": f"A side quest, completable in about {minutes} minutes",
        "winner": quest,
        "body": quest + ".",
        "extra": bonus,
    }


def do_compliment(rng: random.Random, name: str, style: str) -> dict:
    line = pick(rng, COMPLIMENTS[style]).format(name=name)
    return {
        "mode": "compliment",
        "title": "A compliment, delivered at unnecessary volume",
        "winner": line,
        "body": line + ".",
        "extra": "No take-backs. It is on the record now.",
    }


def do_fortune(rng: random.Random, mood: str) -> dict:
    line = pick(rng, FORTUNES[mood])
    return {
        "mode": "fortune",
        "title": f"A {mood} fortune, legally non-binding",
        "winner": line,
        "body": line + ".",
        "extra": "The gremlin accepts no responsibility, only applause.",
    }


def render_text(result: dict) -> str:
    return f"{result['title']}\n\n{result['body']}\n\n{result['extra']}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gremlin",
        description="Chaos Gremlin: dramatic decisions, excuses, quests, "
                    "compliments and fortunes.",
    )
    parser.add_argument("--seed", type=int, default=None,
                        help="Seed for reproducible chaos.")
    parser.add_argument("--format", choices=["text", "json"], default="text",
                        help="Output format. Use json when Muse is presenting.")

    sub = parser.add_subparsers(dest="mode", required=True)

    p = sub.add_parser("decide", help="Hold a tiny trial between options.")
    p.add_argument("options", nargs="+", help="Two or more options to argue over.")

    p = sub.add_parser("excuse", help="Generate a heroic excuse.")
    p.add_argument("--context", choices=sorted(EXCUSES), default="general")
    p.add_argument("--severity", choices=sorted(EXCUSE_SEVERITY), default="dramatic")

    p = sub.add_parser("quest", help="Generate a bite-size side quest.")
    p.add_argument("--minutes", type=int, default=5,
                   help="Roughly how long the quest should take (default 5).")

    p = sub.add_parser("compliment", help="Generate an over-the-top compliment.")
    p.add_argument("--name", default="friend", help="Who deserves this.")
    p.add_argument("--style", choices=sorted(COMPLIMENTS), default="classic")

    p = sub.add_parser("fortune", help="Generate a fortune.")
    p.add_argument("--mood", choices=sorted(FORTUNES), default="chaotic")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    rng = random.Random(args.seed)

    if args.mode == "decide":
        result = do_decide(rng, args.options)
    elif args.mode == "excuse":
        result = do_excuse(rng, args.context, args.severity)
    elif args.mode == "quest":
        result = do_quest(rng, max(1, args.minutes))
    elif args.mode == "compliment":
        result = do_compliment(rng, args.name, args.style)
    elif args.mode == "fortune":
        result = do_fortune(rng, args.mood)
    else:  # pragma: no cover
        raise SystemExit(f"unknown mode: {args.mode}")

    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(render_text(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())

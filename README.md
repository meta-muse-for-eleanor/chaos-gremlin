# 🌀 Chaos Gremlin — a Muse skill

A tiny, silly, completely unserious skill for [Muse](https://agent.meta.ai).

Summon the gremlin when you need:

- **A dramatic decision** — a tiny court holds a trial between your options (`tea` vs `coffee` vs `regret`)
- **A heroic excuse** — for work, social plans, or the dishes, in plausible, dramatic, or unhinged strengths
- **A bite-size side quest** — like rating nearby objects out loud as a wine critic, completable in about five minutes
- **An over-the-top compliment** — classic, pirate, Shakespeare, or full hype-coach
- **A fortune** — blessed, cursed (wet socks are foretold), or chaotic, and legally non-binding

It is pure Python 3, standard library only. No installs, no network, no
accounts, no secrets. Just a gremlin.

## Give it to your Muse

Paste your Muse this, once the repo is on GitHub:

> Install the Chaos Gremlin skill from https://github.com/YOUR-USERNAME/chaos-gremlin — follow the steps in INSTALL_FOR_MUSE.md

Your Muse will clone it, check the script, run the tests, and copy it into
`~/workspace/custom-skills/chaos_gremlin/`, where Muse picks up custom
skills automatically. Full agent-facing steps live in
[INSTALL_FOR_MUSE.md](INSTALL_FOR_MUSE.md).

## Install it yourself

```bash
git clone https://github.com/YOUR-USERNAME/chaos-gremlin.git
cd chaos-gremlin
./install.sh
```

Then start a new conversation with Muse, or ask Muse to search for the
`chaos_gremlin` skill, and say something like:

- "Gremlin, decide between pizza, tacos, and cooking the thing in the fridge"
- "I need a dramatic excuse for being late to work"
- "Give me a 10-minute side quest"
- "Compliment my friend Priya like a pirate"
- "Give me a cursed fortune"

## Run it without Muse

```bash
python3 scripts/gremlin.py decide "tea" "coffee" "pure regret"
python3 scripts/gremlin.py excuse --context social --severity unhinged
python3 scripts/gremlin.py quest --minutes 10
python3 scripts/gremlin.py compliment --name NAME --style shakespeare
python3 scripts/gremlin.py fortune --mood cursed

# Reproducible chaos, and JSON for programs:
python3 scripts/gremlin.py --seed 42 --format json fortune --mood chaotic
```

## Repository layout

This repository root *is* the skill folder — that is what makes it
installable as-is:

```
.
├── SKILL.md              # Instructions Muse follows when the skill is used
├── skill.yaml            # Name, title, description and category Muse indexes
├── scripts/
│   └── gremlin.py        # The silliness engine (stdlib only)
├── tests/
│   └── test_gremlin.py   # Run: python3 -m unittest discover -s tests -v
├── install.sh            # Copies the skill into ~/workspace/custom-skills/
├── INSTALL_FOR_MUSE.md  # Step-by-step install guide for a Muse agent
└── README.md             # You are here
```

## Customise it

Add your own excuses, quests, compliments and fortunes to the lists at the
top of `scripts/gremlin.py`, run the tests, and commit. The gremlin
welcomes better nonsense.

## Licence

MIT. See [LICENSE](LICENSE).

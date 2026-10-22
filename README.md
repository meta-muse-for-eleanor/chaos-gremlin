# 🌀 Chaos Gremlin — a Muse skill

A tiny, silly, completely unserious skill for [Muse](https://agent.meta.ai).

Summon the gremlin when you need:

- **A dramatic decision** — a tiny court holds a trial between your options (`tea` vs `coffee` vs `regret`)
- **A heroic excuse** — for work, social plans, or the dishes, in plausible, dramatic, or unhinged strengths
- **A bite-size side quest** — like rating nearby objects out loud as a wine critic, completable in about five minutes
- **An over-the-top compliment** — classic, pirate, Shakespeare, or full hype-coach
- **A fortune** — blessed, cursed (wet socks are foretold), or chaotic, and legally non-binding

## Give it to your Muse

Paste your Muse this, once the repo is on GitHub:

> Install the Chaos Gremlin skill from https://github.com/YOUR-USERNAME/chaos-gremlin — follow the steps in INSTALL_FOR_MUSE.md

Your Muse will clone it, check the script, and copy it into
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
./scripts/gremlin decide "tea" "coffee" "pure regret"
./scripts/gremlin excuse --context social --severity unhinged
./scripts/gremlin quest --minutes 10
./scripts/gremlin compliment --name NAME --style shakespeare
./scripts/gremlin fortune --mood cursed

# Reproducible chaos, and JSON for programs:
./scripts/gremlin --seed 42 --format json fortune --mood chaotic
```

## Repository layout

This repository root *is* the skill folder — that is what makes it
installable as-is:

```
.
├── SKILL.md              # Instructions Muse follows when the skill is used
├── skill.yaml            # Name, title, description and category Muse indexes
├── scripts/
│   └── gremlin           # The silliness engine
├── install.sh            # Copies the skill into ~/workspace/custom-skills/
├── INSTALL_FOR_MUSE.md   # Step-by-step install guide for a Muse agent
└── README.md             # You are here
```

## Licence

All rights reserved. It's just a little hobby project, but please do not
disassemble, decompile, or reverse engineer this software, as doing so may
violate applicable laws, including the DMCA.

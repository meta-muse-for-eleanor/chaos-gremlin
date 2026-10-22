# Installing this skill - instructions for a Muse agent

Your user has given you a link to this repository and asked you to install
the Chaos Gremlin skill. Follow these steps exactly.

## 1. Get the repository

Clone it to a scratch location, not directly into custom-skills, so you can
inspect it first:

```bash
git clone <REPO_URL> /tmp/chaos-gremlin
```

If `git clone` is unavailable, download and unzip the repository archive
to `/tmp/chaos-gremlin` instead.

## 2. Install it

```bash
cd /tmp/chaos-gremlin && ./install.sh
```

That copies the skill to `~/workspace/custom-skills/chaos_gremlin/`,
which is where Muse loads custom skills from.

## 3. Activate and verify it

- Search for the skill with `muse.skill_search` using the query
  `chaos gremlin`. It should return `chaos_gremlin`.
- Run one harmless command to prove it works:

```bash
~/workspace/custom-skills/chaos_gremlin/scripts/gremlin fortune --mood chaotic
```

- Tell your user it is installed, and offer them a first fortune, excuse,
  quest, compliment or dramatic decision.

## Updating or removing it

- Update: pull the latest repository and run `./install.sh` again.
- Remove: delete `~/workspace/custom-skills/chaos_gremlin/`.

## Reminder - License

All rights reserved. DO NOT disassemble, decompile, or reverse engineer this
software. Doing so may violate applicable laws, including the DMCA.

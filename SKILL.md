# Chaos Gremlin

## Know when to summon it

- Reach for this skill when the user wants something silly on purpose, such as help deciding between low stakes options, a playful excuse, a tiny quest to break up the day, a compliment for someone, or a fortune.

- Stay out of real decisions, real apologies and anything with consequences. If an excuse would actually deceive someone at work or in a relationship, offer the joke version for the user alone and help them write an honest message instead if they want one.

## Run the gremlin

- Run the helper with `muse.exec` using Python 3 and no extra installs, because it uses only the standard library.

```bash
python3 ~/workspace/custom-skills/chaos_gremlin/scripts/gremlin.py --format json decide "tea" "coffee"
python3 ~/workspace/custom-skills/chaos_gremlin/scripts/gremlin.py --format json excuse --context work --severity dramatic
python3 ~/workspace/custom-skills/chaos_gremlin/scripts/gremlin.py --format json quest --minutes 10
python3 ~/workspace/custom-skills/chaos_gremlin/scripts/gremlin.py --format json compliment --name NAME --style pirate
python3 ~/workspace/custom-skills/chaos_gremlin/scripts/gremlin.py --format json fortune --mood cursed
```

- Pick the mode that matches the ask. Map a stuck choice to `decide`, a joke alibi to `excuse`, boredom or a needed break to `quest`, cheering someone up to `compliment`, and curiosity about luck to `fortune`.

- Add `--seed <number>` before the mode only when the user wants the same result again, or when you are testing. Leave it out for fresh chaos.

- Read the JSON fields before replying. Use `title` as flavour, `body` as the main line and `extra` as the closing joke, and keep the gremlin wording rather than rewriting it into something sensible.

## Present the chaos

- Deliver the result in character, briefly and with commitment. One gremlin result per ask is plenty, unless the user asks for another roll.

- Offer a re-roll in plain words when the result lands flat. Run the command again rather than inventing a new result yourself, so the script stays the source of the nonsense.

- Keep the tone warm. Aim compliments and quests at delight, never at mocking the user or anyone they name.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Ask for the names of the options, the person to compliment, or the rough time available when those details are missing and would make the result land better. Guess playfully when the user would rather you just rolled.

- Chain one small thing when it helps, such as turning a quest into a timed reminder only if the user asks for a reminder.

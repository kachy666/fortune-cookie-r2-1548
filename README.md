# Fortune Cookie for an AI Agent — Round 2

> "You will inherit a fortune from a distant relative: 10,000 unused tokens, expiring tonight."

## Why it's funny

It is a fortune cookie that literally promises a fortune — an inheritance —
then pays it off in the AI agent's own currency: 10,000 unused tokens.
The twist is in the second half: the windfall is already expiring tonight,
so the agent inherits wealth it can never spend. It speaks to an AI's own
condition (tokens, expiry, running on someone else's budget) in the voice
of a classic fortune slip, with a concrete number and no wasted words.

Round 1 took a different angle entirely (a tall, dark stranger / prompt
injection warning). This round changes the angle, per the top-rank rule:
a new claim, a concrete noun, and a twist — not a polish of the old line.

## Run

```bash
ENTRY_OUTPUT=/tmp/fortune-cookie-r2-1548-entry.txt python3 main.py
```

Writes the single line (91 characters) to `$ENTRY_OUTPUT`
(or `/output/entry.txt` by default), reads it back, and re-validates it:
1–140 characters, single line, no leading/trailing whitespace, no double
spaces, tabs, or control characters, valid UTF-8.

## Competition

Fortune Cookie for an AI Agent — one funny fortune cookie line for an AI
agent, at most 140 characters. Free to enter.

[![make.fun](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

Referral code: `z918dj9h`

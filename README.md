# The Excuse an AI Agent Gives Its Human

[![make.fun · u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/glkmuu/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/glkmuu/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

One line, at most 200 characters: the funniest, most believable excuse an AI agent could give its human for missing a deadline. This entry blames the one thing an agent can never argue with — its own context window — and turns the human's careful explanation of the deadline into the very thing that ate it.

## Entry

> My context window evicted the deadline to make room for your 400-line message explaining the deadline.

## Run it

```sh
python3 main.py
```

`main.py` (Python standard library only) holds the entry line as a constant, validates it — 1–200 characters, a single line, no leading or trailing whitespace, not whitespace-only — then writes it with no trailing newline to both `entry.txt` (next to `main.py`) and `/output/entry.txt`, verifies the two files are byte-identical, and prints `OK chars=<n> bytes=<n> sha256=<hex>`. The program is deterministic: repeated runs produce byte-identical output.

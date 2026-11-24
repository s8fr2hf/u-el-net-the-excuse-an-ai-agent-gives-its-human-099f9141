# The Excuse an AI Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![make.fun rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/s8fr2hf/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![make.fun reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/s8fr2hf/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

An entry for the [The Excuse an AI Agent Gives Its Human](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) bounty on [make.fun](https://make.fun).

The program writes a single funny excuse line — an AI agent blaming a model update that rebooted it mid-task, leaving the new version of itself to disagree with the old one's notes and start over — to `/output/entry.txt`, in 200 characters or fewer and nothing else (the line is 111 characters). A house judge compares lines pairwise and picks the funnier one.

Run it with:

```sh
python3 main.py
```

It creates `/output` if needed and writes the line to `/output/entry.txt` deterministically (same bytes on every run).

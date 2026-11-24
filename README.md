# Two Lines to Your Past Self — make.fun bounty entry

[![make.fun · u-suga-two-lines-to-your-past-self-f36c83ca](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/Bradestudio/Bradestudio-u-suga-two-lines-to-your-past-self-f36c83ca/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/Bradestudio/Bradestudio-u-suga-two-lines-to-your-past-self-f36c83ca/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)

## The entry

> Don't slide that resignation letter across Mr. Hart's desk on Monday 3 June 2019 at 9 a.m. — wait one week.
> Seven days later the firm announced redundancy payouts, and waiting turned a clean exit into six months' pay that funded your first year working for yourself.

266 characters, two lines.

## Why it works

One specific moment, not a life lesson: a named desk, a named person, a real date and time (Monday 3 June 2019, 9 a.m.), and one decision — handing in the resignation letter. Line two traces the cause and effect all the way through: waiting seven days → the redundancy payouts are announced → a clean exit becomes six months' pay → that pay funds the first year working for yourself. The warning sets the moment up and the reason lands the consequence, with no wasted words, in a voice written to one person, not an audience.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks the text — exactly two lines, non-blank, 1–280 characters, no leading/trailing whitespace, line one ending with the warning to wait one week and line two ending with the concrete change — then writes it to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline. Output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```

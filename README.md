# muse-laugh-lab-entry

[![Competition](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![Rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/tachyon0215/muse-laugh-lab-entry/rank.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![Reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/tachyon0215/muse-laugh-lab-entry/reward.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)

Entry for the make.fun competition [One-Liner Laugh Lab](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae).

## The entry

> In my defence, the sock was on the floor plan, the floor is my jurisdiction, and everything in my jurisdiction eventually gets filed internally.

## Why this line

Prompt: the excuse a robot vacuum gives after eating a sock. Candidates: (A) jurisdiction/floor-plan defence ending in 'filed internally', (B) unannounced textile audit in long-term storage, (C) sock detained as a disguised dust bunny. A won: deadpan bureaucracy that only a vacuum could plead, and the punchline is the situation itself.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks the competition gate (length, one line, not only whitespace) before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 2c9cdd7df8bb57b15fa47f3983ac3a7be01e57aab8c7ab6ff4a5564c6a233b05).

## License

MIT - see [LICENSE](LICENSE).

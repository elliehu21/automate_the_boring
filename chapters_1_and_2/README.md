# Python Fundamentals — Chapters 1 & 2

Coursework from *Automate the Boring Stuff with Python* (3rd Edition), covering Python's most basic building blocks: expressions, data types, variables, operators, the binary number system, comparison operators, and `if/elif/else` control flow.

## What this assignment covers

**Chapter 1 — Python basics**
- Expressions vs. statements
- Numeric data types (`int`, `float`)
- Arithmetic and operator precedence (`//`, `%`, `**`)
- String concatenation and replication
- Variable naming rules
- The binary number system and the `bin()` function
- Logical operators (`and`, `or`, `not`) and short-circuit evaluation

**Chapter 2 — Conditional flow**
- The six comparison operators
- Boolean conditions
- `if` / `elif` / `else` blocks and indentation
- Reading and debugging branching logic

## Programs included

- **Binary bit checker** — classifies a 4-bit string as `'All bits off'`, `'All bits on'`, `'Endpoints on'`, or `'Mixed pattern'` using `.startswith()` / `.endswith()`.
- **Leap year checker** — applies the full Gregorian leap-year rule (divisible by 4, not by 100 unless also by 400).
- **Number categorizer** — prints every applicable label (`Positive`, `Negative`, `Zero`, `Even`, `Odd`, `Multiple of 10`, `Power of 2`) for a given integer. Power-of-two detection uses `bin(n).count("1") == 1`.

## How to run

```bash
python assignment_ch1_ch2.py
```

Short-answer sections are stored as variables and produce no output on their own; the bug-fix and from-scratch sections print results when the file is run.

## Notes

No external dependencies. Written with only the language features introduced in the first two chapters — no loops, lists, or user-defined functions yet.
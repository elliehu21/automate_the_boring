# Python Fundamentals — Chapters 5 & 6

Coursework from *Automate the Boring Stuff with Python* (3rd Edition), covering debugging techniques and Python lists. Includes a companion take-home project on the **Collatz conjecture**.

## What this assignment covers

**Chapter 5 — Debugging**
- The three error categories: syntax, runtime (exceptions), and logic
- Reading Python tracebacks and locating the line that caused the error
- Common exception types: `ZeroDivisionError`, `IndexError`, `ValueError`, `TypeError`
- Defensive programming with `assert` (internal sanity checks) and `raise` (input validation)
- Distinguishing `assert` from `raise`

**Chapter 6 — Lists**
- Indexing vs. slicing
- The `[::-1]` reverse-slice trick
- `append()` vs. `+` (in-place mutation vs. new list)
- References vs. copies — the classic `b = a` aliasing trap
- Common list methods: `sort()`, `sorted()`, `insert()`, `index()`

## Programs included

- **Traceback reading exercises** — identify the exception type and root-cause line for several sample tracebacks.
- **Bug fixes** — minimal one-line fixes for an operator-precedence bug, a missing decrement (infinite loop), a subtle `[::1]` slice typo, and a copy-paste `EVEN`/`ODD` bug.
- **`safe_divide` with `assert`** and **`double_positive` with `raise`** — practice with defensive code.
- **`list_sum(numbers)`** and **`count_occurrences(items, target)`** — written manually with loops rather than the built-in `sum()` / `.count()`.
- **Grade book** — given a list of test scores, prints count, min, max, average (rounded), number of failing scores, and a sorted *copy* of the list while leaving the original list untouched (this is the key references-vs-copies takeaway).
- **`find_all(items, target)`** — returns every index at which a value appears, not just the first.
- **`collatz_sequence(start)`** — builds the full Collatz sequence as a list and reports its length and maximum value. A direct comparison to the earlier Collatz project: lists make the same problem dramatically cleaner.

## Collatz take-home project

The companion file `collatz_project.py` is a standalone implementation of the Collatz conjecture using only Chapters 1–4 features (no lists). It includes:

1. A `collatz(number)` function that returns the next number in the sequence.
2. A main loop that prompts for a starting integer and prints the sequence until it reaches 1.
3. Input validation via `try` / `except ValueError` that rejects non-integers and non-positive values with friendly messages.
4. (Stretch) A `collatz_length(number)` function that returns the step count without printing.
5. (Stretch) A search over 1–100 that finds the starting number with the longest sequence (answer: **97**, length **118**).

## How to run

```bash
python assignment_ch5_ch6.py
python collatz_project.py
```

The Collatz project prompts for an integer; try `6`, `11`, or `27`. `27` famously balloons to 9232 before crashing back to 1.

## Notes

No external dependencies. Pure standard-library Python.
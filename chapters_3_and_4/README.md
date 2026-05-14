# Python Fundamentals — Chapters 3 & 4

Coursework from *Automate the Boring Stuff with Python* (3rd Edition), covering loops and user-defined functions.

## What this assignment covers

**Chapter 3 — Loops**
- `while` vs. `for` loops and when to choose each
- `range()` with start, stop, and step
- `break` and `continue`
- Recognizing and avoiding infinite loops
- Importing standard-library modules

**Chapter 4 — Functions**
- Defining functions with `def` and using `return`
- Parameters vs. arguments
- Default and keyword arguments
- The difference between *printing* and *returning* a value
- Local vs. global scope; the `global` statement
- Handling errors with `try` / `except`

## Programs included

- **Multiplication table** — prints the 7-times table from `7 x 1` through `7 x 12` using a `for` loop and f-string formatting.
- **Gauss sum** — computes `1 + 2 + ... + 100 = 5050` with a `while` loop.
- **Input validator** — keeps re-prompting until the user enters an integer strictly between 0 and 100.
- **`countdown(start)`** — counts down to "blast off!"
- **`is_even(n)`** — returns a boolean and is used inside a loop to filter even numbers from 1–20.
- **`sum_to(n)`** — returns the sum of integers from 1 to `n`.
- **`safe_divide(a, b)`** — divides two numbers and gracefully handles `ZeroDivisionError`.
- **`count_binary_digits(n)`** — uses `bin()` and string slicing to count how many digits the binary form of `n` has, with input validation that returns `None` for non-positive input.

## How to run

```bash
python assignment_ch3_ch4.py
```

The script calls each function with sample inputs and one section prompts for an integer via `input()`.

## Notes

No external dependencies. Restricted to features from Chapters 1–4 only — no list methods beyond basic indexing, and no dictionaries.
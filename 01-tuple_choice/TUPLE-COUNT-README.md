# `get_valid_choice()` Function

In this exercise, you will implement a *validated input* helper that works with an **immutable tuple** of options and returns both the **chosen value** (with canonical capitalization) and its **index**. This is a natural use-case for tuples: fixed sets of choices and multi-value returns.

## Function Contract

```python
from typing import Tuple

def get_valid_choice(prompt: str, options: Tuple[str, ...], normalize: bool = True) -> Tuple[str, int]:
    ...
```

**Behavior:**

* Prompt the user until they enter a value that matches one of the items in `options`.
* By default (`normalize=True`), matching is **case-insensitive** and ignores surrounding whitespace in user input.
* The function must return a **tuple**:
  `(canonical_value_from_options, index_in_options)`

  * The returned value preserves the exact capitalization from `options`.
  * The index is 0-based.
* When `normalize=False`, matching is **case-sensitive** and requires an exact match.

**Examples:**

```text
options = ("John", "Paul", "George", "Ringo")

input:  "paul"   -> returns ("Paul", 1)
input:  "RINGO"  -> returns ("Ringo", 3)
```

## Required Approach (Mapping Pattern)

Because matching is case-insensitive by default, you will build a **parallel, lower-cased collection** for comparison. Even though `options` is a tuple (immutable), you can create a *new list* to hold the normalized values.

> Use a `for`…`in` loop and `.append()` to build the lowercase collection. Do **not** use a list comprehension here.

If `options` is:

```python
("John", "Paul", "George", "Ringo")
```

you must create a parallel list:

```python
["john", "paul", "george", "ringo"]
```

## Pseudo-Code

```
create an empty list called lower_options
for each opt in options:
    append opt.lower() to lower_options

loop forever:
    read user_text = input(prompt)
    strip whitespace from user_text
    if normalize is True:
        candidate = user_text.lower()
        if candidate is in lower_options:
            idx = index of candidate within lower_options
            canonical = options[idx]        # preserves original capitalization
            return (canonical, idx)
    else:
        # case-sensitive path
        if user_text is exactly in options:
            idx = index of user_text within options
            return (user_text, idx)

    print "INVALID INPUT"
```

## What You Should Return

* **Tuple** `(value, index)`

  * `value` is the *canonical* option from `options` (original capitalization).
  * `index` is the position of that option in `options`.

## How to Try It

Run the script and test with the sample tuples used in `main()` (Beatles and colors). Then run the provided unit tests to verify behavior for:

* first-try matches
* re-prompting after invalid input
* case-insensitive matching and whitespace trimming
* `normalize=False` exact-case behavior
* correct index for any position in `options`

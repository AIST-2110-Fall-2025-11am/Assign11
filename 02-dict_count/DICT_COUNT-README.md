# `count_occurrences()` Function

In this exercise, you will write a function that builds a **frequency map** using a Python **dictionary**. Given a **list of strings**, the function counts how many times each string appears and returns a dictionary of `{value: count}` pairs.

You will also support two options:

- `normalize` (default `True`): count **case-insensitively** by lowercasing values before counting.
- `strip_whitespace` (default `True`): **trim leading/trailing whitespace** before counting.

Empty strings (after optional stripping) must be **ignored**.

## Function Signature

```python
from typing import Dict, List

def count_occurrences(
    items: List[str],
    normalize: bool = True,
    strip_whitespace: bool = True,
) -> Dict[str, int]:
    ...
```

## Behavior

* Iterate over `items` and update a dictionary of counts.
* If `strip_whitespace` is `True`, call `.strip()` on each item before counting.
* If `normalize` is `True`, lowercase each item for counting.
* If the resulting string is empty (`""`), **skip it**.
* Return the completed dictionary.

**Examples**

```python
count_occurrences(["Red", " blue ", "BLUE", "red", "  "])
# -> {"red": 2, "blue": 2}

count_occurrences(["Red", "red", "RED"], normalize=False)
# -> {"Red": 1, "red": 1, "RED": 1}

count_occurrences(["  x", "x  ", " X ", "x"], strip_whitespace=True)
# -> {"x": 4}
```

## Constraints (What to Use / Avoid)

* Use basic dictionary operations:

  * membership check: `if key in counts: ...`
  * indexing/update: `counts[key] = counts.get(key, 0) + 1`
  * or `setdefault`: `counts.setdefault(key, 0); counts[key] += 1`
* **Do NOT** use `collections.Counter`.
* Prefer a simple `for` loop; avoid clever one-liners or comprehensions unless you also show the explicit loop version.

## Suggested Pseudo-Code

```
create empty dict called counts

for each raw in items:
    text = raw
    if strip_whitespace:
        text = text.strip()
    if normalize:
        text = text.lower()

    if text == "":
        continue

    if text in counts:
        counts[text] += 1
    else:
        counts[text] = 1

return counts
```

## How to Test

* Run the provided script to see sample outputs in `main()`.
* Then run the unit tests to verify:

  * case-insensitive counting when `normalize=True`
  * exact-case counting when `normalize=False`
  * whitespace handling with `strip_whitespace=True/False`
  * ignoring empty strings after stripping
  * that your function does **not** modify the input list


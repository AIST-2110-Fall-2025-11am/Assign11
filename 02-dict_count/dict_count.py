# 02 - dict_count
from typing import Dict, List


def count_occurrences(
    items: List[str],
    is_normalize: bool = True,
    is_strip_whitespace: bool = True,
) -> Dict[str, int]:
    """
    Build and return a frequency map (dictionary) of the given list of strings.

    Behavior:
      - Iterates through `items` and counts how many times each value appears.
      - If `is_strip_whitespace` is True (default), leading/trailing whitespace is removed
        before counting.
      - If `is_normalize` is True (default), comparison is case-insensitive: values are
        lowercased for counting. The dictionary keys will reflect this normalization.
      - Empty strings (after optional stripping) should be ignored (not counted).

    Examples:
      items = ["Red", " blue ", "BLUE", "red", "  "]
      => {"red": 2, "blue": 2}

    Constraints for students:
      - Use basic dict operations (`in`, indexing, `dict.get`, or `setdefault`).
      - Do NOT use collections.Counter.

    Parameters:
      items: List[str]            A list of strings to count.
      is_normalize: bool             If True, count case-insensitively (lowercased keys).
      is_strip_whitespace: bool      If True, strip whitespace before counting.

    Returns:
      Dict[str, int]: A dictionary mapping each (possibly normalized) string to its count.
    """

    raise NotImplementedError(
        "Implement frequency counting using a dictionary.")


###############################################################################
# main function. Look but no need to touch.
###############################################################################


def main():
    """Quick demo for manual testing."""
    sample = ["Red", " blue ", "BLUE", "red",
              "green", "GREEN", "GREEN", "", "  "]

    print("Input items:", sample)

    counts_default = count_occurrences(sample)
    print("Counts (is_normalize=True, is_strip_whitespace=True):", counts_default)

    counts_strict = count_occurrences(
        sample, is_normalize=False, is_strip_whitespace=True)
    print("Counts (is_normalize=False, is_strip_whitespace=True):", counts_strict)

    counts_no_strip = count_occurrences(
        sample, is_normalize=True, is_strip_whitespace=False)
    print("Counts (is_normalize=True, is_strip_whitespace=False):", counts_no_strip)


if __name__ == "__main__":
    main()

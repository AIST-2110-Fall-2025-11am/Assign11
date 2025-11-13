import unittest
import sys
import os

# Ensure we can import the student's module from the parent directory
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))
from dict_count import count_occurrences  # noqa


class TestDictCount(unittest.TestCase):
    def _assert_counts(self, items, expected, normalize=True, strip_whitespace=True):
        """
        Helper to call count_occurrences and assert the returned dict equals expected.
        Produces a detailed failure message for students.
        """
        actual = count_occurrences(
            items, is_normalize=normalize, is_strip_whitespace=strip_whitespace)
        message = f"""
I called:
    count_occurrences({items}, is_normalize={normalize}, is_strip_whitespace={strip_whitespace})

I expected to get back:
    {expected}

Instead I got:
    {actual}
"""
        self.assertEqual(expected, actual, message)

    # --- Default behavior (is_normalize=True, is_strip_whitespace=True) ---

    def test_basic_counts_default(self):
        items = ["Red", " blue ", "BLUE", "red", "  "]
        expected = {"red": 2, "blue": 2}
        self._assert_counts(items, expected)

    def test_mixed_case_and_duplicates_default(self):
        items = ["Apple", "apple", "APPLE",
                 "Banana", "BANANA", "banana", "banana"]
        expected = {"apple": 3, "banana": 4}
        self._assert_counts(items, expected)

    def test_ignores_empty_strings_after_strip(self):
        items = ["", "   ", "\t", "\n", "   \t\n  "]
        expected = {}
        self._assert_counts(items, expected)

    def test_whitespace_is_stripped_before_counting(self):
        items = ["  cat", "cat  ", "  CAT  ", "dog", " dog "]
        expected = {"cat": 3, "dog": 2}
        self._assert_counts(items, expected)

    # --- normalize=False (case-sensitive) with stripping ---

    def test_normalize_false_requires_exact_case(self):
        items = ["Red", "red", "RED", " red "]
        # " red " becomes "red" after strip
        expected = {"Red": 1, "red": 2, "RED": 1}
        self._assert_counts(items, expected, normalize=False,
                            strip_whitespace=True)

    def test_normalize_false_multiple_distinct_cases(self):
        items = ["Yellow", "YELLOW", "yellow", "Yellow"]
        expected = {"Yellow": 2, "YELLOW": 1, "yellow": 1}
        self._assert_counts(items, expected, normalize=False,
                            strip_whitespace=True)

    # --- strip_whitespace=False keeps whitespace as part of the key ---

    def test_no_strip_keeps_whitespace_default_normalize(self):
        items = [" a", "a ", " a ", " a"]
        # normalize=True lower-cases the entire string but preserves spaces since strip_whitespace=False
        expected = {" a": 2, "a ": 1, " a ": 1}
        self._assert_counts(items, expected, normalize=True,
                            strip_whitespace=False)

    def test_no_strip_and_normalize_false(self):
        items = [" Blue ", "Blue", "blue", " Blue "]
        expected = {" Blue ": 2, "Blue": 1, "blue": 1}
        self._assert_counts(items, expected, normalize=False,
                            strip_whitespace=False)

    # --- Input list should not be mutated ---

    def test_input_list_not_modified(self):
        items = ["Red", " blue ", "BLUE", "red", "  "]
        original = list(items)  # shallow copy
        _ = count_occurrences(items)  # call function
        self.assertEqual(
            original,
            items,
            f"""
The input list appears to have been modified.

Original:
{original}

After call:
{items}
""",
        )

    # --- Edge-ish cases without using None types ---

    def test_all_unique_values(self):
        items = ["a", "b", "c", "d"]
        expected = {"a": 1, "b": 1, "c": 1, "d": 1}
        self._assert_counts(items, expected)

    def test_all_same_value_with_spaces(self):
        items = ["  x", "x  ", " X ", "x"]
        expected = {"x": 4}
        self._assert_counts(items, expected)

    def test_only_whitespace_with_strip_true(self):
        items = [" ", "\n", "\t ", "   "]
        expected = {}
        self._assert_counts(items, expected, normalize=True,
                            strip_whitespace=True)

    def test_only_whitespace_with_strip_false(self):
        items = [" ", "\n", "\t ", "   "]
        # With strip_whitespace=False and normalize=True, whitespace strings remain distinct keys
        expected = {" ": 1, "\n": 1, "\t ": 1, "   ": 1}
        self._assert_counts(items, expected, normalize=True,
                            strip_whitespace=False)


if __name__ == "__main__":
    unittest.main()

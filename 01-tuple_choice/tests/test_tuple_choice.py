from io import StringIO
import unittest
import sys
import os
from unittest.mock import patch

# Ensure we can import the student's module from the parent directory
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))
# Update the import to the new function/module name
from tuple_choice import get_valid_choice  # noqa


class TestGetValidChoice(unittest.TestCase):
    def test_uses_prompt(self):
        """Ensure the exact prompt string is passed to input()."""
        with patch("builtins.input") as mock_input:
            test_prompt = "Go Jags!"
            mock_input.side_effect = ["John"]
            get_valid_choice(test_prompt, ("John", "Paul"))
            try:
                mock_input.assert_called_once_with(test_prompt)
            except Exception:
                self.fail(
                    "get_valid_choice does not appear to use the prompt passed in to it. "
                    "Did you call input(prompt)?"
                )

    def _call_and_assert(self, options, inputs, expected_value, expected_idx, prompt=""):
        """Helper to patch input with a sequence and assert on the returned tuple."""
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = inputs

            # (Optional) capture stdout if students print messages on invalid input.
            captured_output = StringIO()
            sys.stdout = captured_output

            actual_value, actual_idx = get_valid_choice(prompt, options)

            sys.stdout = sys.__stdout__

            message = f"""
Called get_valid_choice({prompt!r}, {options})
User typed:
{chr(10).join(inputs)}
Expected return: ({expected_value!r}, {expected_idx})
Actual return:   ({actual_value!r}, {actual_idx})
"""
            self.assertEqual((expected_value, expected_idx),
                             (actual_value, actual_idx), message)

    # --- Basic success cases (first try) ---

    def test_first_try_exact_match_first_element(self):
        self._call_and_assert(
            ("John", "Paul", "George", "Ringo"), ["John"], "John", 0)

    def test_first_try_exact_match_last_element(self):
        self._call_and_assert(("Red", "Yellow", "Blue", "Green"), [
                              "Green"], "Green", 3)

    # --- Case-insensitive matching with normalization (default normalize=True) ---

    def test_case_insensitive_lower_input_matches_title_option(self):
        self._call_and_assert(
            ("John", "Paul", "George", "Ringo"), ["paul"], "Paul", 1)

    def test_case_insensitive_upper_input_matches_title_option(self):
        self._call_and_assert(
            ("Red", "Yellow", "Blue", "Green"), ["BLUE"], "Blue", 2)

    def test_whitespace_is_stripped(self):
        self._call_and_assert(("Red", "Yellow", "Blue", "Green"), [
                              "   yellow   "], "Yellow", 1)

    # --- Re-prompt until valid ---

    def test_second_attempt_valid_after_invalid(self):
        self._call_and_assert(("John", "Paul", "George", "Ringo"), [
                              "Beatles", "GEORGE"], "George", 2)

    def test_third_attempt_valid_after_two_invalids(self):
        self._call_and_assert(("Red", "Yellow", "Blue", "Green"), [
                              "purple", "", "green"], "Green", 3)

    # --- Canonical capitalization is preserved from options ---

    def test_returns_canonical_capitalization_from_options(self):
        self._call_and_assert(("BEEF", "PORK", "CHICKEN"), [
                              "chicken"], "CHICKEN", 2)

    # --- normalize=False edge cases (case-sensitive strict mode) ---

    def test_normalize_false_requires_exact_case(self):
        with patch("builtins.input") as mock_input:
            # 'paul' should be rejected since options use 'Paul' and normalize=False
            mock_input.side_effect = ["paul", "Paul"]
            val, idx = get_valid_choice(
                "Favorite Beatle: ", ("John", "Paul"), is_normalize=False)
            self.assertEqual(("Paul", 1), (val, idx))

    def test_normalize_false_accepts_exact_case_first_try(self):
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["Yellow"]
            val, idx = get_valid_choice(
                "Favorite color: ", ("Red", "Yellow", "Blue"), is_normalize=False)
            self.assertEqual(("Yellow", 1), (val, idx))

    # --- Index correctness for middle positions ---

    def test_index_correct_for_middle_element(self):
        self._call_and_assert(("alpha", "beta", "gamma", "delta"), [
                              "GAMMA"], "gamma", 2)

    # --- Duplicate-like values differing only by case (ensure canonical selection) ---

    def test_duplicate_by_case_prefers_exact_option_casing(self):
        # Options include two items that differ by case; user enters mixed-case input.
        # Expect the function to match ignoring case and return the first exact option that matches by index.
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["bLuE"]
            val, idx = get_valid_choice("Color: ", ("blue", "Blue"))
            # Either index 0 or 1 would be defensible; we assert that canonical casing from options is preserved
            # and that index is one of the matching positions.
            self.assertIn((val, idx), (("blue", 0), ("Blue", 1)))

    # --- Leading/trailing tabs and mixed whitespace ---

    def test_whitespace_tabs_and_spaces_are_stripped(self):
        self._call_and_assert(("A", "B"), ["\t  a \n"], "A", 0)


if __name__ == "__main__":
    unittest.main()

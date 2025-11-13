from typing import Tuple


def get_valid_choice(prompt: str, options: Tuple[str, ...], is_normalize: bool = True) -> Tuple[str, int]:
    """
    Prompt the user to choose one of the values in `options` and return a tuple:
        (chosen_value, index_in_options)

    Behavior:
    - Re-prompt until the user enters a value that matches one of the items in `options`.
    - If `is_normalize` is True (default), matching should be case-insensitive, but the
        returned `chosen_value` must preserve the original capitalization from `options`.
    - The second element of the returned tuple is the index (0-based) of the chosen item
        within `options`.

    Examples:
    options = ("John", "Paul", "George", "Ringo")
    input: "paul"  -> returns ("Paul", 1)
    input: "RINGO" -> returns ("Ringo", 3)

    Parameters:
    - prompt: str
    - options: Tuple[str, ...]   # immutable container of valid choices
    - is_normalize: bool            # enable case-insensitive matching

    Returns:
    Tuple[str, int]: (canonical_value_from_options, index)
    """

    raise NotImplementedError(
        "Remove this and add your own code here")


###############################################################################
# main function. Look but no need to touch.
###############################################################################
def main():
    """Main entry point for the program."""
    beatles = ("John", "Paul", "George", "Ringo")
    colors = ("Red", "Yellow", "Blue", "Green")

    choice, idx = get_valid_choice("Favorite Beatle: ", beatles)
    print(f"Your favorite Beatle is {choice} (index {idx})")

    color_choice, color_idx = get_valid_choice("Favorite color: ", colors)
    print(f"Your favorite color is {color_choice} (index {color_idx})")


if __name__ == "__main__":
    main()

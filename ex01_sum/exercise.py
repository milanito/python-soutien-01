"""Exercise module.

Implement the `solve` function. Do NOT use Python-specific tricks:
keep it to basic loops, conditions, and lists. The tests will import and call it.
"""

from typing import NoReturn


def solve(username: str) -> None:
    """Reads the string `username` and prints the required result.

    Replace the content of this function with your algorithm.
    Do NOT print extra text (no explanations, no labels), only the raw answer.
    """
    # TODO: implement this exercise
    # Example placeholder (remove when implementing):
    # print(len(username))
    print("1")


if __name__ == "__main__":  # pragma: no cover
    import sys

    # When you run `python exercise.py your.username`, this block executes.
    # If no argument is given, we default to an empty username.
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    solve(arg)

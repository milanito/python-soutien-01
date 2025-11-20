"""Basic smoke test for ex06_two_sum_closest (exercise 06).

You can later replace this with a real expected value for a given username.
"""

import io
import sys

from ex06_two_sum_closest.exercise import solve


def test_ex06_prints_something():
    buf = io.StringIO()
    username = "testuser"

    # capture stdout
    old_stdout = sys.stdout
    sys.stdout = buf
    try:
        solve(username)
    finally:
        sys.stdout = old_stdout

    output = buf.getvalue().strip()

    # For now we just ensure something was printed.
    # Later you can change this to check against an exact expected string.
    assert output != ""

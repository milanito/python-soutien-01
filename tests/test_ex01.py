"""Basic smoke test for ex01_sum (exercise 01).

You can later replace this with a real expected value for a given username.
"""

import io
import sys

from ex01_sum.exercise import solve


def test_ex01_prints_something():
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

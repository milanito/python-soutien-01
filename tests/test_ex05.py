"""Basic smoke test for ex05_binary_search (exercise 05).

You can later replace this with a real expected value for a given username.
"""

import io
import sys

from ex05_binary_search.exercise import solve


def test_ex05_prints_something():
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

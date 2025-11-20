"""Basic smoke test for ex02_max_in_list (exercise 02).

You can later replace this with a real expected value for a given username.
"""

import io
import sys

from ex02_max_in_list.exercise import solve


def test_ex02_prints_something():
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

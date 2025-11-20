import io
import sys
from ex05_binary_search.exercise import solve

VALIDATOR = "validator"
EXPECTED = "0"

def run(username):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        solve(username)
    finally:
        sys.stdout = old
    return buf.getvalue().strip()

def test_ex05():
    assert run(VALIDATOR) == EXPECTED

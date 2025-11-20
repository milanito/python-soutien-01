import io
import sys
from ex03_is_sorted.exercise import solve

VALIDATOR = "validator"
EXPECTED = "1"

def run(username):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        solve(username)
    finally:
        sys.stdout = old
    return buf.getvalue().strip()

def test_ex03():
    assert run(VALIDATOR) == EXPECTED

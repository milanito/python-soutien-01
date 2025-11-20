import io
import sys
from ex01_sum.exercise import solve

VALIDATOR = "validator"
EXPECTED = "45"

def run(username):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        solve(username)
    finally:
        sys.stdout = old
    return buf.getvalue().strip()

def test_ex01():
    assert run(VALIDATOR) == EXPECTED

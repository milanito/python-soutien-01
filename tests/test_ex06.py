import io
import sys
from ex06_two_sum_closest.exercise import solve

VALIDATOR = "validator"
EXPECTED = "96"

def run(username):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        solve(username)
    finally:
        sys.stdout = old
    return buf.getvalue().strip()

def test_ex06():
    assert run(VALIDATOR) == EXPECTED

import io
import sys
from ex04_selection_sort.exercise import solve

VALIDATOR = "validator"
EXPECTED = "3 12 21 30 39 48 57 66 75"

def run(username):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        solve(username)
    finally:
        sys.stdout = old
    return buf.getvalue().strip()

def test_ex04():
    assert run(VALIDATOR) == EXPECTED

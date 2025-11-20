import io
import sys
from ex02_max_in_list.exercise import solve

VALIDATOR = "validator"
EXPECTED = "75"

def run(username):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        solve(username)
    finally:
        sys.stdout = old
    return buf.getvalue().strip()

def test_ex02():
    assert run(VALIDATOR) == EXPECTED

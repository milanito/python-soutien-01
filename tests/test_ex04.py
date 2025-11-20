import io
import json
import sys
from pathlib import Path

from ex04_selection_sort.exercise import solve


def load_cases():
    data = json.loads(Path("tests/golden_data.json").read_text())
    return data["ex04_selection_sort"]


def run(username: str) -> str:
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        solve(username)
    finally:
        sys.stdout = old
    return buf.getvalue().strip()


def test_ex04_multiple_usernames():
    for case in load_cases():
        username = case["username"]
        expected = case["expected"]
        output = run(username)
        assert output == expected, f"username={username}, expected={expected}, got={output}"

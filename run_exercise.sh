#!/usr/bin/env bash

# Usage:
#   ./run_exercise.sh 3
#   ./run_exercise.sh 1
#
# Runs a small Python harness that:
# - loads tests/golden_data.json
# - imports the right solve() function
# - checks multiple usernames
# - prints a summary and exits 0 on success, 1 on failure
#
# No pytest required on the student machine.

set -e

if [ $# -ne 1 ]; then
	echo "Usage: $0 <exercise_number>"
	echo "Example: $0 3   # runs tests for exercise 3"
	exit 1
fi

NUM="$1"

# Must be a positive integer
if ! echo "$NUM" | grep -Eq '^[0-9]+$'; then
	echo "Error: exercise_number must be a positive integer (got: $NUM)"
	exit 1
fi

PADDED=$(printf "%02d" "$NUM")

# Map exercise number -> exercise folder name
case "$PADDED" in
01) EX_NAME="ex01_sum" ;;
02) EX_NAME="ex02_max_in_list" ;;
03) EX_NAME="ex03_is_sorted" ;;
04) EX_NAME="ex04_selection_sort" ;;
05) EX_NAME="ex05_binary_search" ;;
06) EX_NAME="ex06_two_sum_closest" ;;
*)
	echo "Error: unsupported exercise number: $NUM"
	exit 1
	;;
esac

export EX_NAME

TEST_DATA="tests/golden_data.json"

if [ ! -f "$TEST_DATA" ]; then
	echo "Error: golden data file '$TEST_DATA' not found."
	echo "Ask your teacher to regenerate tests/golden_data.json."
	exit 1
fi

if [ ! -f "$EX_NAME/exercise.py" ]; then
	echo "Error: file '$EX_NAME/exercise.py' not found."
	echo "Check that the exercise folder exists and you are in the repo root."
	exit 1
fi

echo "Running local checks for exercise $NUM ($EX_NAME)"
echo

# Make repo root importable
export PYTHONPATH=.

# Run a small Python harness (no pytest needed)
python3 - <<'EOF'
import io
import json
import os
import sys
import importlib
from pathlib import Path

ex_name = os.environ.get("EX_NAME")
if not ex_name:
    print("Internal error: EX_NAME is not set")
    sys.exit(1)

golden_path = Path("tests/golden_data.json")
if not golden_path.exists():
    print("Error: tests/golden_data.json not found")
    sys.exit(1)

data = json.loads(golden_path.read_text())

if ex_name not in data:
    print(f"Error: no golden data for exercise '{ex_name}' in tests/golden_data.json")
    sys.exit(1)

cases = data[ex_name]

try:
    module = importlib.import_module(f"{ex_name}.exercise")
except ImportError as e:
    print(f"Error: could not import module '{ex_name}.exercise': {e}")
    sys.exit(1)

if not hasattr(module, "solve"):
    print(f"Error: '{ex_name}.exercise' has no function 'solve(username: str) -> None'")
    sys.exit(1)

solve = module.solve

def run_case(username: str) -> str:
    buf = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buf
    try:
        solve(username)
    finally:
        sys.stdout = old_stdout
    return buf.getvalue().strip()

failures = 0

print(f"Loaded {len(cases)} test cases for {ex_name}")
print("-" * 50)

for case in cases:
    username = case["username"]
    expected = case["expected"]
    got = run_case(username)

    if got == expected:
        status = "OK "
    else:
        status = "ERR"

    print(f"[{status}] username={username!r} expected={expected!r} got={got!r}")

    if got != expected:
        failures += 1

print("-" * 50)

if failures == 0:
    print("✅ All local tests passed for this exercise.")
    sys.exit(0)
else:
    print(f"❌ {failures} test(s) failed. Check your algorithm and try again.")
    sys.exit(1)
EOF

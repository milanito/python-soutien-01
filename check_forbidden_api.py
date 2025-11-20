#!/usr/bin/env python3

"""
Static check to forbid certain Python helpers for some exercises.

Usage (CI or local):

    python check_forbidden_api.py ex04_selection_sort

Return codes:
    0 = OK (no forbidden usage)
    1 = Error (something forbidden was found, or file missing)
"""

import ast
import sys
from pathlib import Path


# Configure which helpers are forbidden per exercise
# Keys are exercise folder names (ex01_sum, ex02_max_in_list, ...)
FORBIDDEN_CONFIG = {
    # ex01_sum: no restrictions – both loop and formula are fine

    "ex02_max_in_list": {
        # We want them to scan the list manually with a running maximum
        "calls": {"max", "sorted"},
        "methods": {"sort"},
        "in_operator": False,
    },

    "ex03_is_sorted": {
        # We want pairwise comparison, no "sorted(values)" trick
        "calls": {"sorted"},
        "methods": {"sort"},
        "in_operator": False,
    },

    "ex04_selection_sort": {
        # We want a real selection sort, no built-in sort, no min()
        "calls": {"sorted", "min"},
        "methods": {"sort"},
        "in_operator": False,
    },

    "ex05_binary_search": {
        # We want manual binary search over a sorted list
        # No built-in sort, no "target in values", no ".index"
        "calls": {"sorted"},
        "methods": {"sort", "index"},
        "in_operator": True,
    },

    # ex06_two_sum_closest: no restrictions for now
}

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python check_forbidden_api.py <exercise_folder_name>")
        print("Example: python check_forbidden_api.py ex04_selection_sort")
        return 1

    ex_name = sys.argv[1]
    config = FORBIDDEN_CONFIG.get(ex_name)

    # If no config, we consider everything allowed for this exercise
    if config is None:
        print(f"[check_forbidden_api] No specific rules for {ex_name}, skipping.")
        return 0

    file_path = Path(ex_name) / "exercise.py"
    if not file_path.exists():
        print(f"[check_forbidden_api] File not found: {file_path}")
        return 1

    source = file_path.read_text(encoding="utf-8")

    try:
        tree = ast.parse(source, filename=str(file_path))
    except SyntaxError as e:
        print(f"[check_forbidden_api] Syntax error in {file_path}: {e}")
        return 1

    forbidden_calls = config.get("calls", set())
    forbidden_methods = config.get("methods", set())
    forbid_in = config.get("in_operator", False)

    errors = []

    for node in ast.walk(tree):
        # Detect direct function calls: max(...), sorted(...), etc.
        if isinstance(node, ast.Call):
            # simple name: max(x), sorted(x)
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
                if func_name in forbidden_calls:
                    errors.append(
                        f"- Forbidden call to built-in '{func_name}()' at line {node.lineno}"
                    )

            # method call: something.sort(...)
            if isinstance(node.func, ast.Attribute):
                method_name = node.func.attr
                if method_name in forbidden_methods:
                    errors.append(
                        f"- Forbidden method call '.{method_name}()' at line {node.lineno}"
                    )

        # Detect usage of the "in" operator, for binary search exercise
        if forbid_in and isinstance(node, ast.Compare):
            # ops is a list; we look for ast.In or ast.NotIn
            for op in node.ops:
                if isinstance(op, (ast.In, ast.NotIn)):
                    errors.append(
                        f"- Forbidden use of 'in' / 'not in' operator at line {node.lineno}"
                    )

    if not errors:
        print(f"[check_forbidden_api] OK for {ex_name} (no forbidden usage found).")
        return 0

    print(f"[check_forbidden_api] Forbidden usage detected in {file_path}:")
    for err in errors:
        print(err)

    print(
        "\nPlease implement the intended algorithm manually "
        "(for example selection sort or binary search) instead of using these helpers."
    )

    return 1


if __name__ == "__main__":
    raise SystemExit(main())

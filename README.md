# Algorithm Practice – Python Quarter

This repository contains a series of algorithm exercises that you will solve in Python.

The goals are:

* Practice basic algorithms (loops, lists, search, sort, etc.)
* Focus on reasoning, not Python tricks or libraries
* Learn to work with Git, branches, Pull Requests and automated tests

All validation is done by automated tests that run in GitHub Actions when you open a Pull Request.

---

## Prerequisites

On your machine you should have:

* Git
* Python 3.10+ (3.12 on CI)
* vim or vi for edition

Optional but recommended:

* A virtual environment for your Python work

---

## Repository structure

At the root you will find something like:

```
algorithms-python-quarter/
  README.md
  run_exercise.sh

  ex01_sum/
    README.md
    __init__.py
    exercise.py

  ex02_max_in_list/
    README.md
    __init__.py
    exercise.py

  ex03_is_sorted/
    ...

  ex04_selection_sort/
  ex05_binary_search/
  ex06_two_sum_closest/

  tests/
    golden_data.json
    test_ex01.py
    test_ex02.py
    test_ex03.py
    test_ex04.py
    test_ex05.py
    test_ex06.py

  .github/
    workflows/
      exercises.yml
```

You will mostly work in the `exXX_*/exercise.py` files.

Do not modify anything in `tests/` or `.github/` unless instructed.

---

## Git workflow for each exercise

We use a strict branch naming convention to link a Pull Request to a specific exercise.

For exercise number `N` (for example `1`):

* Your branch name must be:
  `your.username@N`

Examples:

* `alice.dupont@1`
* `matthieu.rondeau@3`

For each exercise:

1. Make sure you are on `master` and up to date

   ```bash
   git checkout master
   git pull origin master
   ```

2. Create your exercise branch

   ```bash
   # Example for exercise 1
   git checkout -b your.username@1
   ```

3. Go to the exercise folder and read the instructions

   ```bash
   cd ex01_sum
   cat README.md
   ```

4. Implement the `solve(username: str) -> None` function in `exercise.py`

   * Do not change the function name or parameters
   * Print only the required output (no extra text, messages or debug prints)

5. Run tests locally (see next section)

6. Commit and push

   ```bash
   git add ex01_sum/exercise.py
   git commit -m "Solve exercise 1"
   git push origin your.username@1
   ```

7. Open a Pull Request on GitHub

   * Base branch: `master`
   * Compare branch: `your.username@1`

8. Wait for GitHub Actions

   * If checks are green: you can move on to the next exercise
   * If checks are red: read the logs, fix your code, commit and push again

Repeat the same flow for exercise 2 with branch `your.username@2`, and so on.

---

## Local testing

There are two ways to run tests locally.

### 1. Using the helper script `run_exercise.sh`

From the repository root:

```bash
# Make sure it is executable once
chmod +x run_exercise.sh

# Run tests for exercise 1
./run_exercise.sh 1

# Run tests for exercise 3
./run_exercise.sh 3
```

This script will:

* Check that the test file exists
* Set `PYTHONPATH=.` correctly
* Call `pytest tests/test_ex0N.py`

If tests fail, read the error messages. They will tell you what was expected and what your program printed.

### 2. Running tests manually

If you prefer to run pytest directly:

```bash
# From the repo root
export PYTHONPATH=.
pytest tests/test_ex01.py
pytest tests/test_ex03.py
```

You can also run your function manually to inspect its output:

```bash
python ex01_sum/exercise.py "your.username"
python ex04_selection_sort/exercise.py "validator"
```

---

## Structure of each exercise

Each exercise folder contains:

* `README.md` with the problem statement and learning goals
* `exercise.py` where you implement the `solve` function

The general shape is:

```python
def solve(username: str) -> None:
    """
    Reads the string `username` and prints the required result.

    Do NOT print extra text (no labels, no explanations).
    Only print the final answer expected by the tests.
    """
    # TODO: write your algorithm here
    pass


if __name__ == "__main__":
    import sys
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    solve(arg)
```

Important:

* The tests will import `solve` and call it with several different usernames.
* Your code must work for all of them, not only your own username.
* Do not change the function name or parameter.

---

## How the tests work

In the `tests/` directory:

* `golden_data.json` contains a list of test cases for each exercise:

  * Several usernames
  * The expected output for each username

* `test_ex01.py` … `test_ex06.py`:

  * Load the test cases from `golden_data.json`
  * For each username:

    * Capture what your `solve` function prints
    * Compare it with the expected output

You do not need to modify or understand these files to solve the exercises.
Just be aware that your solution is validated on several inputs.

---

## GitHub Actions (CI) behavior

There is a workflow file: `.github/workflows/exercises.yml`.

When you open a Pull Request:

1. The Action reads the name of your branch, for example `alice.dupont@3`.

2. It extracts the exercise number `3`.

3. It runs:

   ```bash
   pytest tests/test_ex03.py
   ```

4. If the tests pass:

   * The PR checks are green
   * You can move on to the next exercise

5. If the tests fail:

   * The PR checks are red
   * Click on the failed job to see the error messages
   * Fix your code and push again on the same branch

If the branch name does not follow the `username@N` format, the workflow may fail or run on the wrong test.

---

## Rules and constraints

* Focus on algorithms:

  * Use loops, conditions, and lists
  * No external libraries
* Do not change:

  * The function signature `def solve(username: str) -> None`
  * The tests in `tests/`
  * The workflow in `.github/`
* Do not print:

  * Debug messages
  * Explanations
  * Extra spaces or extra lines if the statement requires a precise format

For some exercises (for example selection sort and binary search), you are expected to implement the algorithm yourself, not to rely on built in helpers. If we detect that a solution bypasses the intended algorithm, the Pull Request may be rejected even if the output is correct.

---

## Typical workflow recap

For exercise 2 for example:

```bash
# 1. Update local master
git checkout master
git pull origin master

# 2. Create your branch for exercise 2
git checkout -b your.username@2

# 3. Implement the solution
#    Edit ex02_max_in_list/exercise.py

# 4. Run tests locally
./run_exercise.sh 2

# 5. Commit and push
git add ex02_max_in_list/exercise.py
git commit -m "Solve exercise 2"
git push origin your.username@2

# 6. Open PR on GitHub and check that CI is green
```

When the Pull Request is validated, you can start the next exercise.

Good luck and have fun practicing algorithms!

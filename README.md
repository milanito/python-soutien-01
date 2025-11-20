# Algorithm Practice – Quarter

This repository contains progressive algorithm exercises for the new Python quarter.

You will:

- Clone this repository
- Complete the exercises in order
- For each exercise N, create a branch named: `username@N`
  - Example: `matthieu.rondeau@3`
- Push the branch and open a Pull Request
- A GitHub Action will run tests for exercise N
- When the checks are green, you can move on to the next one

We focus on **algorithms**, not Python tricks. Use simple loops, conditions and lists.

## How to start

```bash
git clone <repo_url>
cd algorithms-python-quarter
```

For exercise N (for example N = 1):

```bash
git checkout master
git pull origin master

git checkout -b your.username@1
cd ex01_sum

# run your solution by giving your username as argument
python exercise.py "your.username"
```

You can also run the tests locally (optional but recommended):

```bash
pip install pytest
pytest tests/test_ex01.py
```

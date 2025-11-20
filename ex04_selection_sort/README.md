# ex04_selection_sort / README.md

## Exercise 4 — Implement selection sort

### Goal

Learn a fundamental O(n²) sorting algorithm.

### Instructions

You receive `username`.
Let `n = len(username)`.

Generate the same list as before:

```
values[i] = (i*n + 3) % 97
```

Sort the list **using selection sort only**.

Then print all numbers on one line, separated by a single space.
No extra spaces.

### Restrictions

Forbidden:

* `sorted()`
* `min()` inside your sorting loop
* `.sort()`

You must manually:

* For each position `i`, find the smallest element in `values[i:]`
* Swap it with `values[i]`

### Example

If the list is:

```
30 12 48 3
```

After selection sort it becomes:

```
3 12 30 48
```

Your output must be exactly:

```
3 12 30 48
```



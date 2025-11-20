# ex03_is_sorted / README.md

## Exercise 3 — Check if a list is sorted (non-decreasing)

### Goal

Learn to compare adjacent elements in a list.

### Instructions

You receive `username`.
Let `n = len(username)`.

Generate the same list as in exercise 2:

```
values[i] = (i*n + 3) % 97
```

Print:

* `1` if the list is **non-decreasing** (each element ≤ next)
* `0` otherwise

### Restrictions

You may **not** use `sorted()` or `.sort()`.
You must compare pairs manually.

### Example

If username = `abc` → length = 3

List:

```
3, 6, 9   (still increasing)
```

Output:

```
1
```

If the list had been `3, 9, 6` → it would not be sorted → output `0`.



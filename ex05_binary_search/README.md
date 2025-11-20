# ex05_binary_search / README.md

## Exercise 5 — Implement binary search

### Goal

Sort manually, then search manually using binary search.

### Instructions

You receive `username`.
Let `n = len(username)`.

Generate list:

```
values[i] = (i*n + 3) % 97
```

1. Sort it manually **(again: selection sort or your previous code)**
2. Compute:

```
target = (n * 42) % 97
```

3. Implement a **binary search** for `target`.

Print:

* `1` if found
* `0` otherwise

### Restrictions

Forbidden:

* `sorted()`
* `.sort()`
* `.index()`
* `if target in values:` (no membership operator)

### Example

If sorted list is:

```
3 12 21 30 39 48
```

and `target = 48` → output `1`.

If target does not appear → output `0`.


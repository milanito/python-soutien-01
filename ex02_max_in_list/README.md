# ex02_max_in_list / README.md

## Exercise 2 — Maximum value in a generated list

### Goal

Learn to build a list using a formula and scan it manually to find the maximum.

### Instructions

You receive a string `username`.
Let `n = len(username)`.

Construct a list:

```
values[i] = (i * n + 3) % 97
```

for each `i` from `0` to `n-1`.

Then print **the maximum value** in that list.

### Restrictions

You may **not** use `max()` or `sorted()` or `.sort()`.
Scan the list manually.

### Example

If username = `ab` → length = 2

List:

```
i=0 → (0*2+3)%97 = 3
i=1 → (1*2+3)%97 = 5
```

Maximum = `5`

Output:

```
5
```



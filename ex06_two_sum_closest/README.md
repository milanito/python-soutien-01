# ex06_two_sum_closest / README.md

## Exercise 6 — Two pointers: closest sum of two elements

### Goal

Learn the classic two-pointer technique on a sorted array.

### Instructions

You receive `username`.
Let `n = len(username)`.

Generate list:

```
values[i] = (i*n + 3) % 97
```

Sort it **manually** (as before).

Compute the target sum:

```
target_sum = (n*n + 13) % 150
```

Find two different elements whose sum is **closest** to `target_sum`.
If several sums are equally close, choose the first one you find using the two-pointer method.

Finally, print **that sum**.

### Two pointer method reminder

For a sorted list:

* Start with `i = 0`, `j = n-1`.
* Compute `current_sum = values[i] + values[j]`.
* Update best result if this sum is closer.
* If `current_sum < target_sum`: move `i` forward.
* Else if `current_sum > target_sum`: move `j` backward.
* Else: exact match → done.

### Example

Sorted list:

```
3 12 21 30 39 48 57
```

If target_sum = 50:

* 3+57 = 60 → diff 10
* 12+39 = 51 → diff 1 (best)
* 21+30 = 51 → diff 1
  Closest sum =


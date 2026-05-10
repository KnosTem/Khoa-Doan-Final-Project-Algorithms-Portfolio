# Chapter 11: Dynamic Programming

## Student Information
- **Name:** Khoa Doan
- **Date:** 04/26/2026
- **Course:** COSC 2436

---

## Algorithm Summary
- **How it works:** It builds a 2D grid where each cell `grid[i][w]` stores the best list of items using only the first `i` items within a weight budget of `w`. For each cell, it compares two options — including or excluding the current item — and keeps whichever yields the higher total value. Because each subproblem is solved once and stored, later cells can build on earlier results without recomputation.
- **Time complexity:** O(n × W), where n is the number of items and W is the knapsack capacity. Each of the n rows fills W cells, and each cell does constant-time work (one comparison).
- **When to use it:** Best suited for optimization problems with a fixed constraint (weight, budget, or time) where you must select a subset of items to maximize total value. Common real-world applications include resource allocation, cargo loading, and portfolio optimization.

---

## Test Results

**Program output** (6 items, capacity = 6 kg):
---
1           2           3           4           5           6
GUITAR          $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)
STEREO          $1500(G)    $1500(G)    $1500(G)    $3000(S)   $4500(GS)   $4500(GS)
LAPTOP          $1500(G)    $1500(G)    $2000(L)   $3500(GL)   $4500(GS)   $4500(GS)
iPHONE          $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
BOOK            $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
GOLD BAR       $30000(G)  $32000(iG) $33500(GiG) $33500(GiG) $34000(LiG)$35500(GLiG)
---
**Optimal result:**

| Capacity | Best Items                          | Total Weight | Total Value |
|----------|-------------------------------------|--------------|-------------|
| 6 kg     | GUITAR + LAPTOP + iPHONE + GOLD BAR | 6 kg         | $35,500     |

---

## Reflection Questions

1. **Why does the algorithm store lists of item names in each cell instead of just dollar values?**  
   Storing only the dollar value would tell us the optimal cost but not which items produced it, making path reconstruction impossible. By storing the actual list of names, each cell carries enough information to identify the winning combination, and we can simply read the bottom-right cell to recover the full solution without any backtracking step.

2. **Why is it important to slice-copy (`[:]`) lists when building `include_solution` and `exclude_solution`?**  
   Python lists are passed by reference, so without the slice copy, multiple grid cells would point to the same list object in memory. Appending an item name to one cell would silently mutate others that were already finalized, corrupting earlier rows. The `[:]` copy ensures each cell owns an independent list that cannot be accidentally modified by later iterations.

3. **Why does the BOOK row produce the same results as the iPHONE row?**  
   BOOK weighs 2 kg but is only worth $100, so it never improves on any combination the first four items already found. At every weight budget, leaving BOOK out and keeping the previous row's solution is strictly better. This illustrates a key property of the algorithm: items with poor value-to-weight ratios are naturally ignored without any special-case logic.

---

## Challenges Encountered

The trickiest part was understanding why slice-copying with `[:]` is required on every list read from the grid. Initially, assigning `include_solution = grid[i-1][w-weight] + [item_name]` without the copy seemed to work on small examples but produced corrupted results on later rows because earlier cells were being silently overwritten. Tracing through a two-item example by hand made the reference aliasing issue clear. Once every assignment had its own copy, the output matched the expected table exactly.

# Lab 1: Binary Search

## Student Information
- **Name:** Khoa Doan
- **Date:** 05/10/2026
- **Course:** COSC 2436

---

## Algorithm Summary

Linear search checks each element one by one from the start until it finds the target or exhausts the array. Binary search works only on sorted arrays — it repeatedly cuts the search space in half by comparing the target to the middle element and discarding the half that can't contain it.

- **Time Complexity:** Linear search O(n); Binary search O(log n)
- **Space Complexity:** O(1) for both — no extra memory beyond a few variables
- **When to use it:** Use binary search whenever the data is sorted and needed for fast lookups at scale. Use linear search for small or unsorted arrays where simplicity matters more than speed.

---

## Test Results

Searching in a sorted list of 128 numbers (values 1–128). Item 200 is not in the list.

| Target | Linear Result | Binary Result | Linear Time (s) | Binary Time (s) | Speedup |
|--------|---------------|---------------|-----------------|-----------------|---------|
| 1      | Index 0       | Index 0       | 0.00000167      | 0.00000286      | 0.58x   |
| 64     | Index 63      | Index 63      | 0.00000548      | 0.00000143      | 3.83x   |
| 128    | Index 127     | Index 127     | 0.00000381      | 0.00000215      | 1.78x   |
| 50     | Index 49      | Index 49      | 0.00000143      | 0.00000095      | 1.50x   |
| 100    | Index 99      | Index 99      | 0.00000405      | 0.00000191      | 2.12x   |
| 25     | Index 24      | Index 24      | 0.00000095      | 0.00000072      | 1.33x   |
| 75     | Index 74      | Index 74      | 0.00000167      | 0.00000119      | 1.40x   |
| 10     | Index 9       | Index 9       | 0.00000048      | 0.00000048      | 1.00x   |
| 90     | Index 89      | Index 89      | 0.00000215      | 0.00000095      | 2.25x   |
| 200    | None          | None          | 0.00000286      | 0.00000095      | 3.00x   |

**Lab Challenge:** The maximum number of steps for binary search on 128 items is log₂(128) = **7 steps**.

---

## Reflection Questions

1. **Why does binary search require a sorted array, but linear search does not?**  
   Binary search works by comparing the target to the middle element and discarding half the array based on whether the target is higher or lower. This logic only holds if the data is in order — in an unsorted array, eliminating half the elements would risk throwing away the answer. Linear search makes no assumptions about order and simply checks every element, so it works on any array.

2. **Why is binary search O(log n) instead of O(n)?**  
   Each iteration of binary search halves the remaining search space. Starting from 128 elements, the sizes are 64, 32, 16, 8, 4, 2, 1 — at most 7 steps. In general, the number of halvings needed to reach 1 element from n is log₂(n). Linear search, by contrast, may need to inspect every element in the worst case, giving O(n).

3. **The timing results show binary search is sometimes slower for small or early-hit searches. Why?**  
   For targets near the beginning of the array (like 1 or 10), linear search finds them in very few steps and returns immediately. Binary search always starts at the middle and takes several iterations even for easy cases, adding overhead. The O(log n) advantage of binary search only becomes significant as the array grows large — on 128 elements the difference is negligible, but on millions of elements it is dramatic.

---

## Challenges Encountered

The trickiest part was getting the boundary updates right in binary search. Setting `high = mid - 1` and `low = mid + 1` (rather than `mid`) is essential — without subtracting or adding 1, the loop can get stuck comparing the same middle element repeatedly and never terminate. Tracing through a small example by hand, watching `low` and `high` converge, made the logic clear.

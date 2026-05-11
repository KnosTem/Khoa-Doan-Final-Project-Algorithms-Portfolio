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


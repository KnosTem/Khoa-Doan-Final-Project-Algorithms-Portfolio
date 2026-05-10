# Lab 02: Selection Sort

- **Name:** Khoa Doan 
- **Date:** 05/10/2026

## Algorithm Summary

**Selection Sort** — O(n²) time, O(1) space

Finds the smallest element, swaps it to the front, then repeats for the remaining unsorted portion. Each pass does one fewer comparison, totaling n×(n−1)/2 — hence O(n²).


## Array vs. Linked List

| Operation | Array | Linked List | Why? |
|-----------|-------|-------------|------|
| Read      | O(1)  | O(n)        | Arrays use index math; linked lists traverse from head |
| Insert    | O(n)  | O(1)*       | Arrays shift elements; linked lists rewire pointers |
| Delete    | O(n)  | O(1)*       | Same as insert |


## Test Results

Selection Sort: 190 comparisons, 19 swaps

Smallest → McAllen: 142,210
Largest  → Houston: 2,304,580


## Reflection

1. **Why O(n²)?**\
   Two nested loops — for each of n positions, it scans all remaining elements. Total comparisons = n×(n−1)/2.

3. **Linked list over array?**\
   When inserting/deleting at the head frequently, or when size changes unpredictably.

5. **Why Python uses arrays by default?**\
    O(1) index access is the most common operation, and contiguous memory makes iteration fast. 

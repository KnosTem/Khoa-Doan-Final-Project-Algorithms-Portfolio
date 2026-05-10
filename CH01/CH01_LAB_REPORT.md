# Lab 01: Binary Search

## Student Information
- **Name:** Khoa Doan
- **Date:** 05/10/2026
- **Course:** COSC 2436
---
## Algorithm Summary

### Linear Search
Checks each element one by one. O(n) time. Use it when the data is unsorted, or you're only searching once (not worth sorting just for one lookup).

### Binary Search
Repeatedly halves a sorted array to find the target. O(log n) time. When the data is already sorted and you need to search it repeatedly. The larger the dataset, the bigger the payoff.
---
## Test Results
 | Target | Linear (ms) | Binary (ms) | Speedup |
 |--------|-------------|-------------|---------|
 |      1 |   0.00286   |   0.04482   |  0.06x  |
 |     10 |   0.00119   |   0.00095   |  1.25x  |
 |     25 |   0.00191   |   0.00286   |  0.67x  |
 |     50 |   0.00191   |   0.00143   |  1.33x  |
 |     64 |   0.00286   |   0.00095   |  3.00x  |
 |     75 |   0.00215   |   0.00191   |  1.12x  |
 |     90 |   0.00286   |   0.00119   |  2.40x  |
 |    100 |   0.00238   |   0.00095   |  2.50x  |
 |    128 |   0.00286   |   0.00167   |  1.71x  |
 |    200 |   0.06604   |   0.00215   | 30.78x  | (not found)

 Lab Challenge: log2(128) = 7 steps maximum

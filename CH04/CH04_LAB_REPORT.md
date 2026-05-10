# Lab 04: Quicksort

**Name:** [Your Name]  
**Date:** [Date]

## Quicksort Concepts

**Divide and Conquer:** Quicksort breaks the problem into smaller subproblems — pick a pivot, split the array into elements smaller and larger than it, then sort each half recursively.

**The Three Steps:**
1. **Choose pivot** — pick the first element as the reference point
2. **Partition** — split remaining elements into `less` (≤ pivot) and `greater` (> pivot)
3. **Recurse and combine** — sort each partition, then join: `quicksort(less) + [pivot] + quicksort(greater)`

## Tracing quicksort([3, 5, 2, 1, 4])

quicksort([3, 5, 2, 1, 4])
  pivot=3, less=[2, 1], greater=[5, 4]

  quicksort([2, 1])
    pivot=2, less=[1], greater=[]
    quicksort([1]) → [1]   ← base case
    quicksort([]) → []     ← base case
    result: [1] + [2] + [] = [1, 2]

  quicksort([5, 4])
    pivot=5, less=[4], greater=[]
    quicksort([4]) → [4]   ← base case
    quicksort([]) → []     ← base case
    result: [4] + [5] + [] = [4, 5]

  result: [1, 2] + [3] + [4, 5] = [1, 2, 3, 4, 5]


## Complexity Analysis

| Case    | Complexity | Why? |
|---------|------------|------|
| Best    | O(n log n) | Pivot splits the array evenly each time, giving log n levels of recursion, each doing O(n) work |
| Average | O(n log n) | Random data produces roughly balanced splits on average |
| Worst   | O(n²)      | Already-sorted data with first-element pivot creates one empty partition every time — n levels instead of log n |


## Reflection

1. **Already sorted + first-element pivot?** Worst case — every call puts all elements in `greater` and nothing in `less`, making n recursive calls instead of log n. Performance degrades to O(n²).

2. **Better pivot selection?** Pick a random element, or use the "median of three" (first, middle, last) to reduce the chance of hitting worst-case splits.

3. **Quicksort vs others?** Faster in practice than bubble sort (O(n²)) due to better cache behavior. Similar average speed to merge sort (both O(n log n)) but quicksort is in-place while merge sort needs extra memory.

4. **Why `array[1:]` not `array`?** The pivot is `array[0]`, so we only partition the *remaining* elements. Using `array` would include the pivot in both partitions, causing infinite recursion.

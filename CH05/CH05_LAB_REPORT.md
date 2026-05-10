# Lab 5: Hash Table

**Name:** Khoa Doan  
**Date:** 02/28/2026

## Key Concepts

**Hash table:** A data structure that stores key-value pairs. A hash function converts each key into an index, allowing near-instant lookups instead of scanning the whole list.

**Linear probing:** When two keys hash to the same index (collision), linear probing steps forward one slot at a time until an empty slot is found. The same stepping happens during search.


## Tracing Exercise

Starting with `HashTable(10)`, inserting apple, banana, orange (assume hash indices 1, 2, 1):

Insert "apple"  → hash=1, slot 1 empty   → table[1] = ("apple", 100)
Insert "banana" → hash=2, slot 2 empty   → table[2] = ("banana", 200)
Insert "orange" → hash=1, slot 1 taken   → probe slot 2, taken → probe slot 3
                                          → table[3] = ("orange", 300)


State after all insertions:

| Index | Contents |
|-------|----------|
| 0     | None |
| 1     | ("apple", 100) |
| 2     | ("banana", 200) |
| 3     | ("orange", 300) |
| 4–9   | None |


## Complexity Analysis

| Operation | Average Case | Worst Case |
|-----------|-------------|------------|
| Insert    | O(1)        | O(n)       |
| Search    | O(1)        | O(n)       |

Worst case happens when many keys collide and linear probing must scan most of the table.

## Reflection

1. **Advantages of hash tables?** Average O(1) insert and lookup — far faster than searching a list (O(n)) or a tree (O(log n)) for most use cases.

2. **How does the hash function affect performance?** A poor hash function clusters keys at the same indices, causing frequent collisions and degrading performance toward O(n). A good one distributes keys evenly.

3. **Other collision resolution techniques?** Chaining (each slot holds a linked list of entries), quadratic probing (step size grows quadratically), and double hashing (a second hash function determines the step size).

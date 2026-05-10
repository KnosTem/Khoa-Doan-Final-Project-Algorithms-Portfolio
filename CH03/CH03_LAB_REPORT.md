#Lab 3 Recursion
## Student Information
- **Name:** Khoa Doan
- **Date:** 02/15/2026

## Recursion Concepts

### Two Parts of Every Recursive Function
1. **Base Case:** [The stopping condition that prevents infinite recursion. It handles the simplest possible input and returns a value without making a recursive call.]
2. **Recursive Case:** [The part where the function calls itself with a smaller or simpler version of the problem, making progress toward the base case.]

### The Call Stack
[The call stack keeps track of function calls. Each recursive call adds a new layer to the stack. When the base case is reached, the stack unwinds as each function returns its result. ]

## Function Analysis

| Function | Base Case | Recursive Case | Time Complexity |
|----------|-----------|----------------|-----------------|
| countdown | i <= 0 | countdown(i-1) | O(n) |
| fact | x <= 1 | x * fact(x-1) | O(n) |
| recursive_sum | empty list | first + sum(rest) | O(n) |
| recursive_count | empty list | 1 + count(rest) | O(n) |
| recursive_max | single item | max(first, max(rest)) | O(n) |

## Reflection Questions

1. What happens if you forget the base case?
The function will call itself infinitely, leading to a stack overflow error

2. Why is the naive Fibonacci implementation inefficient?
The naive recursive Fibonacci recalculates the same values many time, creating exponential time complexity O(2^n)

3. Draw the call stack for fact(4).
fact(4)
    ->4*fact(3)
        ->3*fact(2)
            ->2*fact(1)
                ->return 1
            ->return 2*1 = 2
        ->return 3*2 = 6
    ->return 4*6 = 24

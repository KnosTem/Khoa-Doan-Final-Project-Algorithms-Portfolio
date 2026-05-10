# Lab 3: Recursion

## 1. Introduction and Objectives

### Overview
Explore recursion through classic examples: factorial, countdown, and sum. Understand the call stack and how to identify base cases vs recursive cases.

### Learning Objectives
- Understand recursion and the call stack
- Identify base case and recursive case
- Implement recursive functions
- Trace recursive calls mentally

### Prerequisites
- Complete Labs 1-2
- Read Chapter 3 in "Grokking Algorithms" (pages 41-54)

---

## 2. Algorithm Background

### Recursion Components
1. **Base Case** - When to stop (prevents infinite recursion)
2. **Recursive Case** - Function calls itself with smaller input

### The Call Stack
Each function call adds a frame to the stack:
```
factorial(3)
  → factorial(2)
      → factorial(1)
          → returns 1
      → returns 2 * 1 = 2
  → returns 3 * 2 = 6
```

---

## 3. Getting Started

### How to Access This Lab

1. Go to your **Section page** on StudySite.ai
2. Find **"Lab 03: Recursion"** in the Portfolio Assignments list
3. Click **"Start Coding"** to open the coding environment

### First Time Setup

When you open the lab for the first time:
1. You'll be prompted to **accept the GitHub Classroom assignment** — this creates your personal copy of the lab repository
2. Click **"Accept on GitHub"** and complete the process in the popup window
3. Once accepted, your starter code loads automatically into the editor

### Your Coding Workflow

The StudySite.ai coding environment gives you everything you need:

| Area | What It Does |
|------|-------------|
| **Code Editor** (left) | Edit your `recursion.py` and other files using the tabbed editor |
| **Terminal** (right) | See output when you click the Run button |
| **AI Tutor** (chat panel) | Ask Sherpa for help — it knows this lab and can guide you step by step |

**How to work on the lab:**

1. **Edit** your code in `recursion.py` (click the tab to switch files)
2. Click the **▶ Run** button to execute your code and see output in the terminal
3. Click the **Commit** button to save your work to GitHub and trigger the autograder
4. After a few moments, you'll see a ✅ (green check) or ❌ (red X) indicating whether your tests passed

> **Tip:** Commit early and often! Every commit triggers the autograder so you can see your progress as you implement each function.

---

## 4. Project Structure

```
lab03_recursion/
├── recursion.py              # YOUR WORK - implement recursive functions here
├── main.py                   # Tutorial & test runner - click Run to check your work
├── tests/test_recursion.py   # Automated tests (same tests the autograder uses)
├── Instructions/             # This file
└── README.md                 # Your lab report
```

---

## 5. Step-by-Step Implementation

Open the `recursion.py` tab and implement each function by following the TODO comments.

### Step 1: Implement `countdown`

```python
def countdown(i: int) -> None:
    """
    Print countdown from i to 0.
    Base case: i <= 0
    Recursive case: print i, then countdown(i-1)
    """
    # TODO: Implement countdown
    # 1. If i <= 0, print 0 and return
    # 2. Otherwise, print i
    # 3. Call countdown(i - 1)
```

**Solution approach:**
- Base case: when `i <= 0`, stop
- Recursive case: print `i`, then call `countdown(i - 1)`

### Step 2: Implement `fact`

```python
def fact(x: int) -> int:
    """
    Calculate factorial of x recursively.
    fact(5) = 5 * 4 * 3 * 2 * 1 = 120
    Base case: x == 1, return 1
    Recursive case: x * fact(x-1)
    """
    # TODO: Implement factorial
    # 1. If x <= 1, return 1 (base case)
    # 2. Otherwise, return x * fact(x - 1)
```

**Solution approach:**
- Base case: when `x <= 1`, return `1`
- Recursive case: return `x * fact(x - 1)`

### Step 3: Implement `recursive_sum`

```python
def recursive_sum(arr: List[int]) -> int:
    """
    Sum all elements in array recursively.
    Base case: empty array, return 0
    Recursive case: first element + sum of rest
    """
    # TODO: Implement recursive sum
    # 1. If array is empty, return 0 (base case)
    # 2. Otherwise, return arr[0] + recursive_sum(arr[1:])
```

**Solution approach:**
- Base case: empty list → return `0`
- Recursive case: `arr[0] + recursive_sum(arr[1:])`
- `arr[1:]` is a slice containing everything except the first element

### Step 4: Implement `recursive_count`

```python
def recursive_count(arr: List) -> int:
    """
    Count elements in array recursively.
    Base case: empty array, return 0
    Recursive case: 1 + count of rest
    """
    # TODO: Implement recursive count
    # 1. If array is empty, return 0 (base case)
    # 2. Otherwise, return 1 + recursive_count(arr[1:])
```

**Solution approach:**
- Base case: empty list → return `0`
- Recursive case: `1 + recursive_count(arr[1:])`

### Step 5: Implement `recursive_max`

```python
def recursive_max(arr: List[int]) -> int:
    """
    Find maximum element recursively.
    Base case: single element, return it
    Recursive case: max of (first, max of rest)
    """
    # TODO: Implement recursive max
    # 1. If len(arr) == 1, return arr[0] (base case)
    # 2. Get rest_max = recursive_max(arr[1:])
    # 3. Return arr[0] if arr[0] > rest_max else rest_max
```

**Solution approach:**
- Base case: single element → return `arr[0]`
- Recursive case: compare `arr[0]` with `recursive_max(arr[1:])`

---

## 6. Testing Your Code

### Test Locally

Click the `main.py` tab, then click the **▶ Run** button. You'll see ✅ or ❌ for each function in the terminal output.

### Submit for Grading

1. Click the **Commit** button in the editor toolbar
2. Enter a commit message (e.g., "Implement factorial and recursive_sum")
3. The autograder runs automatically on GitHub
4. Look for ✅ (green check) or ❌ (red X) — you can commit as many times as you need

---

## 7. Tracing Recursive Calls

### Factorial Example: `fact(5)`

```
fact(5)
  → 5 * fact(4)
    → 4 * fact(3)
      → 3 * fact(2)
        → 2 * fact(1)
          → returns 1        ← Base case!
        → returns 2 * 1 = 2
      → returns 3 * 2 = 6
    → returns 4 * 6 = 24
  → returns 5 * 24 = 120
```

### Recursive Sum Example: `recursive_sum([2, 4, 6])`

```
recursive_sum([2, 4, 6])
  → 2 + recursive_sum([4, 6])
    → 4 + recursive_sum([6])
      → 6 + recursive_sum([])
        → returns 0           ← Base case!
      → returns 6 + 0 = 6
    → returns 4 + 6 = 10
  → returns 2 + 10 = 12
```

---

## 8. Autograding

Your code is graded automatically each time you click **Commit**. The autograder runs these tests:

| Test | What It Checks |
|------|---------------|
| `test_fact_1` | `fact(1)` returns 1 |
| `test_fact_5` | `fact(5)` returns 120 |
| `test_fact_3` | `fact(3)` returns 6 |
| `test_sum_basic` | `recursive_sum([2, 4, 6])` returns 12 |
| `test_sum_empty` | `recursive_sum([])` returns 0 |
| `test_sum_single` | `recursive_sum([42])` returns 42 |
| `test_count_basic` | `recursive_count([1,2,3,4,5])` returns 5 |
| `test_count_empty` | `recursive_count([])` returns 0 |
| `test_max_basic` | `recursive_max([3,7,2,9,1])` returns 9 |
| `test_max_single` | `recursive_max([42])` returns 42 |
| `test_max_first` | `recursive_max([99,1,2,3])` returns 99 |

**Total: 11 tests, 100 points**

---

## 9. Lab Report

After completing the code, click the `README.md` tab and fill in your lab report:

```markdown
# Lab 3: Recursion

## Student Information
- **Name:** [Your Name]
- **Date:** [Date]

## Recursion Concepts

### Two Parts of Every Recursive Function
1. **Base Case:** [Explain]
2. **Recursive Case:** [Explain]

### The Call Stack
[Explain how the call stack works with an example]

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

2. Why is the naive Fibonacci implementation inefficient?

3. Draw the call stack for fact(4).
```

---

## 10. Submission Checklist

- [ ] All 5 functions implemented in `recursion.py`
- [ ] Click **▶ Run** on `main.py` — all functions show ✅
- [ ] Click **Commit** — autograder shows ✅ (green check)
- [ ] Lab report completed in `README.md`
- [ ] Final commit with completed lab report

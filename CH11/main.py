# ===========================================================================
# Knapsack Problem — Dynamic Programming
# ---------------------------------------------------------------------------
# Follow Instructions.md step by step. There are 11 TODOs total.
# Replace each "TODO N" block with the code shown in the instructions.
# Do NOT change the items list or the capacity at the bottom.
# ===========================================================================


# ---------------------------------------------------------------------------
# PART 1 — helper function
# ---------------------------------------------------------------------------
def calculate_total_value(solution, items):
    """
    Add up the dollar value of every item name in `solution`.

    Parameters
    ----------
    solution : list[str]
        A list of item names, e.g. ["GUITAR", "LAPTOP"].
    items : list[tuple[str, int, int]]
        The full (name, weight, value) list.

    Returns
    -------
    int
        Sum of values for every name found in `solution`.
    """
    # TODO 1 — implement this helper (see Instructions Part 1).
    total = 0
    for name in solution:
        for item_name, weight, value in items:
            if item_name == name:
                total += value
                break
    return total


# ---------------------------------------------------------------------------
# PART 2 — fill the DP grid
# ---------------------------------------------------------------------------
def knapsack(items, capacity):
    """
    Build a 2D grid where grid[i][w] is the best list of item names
    using only the first i items and a weight budget of w.
    """
    n = len(items)
    # grid[i][w] starts empty; we'll fill it row by row.
    grid = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, weight, value = items[i - 1]
        for w in range(1, capacity + 1):
            if weight > w:
                # TODO 2 — this item is too heavy; copy the cell directly above.
                grid[i][w] = grid[i - 1][w][:]
            else:
                # TODO 3 — build the two candidate solutions (each is a LIST of names).
                include_solution = grid[i - 1][w - weight][:] + [item_name]
                exclude_solution = grid[i - 1][w][:]

                # TODO 4 — compute each candidate's dollar value (each is an INTEGER).
                include_value = calculate_total_value(include_solution, items)
                exclude_value = calculate_total_value(exclude_solution, items)

                # TODO 5 — store whichever solution has the higher value in grid[i][w].
                if include_value > exclude_value:
                    grid[i][w] = include_solution
                else:
                    grid[i][w] = exclude_solution

    return grid


# ---------------------------------------------------------------------------
# PART 3 — pretty-print the grid
# ---------------------------------------------------------------------------
def display_grid(grid, items):
    n = len(items)
    cell_width = 12

    # TODO 6 — build the header row of capacity numbers (1..capacity),
    # each right-aligned in cell_width characters.
    header = ""
    for w in range(1, len(grid[0])):
        header += "{:>{width}}".format(str(w), width=cell_width)

    print(" " * cell_width + header)

    for i in range(1, n + 1):
        # TODO 7 — start each data row with the item name, LEFT-aligned in cell_width.
        row = "{:<{width}}".format(items[i - 1][0], width=cell_width)

        for cell in grid[i][1:]:
            if cell:
                # TODO 8 — format this non-empty cell as "$VALUE(LETTERS)",
                # right-aligned in cell_width.
                letters = "".join(name[0] for name in cell)
                value = calculate_total_value(cell, items)
                row += "{:>{width}}".format("${}({})".format(value, letters), width=cell_width)
            else:
                # TODO 9 — append blank space so empty cells still take cell_width chars.
                row += " " * cell_width

        print(row)


# ---------------------------------------------------------------------------
# PART 4 — run it
# ---------------------------------------------------------------------------
# Test data — do NOT modify these values.
items = [
    ("GUITAR", 1, 1500),
    ("STEREO", 4, 3000),
    ("LAPTOP", 3, 2000),
    ("iPHONE", 1, 2000),
    ("BOOK", 2, 100),
    ("GOLD BAR", 1, 30000),
]

capacity = 6

# TODO 10 — call knapsack(items, capacity) and store the result in `grid`.
grid = knapsack(items, capacity)

# TODO 11 — uncomment the line below to display the finished grid.
display_grid(grid, items)

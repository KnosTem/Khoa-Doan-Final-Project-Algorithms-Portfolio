# Lab 09: Dijkstra's Algorithm 

## Student Information
- **Name:** Khoa Doan
- **Date:** 04/12/2026
- **Course:** COSC 2436

---

## Algorithm Summary
- **How it works:** Dijkstra's algorithm finds the shortest path in a weighted graph by always processing the unvisited node with the lowest known cost first. It maintains a cost table initialized to infinity for all nodes except the start (set to 0), and updates costs whenever a cheaper route is discovered. A parent table records where each node was reached from, allowing the full path to be reconstructed at the end.
- **Time complexity:** O(V²) with a linear scan for the minimum node; O((V + E) log V) with a min-heap/priority queue.
- **When to use it:** Best suited for finding shortest paths in weighted, non-negative graphs — such as road networks, network routing, or any problem where edges have costs and you need the cheapest route from one node to another.

---

## Test Results

**Graph used:** Nodes A, B, C, D — Edges: A-B(1), A-C(4), B-C(2), B-D(6), C-D(3)

| Start | End | Shortest Path | Total Cost |
|-------|-----|---------------|------------|
| A | D | A → B → C → D | 6 |
| A | C | A → B → C | 3 |
| A | B | A → B | 1 |
| B | D | B → C → D | 5 |

**Disconnected test:** Adding isolated node E with no edges — `costs[E]` stays `∞`, program correctly prints "No path found."

**Algorithm trace (A → D):**

| Iteration | Current | costs[A] | costs[B] | costs[C] | costs[D] | Processed |
|-----------|---------|----------|----------|----------|----------|-----------|
| Init | — | 0 | ∞ | ∞ | ∞ | [] |
| 1 | A | 0 | 1 | 4 | ∞ | [A] |
| 2 | B | 0 | 1 | 3 | 7 | [A, B] |
| 3 | C | 0 | 1 | 3 | 6 | [A, B, C] |
| 4 | D | 0 | 1 | 3 | 6 | [A, B, C, D] |

---

## Reflection Questions

1. **Why does the algorithm initialize all node costs to infinity except the start node?**  
   Infinity acts as a placeholder meaning "not yet reachable." The start node is set to 0 because it costs nothing to already be there. Any real path cost will be lower than infinity, so the first time a neighbor is reached its cost is updated — without infinity as the default, the comparisons that drive updates would have no valid baseline.

2. **Why do we store edges in both directions?**  
   Because the graph is undirected — a road between two cities works both ways. Storing only `graph[a][b]` makes the graph effectively directed, so paths that require traversing an edge "backwards" would never be discovered, producing wrong or missing results.

3. **How does the `parents` dictionary allow path reconstruction?**  
   Each time a cheaper route to a node is found, `parents[neighbor] = node` records which node we arrived from, creating a chain of backwards pointers to the start. To reconstruct the path we start at the end and follow `parents` until we reach the start, then reverse the collected list to get the correct start-to-end sequence.

---

## Challenges Encountered

The trickiest part was tracking the path alongside the cost updates. A basic Dijkstra's only computes minimum costs, so storing `parents` to record where each node was reached from — and then walking backwards from destination to start to reconstruct the route — required careful bookkeeping. Understanding why the path list needs to be reversed at the end (because we collect it from end to start) helped clarify how the parent chain works.

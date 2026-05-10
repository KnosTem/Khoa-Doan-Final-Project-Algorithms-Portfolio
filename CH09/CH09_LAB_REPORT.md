# Chapter 9: Dijkstra's Algorithm — Lab Report

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

## Core Data Structures

| Structure | Variable | What It Stores |
|-----------|----------|----------------|
| Adjacency dict | `graph` | Maps each node to a dict of its neighbors and edge weights |
| Cost table | `costs` | Cheapest known total cost to reach each node from start |
| Parent table | `parents` | Which node we came from on the cheapest known route |
| Visited set | `processed` | Nodes whose shortest path is finalized and won't be revisited |

---

## Algorithm Trace

Graph: A-B(1), A-C(4), B-C(2), B-D(6), C-D(3) — tracing from A to D.

| Iteration | Current | costs[A] | costs[B] | costs[C] | costs[D] | Processed |
|-----------|---------|----------|----------|----------|----------|-----------|
| Init | — | 0 | ∞ | ∞ | ∞ | [] |
| 1 | A | 0 | 1 | 4 | ∞ | [A] |
| 2 | B | 0 | 1 | 3 | 7 | [A, B] |
| 3 | C | 0 | 1 | 3 | 6 | [A, B, C] |
| 4 | D | 0 | 1 | 3 | 6 | [A, B, C, D] |

**Shortest path:** A → B → C → D  
**Total cost:** 6

---

## Reflection Questions

1. **Why does the algorithm initialize all node costs to infinity except the start node?**  
   Infinity acts as a placeholder meaning "not yet reachable." The start node is set to 0 because it costs nothing to already be there. Any real path cost will be lower than infinity, so the first time a neighbor is reached its cost is updated — without infinity as the default, the comparisons that drive updates would have no valid baseline.

2. **Why must all edge weights be non-negative for Dijkstra's to work?**  
   Dijkstra's assumes that once a node is marked as processed, its cost is finalized. A negative edge weight could allow a path through a later node to retroactively produce a cheaper route to an already-processed node, violating this assumption and causing incorrect results. The Bellman-Ford algorithm handles negative weights instead.

3. **Why do we store edges in both directions?**  
   Because the graph is undirected — a road between two cities works both ways. Storing only `graph[a][b]` makes the graph effectively directed, so paths that require traversing an edge "backwards" would never be discovered, producing wrong or missing results.

4. **How would a priority queue improve performance?**  
   `find_lowest_cost_node()` scans every node on every iteration, making it O(V) per call and O(V²) overall. A min-heap always has the smallest element at the top, so the minimum extraction is O(log V) rather than O(V) — this matters significantly for large graphs with many nodes and edges.

5. **How does the `parents` dictionary allow path reconstruction?**  
   Each time a cheaper route to a node is found, `parents[neighbor] = node` records which node we arrived from, creating a chain of backwards pointers to the start. To reconstruct the path we start at the end and follow `parents` until we reach the start, then reverse the collected list to get the correct start-to-end sequence.

6. **What happens when source and destination are disconnected?**  
   The algorithm processes every reachable node from the start without ever updating the destination's cost, so it stays at `float("inf")`. The code checks for this and returns `None, None`, which the `main()` function catches to print "No path found."

---

## Challenges Encountered

The trickiest part was tracking the path alongside the cost updates. A basic Dijkstra's only computes minimum costs, so storing `parents` to record where each node was reached from — and then walking backwards from destination to start to reconstruct the route — required careful bookkeeping. Understanding why the path list needs to be reversed at the end (because we collect it from end to start) helped clarify how the parent chain works.

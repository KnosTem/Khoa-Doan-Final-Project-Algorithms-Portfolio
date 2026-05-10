# Lab 06: Breadth-First Search


- **Name:** Khoa Doan  
- **Date:** 03/08/2026
- **Course:** COSC 2436
---
## Graph Concepts

**Adjacency List:** Each city keeps a list of its direct neighbors. Space-efficient for sparse graphs and O(1) to add an edge.

**BFS Algorithm Steps:**
1. Add the start node to a queue and mark it visited
2. Dequeue a node, check if it's the destination
3. Add all unvisited neighbors to the queue and mark them visited
4. Repeat until destination is found or queue is empty

---
## Test Results
```
| Start   | End      | Path                            | Edges |
|---------|----------|---------------------------------|-------|
| Houston | El Paso  | Houston → San Antonio → El Paso | 2     |
| Houston | McKinney | Houston → Dallas → Plano → McKinney | 3 |
| Dallas  | Laredo   | Dallas → Austin → San Antonio → Laredo | 3 |
```
---
## Reflection

1. **Why a queue, not a stack?**  
BFS uses a queue so it explores all nodes at distance 1 before distance 2. A stack would dive deep down one path first, which doesnt guarantee the shortest path.

2. **BFS shortest path vs actual distance?**  
BFS counts the fewest edges, not real-world distance. Houston → El Paso is 2 hops in the graph but over 700 miles in reality. For actual distances, use Dijkstra's algorithm.

3. **BFS vs DFS?**  
Use BFS for shortest path by hops. Use DFS when you just need to know if a path exists or want to explore all possible routes.


## Challenges
The trickiest part was tracking the path alongside the BFS traversal. A basic BFS only visits nodes, so I had to store the full path in the queue as a list alongside each node so I could return the complete route when the destination was reached.

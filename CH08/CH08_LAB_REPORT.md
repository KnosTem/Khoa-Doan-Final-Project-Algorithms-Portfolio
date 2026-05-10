# Lab 08: Balanced Trees

### Student Information
- **Name:** Khoa Doan
- **Date:** 04/04/2026
- **Course:** COSC 2436

### Algorithm Analysis
---
#### AVL Trees
- **Balance Factor Range:** -1, 0, or 1
- **Why rebalance?** An unbalanced BST can degrade to O(n) for all operations.
  efficient operations regardless of insertion order
- **Time Complexity (all operations):** O(log n)
---
#### Rotation Cases
| Case | Imbalance                              | Fix                                      |
|------|----------------------------------------|------------------------------------------|
| LL   | Left-heavy; new node in left-left      | Single right rotation                    |
| RR   | Right-heavy; new node in right-right   | Single left rotation                     |
| LR   | Left-heavy; new node in left-right     | Left rotate left child, then right rotate|
| RL   | Right-heavy; new node in right-left    | Right rotate right child, then left rotate|
---
1. **Why is an unbalanced BST bad?**  
   In the worst case (e.g., inserting already-sorted data), a plain BST becomes a linear chain.
   Every operation — search, insert, delete — degrades from O(log n) to O(n), which defeats the
   purpose of using a tree over a list.

2. **How do rotations maintain the BST property?**  
   Rotations only rewire parent-child pointers; they never move a node past a node with a value
   between them. Because the relative left/right ordering of every node is preserved, the
   BST invariant (left < parent < right) holds after every rotation.

3. **What other self-balancing trees exist?**  
   Red-Black Trees (used in most standard library maps), Splay Trees (self-adjusting via splaying
   recently accessed nodes to the root), B-Trees and B+ Trees (used in databases and filesystems
   for disk-friendly branching), and 2-3 Trees are the most common alternatives.

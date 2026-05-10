# Lab 07: Binary Trees

### Student Information
- **Name:** [Khoa Doan]
- **Date:** [03/28/2026]
- **Course:** COSC 2436
---
### Algorithm Analysis

#### Binary Search Tree
- **Search Time (balanced):** O(log n)
- **Search Time (unbalanced):** O(n)
- **BST Property:** A binary search tree maintains the property that for each node, all elements in the left subtree are less, and all elements in the right subtree are greater.

#### Traversals
| Traversal | Order | Use Case |
|-----------|-------|----------|
| Preorder  | Root, Left, Right | Copying a tree |
| Inorder   | Left, Root, Right | Getting sorted elements |
| Postorder | Left, Right, Root | Deleting a tree |
---
### Reflection Questions

1. Why does inorder traversal give sorted output?
   - Inorder traversal visits nodes in ascending order for a binary search tree, as it processes the left subtree, then the node, and finally the right subtree.

2. When would a BST become unbalanced?
   - A BST becomes unbalanced when nodes are inserted in a sorted order, leading to a linear structure similar to a linked list.

3. What's the difference between BFS and DFS for trees?
   - BFS explores nodes level by level using a queue, while DFS explores as deep as possible along each branch before backtracking, typically using recursion or a stack.

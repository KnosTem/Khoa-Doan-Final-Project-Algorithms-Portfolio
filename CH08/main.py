"""
Lab 08: Balanced Trees
Implement AVL tree from Chapter 8.

Chapter 8 covers:
- BST problems (unbalanced = O(n))
- AVL Trees (self-balancing)
- Splay Trees
- B-Trees
"""
from typing import Optional, Any, List


class AVLNode:
    """AVL tree node with height tracking."""
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height: int = 1


class AVLTree:
    """Self-balancing AVL tree."""
    
    def __init__(self):
        self.root: Optional[AVLNode] = None
    
    def height(self, node: Optional[AVLNode]) -> int:
        """Get height of node (None = 0)."""
        # TODO: Return node.height if node exists, else 0
        return node.height if node else 0
    
    def balance_factor(self, node: AVLNode) -> int:
        """
        Calculate balance factor: height(left) - height(right)
        
        From Chapter 8:
        - Balance factor of -1, 0, or 1 is balanced
        - Other values require rotation
        """
        # TODO: Return height(left) - height(right)
        return self.height(node.left) - self.height(node.right)
    
    def rotate_right(self, y: AVLNode) -> AVLNode:
        r"""
        Right rotation for left-heavy tree.
        
            y                x
           / \              / \
          x   C    -->     A   y
         / \                  / \
        A   B                B   C
        """
        # TODO: Implement right rotation
        x = y.left
        B = x.right

        # Perform rotation
        x.right = y
        y.left = B

        # Update heights (y first, since it's now lower)
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x
    
    def rotate_left(self, x: AVLNode) -> AVLNode:
        """Left rotation for right-heavy tree."""
        # TODO: Implement left rotation
        y = x.right
        B = y.left

        # Perform rotation
        y.left = x
        x.right = B

        # Update heights (x first, since it's now lower)
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y
    
    def insert(self, value: Any) -> None:
        """Insert value and rebalance."""
        self.root = self._insert(self.root, value)
    
    def _insert(self, node: Optional[AVLNode], value: Any) -> AVLNode:
        """Recursive insert with rebalancing."""
        # TODO: Implement AVL insert
        # 1. Standard BST insert
        # 2. Update height
        # 3. Check balance factor
        # 4. Rotate if needed (4 cases: LL, RR, LR, RL)
        # Step 1: Standard BST insert
        if not node:
            return AVLNode(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        # Step 2: Update height of current node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # Step 3: Check balance factor
        balance = self.balance_factor(node)

        # Step 4: Rotate if needed — 4 cases

        # LL Case: left-heavy and new value went into left subtree's left side
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        # RR Case: right-heavy and new value went into right subtree's right side
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        # LR Case: left-heavy but new value went into left subtree's right side
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # RL Case: right-heavy but new value went into right subtree's left side
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
    
    def inorder(self) -> List[Any]:
        """Return sorted values."""
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node: Optional[AVLNode], result: List) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

if __name__ == "__main__":
    tree = AVLTree()
    for val in [10, 20, 5, 4, 15]:
        tree.insert(val)
    print("Inorder traversal:", tree.inorder())

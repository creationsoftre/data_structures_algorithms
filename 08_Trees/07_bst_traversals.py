# ============================================================
# BST Traversals
# ============================================================
#
# Traversal means visiting every node in the tree.
#
# A BST stores values using this rule:
#
#   smaller values go left
#   larger values go right
#
# But traversal is about the order we visit the nodes.
#
# ------------------------------------------------------------
# TREE USED IN THIS FILE
# ------------------------------------------------------------
#
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
#
# ------------------------------------------------------------
# MAIN TRAVERSAL TYPES
# ------------------------------------------------------------
#
# 1. Inorder traversal
#
#      left -> root -> right
#
#    For a BST, this prints values in sorted order.
#
#    Output:
#
#      2, 5, 7, 10, 12, 15, 20
#
# ------------------------------------------------------------
#
# 2. Preorder traversal
#
#      root -> left -> right
#
#    Useful when you want to copy or save the tree structure.
#
#    Output:
#
#      10, 5, 2, 7, 15, 12, 20
#
# ------------------------------------------------------------
#
# 3. Postorder traversal
#
#      left -> right -> root
#
#    Useful when deleting/freeing a tree because children are
#    handled before the parent.
#
#    Output:
#
#      2, 7, 5, 12, 20, 15, 10
#
# ------------------------------------------------------------
#
# 4. Level order traversal
#
#      Visit nodes level by level from top to bottom.
#
#    Output:
#
#      10, 5, 15, 2, 7, 12, 20
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# All traversals:
#
#   O(n)
#
# Speed:
#   Linear.
#
# Why?
#   Every traversal visits every node once.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Recursive traversals:
#
#   O(h)
#
# Why?
#   Recursion uses the call stack.
#
# h = height of the tree
#
# Balanced tree:
#
#   O(log n)
#
# Unbalanced tree:
#
#   O(n)
#
# Level order traversal:
#
#   O(w)
#
# w = maximum width of the tree
#
# Why?
#   The queue may hold many nodes from the same level.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Inorder traversal is special for a BST.
#
# Why?
#   It visits:
#
#      smaller values first
#      then the root
#      then larger values
#
# So it gives the values in sorted order.
# ============================================================


from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # --------------------------------------------------------
    # Insert
    # --------------------------------------------------------
    #
    # We include insert so we can build a BST for traversal.
    # --------------------------------------------------------

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return

                current = current.left

            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return

                current = current.right

            else:
                return

    # --------------------------------------------------------
    # Inorder traversal
    # --------------------------------------------------------
    #
    # Order:
    #
    #   left -> root -> right
    #
    # For a BST, this prints values in sorted order.
    #
    # Example:
    #
    #              10
    #            /    \
    #           5      15
    #          / \    /  \
    #         2   7  12   20
    #
    # Steps:
    #
    #   Visit left side of 10: 2, 5, 7
    #   Visit 10
    #   Visit right side of 10: 12, 15, 20
    #
    # Output:
    #
    #   2, 5, 7, 10, 12, 15, 20
    # --------------------------------------------------------

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is None:
            return

        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._inorder_recursive(node.right, result)

    # --------------------------------------------------------
    # Preorder traversal
    # --------------------------------------------------------
    #
    # Order:
    #
    #   root -> left -> right
    #
    # This visits the root before the children.
    #
    # Output:
    #
    #   10, 5, 2, 7, 15, 12, 20
    # --------------------------------------------------------

    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node is None:
            return

        result.append(node.value)
        self._preorder_recursive(node.left, result)
        self._preorder_recursive(node.right, result)

    # --------------------------------------------------------
    # Postorder traversal
    # --------------------------------------------------------
    #
    # Order:
    #
    #   left -> right -> root
    #
    # This visits children before the parent.
    #
    # Output:
    #
    #   2, 7, 5, 12, 20, 15, 10
    # --------------------------------------------------------

    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node is None:
            return

        self._postorder_recursive(node.left, result)
        self._postorder_recursive(node.right, result)
        result.append(node.value)

    # --------------------------------------------------------
    # Level order traversal
    # --------------------------------------------------------
    #
    # Order:
    #
    #   top to bottom
    #   left to right
    #
    # This uses a queue.
    #
    # Output:
    #
    #   10, 5, 15, 2, 7, 12, 20
    # --------------------------------------------------------

    def level_order(self):
        result = []

        if self.root is None:
            return result

        queue = deque()
        queue.append(self.root)

        while len(queue) > 0:
            current = queue.popleft()
            result.append(current.value)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        return result

    # --------------------------------------------------------
    # Traversals with explanation
    # --------------------------------------------------------

    def explain_inorder(self):
        print("Inorder Traversal")
        print("=" * 60)
        print("Order:")
        print("left -> root -> right")
        print()
        print("For a BST, this gives sorted order.")
        print()
        print("Tree:")
        self.print_tree_visual()
        print()
        print("Result:")
        print(self.inorder())
        print()

    def explain_preorder(self):
        print("Preorder Traversal")
        print("=" * 60)
        print("Order:")
        print("root -> left -> right")
        print()
        print("This visits the root before the children.")
        print()
        print("Tree:")
        self.print_tree_visual()
        print()
        print("Result:")
        print(self.preorder())
        print()

    def explain_postorder(self):
        print("Postorder Traversal")
        print("=" * 60)
        print("Order:")
        print("left -> right -> root")
        print()
        print("This visits children before the parent.")
        print()
        print("Tree:")
        self.print_tree_visual()
        print()
        print("Result:")
        print(self.postorder())
        print()

    def explain_level_order(self):
        print("Level Order Traversal")
        print("=" * 60)
        print("Order:")
        print("top to bottom, left to right")
        print()
        print("This uses a queue.")
        print()
        print("Tree:")
        self.print_tree_visual()
        print()
        print("Result:")
        print(self.level_order())
        print()

    # --------------------------------------------------------
    # Print tree visually
    # --------------------------------------------------------
    #
    # This prints the tree with / and \.
    #
    # It works best for small trees.
    # --------------------------------------------------------

    def print_tree_visual(self):
        if self.root is None:
            print("Tree is empty.")
            return

        lines = self._build_tree_lines(self.root)

        for line in lines:
            print(line)

    def _build_tree_lines(self, node):
        if node is None:
            return []

        node_text = str(node.value)

        if node.left is None and node.right is None:
            return [node_text]

        left_lines = self._build_tree_lines(node.left)
        right_lines = self._build_tree_lines(node.right)

        left_width = max(len(line) for line in left_lines) if left_lines else 0
        right_width = max(len(line) for line in right_lines) if right_lines else 0

        left_lines = [line.ljust(left_width) for line in left_lines]
        right_lines = [line.ljust(right_width) for line in right_lines]

        root_line = " " * left_width + node_text + " " * right_width

        branch_line = ""

        if node.left is not None:
            branch_line += " " * (left_width - 1) + "/"
        else:
            branch_line += " " * left_width

        branch_line += " " * len(node_text)

        if node.right is not None:
            branch_line += "\\"
        else:
            branch_line += " "

        branch_line += " " * (right_width - 1)

        child_lines = []
        max_child_lines = max(len(left_lines), len(right_lines))

        for i in range(max_child_lines):
            if i < len(left_lines):
                left_part = left_lines[i]
            else:
                left_part = " " * left_width

            if i < len(right_lines):
                right_part = right_lines[i]
            else:
                right_part = " " * right_width

            child_lines.append(left_part + " " * len(node_text) + right_part)

        return [root_line, branch_line] + child_lines


# ------------------------------------------------------------
# Build the BST
# ------------------------------------------------------------

bst = BinarySearchTree()

values = [10, 5, 15, 2, 7, 12, 20]

for value in values:
    bst.insert(value)


print("BST Traversals")
print("=" * 60)
print()

print("Starting Tree")
print("-" * 60)
bst.print_tree_visual()
print()


# ------------------------------------------------------------
# Traversal examples
# ------------------------------------------------------------

bst.explain_inorder()
bst.explain_preorder()
bst.explain_postorder()
bst.explain_level_order()


# ------------------------------------------------------------
# Quick summary
# ------------------------------------------------------------

print("Traversal Summary")
print("=" * 60)

print("Inorder:")
print("left -> root -> right")
print("Sorted order for a BST.")
print(bst.inorder())
print()

print("Preorder:")
print("root -> left -> right")
print("Good for copying/saving tree structure.")
print(bst.preorder())
print()

print("Postorder:")
print("left -> right -> root")
print("Good for deleting/freeing a tree.")
print(bst.postorder())
print()

print("Level order:")
print("top to bottom, left to right")
print("Uses a queue.")
print(bst.level_order())
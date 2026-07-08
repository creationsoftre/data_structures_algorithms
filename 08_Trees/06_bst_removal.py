# ============================================================
# BST Removal
# ============================================================
#
# Removing from a Binary Search Tree is harder than searching
# or inserting because we may need to reconnect nodes.
#
# BST rule:
#
#   smaller values go left
#   larger values go right
#
# When removing a node, we must keep that rule true.
#
# ------------------------------------------------------------
# THREE REMOVAL CASES
# ------------------------------------------------------------
#
# Case 1:
#   Remove a leaf node.
#
#   A leaf has no children.
#
#   Example:
#
#              10
#            /    \
#           5      15
#          /
#         2
#
#   Remove 2.
#
#   Since 2 has no children, just delete it.
#
# ------------------------------------------------------------
#
# Case 2:
#   Remove a node with one child.
#
#   Example:
#
#              10
#            /    \
#           5      15
#          /
#         2
#
#   Remove 5.
#
#   Node 5 has one child: 2.
#
#   Replace 5 with 2.
#
# ------------------------------------------------------------
#
# Case 3:
#   Remove a node with two children.
#
#   Example:
#
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
#
#   Remove 10.
#
#   Node 10 has two children.
#
#   We need a replacement value.
#
#   Common choice:
#
#       Use the smallest value from the right subtree.
#
#   This is called the inorder successor.
#
#   Right subtree of 10:
#
#              15
#             /  \
#            12   20
#
#   Smallest value in that subtree is 12.
#
#
#   Full Tree After 12 replaces 10.
#         12
#       /    \
#      5      15
#     / \       \
#    2   7       20
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Remove in a balanced BST:
#
#   O(log n)
#
# Speed:
#   Fast.
#
# Why?
#   We follow one path down the tree.
#
# Remove in an unbalanced BST:
#
#   O(n)
#
# Speed:
#   Slow.
#
# Why?
#   The tree can become a chain.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Recursive removal:
#
#   O(h)
#
# h = height of the tree
#
# Balanced tree:
#
#   h = log n
#
# Unbalanced tree:
#
#   h = n
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# The hardest case is removing a node with two children.
#
# Why?
#   We cannot simply delete it because it has two subtrees
#   connected to it.
#
# Fix:
#   Replace it with the inorder successor.
#
# Inorder successor:
#   The smallest value in the node's right subtree.
# ============================================================

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
    # We include insert so we can build a tree to test removal.
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
    # Remove
    # --------------------------------------------------------
    #
    # This starts the remove process.
    #
    # We call a helper because removal is easier with recursion.
    # --------------------------------------------------------

    def remove(self, value):
        self.root = self._remove_recursive(self.root, value)

    # --------------------------------------------------------
    # Remove recursive helper
    # --------------------------------------------------------
    #
    # This function returns the updated subtree root.
    #
    # That matters because removing a node may change which node
    # should be connected to the parent.
    # --------------------------------------------------------

    def _remove_recursive(self, node, value):
        # Base case:
        # If node is None, the value was not found.
        if node is None:
            return None

        # If value is smaller, search the left subtree.
        if value < node.value:
            node.left = self._remove_recursive(node.left, value)
            return node

        # If value is larger, search the right subtree.
        if value > node.value:
            node.right = self._remove_recursive(node.right, value)
            return node

        # If we get here, node.value == value.
        # This is the node we want to remove.

        # ----------------------------------------------------
        # Case 1: Node has no children
        # ----------------------------------------------------
        #
        # Example:
        #
        #   Remove 2
        #
        #       5
        #      /
        #     2
        #
        # 2 has no children.
        # Return None to disconnect it.
        # ----------------------------------------------------

        if node.left is None and node.right is None:
            return None

        # ----------------------------------------------------
        # Case 2A: Node has only a right child
        # ----------------------------------------------------
        #
        # Example:
        #
        #   Remove 15
        #
        #       15
        #         \
        #          20
        #
        # Replace 15 with 20.
        # ----------------------------------------------------

        if node.left is None:
            return node.right

        # ----------------------------------------------------
        # Case 2B: Node has only a left child
        # ----------------------------------------------------
        #
        # Example:
        #
        #   Remove 5
        #
        #       5
        #      /
        #     2
        #
        # Replace 5 with 2.
        # ----------------------------------------------------

        if node.right is None:
            return node.left

        # ----------------------------------------------------
        # Case 3: Node has two children
        # ----------------------------------------------------
        #
        # Example:
        #
        #              10
        #            /    \
        #           5      15
        #                 /
        #                12
        #
        # Remove 10.
        #
        # 10 has two children.
        #
        # Find the smallest value on the right side.
        #
        # That value is 12.
        #
        # Replace 10 with 12.
        # Then remove the old 12 node from the right subtree.
        # ----------------------------------------------------

        successor = self._find_min(node.right)

        # Replace the current node's value with the successor value.
        node.value = successor.value

        # Remove the duplicate successor node from the right subtree.
        node.right = self._remove_recursive(node.right, successor.value)

        return node

    # --------------------------------------------------------
    # Find minimum value
    # --------------------------------------------------------
    #
    # In a BST, smaller values are always on the left.
    #
    # So to find the minimum value:
    #
    #   keep going left
    #
    # The leftmost node is the smallest.
    # --------------------------------------------------------

    def _find_min(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    # --------------------------------------------------------
    # Print tree visually
    # --------------------------------------------------------
    #
    # This prints the tree with / and \.
    #
    # It works best for small trees.
    # --------------------------------------------------------

    def print_tree_visual(self):
        print("Current BST:")
        print("-" * 60)

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

    # --------------------------------------------------------
    # Remove with explanation
    # --------------------------------------------------------

    def remove_with_steps(self, value):
        print(f"Remove {value}")
        print("=" * 60)

        print("Before removal:")
        self.print_tree_visual()
        print()

        self.remove(value)

        print("After removal:")
        self.print_tree_visual()
        print()


# ------------------------------------------------------------
# Build the BST
# ------------------------------------------------------------

bst = BinarySearchTree()

values = [10, 5, 15, 2, 7, 12, 20]

for value in values:
    bst.insert(value)

print("BST Removal Examples")
print("=" * 60)
print()

print("Starting tree:")
bst.print_tree_visual()
print()


# ------------------------------------------------------------
# Case 1: Remove a leaf node
# ------------------------------------------------------------

print("Case 1: Remove a leaf node")
print("-" * 60)
print("Remove 2.")
print("2 has no children, so it can be deleted directly.")
print()

bst.remove_with_steps(2)


# ------------------------------------------------------------
# Case 2: Remove a node with one child
# ------------------------------------------------------------
#
# Add 1 under 5 so we can show a one-child removal clearly.
# After removing 2, node 5 has children 7 only.
# So removing 5 means 7 replaces 5.
# ------------------------------------------------------------

print("Case 2: Remove a node with one child")
print("-" * 60)
print("Remove 5.")
print("5 has one child: 7.")
print("So 7 moves up and replaces 5.")
print()

bst.remove_with_steps(5)


# ------------------------------------------------------------
# Case 3: Remove a node with two children
# ------------------------------------------------------------

print("Case 3: Remove a node with two children")
print("-" * 60)
print("Remove 10.")
print("10 has two children.")
print("We replace 10 with the smallest value in the right subtree.")
print()
print("Right subtree of 10:")
print("15")
print("/")
print("12")
print()
print("Smallest value on the right side is 12.")
print("So 12 replaces 10.")
print()

bst.remove_with_steps(10)
# ============================================================
# BST Height and Insertion Order
# ============================================================
#
# A Binary Search Tree can be fast or slow depending on its shape.
#
# The shape depends on the order values are inserted.
#
# ------------------------------------------------------------
# IMPORTANT IDEA
# ------------------------------------------------------------
#
# Same values, different insert order, different tree shape.
#
# Values:
#
#   1, 2, 3, 4, 5, 6, 7
#
# Bad insertion order:
#
#   1, 2, 3, 4, 5, 6, 7
#
# Better insertion order:
#
#   4, 2, 6, 1, 3, 5, 7
#
# ------------------------------------------------------------
# BAD INSERTION ORDER
# ------------------------------------------------------------
#
# Insert values in sorted order:
#
#   1, 2, 3, 4, 5, 6, 7
#
# The BST becomes:
#
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#          \
#           5
#            \
#             6
#              \
#               7
#
# This tree is technically still a BST.
#
# But it is shaped like a linked list.
#
# Search for 7:
#
#   1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
#
# That checks 7 nodes.
#
# Time Complexity:
#
#   O(n)
#
# Speed:
#   Slow.
#
# ------------------------------------------------------------
# BETTER INSERTION ORDER
# ------------------------------------------------------------
#
# Insert values in this order:
#
#   4, 2, 6, 1, 3, 5, 7
#
# The BST becomes:
#
#              4
#            /   \
#           2     6
#          / \   / \
#         1   3 5   7
#
# Search for 7:
#
#   4 -> 6 -> 7
#
# That checks 3 nodes.
#
# Time Complexity:
#
#   O(log n)
#
# Speed:
#   Fast.
#
# ------------------------------------------------------------
# WHY BALANCED IS FASTER
# ------------------------------------------------------------
#
# Balanced tree:
#
#              4
#            /   \
#           2     6
#          / \   / \
#         1   3 5   7
#
# Each step removes about half of the remaining tree.
#
# Search for 7:
#
#   Start at 4.
#   7 > 4, so skip the entire left side.
#
#   Now at 6.
#   7 > 6, so go right.
#
#   Now at 7.
#   Found it.
#
# We skipped:
#
#   2, 1, 3, 5
#
# ------------------------------------------------------------
# HEIGHT COMPARISON
# ------------------------------------------------------------
#
# Balanced tree with 7 nodes:
#
#              4
#            /   \
#           2     6
#          / \   / \
#         1   3 5   7
#
# Levels:
#
#   Level 1: 4
#   Level 2: 2, 6
#   Level 3: 1, 3, 5, 7
#
# Height:
#
#   2
#
# Why?
#   Height counts edges, not levels.
#
#   4 -> 6 -> 7
#
#   4 to 6 = 1 edge
#   6 to 7 = 1 edge
#
#   height = 2
#
# ------------------------------------------------------------
#
# Unbalanced tree with 7 nodes:
#
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#          \
#           5
#            \
#             6
#              \
#               7
#
# Height:
#
#   6
#
# Why?
#   Longest path:
#
#   1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
#
#   That path has 6 edges.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Balanced BST:
#
#   Search: O(log n)
#   Insert: O(log n)
#   Remove: O(log n)
#
# Speed:
#   Fast.
#
# Why?
#   The tree height is short.
#
# ------------------------------------------------------------
#
# Unbalanced BST:
#
#   Search: O(n)
#   Insert: O(n)
#   Remove: O(n)
#
# Speed:
#   Slow.
#
# Why?
#   The tree height can become almost the same as the number
#   of nodes.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Storing the BST:
#
#   O(n)
#
# Why?
#   We store n nodes.
#
# Recursive operations:
#
#   O(h)
#
# h = height of the tree
#
# Balanced:
#
#   h = log n
#
# Unbalanced:
#
#   h = n
#
# ------------------------------------------------------------
# MAIN TAKEAWAY
# ------------------------------------------------------------
#
# A BST does not automatically stay balanced.
#
# If values are inserted in sorted order, the BST can become slow.
#
# Same values:
#
#   1, 2, 3, 4, 5, 6, 7
#
# Bad order:
#
#   1, 2, 3, 4, 5, 6, 7
#
# Better order:
#
#   4, 2, 6, 1, 3, 5, 7
#
# Same data.
# Different shape.
# Different speed.
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
    # Search with step count
    # --------------------------------------------------------
    #
    # This counts how many nodes are checked during search.
    # --------------------------------------------------------

    def search_with_count(self, target):
        current = self.root
        comparisons = 0

        while current is not None:
            comparisons += 1

            if target == current.value:
                return True, comparisons

            elif target < current.value:
                current = current.left

            else:
                current = current.right

        return False, comparisons

    # --------------------------------------------------------
    # Height
    # --------------------------------------------------------
    #
    # Height counts edges from root to deepest leaf.
    #
    # A tree with one node has height 0.
    #
    # Empty tree returns -1 so a leaf node becomes:
    #
    #   1 + max(-1, -1)
    #   1 + -1
    #   0
    # --------------------------------------------------------

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1

        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)

        return 1 + max(left_height, right_height)

    # --------------------------------------------------------
    # Print tree visually
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
# Build an unbalanced BST
# ------------------------------------------------------------

unbalanced_bst = BinarySearchTree()

bad_order = [1, 2, 3, 4, 5, 6, 7]

for value in bad_order:
    unbalanced_bst.insert(value)


# ------------------------------------------------------------
# Build a balanced-looking BST
# ------------------------------------------------------------

balanced_bst = BinarySearchTree()

better_order = [4, 2, 6, 1, 3, 5, 7]

for value in better_order:
    balanced_bst.insert(value)


# ------------------------------------------------------------
# Compare both trees
# ------------------------------------------------------------

print("BST Height and Insertion Order")
print("=" * 60)
print()

print("Same values:")
print("1, 2, 3, 4, 5, 6, 7")
print()

print("Bad insertion order:")
print(bad_order)
print()

print("Unbalanced BST:")
print("-" * 60)
unbalanced_bst.print_tree_visual()
print()

print("Height explanation:")
print("Height starts at 0 and counts edges.")
print("The longest path is:")
print("1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7")
print("That path has 6 edges.")
print(f"Unbalanced tree height: {unbalanced_bst.height()}")
print()

found, comparisons = unbalanced_bst.search_with_count(7)

print("Search for 7 in unbalanced BST:")
print("Path:")
print("1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7")
print(f"Found: {found}")
print(f"Comparisons: {comparisons}")
print()

print("=" * 60)
print()

print("Better insertion order:")
print(better_order)
print()

print("Balanced-looking BST:")
print("-" * 60)
balanced_bst.print_tree_visual()
print()

print("Height explanation:")
print("Height starts at 0 and counts edges.")
print("The longest path is:")
print("4 -> 6 -> 7")
print("That path has 2 edges.")
print(f"Balanced tree height: {balanced_bst.height()}")
print()

found, comparisons = balanced_bst.search_with_count(7)

print("Search for 7 in balanced-looking BST:")
print("Path:")
print("4 -> 6 -> 7")
print(f"Found: {found}")
print(f"Comparisons: {comparisons}")
print()

print("=" * 60)
print("Main Takeaway")
print("=" * 60)

print("A BST can be fast or slow depending on its shape.")
print()
print("Sorted insert order can create a chain.")
print("That makes search O(n).")
print()
print("A balanced shape keeps the tree short.")
print("That makes search O(log n).")
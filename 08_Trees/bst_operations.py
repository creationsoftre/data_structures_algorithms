# ============================================================
# BST Operations - Search and Insert
# ============================================================
#
# A Binary Search Tree uses this rule:
#
#   smaller values go left
#   larger values go right
#
# Because of this rule, we do not always need to check every node.
#
# ------------------------------------------------------------
# SIMPLE BST EXAMPLE
# ------------------------------------------------------------
#
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
#
# Search for 12:
#
#   Start at 10.
#   12 > 10, so go right.
#
#   Now at 15.
#   12 < 15, so go left.
#
#   Now at 12.
#   Found it.
#
# We skipped:
#
#   5, 2, 7, 20
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Search in a balanced BST:
#
#   O(log n)
#
# Speed:
#   Fast.
#
# Why?
#   Each comparison removes about half of the remaining tree.
#
# Insert in a balanced BST:
#
#   O(log n)
#
# Speed:
#   Fast.
#
# Why?
#   Insert follows the same left/right path as search.
#
# ------------------------------------------------------------
# WORST CASE
# ------------------------------------------------------------
#
# Search in an unbalanced BST:
#
#   O(n)
#
# Insert in an unbalanced BST:
#
#   O(n)
#
# Speed:
#   Slow.
#
# Why?
#   The tree can become a chain.
#
# Example:
#
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#
# Searching for 4 checks:
#
#   1 -> 2 -> 3 -> 4
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
# Iterative search:
#
#   O(1)
#
# Why?
#   We only use a few variables.
#
# Recursive search:
#
#   O(h)
#
# Why?
#   Recursive calls use the call stack.
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
# BST speed depends on tree height.
#
# Short tree:
#   Faster search.
#
# Tall chain-like tree:
#   Slower search.
# ============================================================

class Node:
    def __init__(self, value):
        # Store the value inside the node.
        self.value = value

        # Smaller values go on the left.
        self.left = None

        # Larger values go on the right.
        self.right = None


class BinarySearchTree:
    def __init__(self):
        # The root is the first node in the tree.
        #
        # If root is None, the tree is empty.
        self.root = None

# --------------------------------------------------------
    # Insert
    # --------------------------------------------------------
    #
    # Insert adds a new value into the BST.
    #
    # Rule:
    #
    #   If new value is smaller, go left.
    #   If new value is larger, go right.
    #
    # Time Complexity:
    #
    #   Balanced tree:   O(log n)
    #   Unbalanced tree: O(n)
    # --------------------------------------------------------

    def insert(self, value):
        new_node = Node(value)

        # If the tree is empty, the new node becomes the root.
        if self.root is None:
            self.root = new_node
            return

        # Start at the root.
        current = self.root

        while True:
            # If the new value is smaller, go left.
            if value < current.value:

                # If there is no left child, insert here.
                if current.left is None:
                    current.left = new_node
                    return

                # Otherwise, keep moving left.
                current = current.left

            # If the new value is larger, go right.
            elif value > current.value:

                # If there is no right child, insert here.
                if current.right is None:
                    current.right = new_node
                    return

                # Otherwise, keep moving right.
                current = current.right

            else:
                # If the value already exists, do nothing.
                #
                # This simple BST does not allow duplicates.
                return


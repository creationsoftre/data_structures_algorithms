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


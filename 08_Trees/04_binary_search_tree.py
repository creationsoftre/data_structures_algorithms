# ============================================================
# Binary Search Tree Basics
# ============================================================
#
# A Binary Search Tree is also called a BST.
#
# A BST is a special type of binary tree.
#
# Binary tree rule:
#
#   Each node has at most two children.
#
# BST rule:
#
#   Smaller values go to the left.
#   Larger values go to the right.
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
# For node 10:
#
#   Values smaller than 10 go left.
#   Values larger than 10 go right.
#
# Left side of 10:
#
#   5, 2, 7
#
# Right side of 10:
#
#   15, 12, 20
#
# ------------------------------------------------------------
# IMPORTANT BST RULE
# ------------------------------------------------------------
#
# The BST rule applies to every node, not just the root.
#
# Example:
#
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
#
# For node 5:
#
#   2 is smaller than 5, so it goes left.
#   7 is larger than 5, so it goes right.
#
# For node 15:
#
#   12 is smaller than 15, so it goes left.
#   20 is larger than 15, so it goes right.
#
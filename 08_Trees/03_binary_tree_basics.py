# ============================================================
# Binary Tree Basics
# ============================================================
#
# A binary tree is a tree where each node has at most two children.
#
# The two children are usually called:
#
#   left child
#   right child
#
# Example:
#
#              A
#            /   \
#           B     C
#          / \     \
#         D   E     F
#
# A is the root.
# B is A's left child.
# C is A's right child.
# D and E are children of B.
# F is the right child of C.
#
# ------------------------------------------------------------
# BINARY TREE RULE
# ------------------------------------------------------------
#
# A binary tree does not have to be sorted.
#
# The only rule is:
#
#   Each node can have at most two children.
#
# This is different from a Binary Search Tree.
#
# Binary Tree:
#
#   At most two children.
#
# Binary Search Tree:
#
#   At most two children,
#   AND smaller values go left,
#   AND larger values go right.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Searching a normal binary tree:
#
#   O(n)
#
# Speed:
#   Can be slow.
#
# Why?
#   A regular binary tree has no sorting rule.
#   The value could be anywhere.
#   We may need to check every node.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Storing the tree:
#
#   O(n)
#
# Why?
#   A tree with n nodes stores n node objects.
#
# Recursive traversal:
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
# A binary tree is a structure.
#
# A binary search tree is a structure plus an ordering rule.
#
# Do not assume a binary tree is sorted.
# ============================================================
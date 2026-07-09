# ============================================================
# AVL Trees - High Level Notes
# ============================================================
#
# An AVL Tree is a self-balancing Binary Search Tree.
#
# It follows the normal BST rule:
#
#   smaller values go left
#   larger values go right
#
# But it adds one extra rule:
#
#   The tree must stay balanced.
#
# ------------------------------------------------------------
# WHY AVL TREES EXIST
# ------------------------------------------------------------
#
# A normal BST can become slow if values are inserted in sorted order.
#
# Example:
#
#   Insert:
#   1, 2, 3, 4, 5
#
# Normal BST:
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
#
# This becomes a chain.
#
# Search becomes:
#
#   O(n)
#
# Speed:
#   Slow.
#
# AVL trees fix this by rotating nodes to keep the tree balanced.
#
# ------------------------------------------------------------
# AVL TREE RULE
# ------------------------------------------------------------
#
# Every node has a balance factor.
#
# Balance factor:
#
#   balance_factor = height(left subtree) - height(right subtree)
#
# A node is balanced if its balance factor is:
#
#   -1, 0, or 1
#
# That means:
#
#   -1 = right side is taller by 1
#    0 = both sides are the same height
#    1 = left side is taller by 1
#
# If the balance factor becomes:
#
#   less than -1
#   or
#   greater than 1
#
# then the AVL tree is unbalanced and needs a rotation.
#
# ------------------------------------------------------------
# SIMPLE BALANCE EXAMPLE
# ------------------------------------------------------------
#
# Balanced:
#
#       10
#      /  \
#     5    15
#
# left height = 0
# right height = 0
#
# balance_factor = left height - right height
# balance_factor = 0 - 0
# balance_factor = 0
#
# This is balanced.
#
# ------------------------------------------------------------
# UNBALANCED EXAMPLE
# ------------------------------------------------------------
#
#       10
#      /
#     5
#    /
#   2
#
# For node 10:
#
# left height = 1
# right height = -1
#
# balance_factor = left height - right height
# balance_factor = 1 - (-1)
# balance_factor = 2
#
# 2 is greater than 1, so this node is unbalanced.
#
# The AVL tree must rotate.
#
# ------------------------------------------------------------
# ROTATIONS
# ------------------------------------------------------------
#
# A rotation rearranges nodes while keeping the BST rule true.
#
# Rotations are how AVL trees rebalance themselves.
#
# There are 4 common rotation cases:
#
#   1. Left Left case
#   2. Right Right case
#   3. Left Right case
#   4. Right Left case
#
# ------------------------------------------------------------
# LEFT LEFT CASE
# ------------------------------------------------------------
#
# Happens when the tree is too heavy on the left-left side.
#
# Example:
#
#       30
#      /
#     20
#    /
#   10
#
# Fix:
#
#   Right rotation.
#
# After rotation:
#
#       20
#      /  \
#     10   30
#
# ------------------------------------------------------------
# RIGHT RIGHT CASE
# ------------------------------------------------------------
#
# Happens when the tree is too heavy on the right-right side.
#
# Example:
#
#   10
#     \
#      20
#        \
#         30
#
# Fix:
#
#   Left rotation.
#
# After rotation:
#
#       20
#      /  \
#     10   30
#
# ------------------------------------------------------------
# LEFT RIGHT CASE
# ------------------------------------------------------------
#
# Happens when the tree is too heavy on the left-right side.
#
# Example:
#
#       30
#      /
#     10
#       \
#        20
#
# Fix:
#
#   1. Left rotation on 10
#   2. Right rotation on 30
#
# After rotation:
#
#       20
#      /  \
#     10   30
#
# ------------------------------------------------------------
# RIGHT LEFT CASE
# ------------------------------------------------------------
#
# Happens when the tree is too heavy on the right-left side.
#
# Example:
#
#   10
#     \
#      30
#     /
#    20
#
# Fix:
#
#   1. Right rotation on 30
#   2. Left rotation on 10
#
# After rotation:
#
#       20
#      /  \
#     10   30
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# AVL search:
#
#   O(log n)
#
# Speed:
#   Fast.
#
# Why?
#   The tree stays balanced.
#
# AVL insert:
#
#   O(log n)
#
# Speed:
#   Fast.
#
# Why?
#   We search for the insert spot, insert the node, then rebalance.
#
# AVL remove:
#
#   O(log n)
#
# Speed:
#   Fast.
#
# Why?
#   We remove the node, then rebalance if needed.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Storing the AVL tree:
#
#   O(n)
#
# Why?
#   We store n nodes.
#
# Recursive operations:
#
#   O(log n)
#
# Why?
#   The height stays balanced, so the call stack stays short.
#
# ------------------------------------------------------------
# AVL VS NORMAL BST
# ------------------------------------------------------------
#
# Normal BST:
#
#   Simple to code.
#   Can become unbalanced.
#   Worst-case search is O(n).
#
# AVL Tree:
#
#   More complex to code.
#   Keeps itself balanced.
#   Search stays O(log n).
#
# ------------------------------------------------------------
# MAIN TAKEAWAY
# ------------------------------------------------------------
#
# An AVL tree is a BST that refuses to become too tall on one side.
#
# It checks balance factors after insertions and removals.
#
# If a node becomes unbalanced, the tree uses rotations to fix itself.
#
# The point of AVL trees is to keep search, insert, and remove fast:
#
#   O(log n)
# ============================================================
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
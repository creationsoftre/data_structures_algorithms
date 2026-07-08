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
# ------------------------------------------------------------
# WHY BST SEARCH CAN BE FAST
# ------------------------------------------------------------
#
# A regular binary tree is not sorted.
#
# So if we search for a value, we may need to check every node.
#
# Regular binary tree search:
#
#   O(n)
#
# A BST is sorted by a rule.
#
# At each node, we can decide which side to search.
#
# If target is smaller:
#
#   go left
#
# If target is larger:
#
#   go right
#
# That means we can ignore about half of the tree each step,
# if the tree is balanced.
#
# Balanced BST search:
#
#   O(log n)
#
# ------------------------------------------------------------
# SEARCH EXAMPLE
# ------------------------------------------------------------
#
# Search for 12:
#
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
#
# Step 1:
#
#   Start at 10.
#
#   12 > 10
#
#   Go right.
#
# Step 2:
#
#   Now at 15.
#
#   12 < 15
#
#   Go left.
#
# Step 3:
#
#   Now at 12.
#
#   Found it.
#
# We only checked:
#
#   10 -> 15 -> 12
#
# We did not check:
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
#   Each step removes about half of the remaining nodes.
#
# Insert in a balanced BST:
#
#   O(log n)
#
# Speed:
#   Fast.
#
# Why?
#   We follow the same left/right rule to find the open spot.
#
# Remove in a balanced BST:
#
#   O(log n)
#
# Speed:
#   Fast, but removal has more cases.
#
# Why?
#   We first search for the node, then rearrange links.
#
# ------------------------------------------------------------
# WORST CASE
# ------------------------------------------------------------
#
# A BST can become slow if values are inserted in sorted order.
#
# Example:
#
# Insert:
#
#   1, 2, 3, 4, 5
#
# The tree becomes:
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
# This is basically a linked list.
#
# Search becomes:
#
#   O(n)
#
# Speed:
#   Slow.
#
# Why?
#   We may need to move through every node one at a time.
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
#   The tree stores n nodes.
#
# Recursive search / insert:
#
#   O(h)
#
# h = height of the tree
#
# Balanced BST:
#
#   h = log n
#
# Unbalanced BST:
#
#   h = n
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# A BST is only fast when it stays balanced.
#
# Balanced tree:
#
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
#
# Search is fast because the tree spreads out.
#
# Unbalanced tree:
#
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#
# Search is slow because the tree is shaped like a chain.
# ============================================================


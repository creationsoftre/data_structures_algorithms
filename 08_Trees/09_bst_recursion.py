# ============================================================
# BST Recursion
# ============================================================
#
# Recursion means a function calls itself.
#
# Trees work well with recursion because each part of a tree is
# also a smaller tree.
#
# Example:
#
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
#
# The whole tree starts at 10.
#
# But the left side is also a tree:
#
#           5
#          / \
#         2   7
#
# And the right side is also a tree:
#
#           15
#          /  \
#         12   20
#
# This is why recursion fits trees.
#
# ------------------------------------------------------------
# RECURSION IDEA
# ------------------------------------------------------------
#
# A recursive tree function usually has:
#
#   1. Base case
#   2. Work on current node
#   3. Recursive call on left child
#   4. Recursive call on right child
#
# ------------------------------------------------------------
# BASE CASE
# ------------------------------------------------------------
#
# The base case tells recursion when to stop.
#
# For trees, the base case is usually:
#
#   if node is None:
#       stop
#
# Why?
#   None means we went past a leaf node.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Recursive traversal:
#
#   O(n)
#
# Speed:
#   Linear.
#
# Why?
#   We visit every node one time.
#
# Recursive search in a balanced BST:
#
#   O(log n)
#
# Speed:
#   Fast.
#
# Why?
#   Each step goes left or right, not both.
#
# Recursive search in an unbalanced BST:
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
# Recursive functions use the call stack.
#
# Space complexity:
#
#   O(h)
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
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Recursion does not always mean O(n).
#
# The time depends on how many nodes the function visits.
#
# Traversal visits every node:
#
#   O(n)
#
# BST search follows one path:
#
#   O(log n) average
#   O(n) worst case
# ============================================================
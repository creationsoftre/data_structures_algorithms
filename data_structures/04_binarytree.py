## TIME COMPLEXITY:
# Big O describes how the work grows as the amount of data grows.
#
# From fastest to slower:
# O(1)     -> Constant time
#             The operation takes about the same amount of work no matter how much data exists.
#
# O(log n) -> Logarithmic time
#             The operation gets faster than O(n) because the data is split into smaller parts.
#
# O(n)     -> Linear time
#             The operation gets slower as the amount of data grows because you may need to check each item.
#
# Simple rule:
# O(1) is usually better/faster than O(log n), and O(log n) is usually better/faster than O(n).
#
# BINARY SEARCH TREE TIME COMPLEXITY:
#
# - Search: O(log n) average, O(n) worst case
#   A balanced tree lets you eliminate about half the remaining nodes each step.
#   A badly unbalanced tree can act like a linked list.
#
# - Insert: O(log n) average, O(n) worst case
#   You move left or right until you find the correct empty spot.
#
# - Delete: O(log n) average, O(n) worst case
#   You must first search for the node, then reconnect the tree.
#
# - Traverse all nodes: O(n)
#   You must visit every node once.
#
# - Find minimum/maximum: O(log n) average, O(n) worst case
#   You keep moving left for minimum or right for maximum.
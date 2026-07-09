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

# ------------------------------------------------------------
# Node class
# ------------------------------------------------------------
#
# A BST node stores:
#
#   1. A value
#   2. A left child
#   3. A right child
#
# The left child should contain smaller values.
# The right child should contain larger values.
# ------------------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ------------------------------------------------------------
# Build a BST manually
# ------------------------------------------------------------
#
# We will build this tree:
#
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
#
# This is a valid BST because:
#
#   left values are smaller
#   right values are larger
# ------------------------------------------------------------

root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)

root.right.left = Node(12)
root.right.right = Node(20)


print("Binary Search Tree Basics")
print("=" * 60)

print("BST structure:")
print()
print("             10")
print("           /    \\")
print("          5      15")
print("         / \\    /  \\")
print("        2   7  12   20")
print()

print("BST Rule:")
print("Smaller values go left.")
print("Larger values go right.")
print()

# ------------------------------------------------------------
# Explain root rule
# ------------------------------------------------------------

print("Root Rule")
print("-" * 60)

print("Root value: 10")
print()
print("Left side of 10:")
print("5, 2, and 7 are smaller than 10.")
print()
print("Right side of 10:")
print("15, 12, and 20 are larger than 10.")
print()

# ------------------------------------------------------------
# Explain child node rules
# ------------------------------------------------------------

print("The Rule Applies To Every Node")
print("-" * 60)

print("For node 5:")
print("2 is smaller than 5, so 2 is on the left.")
print("7 is larger than 5, so 7 is on the right.")
print()

print("For node 15:")
print("12 is smaller than 15, so 12 is on the left.")
print("20 is larger than 15, so 20 is on the right.")
print()

# ------------------------------------------------------------
# Search idea without writing full search code yet
# ------------------------------------------------------------

print("Search Idea")
print("-" * 60)

print("Search for 12:")
print()

print("Step 1:")
print("Start at 10.")
print("12 > 10, so go right.")
print()

print("Step 2:")
print("Now at 15.")
print("12 < 15, so go left.")
print()

print("Step 3:")
print("Now at 12.")
print("Found it.")
print()

print("Nodes checked:")
print("10 -> 15 -> 12")
print()

print("Nodes skipped:")
print("5, 2, 7, 20")
print()

# ------------------------------------------------------------
# Balanced vs unbalanced explanation
# ------------------------------------------------------------

print("Balanced vs Unbalanced BST")
print("=" * 60)

print("Balanced BST:")
print()
print("             10")
print("           /    \\")
print("          5      15")
print("         / \\    /  \\")
print("        2   7  12   20")
print()

print("A balanced BST spreads values out.")
print("Search can be O(log n).")
print()

print("Unbalanced BST:")
print()
print("1")
print(" \\")
print("  2")
print("   \\")
print("    3")
print("     \\")
print("      4")
print("       \\")
print("        5")
print()

print("An unbalanced BST can become a chain.")
print("Search can become O(n).")
print()
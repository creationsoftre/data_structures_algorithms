# ============================================================
# Trees - Study Notes
# ============================================================
#
# A tree is a data structure made of nodes connected by edges.
#
# A tree starts with one top node called the root.
#
# Example:
#
#              A
#            /   \
#           B     C
#          / \     \
#         D   E     F
#
# A = root
# B and C = children of A
# A = parent of B and C
# D, E, and F = leaf nodes
#
# ------------------------------------------------------------
# COMMON TREE WORDS
# ------------------------------------------------------------
#
# Root:
#   The top node in the tree.
#
# Parent:
#   A node that has children.
#
# Child:
#   A node connected under another node.
#
# Leaf:
#   A node with no children.
#
# Edge:
#   A connection between two nodes.
#
# Height:
#   The longest path from a node down to a leaf.
#
# Depth:
#   How far a node is from the root.
#
# Level:
#   A row in the tree.
#
# ------------------------------------------------------------
# BINARY TREE
# ------------------------------------------------------------
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
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
#
# Each node has no more than two children.
#
# ------------------------------------------------------------
# PERFECT BINARY TREE
# ------------------------------------------------------------
#
# A perfect binary tree has every level completely filled.
#
# Example with 15 nodes:
#
#              1
#           /     \
#          2       3
#        /  \     /  \
#       4    5   6    7
#      / \  / \ / \  / \
#     8  9 10 11 12 13 14 15
#
# Number of nodes by level:
#
#   Level 1: 1 node
#   Level 2: 2 nodes
#   Level 3: 4 nodes
#   Level 4: 8 nodes
#
# Total:
#
#   1 + 2 + 4 + 8 = 15
#
# ------------------------------------------------------------
# IMPORTANT FORMULAS
# ------------------------------------------------------------
#
# Perfect binary tree nodes:
#
#   N = 2^levels - 1
#
# Example:
#
#   levels = 4
#   N = 2^4 - 1
#   N = 16 - 1
#   N = 15
#
# Find levels from nodes:
#
#   levels = log2(N + 1)
#
# Example:
#
#   N = 15
#   levels = log2(15 + 1)
#   levels = log2(16)
#   levels = 4
#
# Worst-case comparisons in a perfect BST:
#
#   comparisons = levels
#
# Example:
#
#   N = 15
#   comparisons = 4
#
# Why?
#   In the worst case, search checks one node per level.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Binary tree search:
#   O(n)
#
# Speed:
#   Can be slow.
#
# Why?
#   A normal binary tree has no ordering rule.
#   We may need to check every node.
#
# Binary search tree search:
#   O(log n) average
#   O(n) worst case
#
# Speed:
#   Fast when the tree is balanced.
#   Slow when the tree becomes a chain.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Storing a tree:
#   O(n)
#
# Why?
#   We store n nodes.
#
# Recursive traversal:
#   O(h)
#
# Why?
#   The call stack grows based on tree height.
#
# h = height of the tree
#
# Balanced tree:
#   h = log n
#
# Unbalanced tree:
#   h = n
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# A binary tree and a binary search tree are not the same thing.
#
# Binary tree:
#   Each node has at most two children.
#
# Binary search tree:
#   Each node has at most two children AND follows this rule:
#
#       left side  = smaller values
#       right side = larger values
#
# The ordering rule is what makes BST search faster.
# ============================================================
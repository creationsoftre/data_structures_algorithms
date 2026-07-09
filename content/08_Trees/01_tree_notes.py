# ============================================================
# Trees - Chapter Notes
# ============================================================
#
# A tree is a data structure made of nodes connected by edges.
#
# Trees are useful when data has a parent-child relationship.
#
# Simple examples:
#
#   folders and files
#   company org chart
#   family tree
#   HTML document structure
#   decision trees
#   search trees
#
# ------------------------------------------------------------
# BASIC TREE EXAMPLE
# ------------------------------------------------------------
#
#              A
#            /   \
#           B     C
#          / \     \
#         D   E     F
#
# A is the root.
# B and C are children of A.
# A is the parent of B and C.
# D, E, and F are leaf nodes.
#
# ------------------------------------------------------------
# COMMON TREE TERMS
# ------------------------------------------------------------
#
# Root:
#   The top node in the tree.
#
# Parent:
#   A node that has child nodes under it.
#
# Child:
#   A node connected below another node.
#
# Leaf:
#   A node with no children.
#
# Edge:
#   A connection between two nodes.
#
# Sibling:
#   Nodes that share the same parent.
#
# Subtree:
#   A smaller tree inside a larger tree.
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
# BINARY TREE VS BINARY SEARCH TREE
# ------------------------------------------------------------
#
# Binary tree:
#
#   Each node has at most two children.
#
# Binary search tree:
#
#   Each node has at most two children
#   AND follows an ordering rule.
#
# BST rule:
#
#   Left side  = smaller values
#   Right side = larger values
#
# Example BST:
#
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
#
# For node 10:
#
#   5, 2, and 7 are smaller, so they are on the left.
#   15, 12, and 20 are larger, so they are on the right.
#
# ------------------------------------------------------------
# DEPTH, HEIGHT, AND LEVELS
# ------------------------------------------------------------
#
# These terms are easy to mix up.
#
# Depth:
#   How far a node is from the root.
#
# Height:
#   The longest path from a node down to a leaf.
#
# Level:
#   The row number of a node.
#
# Example:
#
#              A          Level 1, depth 0
#            /   \
#           B     C       Level 2, depth 1
#          / \     \
#         D   E     F     Level 3, depth 2
#
# Root depth:
#
#   A has depth 0.
#
# Leaf height:
#
#   D, E, and F have height 0.
#
# Tree height:
#
#   The tree height is 2 if counting edges.
#
# Important:
#
#   Levels usually start at 1.
#   Depth usually starts at 0.
#   Height usually counts edges.
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
# FULL BINARY TREE
# ------------------------------------------------------------
#
# A full binary tree means every node has either:
#
#   0 children
#   or
#   2 children
#
# No node has only one child.
#
# Example:
#
#              A
#            /   \
#           B     C
#          / \
#         D   E
#
# This is full because:
#
#   A has 2 children.
#   B has 2 children.
#   C, D, and E have 0 children.
#
# ------------------------------------------------------------
# COMPLETE BINARY TREE
# ------------------------------------------------------------
#
# A complete binary tree is filled from left to right.
#
# Every level is full except maybe the last level.
#
# The last level must be filled from left to right.
#
# Example:
#
#              A
#            /   \
#           B     C
#          / \   /
#         D   E F
#
# This is complete because the last level is filled left to right.
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
# Convert levels to height:
#
#   height = levels - 1
#
# Example:
#
#   levels = 4
#   height = 4 - 1
#   height = 3
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Normal binary tree search:
#
#   O(n)
#
# Speed:
#   Can be slow.
#
# Why?
#   A regular binary tree has no ordering rule.
#   We may need to check every node.
#
# Binary search tree search:
#
#   Average case: O(log n)
#   Worst case:   O(n)
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
#
#   O(n)
#
# Why?
#   We store n nodes.
#
# Recursive tree operations:
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
# APPLICATIONS OF TREES
# ------------------------------------------------------------
#
# Trees are used in many real systems.
#
# File systems:
#
#   Folders contain files and other folders.
#
# HTML / XML:
#
#   Web pages are stored as tree structures.
#
# Databases:
#
#   Indexes often use tree-like structures.
#
# Compilers:
#
#   Code can be parsed into syntax trees.
#
# Search:
#
#   Binary search trees help organize searchable data.
#
# Autocomplete:
#
#   Tries can store words by prefix.
#
# Priority queues:
#
#   Heaps are tree-like structures stored in arrays.
#
# ------------------------------------------------------------
# MAIN TAKEAWAY
# ------------------------------------------------------------
#
# A tree organizes data in a hierarchy.
#
# A binary tree limits each node to at most two children.
#
# A binary search tree adds an ordering rule:
#
#   smaller values go left
#   larger values go right
#
# That ordering rule is what makes searching faster.
# ============================================================


print("Trees - Chapter Notes")
print("=" * 50)
print("This file is mostly comments for studying.")
print("Read the comments above to understand tree vocabulary, diagrams, and Big O.")
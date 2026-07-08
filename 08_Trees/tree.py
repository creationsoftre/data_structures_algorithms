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
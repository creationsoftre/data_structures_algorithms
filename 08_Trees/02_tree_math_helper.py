# ============================================================
# Tree Math Helper
# ============================================================
#
# This file helps explain common tree math problems.
#
# The goal:
#
#   Show the formula.
#   Plug in the values.
#   Explain what the answer means.
#
# ------------------------------------------------------------
# COMMON QUESTIONS
# ------------------------------------------------------------
#
# 1. Given a perfect binary tree with N nodes, how many levels?
#
# 2. Given the number of levels, how many nodes are in a perfect
#    binary tree?
#
# 3. Given a perfect BST with N nodes, what is the worst-case
#    number of comparisons?
#
# 4. What is the height of a perfect binary tree?
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Levels and height are easy to mix up.
#
# If counting levels:
#
#   Root is level 1.
#
# If counting height by edges:
#
#   Root has height 0 when the tree has only one node.
#
# Example:
#
#   A perfect tree with 15 nodes has:
#
#       4 levels
#       height 3
#
# Why?
#
#   Level count: 1, 2, 3, 4
#   Edge count from root to leaf: 3
# ============================================================


import math


def explain_levels_from_nodes(number_of_nodes):
    levels = int(math.log2(number_of_nodes + 1))

    print("Find Levels From Nodes")
    print("=" * 50)
    print(f"Given nodes: {number_of_nodes}")
    print()
    print("Formula for a perfect binary tree:")
    print("  levels = log2(N + 1)")
    print()
    print("Plug in values:")
    print(f"  levels = log2({number_of_nodes} + 1)")
    print(f"  levels = log2({number_of_nodes + 1})")
    print(f"  levels = {levels}")
    print()
    print(f"Answer: A perfect binary tree with {number_of_nodes} nodes has {levels} levels.")

    return levels


def explain_nodes_from_levels(levels):
    nodes = (2 ** levels) - 1

    print("Find Nodes From Levels")
    print("=" * 50)
    print(f"Given levels: {levels}")
    print()
    print("Formula:")
    print("  N = 2^levels - 1")
    print()
    print("Plug in values:")
    print(f"  N = 2^{levels} - 1")
    print(f"  N = {2 ** levels} - 1")
    print(f"  N = {nodes}")
    print()
    print(f"Answer: A perfect binary tree with {levels} levels has {nodes} nodes.")

    return nodes


def explain_worst_case_comparisons_perfect_bst(number_of_nodes):
    levels = int(math.log2(number_of_nodes + 1))

    print("Worst-Case Comparisons in a Perfect BST")
    print("=" * 50)
    print(f"Given nodes: {number_of_nodes}")
    print()
    print("A perfect BST is balanced and completely filled.")
    print("In the worst case, search checks one node per level.")
    print()
    print("Formula:")
    print("  comparisons = log2(N + 1)")
    print()
    print("Plug in values:")
    print(f"  comparisons = log2({number_of_nodes} + 1)")
    print(f"  comparisons = log2({number_of_nodes + 1})")
    print(f"  comparisons = {levels}")
    print()
    print(f"Answer: Worst-case comparisons = {levels}")
    print()
    print("Why?")
    print(f"  A perfect BST with {number_of_nodes} nodes has {levels} levels.")
    print("  Search may check one node on each level before finding the value or stopping.")

    return levels


def explain_height_from_nodes_perfect_tree(number_of_nodes):
    levels = int(math.log2(number_of_nodes + 1))
    height = levels - 1

    print("Find Height From Nodes")
    print("=" * 50)
    print(f"Given nodes: {number_of_nodes}")
    print()
    print("Step 1: Find levels.")
    print("  levels = log2(N + 1)")
    print(f"  levels = log2({number_of_nodes} + 1)")
    print(f"  levels = log2({number_of_nodes + 1})")
    print(f"  levels = {levels}")
    print()
    print("Step 2: Convert levels to height.")
    print("  height = levels - 1")
    print(f"  height = {levels} - 1")
    print(f"  height = {height}")
    print()
    print(f"Answer: Height = {height}")
    print()
    print("Important:")
    print("  Levels count nodes rows.")
    print("  Height usually counts edges from root to leaf.")

    return height


# ------------------------------------------------------------
# Test examples
# ------------------------------------------------------------

print("Tree Math Helper")
print("=" * 50)
print()

explain_levels_from_nodes(15)

print()
explain_nodes_from_levels(4)

print()
explain_worst_case_comparisons_perfect_bst(15)

print()
explain_height_from_nodes_perfect_tree(15)
print()
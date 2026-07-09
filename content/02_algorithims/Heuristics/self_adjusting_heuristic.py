# ============================================================
# Self-Adjusting and Balanced Trees
# ============================================================
#
# Some trees reorganize themselves to stay efficient.
#
# There are two main ideas:
#
#   1. Balance the tree by height.
#   2. Adjust the tree based on what is accessed often.
#
# AVL Tree:
#
#   Keeps the tree strictly balanced.
#   Good for fast searching.
#
# Red-Black Tree:
#
#   Keeps the tree mostly balanced using color rules.
#   Good general-purpose balanced tree.
#
# Splay Tree:
#
#   Moves recently accessed nodes closer to the root.
#   Good when recently used values are likely to be used again.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# AVL Tree:
#   Search: O(log n)
#   Insert: O(log n)
#   Delete: O(log n)
#
# Red-Black Tree:
#   Search: O(log n)
#   Insert: O(log n)
#   Delete: O(log n)
#
# Splay Tree:
#   Single operation worst case: O(n)
#   Many operations averaged together: O(log n)
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# AVL and Red-Black Trees use balancing rules.
#
# Splay Trees use a self-adjusting heuristic:
#
#   Recently accessed nodes are moved closer to the root.
#
# That can make repeated access faster.
# ============================================================
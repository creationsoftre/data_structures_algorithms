# ============================================================
# Hash Table - Chaining
# ============================================================
#
# A collision happens when two different keys calculate the same
# hash table index.
#
# Example:
#
#   table_size = 5
#
#   10 % 5 = 0
#   15 % 5 = 0
#   20 % 5 = 0
#
# All three keys want to go to index 0.
#
# Chaining handles this by storing a list at each index.
#
# Instead of each index storing only one key-value pair, each index
# can store multiple key-value pairs.
#
# Example:
#
#   Index 0: [[10, "Trevonte"], [15, "Jordan"], [20, "Alex"]]
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Average insert/search/remove:
#   O(1)
#   Very fast when keys are spread out well.
#
# Worst-case insert/search/remove:
#   O(n)
#   Slower if many keys land in the same chain.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# O(n)
#
# We store n key-value pairs.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Chaining does not avoid collisions.
#
# It gives collisions a place to go.
#
# If many keys land at the same index, that index's chain becomes
# longer, and searching inside that chain becomes slower.
# ============================================================

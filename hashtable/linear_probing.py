# ============================================================
# Hash Table - Linear Probing
# ============================================================
#
# Linear probing is a collision-handling technique.
#
# A collision happens when two keys calculate the same index.
#
# Linear probing handles collisions by checking the next index
# one spot at a time until it finds an empty spot.
#
# ------------------------------------------------------------
# FORMULA
# ------------------------------------------------------------
#
# Starting index:
#
#   hash_index = key % table_size
#
# If there is a collision:
#
#   index = (hash_index + i) % table_size
#
# where:
#
#   i = 0, 1, 2, 3, ...
#
# ------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------
#
# table_size = 10
#
# Insert key 20:
#
#   20 % 10 = 0
#
# Store key 20 at index 0.
#
# Insert key 30:
#
#   30 % 10 = 0
#
# Index 0 is already used.
#
# Try the next index:
#
#   index = (0 + 1) % 10
#   index = 1
#
# Store key 30 at index 1.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Average insert/search/remove:
#   O(1)
#   Very fast when the table is not too full.
#
# Worst-case insert/search/remove:
#   O(n)
#   Slower if many keys collide or the table is almost full.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# O(n)
#
# We store n key-value pairs.
#
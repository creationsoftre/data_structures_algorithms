# ============================================================
# Hash Table - Quadratic Probing
# ============================================================
#
# Quadratic probing is a collision-handling technique.
#
# Like linear probing, it stores values directly inside the table.
#
# The difference:
#
#   Linear probing checks the next spot one at a time.
#   Quadratic probing jumps farther each time.
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
#   index = (hash_index + i^2) % table_size
#
# where:
#
#   i = 0, 1, 2, 3, ...
#
# ------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------
#
# table_size = 11
#
# Insert key 22:
#
#   22 % 11 = 0
#
# Store key 22 at index 0.
#
# Insert key 33:
#
#   33 % 11 = 0
#
# Index 0 is already used.
#
# Try i = 1:
#
#   index = (0 + 1^2) % 11
#   index = 1
#
# Store key 33 at index 1.
#
# Insert key 44:
#
#   44 % 11 = 0
#
# Index 0 is already used.
#
# Try i = 1:
#
#   index = (0 + 1^2) % 11
#   index = 1
#
# Index 1 is already used.
#
# Try i = 2:
#
#   index = (0 + 2^2) % 11
#   index = 4
#
# Store key 44 at index 4.
#
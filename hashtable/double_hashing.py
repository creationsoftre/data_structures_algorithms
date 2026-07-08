# ============================================================
# Hash Table - Double Hashing
# ============================================================
#
# Double hashing is a collision-handling technique.
#
# It uses two hash functions:
#
#   1. The first hash finds the starting index.
#   2. The second hash decides the jump size.
#
# This helps spread values out better than linear probing.
#
# ------------------------------------------------------------
# FORMULA
# ------------------------------------------------------------
#
# First hash:
#
#   hash1 = key % table_size
#
# Second hash:
#
#   hash2 = step_size - (key % step_size)
#
# Probing formula:
#
#   index = (hash1 + i * hash2) % table_size
#
# where:
#
#   i = 0, 1, 2, 3, ...
#
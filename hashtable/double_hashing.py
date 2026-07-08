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
# ------------------------------------------------------------
# SIMPLE IDEA
# ------------------------------------------------------------
#
# Linear probing:
#
#   Always jumps by 1.
#
# Quadratic probing:
#
#   Jumps by square numbers.
#
# Double hashing:
#
#   Uses a second hash function to create a custom jump size
#   for each key.
#
# ------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------
#
# table_size = 11
# step_size = 7
#
# Insert key 22:
#
#   hash1 = 22 % 11
#   hash1 = 0
#
# Index 0 is empty.
# Store key 22 at index 0.
#
# Insert key 33:
#
#   hash1 = 33 % 11
#   hash1 = 0
#
# Index 0 is already used.
#
# Find the jump size:
#
#   hash2 = 7 - (33 % 7)
#   hash2 = 7 - 5
#   hash2 = 2
#
# Try i = 1:
#
#   index = (0 + 1 * 2) % 11
#   index = 2
#
# Store key 33 at index 2.
#
# Insert key 44:
#
#   hash1 = 44 % 11
#   hash1 = 0
#
# Index 0 is already used.
#
# Find the jump size:
#
#   hash2 = 7 - (44 % 7)
#   hash2 = 7 - 2
#   hash2 = 5
#
# Try i = 1:
#
#   index = (0 + 1 * 5) % 11
#   index = 5
#
# Store key 44 at index 5.
#
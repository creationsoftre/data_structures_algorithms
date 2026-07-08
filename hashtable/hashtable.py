# ============================================================
# Hash Tables
# ============================================================
#
# A hash table stores key-value pairs.
#
# The key is passed into a hash function.
# The hash function returns an index.
# The value is stored at that index.
#
# Simple formula:
#
#   index = key % table_size
#
# Example:
#
#   key = 1027
#   table_size = 10
#
#   index = 1027 % 10
#   index = 7
#
# So key 1027 is stored at index 7.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Average search:
#   O(1)
#   Very fast.
#
# Worst-case search:
#   O(n)
#   Slower if many keys collide.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# O(n)
#
# We store n key-value pairs.
#
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
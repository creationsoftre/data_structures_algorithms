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
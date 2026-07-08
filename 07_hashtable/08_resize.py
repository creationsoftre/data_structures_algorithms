# ============================================================
# Hash Table - Resizing
# ============================================================
#
# Hash table resizing happens when the table gets too full.
#
# Why?
#
#   The fuller the table gets, the more collisions happen.
#   More collisions can make insert and search slower.
#
# To fix this, the hash table can resize itself.
#
# Resizing means:
#
#   1. Create a larger table.
#   2. Reinsert the old key-value pairs.
#   3. Recalculate each key's index using the new table size.
#
# This is called rehashing.
#
# ============================================================
# Hash Table - Resizing
# ============================================================
#
# Hash table resizing happens when the table gets too full.
#
# Why?
#
#   The fuller the table gets, the more collisions happen.
#   More collisions can make insert and search slower.
#
# To fix this, the hash table can resize itself.
#
# Resizing means:
#
#   1. Create a larger table.
#   2. Reinsert the old key-value pairs.
#   3. Recalculate each key's index using the new table size.
#
# This is called rehashing.
#
# ------------------------------------------------------------
# LOAD FACTOR
# ------------------------------------------------------------
#
# Load factor measures how full the hash table is.
#
# Formula:
#
#   load_factor = number_of_items / table_size
#
# Example:
#
#   number_of_items = 7
#   table_size = 10
#
#   load_factor = 7 / 10
#   load_factor = 0.7
#
# If the load factor gets too high, we resize the table.
#
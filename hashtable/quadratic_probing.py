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
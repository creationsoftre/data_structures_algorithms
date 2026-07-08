# ============================================================
# Direct Hashing
# ============================================================
#
# Direct hashing uses the key directly as the index.
#
# Simple idea:
#
#   key = index
#
# Example:
#
#   student_id = 4
#
#   table[4] stores that student's name.
#
# This is very fast because we do not need a hash formula like:
#
#   key % table_size
#
# The key already tells us where the value belongs.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Insert:
#   O(1)
#   Very fast.
#
# Search:
#   O(1)
#   Very fast.
#
# Remove:
#   O(1)
#   Very fast.
#
# Why?
#   The key directly points to the index.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# O(k)
#
# k = size of the possible key range.
#
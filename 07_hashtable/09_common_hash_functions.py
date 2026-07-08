# ============================================================
# Common Hash Functions
# ============================================================
#
# A hash function converts a key into a number.
#
# That number is then used to find an index in a hash table.
#
# Simple idea:
#
#   key -> hash function -> index
#
# Different key types need different hash functions.
#
# Examples:
#
#   Integer key:
#       1023
#
#   String key:
#       "CAT"
#
#   Username key:
#       "trevonte"
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Integer hash:
#   O(1)
#   Very fast.
#
# String hash:
#   O(k)
#   Slower than integer hashing because each character may need
#   to be checked.
#
#   k = number of characters in the string.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# O(1)
#
# These hash functions only use a few variables while calculating.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# A good hash function spreads keys evenly across the table.
#
# Bad hash function:
#   Sends too many keys to the same index.
#
# Good hash function:
#   Spreads keys across many indexes.
#
# A hash function does not remove collisions completely.
# It only tries to reduce them.
# ============================================================

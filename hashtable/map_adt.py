# ============================================================
# Map ADT
# ============================================================
#
# ADT means Abstract Data Type.
#
# A Map ADT stores key-value pairs.
#
# Simple idea:
#
#   Use a key to find a value.
#
# Examples:
#
#   student_id -> student_name
#   username   -> email
#   word       -> definition
#
# A key should be unique.
#
# That means:
#
#   One key maps to one value.
#
# If we add the same key again, we update the value.
#
# ------------------------------------------------------------
# COMMON MAP OPERATIONS
# ------------------------------------------------------------
#
# put(key, value)
#   Add a new key-value pair.
#   If the key already exists, update the value.
#
# get(key)
#   Return the value connected to the key.
#
# remove(key)
#   Delete a key-value pair.
#
# contains_key(key)
#   Check if a key exists.
#
# print_map()
#   Print all key-value pairs.
#
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
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# This simple version uses a list.
#
# Search:
#   O(n)
#
# Speed:
#   Can be slow as the map grows.
#
# Why?
#   We may need to check each key one by one.
#
# Insert:
#   O(n)
#
# Speed:
#   Can be slow if we need to check whether the key already exists.
#
# Remove:
#   O(n)
#
# Speed:
#   Can be slow because we may need to search through the list.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   O(n)
#
# Why?
#   We store n key-value pairs.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# This file explains the Map ADT concept.
#
# It does not use hashing yet.
#
# Later, a hash table will make map operations faster by using
# a hash function to jump directly to an index.
# ============================================================
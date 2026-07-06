# ============================================================
# Move-To-Front Self-Adjusting Heuristic
# ============================================================
#
# Move-to-front is a self-adjusting heuristic.
#
# Simple idea:
#
#   When an item is found, move it to the front of the list.
#
# Why?
#
#   If we searched for that item recently, we may search for it
#   again soon.
#
# This can make repeated searches faster over time.
#
# ------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------
#
# Starting list:
#
#   ["A", "B", "C", "D", "E"]
#
# Search for "D":
#
#   Check A
#   Check B
#   Check C
#   Check D
#
# Found D.
#
# Move D to the front:
#
#   ["D", "A", "B", "C", "E"]
#
# Now if we search for D again, it is found immediately.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Search Time:
#   O(n)
#
# Speed:
#   Slow if the item is near the end or missing.
#   Fast if the item was recently moved to the front.
#
# Why?
#   In the worst case, we may still check every item.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   O(1)
#
# Why?
#   We rearrange the existing list.
#   We do not create a new list.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Move-to-front does not guarantee the best possible order.
#
# It is a heuristic.
#
# That means:
#
#   It uses a smart guess.
#
# The guess is:
#
#   Recently searched items may be searched again soon.
#
# This is useful when some items are accessed more often than others.
# ============================================================


# ------------------------------------------------------------
# Move-to-front search
# ------------------------------------------------------------
#
# This function searches for a target in a list.
#
# If the target is found:
#
#   1. Remove it from its current position.
#   2. Insert it at the front.
#   3. Return True.
#
# If the target is not found:
#
#   Return False.
# ------------------------------------------------------------
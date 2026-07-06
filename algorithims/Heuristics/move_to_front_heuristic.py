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
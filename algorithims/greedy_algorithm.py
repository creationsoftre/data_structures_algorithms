# ============================================================
# Greedy Algorithm
# ============================================================
#
# A greedy algorithm makes the best-looking choice at each step.
#
# Simple idea:
#
#   Pick the best option right now.
#   Repeat until the problem is solved.
#
# Greedy algorithms can be fast and simple.
#
# But greedy does not always give the best answer for every problem.
#
# ------------------------------------------------------------
# EXAMPLE: COIN CHANGE
# ------------------------------------------------------------
#
# Problem:
#
#   Given an amount of money, use the fewest coins possible.
#
# Example:
#
#   amount = 87
#
# Using common U.S. coins:
#
#   quarter = 25
#   dime    = 10
#   nickel  = 5
#   penny   = 1
#
# Greedy choice:
#
#   Always take the largest coin that does not go over the
#   remaining amount.
#
# For 87:
#
#   Take 25, remaining 62
#   Take 25, remaining 37
#   Take 25, remaining 12
#   Take 10, remaining 2
#   Take 1, remaining 1
#   Take 1, remaining 0
#
# Result:
#
#   [25, 25, 25, 10, 1, 1]
#
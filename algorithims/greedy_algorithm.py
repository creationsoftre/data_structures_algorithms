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
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Time Complexity:
#   O(n)
#
# Speed:
#   Fast.
#
# Why?
#   We loop through the coin types.
#
#   n = number of coin types
#
# Note:
#   The exact speed can depend on how the solution is written.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   O(k)
#
# Why?
#   We store the coins used in a list.
#
#   k = number of coins used
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Greedy does not always guarantee the best answer.
#
# It works well for U.S. coin change because the coin system
# is designed in a way where taking the largest coin first works.
#
# But for some coin systems, greedy can fail.
#
# Example:
#
#   coins = [4, 3, 1]
#   amount = 6
#
# Greedy would choose:
#
#   4 + 1 + 1 = 6
#
# That uses 3 coins.
#
# But the best answer is:
#
#   3 + 3 = 6
#
# That uses 2 coins.
#
# This shows that greedy can be fast, but it is not always correct
# for every problem.
# ============================================================

# ------------------------------------------------------------
# Greedy coin change
# ------------------------------------------------------------
#
# This function returns a list of coins used to make the amount.
#
# The greedy rule:
#
#   Always use the largest coin that does not go over the
#   remaining amount.
# ------------------------------------------------------------

def coin_change_greedy(amount, coins):
    # Sort coins from largest to smallest
    coins.sort(reverse = True)

    # Store the coins we choose.
    result = []

    # Go through each coin.
    for coin in coins:
        # Use this coin as many times as possible
        while amount >= coin:
            result.append(coin)

            # Subtract the coin from the remaining amount. 
            amount -= coin
            
    return result
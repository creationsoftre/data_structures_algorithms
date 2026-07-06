# ============================================================
# Fractional Knapsack - Greedy Algorithm
# ============================================================
#
# Fractional knapsack is a greedy problem.
#
# Problem:
#
#   We have a bag with a weight limit.
#   We have items with a value and a weight.
#   We want to get the most value possible.
#
# The important rule:
#
#   We are allowed to take part of an item.
#
# This is why it is called fractional knapsack.
#
# Example:
#
#   Item A:
#       value = 60
#       weight = 10
#
#   Item B:
#       value = 100
#       weight = 20
#
#   Item C:
#       value = 120
#       weight = 30
#
#   capacity = 50
#
# ------------------------------------------------------------
# GREEDY IDEA
# ------------------------------------------------------------
#
# For each item, calculate:
#
#   value_per_weight = value / weight
#
# Then:
#
#   Take the item with the highest value_per_weight first.
#
# Why?
#
#   It gives us the most value for each unit of weight.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Time Complexity:
#   O(n log n)
#
# Speed:
#   Usually fast.
#
# Why?
#   We sort the items by value_per_weight.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   O(n)
#
# Why?
#   We store the selected items.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Greedy works for fractional knapsack because we can take part
# of an item.
#
# Greedy does not always work for 0/1 knapsack because we cannot
# split items.
#
# Fractional knapsack:
#
#   Take all of an item, or take part of it.
#
# 0/1 knapsack:
#
#   Take the whole item, or skip it.
# ============================================================

# ============================================================
# Dynamic Programming
# ============================================================
#
# Dynamic programming is a technique used to make some problems faster.
#
# The simple idea:
#
#   Do not repeat the same work again and again.
#
# Instead:
#
#   Solve smaller problems.
#   Store the answers.
#   Reuse those answers later.
#
# ------------------------------------------------------------
# SIMPLE EXAMPLE
# ------------------------------------------------------------
#
# Fibonacci sequence:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21...
#
# Each number is made by adding the two numbers before it.
#
# Example:
#   3        2        1
#   fib(5) = fib(4) + fib(3)
#
# The problem:
#
#   A basic recursive solution recalculates the same values many times.
#
# Dynamic programming fixes this by remembering answers.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Basic recursion:
#   O(2^n)
#   Very slow as n grows.
#
# Dynamic programming:
#   O(n)
#   Much faster.
#
# Why?
#   Each Fibonacci number is solved once and reused.
#
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
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Memoization version:
#   O(n)
#
# Why?
#   We store answers in a dictionary.
#
# Bottom-up version:
#   O(n)
#
# Why?
#   We store answers in a list.
#
# Optimized bottom-up version:
#   O(1)
#
# Why?
#   We only keep the last two values.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Dynamic programming is useful when a problem has repeated work.
#
# If the same smaller problem shows up multiple times, we can store
# the answer instead of solving it again.
#
# This is why dynamic programming can make some slow problems faster.
# ============================================================


# ------------------------------------------------------------
# Example 1: Basic recursion
# ------------------------------------------------------------
#
# This version works, but it is slow.
#
# Why?
#
#   It recalculates the same Fibonacci values many times.
#
# Example:
#
#   fib(5)
#   = fib(4) + fib(3)
#
#   fib(4)
#   = fib(3) + fib(2)
#
# Notice fib(3) appears more than once.
# That means repeated work.
# ------------------------------------------------------------

def fibonacci_recursive(n):
    # Base case:
    # fib(0) is 0.
    if n == 0:
        return 0

    # Base case:
    # fib(1) is 1.
    if n == 1:
        return 1

    # Recursive case:
    # Add the previous two Fibonacci numbers.
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# ------------------------------------------------------------
# Example 2: Dynamic programming with memoization
# ------------------------------------------------------------
#
# Memoization means:
#
#   Store answers after calculating them.
#
# This version uses a dictionary called memo.
#
# If we already solved fib(n), we reuse it.
# ------------------------------------------------------------

def fibonacci_memo(n, memo=None):
    # Create the memo dictionary the first time the function runs.
    if memo is None:
        memo = {}

    # If we already solved this value, return the stored answer.
    if n in memo:
        return memo[n]

    # Base case:
    # fib(0) is 0.
    if n == 0:
        return 0

    # Base case:
    # fib(1) is 1.
    if n == 1:
        return 1

    # Solve the problem and store the answer.
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    # Return the stored answer.
    return memo[n]










# ============================================
# MAIN PROGRAM
# ============================================

n = 6 

print("Dynamic Programing")
print("=" * 40)

print(f"Goal: Find fib({n})")
print()

print("Regular recursion:")
print("-" * 40)
print(f"fib({n}) = {fibonacci_recursive(n)}")

print()
print("Dynamic programming with memoization:")
print("-" * 40)
print(f"fib({n}) = {fibonacci_memo(n)}")
# ============================================================
# Iterative Dynamic Programming
# ============================================================
#
# Dynamic programming means:
#
#   Store answers to smaller problems.
#   Reuse those answers to solve bigger problems.
#
# Iterative dynamic programming does this with a loop.
#
# Instead of using recursion, we build the answer from the bottom up.
#
# ------------------------------------------------------------
# SIMPLE EXAMPLE
# ------------------------------------------------------------
#
# Fibonacci sequence:
#
#   0, 1, 1, 2, 3, 5, 8
#
# Rule:
#
#   fib(n) = fib(n - 1) + fib(n - 2)
#
# Example:
#
#   fib(6) = fib(5) + fib(4)
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Time Complexity:
#   O(n)
#
# Speed:
#   Fast compared to basic recursion.
#
# Why?
#   Each Fibonacci number is calculated once.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   O(n)
#
# Why?
#   We store the Fibonacci answers in a list.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Iterative DP avoids recursion.
#
# This means:
#
#   No recursive call stack.
#   Easier to trace with a loop.
#   Still stores previous answers for reuse.
# ============================================================


# ------------------------------------------------------------
# Iterative dynamic programming
# ------------------------------------------------------------
#
# This version uses a list called dp.
#
# dp means dynamic programming table.
#
# Each index stores the answer for that Fibonacci number.
#
# Example:
#
#   dp[0] stores fib(0)
#   dp[1] stores fib(1)
#   dp[2] stores fib(2)
#   dp[3] stores fib(3)
#
# The goal:
#
#   Build the list from the smallest answer up to fib(n).
# ------------------------------------------------------------

def fibonacci_iterative_dp(n):
    # If n is 0, the answer is 0
    if n == 0:
        return 0
    
    # Create a list with enough space to store answers from 0 to n
    dp =[0] * (n +1)

    # Store the first two known Fibonacci values.
    dp[0] = 0
    dp[1] = 1

    # Build the answers from fib(2) up to fib(n)

    for i in range (2, n +1):
        # Each answers from fib(2) up to fib(n).
        dp[i] = dp[i - 1] + dp[i - 2]

    # Return the answer stored at index n
    return dp[n]


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

n = 6

print("Iterative Dynamic Programming Example")
print("=" * 40)
print()

print("Using a DP table:")
print("-" * 40)
print(f"fib({n}) = {fibonacci_iterative_dp(n)}")
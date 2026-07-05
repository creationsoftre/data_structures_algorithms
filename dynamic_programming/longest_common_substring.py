# ============================================================
# Longest Common Substring
# ============================================================
#
# The longest common substring is the longest matching part that
# appears continuously in both strings.
#
# Continuous means the characters must be next to each other.
#
# Example:
#
#   str1 = "ABABC"
#   str2 = "BABCA"
#
# Common substrings include:
#
#   "A"
#   "B"
#   "AB"
#   "ABC"
#   "BABC"
#
# The longest common substring is:
#
#   "BABC"
#
# ------------------------------------------------------------
# SUBSTRING VS SUBSEQUENCE
# ------------------------------------------------------------
#
# Substring:
#   Characters must be next to each other.
#
#   Example:
#       "ABC" is a substring of "ABCD"
#
# Subsequence:
#   Characters do not have to be next to each other.
#
#   Example:
#       "ACD" is a subsequence of "ABCD"
#
# This file is about substring, not subsequence.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Time Complexity:
#   O(m * n)
#
# Speed:
#   Slower than a simple loop, but much faster than checking
#   every possible substring manually.
#
# Why?
#   We compare each character from str1 with each character from str2.
#
#   m = length of str1
#   n = length of str2
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   O(m * n)
#
# Why?
#   We create a table with rows for str1 and columns for str2.
#
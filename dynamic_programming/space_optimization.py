# ============================================================
# Longest Common Substring - Space Optimized
# ============================================================
#
# The normal dynamic programming version uses a full matrix.
#
# Space:
#   O(m * n)
#
# But each cell only needs the diagonal value from the previous row:
#
#   matrix[row - 1][col - 1]
#
# So instead of storing the whole matrix, we can store only:
#
#   previous_row
#   current_row
#
# This reduces space.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Time Complexity:
#   O(m * n)
#
# Speed:
#   Same speed as the full matrix version.
#
# Why?
#   We still compare each character from str1 with each character
#   from str2.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   O(n)
#
# Why?
#   We only store two rows at a time.
#
#   n = length of str2
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Space optimization saves memory, but the tradeoff is:
#
#   We no longer have the full matrix to print or inspect later.
#
# Use the full matrix version when learning or debugging.
# Use the optimized version when you only need the final answer.
# ============================================================

# ------------------------------------------------------------
# Space optimized longest common substring
# ------------------------------------------------------------
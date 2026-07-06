# ============================================================
# Compression - Run-Length Encoding
# ============================================================
#
# Compression means:
#
#   Store the same information using less space.
#
# Run-Length Encoding, also called RLE, is a simple compression
# technique.
#
# The idea:
#
#   If the same character repeats, store the character and the
#   number of times it repeats.
#
# ------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------
#
# Original string:
#
#   "AAAABBBCCDAA"
#
# Compressed string:
#
#   "A4B3C2D1A2"
#
# Meaning:
#
#   A4 -> A appears 4 times
#   B3 -> B appears 3 times
#   C2 -> C appears 2 times
#   D1 -> D appears 1 time
#   A2 -> A appears 2 times
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
#   We scan through the string one time.
#
#   n = number of characters in the string
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   O(n)
#
# Why?
#   In the worst case, the compressed result can be about the
#   same size or larger than the original input.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Compression is not always smaller.
#
# RLE works well when there are many repeated characters.
#
# Good example:
#
#   "AAAAAABBBBCC"
#
# Bad example:
#
#   "ABCDEF"
#
# "ABCDEF" could become:
#
#   "A1B1C1D1E1F1"
#
# That is larger than the original.
#
# So a real compression function should only return the compressed
# version if it is actually smaller.
# ============================================================


# ------------------------------------------------------------
# Compress using Run-Length Encoding
# ------------------------------------------------------------
#
# This function compresses repeated characters.
#
# Example:
#
#   "AAAABBBCCDAA"
#
# becomes:
#
#   "A4B3C2D1A2"
# ------------------------------------------------------------
# ============================================================
# Compression - Frequency Table
# ============================================================
#
# A frequency table counts how often each character appears.
#
# This is useful in compression because repeated characters can
# sometimes be stored with shorter codes.
#
# Simple idea:
#
#   Count each character.
#   Characters that appear more often have higher frequency.
#
# ------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------
#
# Text:
#
#   "AAAABBBCCDAA"
#
# Frequency table:
#
#   A -> 6
#   B -> 3
#   C -> 2
#   D -> 1
#
# Meaning:
#
#   A appears 6 times.
#   B appears 3 times.
#   C appears 2 times.
#   D appears 1 time.
#
# ------------------------------------------------------------
# WHY THIS MATTERS FOR COMPRESSION
# ------------------------------------------------------------
#
# Some compression algorithms use frequency to decide how to
# represent data.
#
# Example idea:
#
#   Characters that appear often can get shorter codes.
#   Characters that appear rarely can get longer codes.
#
# This is the main idea behind Huffman Coding.
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
#   We scan through the text one time.
#
#   n = number of characters in the text
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   O(k)
#
# Why?
#   We store each unique character in the frequency table.
#
#   k = number of unique characters
#
# Example:
#
#   "AAAABBBCCDAA"
#
#   n = 12 total characters
#   k = 4 unique characters
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# A frequency table does not compress the text by itself.
#
# It is a helper step.
#
# It gives us information that another compression algorithm can
# use to build a better compressed version.
# ============================================================
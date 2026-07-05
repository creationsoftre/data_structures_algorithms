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
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# A value in the table means:
#
#   How long is the matching substring ending at this position?
#
# If the characters match:
#
#   Use the diagonal value and add 1.
#
# If the characters do not match:
#
#   Store 0.
#
# Why 0?
#   Because a substring must be continuous.
#   Once the characters do not match, the current streak ends.
# ============================================================


# ------------------------------------------------------------
# Longest common substring
# ------------------------------------------------------------
#
# This function returns the longest common substring.
#
# The table stores matching streak lengths.
#
# Example:
#
#   If str1[row] == str2[col],
#   then the current match continues from the diagonal cell.
#
#   matrix[row][col] = matrix[row - 1][col - 1] + 1
#
# The diagonal matters because a substring must continue in order.
# ------------------------------------------------------------

def longest_common_substring(str1, str2):
    # If either string is empty, there can be no common substring.
    if len(str1) == 0 or len(str2) == 0:
        return ""

    # Create a matrix filled with zeros.
    #
    # Rows represent characters from str1.
    # Columns represent characters from str2.
    matrix = []

    for row in range(len(str1)):
        matrix.append([0] * len(str2))

    # Store the length of the longest match found so far.
    max_length = 0

    # Store where the longest match ends in str1.
    end_index = 0

    # Compare every character in str1 with every character in str2.
    for row in range(len(str1)):
        for col in range(len(str2)):

            # If the characters match, we continue a matching streak.
            if str1[row] == str2[col]:

                # If we are on the first row or first column,
                # there is no diagonal cell to look at.
                #
                # So the matching streak starts at 1.
                if row == 0 or col == 0:
                    matrix[row][col] = 1

                # Otherwise, continue from the diagonal cell.
                else:
                    matrix[row][col] = matrix[row - 1][col - 1] + 1

                # If this is the longest match so far, save it.
                if matrix[row][col] > max_length:
                    max_length = matrix[row][col]
                    end_index = row

            # If the characters do not match, the current streak ends.
            else:
                matrix[row][col] = 0

    # Use the ending index and length to slice the answer from str1.
    start_index = end_index - max_length + 1

    return str1[start_index:end_index + 1]


# ------------------------------------------------------------
# Trace version
# ------------------------------------------------------------
#
# This version prints what is happening.
#
# It helps us see:
#
#   Which characters are being compared
#   When a match starts
#   When a match continues
#   When the longest substring changes
# ------------------------------------------------------------

def longest_common_substring_with_trace(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        print("One of the strings is empty.")
        return ""

    matrix = []

    for row in range(len(str1)):
        matrix.append([0] * len(str2))

    max_length = 0
    end_index = 0

    print("Longest Common Substring Trace")
    print("=" * 40)
    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    print()
    print("Goal: Find the longest matching section that appears continuously in both strings.")
    print("-" * 40)
    print()

    for row in range(len(str1)):
        for col in range(len(str2)):
            char1 = str1[row]
            char2 = str2[col]

            print(f"Compare str1[{row}] = '{char1}' with str2[{col}] = '{char2}'")

            if char1 == char2:
                if row == 0 or col == 0:
                    matrix[row][col] = 1
                    print("Characters match.")
                    print("This is on the first row or column, so the streak starts at 1.")
                else:
                    diagonal = matrix[row - 1][col - 1]
                    matrix[row][col] = diagonal + 1

                    print("Characters match.")
                    print(f"Look diagonally up-left: {diagonal}")
                    print(f"Current streak length: {diagonal} + 1 = {matrix[row][col]}")

                if matrix[row][col] > max_length:
                    max_length = matrix[row][col]
                    end_index = row

                    start_index = end_index - max_length + 1
                    current_substring = str1[start_index:end_index + 1]

                    print(f"New longest substring found: '{current_substring}'")
                    print(f"Length: {max_length}")

            else:
                matrix[row][col] = 0
                print("Characters do not match.")
                print("Store 0 because a substring must be continuous.")

            print()

    start_index = end_index - max_length + 1
    result = str1[start_index:end_index + 1]

    print("-" * 40)
    print(f"Final longest common substring: '{result}'")
    print(f"Length: {max_length}")

    return result


# ------------------------------------------------------------
# Print matrix
# ------------------------------------------------------------
#
# This helper prints the matrix in a cleaner way.
# ------------------------------------------------------------

def print_matrix(matrix, str1, str2):
    print("Matrix:")
    print()

    # Print column header using str2 characters.
    print("      ", end="")
    for char in str2:
        print(f"{char:>3}", end="")
    print()

    # Print each row with the matching str1 character.
    for row in range(len(matrix)):
        print(f"{str1[row]:>3}   ", end="")
        for col in range(len(matrix[row])):
            print(f"{matrix[row][col]:>3}", end="")
        print()


# ------------------------------------------------------------
# Longest common substring with matrix
# ------------------------------------------------------------
#
# This version returns both the substring and the matrix.
#
# This is useful when we want to print the table after solving.
# ------------------------------------------------------------

def longest_common_substring_with_matrix(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return "", []

    matrix = []

    for row in range(len(str1)):
        matrix.append([0] * len(str2))

    max_length = 0
    end_index = 0

    for row in range(len(str1)):
        for col in range(len(str2)):
            if str1[row] == str2[col]:
                if row == 0 or col == 0:
                    matrix[row][col] = 1
                else:
                    matrix[row][col] = matrix[row - 1][col - 1] + 1

                if matrix[row][col] > max_length:
                    max_length = matrix[row][col]
                    end_index = row
            else:
                matrix[row][col] = 0

    start_index = end_index - max_length + 1
    result = str1[start_index:end_index + 1]

    return result, matrix


# ------------------------------------------------------------
# Test examples
# ------------------------------------------------------------

str1 = "ABABC"
str2 = "BABCA"

print("Longest Common Substring Example")
print("=" * 40)
print(f"String 1: {str1}")
print(f"String 2: {str2}")
print()
print("Goal: Find the longest continuous matching substring.")
print()

result, matrix = longest_common_substring_with_matrix(str1, str2)

print("Result")
print("-" * 40)
print(f"Longest common substring: '{result}'")
print()

print_matrix(matrix, str1, str2)

print()
longest_common_substring_with_trace(str1, str2)
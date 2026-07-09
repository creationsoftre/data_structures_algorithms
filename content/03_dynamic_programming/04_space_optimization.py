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

def longest_common_substring_optimized(str1, str2):
    # If either string is empty, there is no common substring.
    if len(str1) == 0 or len(str2) == 0:
        return ""

    # previous_row stores values from the row above.
    previous_row = [0] * len(str2)

    # Store the longest matching length found so far.
    max_length = 0

    # Store where the longest match ends in str1.
    end_index = 0

    # Go through each character in str1.
    for row in range(len(str1)):

        # current_row stores values for the row we are building now.
        current_row = [0] * len(str2)

        # Go through each character in str2.
        for col in range(len(str2)):

            # If the characters match, continue the streak.
            if str1[row] == str2[col]:

                # If we are on the first row or first column,
                # the streak starts at 1.
                if row == 0 or col == 0:
                    current_row[col] = 1

                # Otherwise, use the diagonal value from the previous row.
                else:
                    current_row[col] = previous_row[col - 1] + 1

                # If this is the longest match so far, save it.
                if current_row[col] > max_length:
                    max_length = current_row[col]
                    end_index = row

            # If the characters do not match, the streak ends.
            else:
                current_row[col] = 0

        # The current row becomes the previous row for the next loop.
        previous_row = current_row

    # Slice the longest substring from str1.
    start_index = end_index - max_length + 1

    return str1[start_index:end_index + 1]

# ------------------------------------------------------------
# Space optimized trace version
# ------------------------------------------------------------
#
# This version shows the two-row idea.
#
# It helps us see:
#
#   previous_row = the row above
#   current_row  = the row being built
# ------------------------------------------------------------

def longest_common_substring_optimized_with_trace(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        print("One of the strings is empty.")
        return ""

    previous_row = [0] * len(str2)

    max_length = 0
    end_index = 0

    print("Space Optimized Longest Common Substring")
    print("=" * 50)
    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    print()
    print("Instead of storing the full matrix, we only store two rows:")
    print("  previous_row")
    print("  current_row")
    print("-" * 50)
    print()

    for row in range(len(str1)):
        current_row = [0] * len(str2)

        print(f"Building row for str1[{row}] = '{str1[row]}'")
        print(f"Previous row: {previous_row}")

        for col in range(len(str2)):
            char1 = str1[row]
            char2 = str2[col]

            if char1 == char2:
                if row == 0 or col == 0:
                    current_row[col] = 1

                    print(f"  Match: '{char1}' == '{char2}'")
                    print(f"  First row/column, so current_row[{col}] = 1")

                else:
                    diagonal = previous_row[col - 1]
                    current_row[col] = diagonal + 1

                    print(f"  Match: '{char1}' == '{char2}'")
                    print(f"  Use previous_row[{col - 1}] = {diagonal}")
                    print(f"  current_row[{col}] = {diagonal} + 1 = {current_row[col]}")

                if current_row[col] > max_length:
                    max_length = current_row[col]
                    end_index = row

                    start_index = end_index - max_length + 1
                    current_substring = str1[start_index:end_index + 1]

                    print(f"  New longest substring: '{current_substring}'")

            else:
                current_row[col] = 0

        print(f"Current row:  {current_row}")
        print("Move current_row into previous_row for the next loop.")
        print()

        previous_row = current_row

    start_index = end_index - max_length + 1
    result = str1[start_index:end_index + 1]

    print("-" * 50)
    print(f"Final longest common substring: '{result}'")
    print(f"Length: {max_length}")

    return result

# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

str1 = "ABABC"
str2 = "BABCA"

print("Longest Common Substring - Space Optimized Example")
print("=" * 50)
print(f"String 1: {str1}")
print(f"String 2: {str2}")
print()

result = longest_common_substring_optimized(str1, str2)

print("Result")
print("-" * 50)
print(f"Longest common substring: '{result}'")

print()
longest_common_substring_optimized_with_trace(str1, str2)
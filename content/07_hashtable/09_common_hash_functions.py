# ============================================================
# Common Hash Functions
# ============================================================
#
# A hash function converts a key into a number.
#
# That number is then used to find an index in a hash table.
#
# Simple idea:
#
#   key -> hash function -> index
#
# Different key types need different hash functions.
#
# Examples:
#
#   Integer key:
#       1023
#
#   String key:
#       "CAT"
#
#   Username key:
#       "trevonte"
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Integer hash:
#   O(1)
#   Very fast.
#
# String hash:
#   O(k)
#   Slower than integer hashing because each character may need
#   to be checked.
#
#   k = number of characters in the string.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# O(1)
#
# These hash functions only use a few variables while calculating.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# A good hash function spreads keys evenly across the table.
#
# Bad hash function:
#   Sends too many keys to the same index.
#
# Good hash function:
#   Spreads keys across many indexes.
#
# A hash function does not remove collisions completely.
# It only tries to reduce them.
# ============================================================
#
# ------------------------------------------------------------
# Integer hash
# ------------------------------------------------------------
#
# This is the simplest hash function for integer keys.
#
# Formula:
#
#   index = key % table_size
#
# Example:
#
#   key = 1023
#   table_size = 10
#
#   index = 1023 % 10
#   index = 3
# ------------------------------------------------------------

def integer_hash(key, table_size):
    return key % table_size

# ------------------------------------------------------------
# ASCII sum hash
# ------------------------------------------------------------
#
# This hash function works with strings.
#
# It converts each character to its ASCII number.
#
# Example:
#
#   "CAT"
#
#   C = 67
#   A = 65
#   T = 84
#
#   hash_value = 67 + 65 + 84
#   hash_value = 216
#
# Then:
#
#   index = 216 % table_size
# ------------------------------------------------------------
def ascii_sum_hash(key, table_size):
    hash_value = 0

    for char in key:
        hash_value += ord(char)

    return hash_value % table_size

# ------------------------------------------------------------
# Weighted string hash
# ------------------------------------------------------------
#
# ASCII sum hash has a weakness.
#
# Example:
#
#   "CAT"
#   "ACT"
#
# Both have the same letters.
#
# So both produce the same ASCII sum.
#
# Weighted string hash improves this by using the character position.
#
# Example:
#
#   hash_value += ASCII value * position
#
# This means characters in different positions affect the hash
# differently.
# ------------------------------------------------------------

def weighted_string_hash(key, table_size):
    hash_value = 0

    for index in range(len(key)):
        char = key[index]
        position = index + 1
        hash_value += ord(char) * position

    return hash_value % table_size

# ------------------------------------------------------------
# Polynomial rolling hash
# ------------------------------------------------------------
#
# This is a common idea for hashing strings.
#
# It uses a multiplier to spread values out more.
#
# Simple version:
#
#   hash_value = hash_value * base + ASCII value
#
# Then use modulo to keep the number inside the table size.
#
# This tends to spread strings better than a simple ASCII sum.
# ------------------------------------------------------------

def polynomial_rolling_hash(key, table_size):
    hash_value = 0
    base = 31

    for char in key:
        hash_value = hash_value * base + ord(char)

    return hash_value % table_size

# ------------------------------------------------------------
# Print helper
# ------------------------------------------------------------
#
# This helper prints where a key lands using each hash function.
# ------------------------------------------------------------

def explain_weighted_string_hash(key, table_size):
    print(f"Weighted string hash for: {key}")
    print("-" * 60)

    hash_value = 0

    for index in range(len(key)):
        char = key[index]
        position = index + 1
        ascii_value = ord(char)
        amount_added = ascii_value * position

        print(f"{char} = {ascii_value}, position = {position}")
        print(f"{ascii_value} * {position} = {amount_added}")
        print()

        hash_value += amount_added

    print(f"hash_value = {hash_value}")
    print(f"index = {hash_value} % {table_size}")
    print(f"index = {hash_value % table_size}")

    return hash_value % table_size


def explain_polynomial_rolling_hash(key, table_size):
    print(f"Polynomial rolling hash for: {key}")
    print("-" * 60)

    hash_value = 0
    base = 31

    print(f"base = {base}")
    print(f"start hash_value = {hash_value}")
    print()

    for char in key:
        ascii_value = ord(char)

        print(f"Character: {char}")
        print(f"hash_value = {hash_value} * {base} + {ascii_value}")

        hash_value = hash_value * base + ascii_value

        print(f"hash_value = {hash_value}")
        print()

    print(f"index = {hash_value} % {table_size}")
    print(f"index = {hash_value % table_size}")

    return hash_value % table_size
# ------------------------------------------------------------
# Real example: Hashing badge IDs and usernames
# ------------------------------------------------------------

table_size = 10

print("Common Hash Functions Example")
print("=" * 60)
print(f"Table size: {table_size}")
print()


# ------------------------------------------------------------
# Integer key example
# ------------------------------------------------------------

print("Integer Key Example")
print("-" * 60)

badge_id = 1023

# Integer hash:
# 1023 % 10 = 3
# Badge 1023 would be stored at index 3.
print(f"Badge ID: {badge_id}")
print(f"Hash formula: {badge_id} % {table_size}")
print(f"Index: {integer_hash(badge_id, table_size)}")
print()


# ------------------------------------------------------------
# String key example using ASCII sum
# ------------------------------------------------------------

print("String Key Example: ASCII Sum Hash")
print("-" * 60)

key = "CAT"

# ASCII values:
# C = 67
# A = 65
# T = 84
#
# hash_value = 67 + 65 + 84
# hash_value = 216
#
# index = 216 % 10
# index = 6
print(f"Key: {key}")
print("ASCII values:")
print("C = 67")
print("A = 65")
print("T = 84")
print()
print("hash_value = 67 + 65 + 84")
print("hash_value = 216")
print(f"index = 216 % {table_size}")
print(f"index = {ascii_sum_hash(key, table_size)}")
print()


# ------------------------------------------------------------
# Collision example
# ------------------------------------------------------------

print("Collision Example: ASCII Sum Weakness")
print("-" * 60)

key_one = "CAT"
key_two = "ACT"

# CAT and ACT use the same letters.
#
# CAT:
# C + A + T
#
# ACT:
# A + C + T
#
# The order changes, but the sum is the same.
print(f"{key_one} ASCII sum index: {ascii_sum_hash(key_one, table_size)}")
print(f"{key_two} ASCII sum index: {ascii_sum_hash(key_two, table_size)}")
print()
print("Both keys land at the same index because ASCII sum ignores order.")
print()


# ------------------------------------------------------------
# Better string hashing examples
# ------------------------------------------------------------

print("Better String Hashing Examples")
print("-" * 60)

explain_weighted_string_hash("CAT", table_size)
print()
explain_weighted_string_hash("ACT", table_size)

print()
explain_polynomial_rolling_hash("CAT", table_size)
print()
explain_polynomial_rolling_hash("ACT", table_size)


# ------------------------------------------------------------
# Username example
# ------------------------------------------------------------
print()
print("Username Hashing Example")
print("-" * 60)

username = "trevonte"

# This shows how a string username can be turned into an index.
print(f"Username: {username}")
print(f"ASCII sum index: {ascii_sum_hash(username, table_size)}")
print(f"Weighted index: {weighted_string_hash(username, table_size)}")
print(f"Polynomial index: {polynomial_rolling_hash(username, table_size)}")
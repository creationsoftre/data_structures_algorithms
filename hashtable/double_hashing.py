# ============================================================
# Hash Table - Double Hashing
# ============================================================
#
# Double hashing is a collision-handling technique.
#
# It uses two hash functions:
#
#   1. The first hash finds the starting index.
#   2. The second hash decides the jump size.
#
# This helps spread values out better than linear probing.
#
# ------------------------------------------------------------
# FORMULA
# ------------------------------------------------------------
#
# First hash:
#
#   hash1 = key % table_size
#
# Second hash:
#
#   hash2 = step_size - (key % step_size)
#
# Probing formula:
#
#   index = (hash1 + i * hash2) % table_size
#
# where:
#
#   i = 0, 1, 2, 3, ...
#
# ------------------------------------------------------------
# SIMPLE IDEA
# ------------------------------------------------------------
#
# Linear probing:
#
#   Always jumps by 1.
#
# Quadratic probing:
#
#   Jumps by square numbers.
#
# Double hashing:
#
#   Uses a second hash function to create a custom jump size
#   for each key.
#
# ------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------
#
# table_size = 11
# step_size = 7
#
# Insert key 22:
#
#   hash1 = 22 % 11
#   hash1 = 0
#
# Index 0 is empty.
# Store key 22 at index 0.
#
# Insert key 33:
#
#   hash1 = 33 % 11
#   hash1 = 0
#
# Index 0 is already used.
#
# Find the jump size:
#
#   hash2 = 7 - (33 % 7)
#   hash2 = 7 - 5
#   hash2 = 2
#
# Try i = 1:
#
#   index = (0 + 1 * 2) % 11
#   index = 2
#
# Store key 33 at index 2.
#
# Insert key 44:
#
#   hash1 = 44 % 11
#   hash1 = 0
#
# Index 0 is already used.
#
# Find the jump size:
#
#   hash2 = 7 - (44 % 7)
#   hash2 = 7 - 2
#   hash2 = 5
#
# Try i = 1:
#
#   index = (0 + 1 * 5) % 11
#   index = 5
#
# Store key 44 at index 5.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Average insert/search/remove:
#   O(1)
#   Very fast when the table is not too full.
#
# Worst-case insert/search/remove:
#   O(n)
#   Slower if many keys collide or the table is almost full.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# O(n)
#
# We store n key-value pairs.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Double hashing usually reduces clustering better than linear
# probing and quadratic probing.
#
# The second hash function must not return 0.
#
# If the jump size were 0, the algorithm would keep checking the
# same index forever.
# ============================================================
class DoubleHashingHashTable:
    def __init__(self, size, step_size):
        # Store the size of the hash table.
        #
        # Example:
        #   If size = 11, valid indexes are 0 through 10.
        self.size = size

        # Store the step size used by the second hash function.
        #
        # This is usually a smaller prime number than the table size.
        #
        # Example:
        #   table_size = 11
        #   step_size = 7
        self.step_size = step_size

        # Create the table.
        #
        # Each spot starts as None because it is empty.
        self.table = [None] * size

        # This marker is used when a value is removed.
        #
        # In probing, we do not want search to stop too early
        # after something has been removed.
        self.deleted = "DELETED"

    def hash_function_one(self, key):
        # First hash function.
        #
        # This gives us the starting index.
        #
        # Formula:
        #   hash1 = key % table_size
        return key % self.size

    def hash_function_two(self, key):
        # Second hash function.
        #
        # This gives us the jump size.
        #
        # Formula:
        #   hash2 = step_size - (key % step_size)
        #
        # This should never return 0.
        return self.step_size - (key % self.step_size)

    def insert(self, key, value):
        # Calculate the starting index.
        hash1 = self.hash_function_one(key)

        # Calculate the jump size.
        hash2 = self.hash_function_two(key)

        # Try each possible position in the table.
        for i in range(self.size):
            # Double hashing formula:
            #
            #   index = (hash1 + i * hash2) % table_size
            #
            # i controls how many jumps we take.
            index = (hash1 + i * hash2) % self.size

            # If the spot is empty or deleted, insert here.
            if self.table[index] is None or self.table[index] == self.deleted:
                self.table[index] = [key, value]
                return True

            # If the key already exists, update the value.
            stored_key = self.table[index][0]

            if stored_key == key:
                self.table[index][1] = value
                return True

        # If the loop finishes, no open spot was found.
        return False

    def get(self, key):
        # Calculate the starting index.
        hash1 = self.hash_function_one(key)

        # Calculate the jump size.
        hash2 = self.hash_function_two(key)

        # Search using double hashing.
        for i in range(self.size):
            index = (hash1 + i * hash2) % self.size

            # If we hit a true empty spot, the key is not in the table.
            if self.table[index] is None:
                return None

            # If this spot was deleted, keep searching.
            if self.table[index] == self.deleted:
                continue

            stored_key = self.table[index][0]
            stored_value = self.table[index][1]

            # If the key matches, return the value.
            if stored_key == key:
                return stored_value

        # Key was not found.
        return None

    def remove(self, key):
        # Calculate the starting index.
        hash1 = self.hash_function_one(key)

        # Calculate the jump size.
        hash2 = self.hash_function_two(key)

        # Search using double hashing.
        for i in range(self.size):
            index = (hash1 + i * hash2) % self.size

            # If we hit a true empty spot, the key is not in the table.
            if self.table[index] is None:
                return False

            # If this spot was deleted, keep searching.
            if self.table[index] == self.deleted:
                continue

            stored_key = self.table[index][0]

            # If the key matches, mark the spot as deleted.
            if stored_key == key:
                self.table[index] = self.deleted
                return True

        # Key was not found.
        return False

    def print_table(self):
        # Print each index and the data stored there.
        print("Double Hashing Hash Table")
        print("-" * 50)

        for index in range(self.size):
            print(f"Index {index}: {self.table[index]}")


# ------------------------------------------------------------
# Main Programming
# ------------------------------------------------------------

employee_table = DoubleHashingHashTable(11, 7)

# Insert badge 22.
# hash1 = 22 % 11 = 0
# Index 0 is empty.
# Store [22, "Trevonte"] at index 0.
employee_table.insert(22, "Trevonte")

# Insert badge 33.
# hash1 = 33 % 11 = 0
# Index 0 is already used by badge 22.
#
# hash2 = 7 - (33 % 7)
# hash2 = 7 - 5
# hash2 = 2
#
# Try i = 1:
# index = (0 + 1 * 2) % 11 = 2
# Store [33, "Jordan"] at index 2.
employee_table.insert(33, "Jordan")

# Insert badge 44.
# hash1 = 44 % 11 = 0
# Index 0 is already used.
#
# hash2 = 7 - (44 % 7)
# hash2 = 7 - 2
# hash2 = 5
#
# Try i = 1:
# index = (0 + 1 * 5) % 11 = 5
# Store [44, "Alex"] at index 5.
employee_table.insert(44, "Alex")

# Insert badge 55.
# hash1 = 55 % 11 = 0
# Index 0 is already used.
#
# hash2 = 7 - (55 % 7)
# hash2 = 7 - 6
# hash2 = 1
#
# Try i = 1:
# index = (0 + 1 * 1) % 11 = 1
# Store [55, "Morgan"] at index 1.
employee_table.insert(55, "Morgan")

# Insert badge 23.
# hash1 = 23 % 11 = 1
# Index 1 is already used by badge 55.
#
# hash2 = 7 - (23 % 7)
# hash2 = 7 - 2
# hash2 = 5
#
# Try i = 1:
# index = (1 + 1 * 5) % 11 = 6
# Store [23, "Casey"] at index 6.
employee_table.insert(23, "Casey")


print("Employee Badge Hash Table - Double Hashing")
print("=" * 50)

employee_table.print_table()


print()
print("Lookup Employees")
print("-" * 50)

# Search for badge 22.
# hash1 = 22 % 11 = 0
# Check index 0.
# Stored key is 22, so return "Trevonte".
print(f"Badge 22: {employee_table.get(22)}")

# Search for badge 44.
# hash1 = 44 % 11 = 0
# hash2 = 7 - (44 % 7) = 5
#
# Check index 0: stored key is 22, not 44.
# Try i = 1:
# index = (0 + 1 * 5) % 11 = 5
# Check index 5: stored key is 44, so return "Alex".
print(f"Badge 44: {employee_table.get(44)}")

# Search for badge 23.
# hash1 = 23 % 11 = 1
# hash2 = 7 - (23 % 7) = 5
#
# Check index 1: stored key is 55, not 23.
# Try i = 1:
# index = (1 + 1 * 5) % 11 = 6
# Check index 6: stored key is 23, so return "Casey".
print(f"Badge 23: {employee_table.get(23)}")

# Search for badge 99.
# hash1 = 99 % 11 = 0
# hash2 = 7 - (99 % 7) = 7
#
# Check the double hashing path.
# If the key is not found, return None.
print(f"Badge 99: {employee_table.get(99)}")


print()
print("Update Employee")
print("-" * 50)

# Update badge 33.
# hash1 = 33 % 11 = 0
# hash2 = 7 - (33 % 7) = 2
#
# Check index 0: stored key is 22.
# Try i = 1:
# index = (0 + 1 * 2) % 11 = 2
# Check index 2: stored key is 33.
# Update value to "Jordan Smith".
employee_table.insert(33, "Jordan Smith")

print("Updated badge 33 to Jordan Smith.")
print()
employee_table.print_table()


print()
print("Remove Employee")
print("-" * 50)

# Remove badge 44.
# hash1 = 44 % 11 = 0
# hash2 = 7 - (44 % 7) = 5
#
# Check index 0: stored key is 22.
# Try i = 1:
# index = (0 + 1 * 5) % 11 = 5
# Check index 5: stored key is 44.
# Mark index 5 as DELETED.
removed = employee_table.remove(44)

print(f"Removed badge 44: {removed}")

print()
employee_table.print_table()
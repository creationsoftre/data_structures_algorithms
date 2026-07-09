# ============================================================
# Hash Tables
# ============================================================
#
# A hash table stores key-value pairs.
#
# The key is passed into a hash function.
# The hash function returns an index.
# The value is stored at that index.
#
# Simple formula:
#
#   index = key % table_size
#
# Example:
#
#   key = 1027
#   table_size = 10
#
#   index = 1027 % 10
#   index = 7
#
# So key 1027 is stored at index 7.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Average search:
#   O(1)
#   Very fast.
#
# Worst-case search:
#   O(n)
#   Slower if many keys collide.
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
# This basic version does not fully handle collisions yet.
#
# A collision happens when two keys create the same index.
#
# Example:
#
#   1027 % 10 = 7
#   2037 % 10 = 7
#
# Both keys want index 7.
#
# Collision handling comes next with chaining and probing.
# ============================================================

class HashTable:
    def __init__(self, size):
        # Store the size of the hash table.
        #
        # Example:
        #   If size = 10, the table will have indexes 0 through 9.
        self.size = size

        # Create the actual table.
        #
        # Each spot starts as None because no data has been added yet.
        #
        # Example:
        #   [None, None, None, None, None]
        self.table = [None] * size

    def hash_function(self, key):
        # The hash function turns a key into an index.
        #
        # This example uses the modulo operator.
        #
        # Formula:
        #   index = key % table_size
        #
        # Example:
        #   key = 1023
        #   table_size = 10
        #
        #   index = 1023 % 10
        #   index = 3
        #
        # So key 1023 should go into index 3.
        return key % self.size

    def insert(self, key, value):
        # First, use the hash function to find where this key belongs.
        index = self.hash_function(key)

        # Store the key and value together at the calculated index.
        #
        # We store both the key and value because later we need to check
        # that the key at this index is the key we are looking for.
        #
        # Example:
        #   table[3] = [1023, "Alex"]
        self.table[index] = [key, value]

    def get(self, key):
        # Use the hash function to calculate where the key should be.
        index = self.hash_function(key)

        # If the spot is empty, the key is not in the table.
        if self.table[index] is None:
            return None

        # Get the stored key and value from this index.
        stored_key = self.table[index][0]
        stored_value = self.table[index][1]

        # Make sure the stored key matches the key we searched for.
        #
        # This matters because two different keys can create the same index.
        #
        # Example:
        #   1023 % 10 = 3
        #   2033 % 10 = 3
        #
        # Both keys want index 3.
        if stored_key == key:
            return stored_value

        # If the stored key does not match, return None.
        #
        # This basic version does not handle collisions yet.
        return None

    def remove(self, key):
        # Use the hash function to find where the key should be.
        index = self.hash_function(key)

        # If the spot is empty, there is nothing to remove.
        if self.table[index] is None:
            return False

        # Get the key stored at this index.
        stored_key = self.table[index][0]

        # Only remove the data if the stored key matches the key we want.
        if stored_key == key:
            self.table[index] = None
            return True

        # If the stored key does not match, the key was not removed.
        return False

    def print_table(self):
        # Print each index and the data stored there.
        #
        # This makes it easier to see how the hash table is storing values.
        print("Hash Table")
        print("-" * 40)

        for index in range(self.size):
            print(f"Index {index}: {self.table[index]}")

# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

employee_table = HashTable(10)

# Insert badge 1021.
# 1021 % 10 = 1
# Store ["1021", "Trevonte"] at index 1.
employee_table.insert(1021, "Trevonte")

# Insert badge 1022.
# 1022 % 10 = 2
# Store ["1022", "Jordan"] at index 2.
employee_table.insert(1022, "Jordan")

# Insert badge 1023.
# 1023 % 10 = 3
# Store ["1023", "Alex"] at index 3.
employee_table.insert(1023, "Alex")

# Insert badge 1024.
# 1024 % 10 = 4
# Store ["1024", "Morgan"] at index 4.
employee_table.insert(1024, "Morgan")


print("Employee Badge Hash Table")
print("=" * 40)

employee_table.print_table()

print()
print("Lookup Employees")
print("-" * 40)

# Search for badge 1021.
# 1021 % 10 = 1
# Check index 1.
# Stored key is 1021, so return "Trevonte".
print(f"Badge 1021: {employee_table.get(1021)}")

# Search for badge 1023.
# 1023 % 10 = 3
# Check index 3.
# Stored key is 1023, so return "Alex".
print(f"Badge 1023: {employee_table.get(1023)}")

# Search for badge 9999.
# 9999 % 10 = 9
# Check index 9.
# Index 9 is empty, so return None.
print(f"Badge 9999: {employee_table.get(9999)}")


print()
print("Remove Employee")
print("-" * 40)

# Remove badge 1022.
# 1022 % 10 = 2
# Check index 2.
# Stored key is 1022, so set index 2 back to None.
removed = employee_table.remove(1022)

print(f"Removed badge 1022: {removed}")

print()
employee_table.print_table()
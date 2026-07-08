# ============================================================
# Hash Table - Chaining
# ============================================================
#
# A collision happens when two different keys calculate the same
# hash table index.
#
# Example:
#
#   table_size = 5
#
#   10 % 5 = 0
#   15 % 5 = 0
#   20 % 5 = 0
#
# All three keys want to go to index 0.
#
# Chaining handles this by storing a list at each index.
#
# Instead of each index storing only one key-value pair, each index
# can store multiple key-value pairs.
#
# Example:
#
#   Index 0: [[10, "Trevonte"], [15, "Jordan"], [20, "Alex"]]
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Average insert/search/remove:
#   O(1)
#   Very fast when keys are spread out well.
#
# Worst-case insert/search/remove:
#   O(n)
#   Slower if many keys land in the same chain.
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
# Chaining does not avoid collisions.
#
# It gives collisions a place to go.
#
# If many keys land at the same index, that index's chain becomes
# longer, and searching inside that chain becomes slower.
# ============================================================
class ChainedHashTable:
    def __init__(self, size):
        # Store the size of the hash table.
        #
        # Example:
        #   If size = 5, valid indexes are 0 through 4.
        self.size = size

        # Create the table.
        #
        # Each index starts with an empty list.
        #
        # Each list is a chain.
        #
        # Example:
        #   [
        #       [],  # index 0
        #       [],  # index 1
        #       [],  # index 2
        #       [],  # index 3
        #       []   # index 4
        #   ]
        self.table = []

        for _ in range(size):
            self.table.append([])

    def hash_function(self, key):
        # Convert the key into an index.
        #
        # Formula:
        #   index = key % table_size
        #
        # Example:
        #   key = 15
        #   table_size = 5
        #
        #   index = 15 % 5
        #   index = 0
        return key % self.size

    def insert(self, key, value):
        # Find the index where this key should go.
        index = self.hash_function(key)

        # Get the chain at this index.
        chain = self.table[index]

        # Check if the key already exists in the chain.
        #
        # If it does, update the value instead of adding a duplicate.
        for pair in chain:
            stored_key = pair[0]

            if stored_key == key:
                pair[1] = value
                return

        # If the key was not found, add a new key-value pair
        # to the chain.
        chain.append([key, value])

    def get(self, key):
        # Find the index where this key should be.
        index = self.hash_function(key)

        # Get the chain at that index.
        chain = self.table[index]

        # Search through the chain for the key.
        for pair in chain:
            stored_key = pair[0]
            stored_value = pair[1]

            if stored_key == key:
                return stored_value

        # If the key was not found, return None.
        return None

    def remove(self, key):
        # Find the index where this key should be.
        index = self.hash_function(key)

        # Get the chain at that index.
        chain = self.table[index]

        # Search through the chain using an index so we can remove.
        for pair_index in range(len(chain)):
            stored_key = chain[pair_index][0]

            if stored_key == key:
                chain.pop(pair_index)
                return True

        # If the key was not found, nothing was removed.
        return False

    def print_table(self):
        # Print each index and its chain.
        print("Chained Hash Table")
        print("-" * 50)

        for index in range(self.size):
            print(f"Index {index}: {self.table[index]}")

# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

employee_table = ChainedHashTable(5)

# Insert badge 10.
# 10 % 5 = 0
# Store [10, "Trevonte"] in the chain at index 0.
employee_table.insert(10, "Trevonte")

# Insert badge 15.
# 15 % 5 = 0
# Index 0 already has data.
# Chaining adds [15, "Jordan"] to the same chain.
employee_table.insert(15, "Jordan")

# Insert badge 20.
# 20 % 5 = 0
# Index 0 already has data.
# Chaining adds [20, "Alex"] to the same chain.
employee_table.insert(20, "Alex")

# Insert badge 21.
# 21 % 5 = 1
# Store [21, "Morgan"] in the chain at index 1.
employee_table.insert(21, "Morgan")

# Insert badge 22.
# 22 % 5 = 2
# Store [22, "Casey"] in the chain at index 2.
employee_table.insert(22, "Casey")


print("Employee Badge Hash Table - Chaining")
print("=" * 50)

employee_table.print_table()


print()
print("Lookup Employees")
print("-" * 50)

# Search for badge 10.
# 10 % 5 = 0
# Check the chain at index 0.
# Find [10, "Trevonte"], so return "Trevonte".
print(f"Badge 10: {employee_table.get(10)}")

# Search for badge 15.
# 15 % 5 = 0
# Check the chain at index 0.
# Find [15, "Jordan"], so return "Jordan".
print(f"Badge 15: {employee_table.get(15)}")

# Search for badge 20.
# 20 % 5 = 0
# Check the chain at index 0.
# Find [20, "Alex"], so return "Alex".
print(f"Badge 20: {employee_table.get(20)}")

# Search for badge 99.
# 99 % 5 = 4
# Check the chain at index 4.
# Index 4 has an empty chain, so return None.
print(f"Badge 99: {employee_table.get(99)}")


print()
print("Update Employee")
print("-" * 50)

# Update badge 15.
# 15 % 5 = 0
# Check the chain at index 0.
# Badge 15 already exists, so update the value.
employee_table.insert(15, "Jordan Smith")

print("Updated badge 15 to Jordan Smith.")
print()
employee_table.print_table()


print()
print("Remove Employee")
print("-" * 50)

# Remove badge 20.
# 20 % 5 = 0
# Check the chain at index 0.
# Find [20, "Alex"] and remove it from the chain.
removed = employee_table.remove(20)

print(f"Removed badge 20: {removed}")

print()
employee_table.print_table()
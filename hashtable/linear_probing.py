# ============================================================
# Hash Table - Linear Probing
# ============================================================
#
# Linear probing is a collision-handling technique.
#
# A collision happens when two keys calculate the same index.
#
# Linear probing handles collisions by checking the next index
# one spot at a time until it finds an empty spot.
#
# ------------------------------------------------------------
# FORMULA
# ------------------------------------------------------------
#
# Starting index:
#
#   hash_index = key % table_size
#
# If there is a collision:
#
#   index = (hash_index + i) % table_size
#
# where:
#
#   i = 0, 1, 2, 3, ...
#
# ------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------
#
# table_size = 10
#
# Insert key 20:
#
#   20 % 10 = 0
#
# Store key 20 at index 0.
#
# Insert key 30:
#
#   30 % 10 = 0
#
# Index 0 is already used.
#
# Try the next index:
#
#   index = (0 + 1) % 10
#   index = 1
#
# Store key 30 at index 1.
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
# Linear probing can cause clustering.
#
# Clustering means many filled spots group together.
#
# When that happens, searching and inserting can become slower
# because the algorithm may need to check many indexes.
# ============================================================
class LinearProbingHashTable:
    def __init__(self, size):
        # Store the size of the hash table.
        self.size = size

        # Create the table.
        #
        # Each spot starts as None because it is empty.
        self.table = [None] * size

    def hash_function(self, key):
        # Convert the key into a starting index.
        #
        # Formula:
        #   index = key % table_size
        return key % self.size

    def insert(self, key, value):
        # Calculate the starting index.
        hash_index = self.hash_function(key)

        # Try each possible position in the table.
        for i in range(self.size):
            # Linear probing formula:
            #
            #   index = (hash_index + i) % table_size
            #
            # The modulo lets us wrap around to the beginning
            # of the table if we reach the end.
            index = (hash_index + i) % self.size

            # If the spot is empty, insert the key-value pair here.
            if self.table[index] is None:
                self.table[index] = [key, value]
                return True

            # If the key already exists, update the value.
            stored_key = self.table[index][0]

            if stored_key == key:
                self.table[index][1] = value
                return True

        # If the loop finishes, the table is full.
        return False

    def get(self, key):
        # Calculate the starting index.
        hash_index = self.hash_function(key)

        # Search using linear probing.
        for i in range(self.size):
            index = (hash_index + i) % self.size

            # If we hit an empty spot, the key is not in the table.
            #
            # Why?
            # If the key had been inserted, it would have appeared
            # before this empty spot in the probing sequence.
            if self.table[index] is None:
                return None

            stored_key = self.table[index][0]
            stored_value = self.table[index][1]

            # If the key matches, return the stored value.
            if stored_key == key:
                return stored_value

        # Key was not found.
        return None

    def remove(self, key):
        # Calculate the starting index.
        hash_index = self.hash_function(key)

        # Search using linear probing.
        for i in range(self.size):
            index = (hash_index + i) % self.size

            # If we hit an empty spot, the key is not in the table.
            if self.table[index] is None:
                return False

            stored_key = self.table[index][0]

            # If the key matches, remove it.
            if stored_key == key:
                self.table[index] = None
                return True

        # Key was not found.
        return False

    def print_table(self):
        # Print each index and the data stored there.
        print("Linear Probing Hash Table")
        print("-" * 50)

        for index in range(self.size):
            print(f"Index {index}: {self.table[index]}")


# ------------------------------------------------------------
# Real example: Employee badge lookup with linear probing
# ------------------------------------------------------------

employee_table = LinearProbingHashTable(10)

# Insert badge 20.
# 20 % 10 = 0
# Index 0 is empty, so store [20, "Trevonte"] at index 0.
employee_table.insert(20, "Trevonte")

# Insert badge 30.
# 30 % 10 = 0
# Index 0 is already used by badge 20.
# Linear probing checks the next index.
# (0 + 1) % 10 = 1
# Store [30, "Jordan"] at index 1.
employee_table.insert(30, "Jordan")

# Insert badge 40.
# 40 % 10 = 0
# Index 0 is already used.
# (0 + 1) % 10 = 1
# Index 1 is already used.
# (0 + 2) % 10 = 2
# Store [40, "Alex"] at index 2.
employee_table.insert(40, "Alex")

# Insert badge 51.
# 51 % 10 = 1
# Index 1 is already used by badge 30.
# (1 + 1) % 10 = 2
# Index 2 is already used by badge 40.
# (1 + 2) % 10 = 3
# Store [51, "Morgan"] at index 3.
employee_table.insert(51, "Morgan")

# Insert badge 72.
# 72 % 10 = 2
# Index 2 is already used by badge 40.
# (2 + 1) % 10 = 3
# Index 3 is already used by badge 51.
# (2 + 2) % 10 = 4
# Store [72, "Casey"] at index 4.
employee_table.insert(72, "Casey")


print("Employee Badge Hash Table - Linear Probing")
print("=" * 50)

employee_table.print_table()


print()
print("Lookup Employees")
print("-" * 50)

# Search for badge 20.
# 20 % 10 = 0
# Check index 0.
# Stored key is 20, so return "Trevonte".
print(f"Badge 20: {employee_table.get(20)}")

# Search for badge 40.
# 40 % 10 = 0
# Check index 0: stored key is 20, not 40.
# Check index 1: stored key is 30, not 40.
# Check index 2: stored key is 40, so return "Alex".
print(f"Badge 40: {employee_table.get(40)}")

# Search for badge 51.
# 51 % 10 = 1
# Check index 1: stored key is 30, not 51.
# Check index 2: stored key is 40, not 51.
# Check index 3: stored key is 51, so return "Morgan".
print(f"Badge 51: {employee_table.get(51)}")

# Search for badge 99.
# 99 % 10 = 9
# Check index 9.
# Index 9 is empty, so return None.
print(f"Badge 99: {employee_table.get(99)}")


print()
print("Update Employee")
print("-" * 50)

# Update badge 30.
# 30 % 10 = 0
# Check index 0: stored key is 20.
# Check index 1: stored key is 30.
# Update value to "Jordan Smith".
employee_table.insert(30, "Jordan Smith")

print("Updated badge 30 to Jordan Smith.")
print()
employee_table.print_table()


print()
print("Remove Employee")
print("-" * 50)

# Remove badge 72.
# 72 % 10 = 2
# Check index 2: stored key is 40.
# Check index 3: stored key is 51.
# Check index 4: stored key is 72.
# Set index 4 to None.
removed = employee_table.remove(72)

print(f"Removed badge 72: {removed}")

print()
employee_table.print_table()
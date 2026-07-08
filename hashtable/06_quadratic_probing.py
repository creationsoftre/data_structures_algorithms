# ============================================================
# Hash Table - Quadratic Probing
# ============================================================
#
# Quadratic probing is a collision-handling technique.
#
# Like linear probing, it stores values directly inside the table.
#
# The difference:
#
#   Linear probing checks the next spot one at a time.
#   Quadratic probing jumps farther each time.
#
# ------------------------------------------------------------
# FORMULA
# ------------------------------------------------------------
#
# Quadratic probing starts with the normal hash index.
#
# Starting index:
#
#   hash_index = key % table_size
#
# If the starting index is empty, insert the key there.
#
# If the starting index is already taken, use quadratic probing:
#
#   index = (hash_index + i^2) % table_size
#
# where:
#
#   i = 0, 1, 2, 3, ...
#
# The jumps are:
#
#   i = 0  ->  +0
#   i = 1  ->  +1
#   i = 2  ->  +4
#   i = 3  ->  +9
#   i = 4  ->  +16
#
# Important:
#
#   1^2 = 1
#
# So the first collision check is only one index away from the
# original hash index.
#
# The bigger jumps happen after more collisions.
# ------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------
#
# table_size = 11
#
# Insert key 22:
#
#   hash_index = 22 % 11
#   hash_index = 0
#
# Index 0 is empty.
# Store key 22 at index 0.
#
# Insert key 33:
#
#   hash_index = 33 % 11
#   hash_index = 0
#
# Index 0 is already used.
#
# Try i = 1:
#
#   index = (0 + 1^2) % 11
#   index = (0 + 1) % 11
#   index = 1
#
# Index 1 is empty.
# Store key 33 at index 1.
#
# Insert key 44:
#
#   hash_index = 44 % 11
#   hash_index = 0
#
# Index 0 is already used.
#
# Try i = 1:
#
#   index = (0 + 1^2) % 11
#   index = (0 + 1) % 11
#   index = 1
#
# Index 1 is already used.
#
# Try i = 2:
#
#   index = (0 + 2^2) % 11
#   index = (0 + 4) % 11
#   index = 4
#
# Index 4 is empty.
# Store key 44 at index 4.
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
# Quadratic probing can reduce clustering compared to linear probing.
#
# But it can still have problems if the table gets too full.
#
# It is common to use a prime table size, like 11, 17, or 23,
# to help spread values better.
# ============================================================
class QuadraticProbingHashTable:
    def __init__(self, size):
        # Store the size of the hash table.
        self.size = size

        # Create the table.
        #
        # Each spot starts as None because it is empty.
        self.table = [None] * size

        # This marker is used when a value is removed.
        #
        # Why not just set removed spots to None?
        #
        # In probing, search may need to continue past a removed spot.
        # If we used None, search could stop too early.
        self.deleted = "DELETED"

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
            # Quadratic probing formula:
            #
            #   index = (hash_index + i^2) % table_size
            #
            # i^2 means the jump gets larger each time.
            index = (hash_index + i ** 2) % self.size

            # If the spot is empty or was deleted, insert here.
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
        hash_index = self.hash_function(key)

        # Search using quadratic probing.
        for i in range(self.size):
            index = (hash_index + i ** 2) % self.size

            # If we hit a true empty spot, the key is not in the table.
            if self.table[index] is None:
                return None

            # If the spot was deleted, keep searching.
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
        hash_index = self.hash_function(key)

        # Search using quadratic probing.
        for i in range(self.size):
            index = (hash_index + i ** 2) % self.size

            # If we hit a true empty spot, the key is not in the table.
            if self.table[index] is None:
                return False

            # If the spot was deleted, keep searching.
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
        print("Quadratic Probing Hash Table")
        print("-" * 50)

        for index in range(self.size):
            print(f"Index {index}: {self.table[index]}")


# ------------------------------------------------------------
# Real example: Employee badge lookup with quadratic probing
# ------------------------------------------------------------

employee_table = QuadraticProbingHashTable(11)

# Insert badge 22.
# 22 % 11 = 0
# Index 0 is empty, so store [22, "Trevonte"] at index 0.
employee_table.insert(22, "Trevonte")

# Insert badge 33.
# 33 % 11 = 0
# Index 0 is already used by badge 22.
# Try i = 1.
# (0 + 1^2) % 11 = 1
# Store [33, "Jordan"] at index 1.
employee_table.insert(33, "Jordan")

# Insert badge 44.
# 44 % 11 = 0
# Index 0 is already used.
# Try i = 1.
# (0 + 1^2) % 11 = 1
# Index 1 is already used.
# Try i = 2.
# (0 + 2^2) % 11 = 4
# Store [44, "Alex"] at index 4.
employee_table.insert(44, "Alex")

# Insert badge 55.
# 55 % 11 = 0
# Index 0 is already used.
# Try i = 1.
# (0 + 1^2) % 11 = 1
# Index 1 is already used.
# Try i = 2.
# (0 + 2^2) % 11 = 4
# Index 4 is already used.
# Try i = 3.
# (0 + 3^2) % 11 = 9
# Store [55, "Morgan"] at index 9.
employee_table.insert(55, "Morgan")

# Insert badge 23.
# 23 % 11 = 1
# Index 1 is already used by badge 33.
# Try i = 1.
# (1 + 1^2) % 11 = 2
# Store [23, "Casey"] at index 2.
employee_table.insert(23, "Casey")


print("Employee Badge Hash Table - Quadratic Probing")
print("=" * 50)

employee_table.print_table()


print()
print("Lookup Employees")
print("-" * 50)

# Search for badge 22.
# 22 % 11 = 0
# Check index 0.
# Stored key is 22, so return "Trevonte".
print(f"Badge 22: {employee_table.get(22)}")

# Search for badge 44.
# 44 % 11 = 0
# Check index 0: stored key is 22, not 44.
# Try i = 1.
# (0 + 1^2) % 11 = 1
# Check index 1: stored key is 33, not 44.
# Try i = 2.
# (0 + 2^2) % 11 = 4
# Check index 4: stored key is 44, so return "Alex".
print(f"Badge 44: {employee_table.get(44)}")

# Search for badge 55.
# 55 % 11 = 0
# Check index 0: stored key is 22, not 55.
# Check index 1: stored key is 33, not 55.
# Check index 4: stored key is 44, not 55.
# Check index 9: stored key is 55, so return "Morgan".
print(f"Badge 55: {employee_table.get(55)}")

# Search for badge 99.
# 99 % 11 = 0
# Check the quadratic probing path.
# If the key is not found, return None.
print(f"Badge 99: {employee_table.get(99)}")


print()
print("Update Employee")
print("-" * 50)

# Update badge 33.
# 33 % 11 = 0
# Check index 0: stored key is 22.
# Check index 1: stored key is 33.
# Update value to "Jordan Smith".
employee_table.insert(33, "Jordan Smith")

print("Updated badge 33 to Jordan Smith.")
print()
employee_table.print_table()


print()
print("Remove Employee")
print("-" * 50)

# Remove badge 44.
# 44 % 11 = 0
# Check index 0: stored key is 22.
# Check index 1: stored key is 33.
# Check index 4: stored key is 44.
# Mark index 4 as DELETED.
removed = employee_table.remove(44)

print(f"Removed badge 44: {removed}")

print()
employee_table.print_table()
# ============================================================
# Direct Hashing
# ============================================================
#
# Direct hashing uses the key directly as the index.
#
# Simple idea:
#
#   key = index
#
# Example:
#
#   student_id = 4
#
#   table[4] stores that student's name.
#
# This is very fast because we do not need a hash formula like:
#
#   key % table_size
#
# The key already tells us where the value belongs.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Insert:
#   O(1)
#   Very fast.
#
# Search:
#   O(1)
#   Very fast.
#
# Remove:
#   O(1)
#   Very fast.
#
# Why?
#   The key directly points to the index.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# O(k)
#
# k = size of the possible key range.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Direct hashing is fast, but it can waste memory.
#
# It works well when keys are small and close together.
#
# Good example:
#
#   Student IDs from 0 to 9
#
# Bad example:
#
#   One employee ID is 1000000
#
# If we use the key directly as the index, we would need a list
# with at least 1,000,001 spots just to store one value.
# ============================================================
class DirectHashTable:
    def __init__(self, size):
        # Store the size of the table.
        #
        # Example:
        #   If size = 10, valid indexes are 0 through 9.
        self.size = size

        # Create the table.
        #
        # Each spot starts as None because no values are stored yet.
        self.table = [None] * size

    def insert(self, key, value):
        # Direct hashing uses the key as the index.
        #
        # Example:
        #   key = 4
        #   table[4] = value

        # Make sure the key is inside the table range.
        if key < 0 or key >= self.size:
            return False

        # Store the value directly at the key's index.
        self.table[key] = value
        return True

    def get(self, key):
        # Make sure the key is inside the table range.
        if key < 0 or key >= self.size:
            return None

        # Return the value stored at the key's index.
        return self.table[key]

    def remove(self, key):
        # Make sure the key is inside the table range.
        if key < 0 or key >= self.size:
            return False

        # If the spot is already empty, nothing was removed.
        if self.table[key] is None:
            return False

        # Remove the value by setting the spot back to None.
        self.table[key] = None
        return True

    def print_table(self):
        print("Direct Hash Table")
        print("-" * 50)

        for index in range(self.size):
            print(f"Index {index}: {self.table[index]}")

# ------------------------------------------------------------
# Real example: Small student ID lookup
# ------------------------------------------------------------

student_table = DirectHashTable(10)

print("Direct Hashing Example")
print("=" * 50)
print("Student IDs are small numbers from 0 to 9.")
print("Because the IDs are small, we can use each ID directly as an index.")
print()


# ------------------------------------------------------------
# Insert students
# ------------------------------------------------------------

print("Insert Students")
print("-" * 50)

# Insert student ID 2.
# Direct hashing:
# key = 2
# index = 2
# Store "Trevonte" at table[2].
student_table.insert(2, "Trevonte")
print('Student ID 2 goes directly to index 2 -> "Trevonte"')

# Insert student ID 5.
# Direct hashing:
# key = 5
# index = 5
# Store "Jordan" at table[5].
student_table.insert(5, "Jordan")
print('Student ID 5 goes directly to index 5 -> "Jordan"')

# Insert student ID 7.
# Direct hashing:
# key = 7
# index = 7
# Store "Alex" at table[7].
student_table.insert(7, "Alex")
print('Student ID 7 goes directly to index 7 -> "Alex"')

print()
student_table.print_table()


# ------------------------------------------------------------
# Lookup students
# ------------------------------------------------------------

print()
print("Lookup Students")
print("-" * 50)

# Search for student ID 2.
# key = 2
# index = 2
# Check table[2].
print("Lookup student ID 2")
print("key = 2")
print("index = 2")
print(f"Result: {student_table.get(2)}")
print()

# Search for student ID 5.
# key = 5
# index = 5
# Check table[5].
print("Lookup student ID 5")
print("key = 5")
print("index = 5")
print(f"Result: {student_table.get(5)}")
print()

# Search for student ID 9.
# key = 9
# index = 9
# Check table[9].
# No value was stored there, so return None.
print("Lookup student ID 9")
print("key = 9")
print("index = 9")
print(f"Result: {student_table.get(9)}")


# ------------------------------------------------------------
# Remove student
# ------------------------------------------------------------

print()
print("Remove Student")
print("-" * 50)

# Remove student ID 5.
# key = 5
# index = 5
# Set table[5] back to None.
removed = student_table.remove(5)

print("Remove student ID 5")
print("key = 5")
print("index = 5")
print(f"Removed: {removed}")

print()
student_table.print_table()


# ------------------------------------------------------------
# Memory warning example
# ------------------------------------------------------------

print()
print("Why Direct Hashing Can Waste Memory")
print("=" * 50)

print("Direct hashing is great when keys are small.")
print("But it can waste memory when keys are very large.")
print()

print("Example:")
print("If the only employee ID is 1000000, direct hashing would need:")
print("indexes 0 through 1000000")
print()
print("That means a list with 1,000,001 spots just to store one employee.")
print()
print("This is why normal hash tables usually use a hash function like:")
print("index = key % table_size")
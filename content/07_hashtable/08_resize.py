# ============================================================
# Hash Table - Resizing
# ============================================================
#
# Hash table resizing happens when the table gets too full.
#
# Why?
#
#   The fuller the table gets, the more collisions happen.
#   More collisions can make insert and search slower.
#
# To fix this, the hash table can resize itself.
#
# Resizing means:
#
#   1. Create a larger table.
#   2. Reinsert the old key-value pairs.
#   3. Recalculate each key's index using the new table size.
#
# This is called rehashing.
#
# ============================================================
# Hash Table - Resizing
# ============================================================
#
# Hash table resizing happens when the table gets too full.
#
# Why?
#
#   The fuller the table gets, the more collisions happen.
#   More collisions can make insert and search slower.
#
# To fix this, the hash table can resize itself.
#
# Resizing means:
#
#   1. Create a larger table.
#   2. Reinsert the old key-value pairs.
#   3. Recalculate each key's index using the new table size.
#
# This is called rehashing.
#
# ------------------------------------------------------------
# LOAD FACTOR
# ------------------------------------------------------------
#
# Load factor measures how full the hash table is.
#
# Formula:
#
#   load_factor = number_of_items / table_size
#
# Example:
#
#   number_of_items = 7
#   table_size = 10
#
#   load_factor = 7 / 10
#   load_factor = 0.7
#
# If the load factor gets too high, we resize the table.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Average insert/search/remove:
#   O(1)
#   Very fast when the table is not too full.
#
# Resize:
#   O(n)
#   Slower because every existing item must be rehashed.
#
# Important:
#   Resizing does not happen every insert.
#   It only happens when the table gets too full.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# O(n)
#
# We store n key-value pairs.
#
# During resizing, we temporarily create a larger table.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Resizing helps keep hash table operations fast.
#
# Without resizing, the table can become crowded.
#
# A crowded table causes more collisions, which can make searching
# and inserting slower.
# ============================================================
class ResizingHashTable:
    def __init__(self, size):
        # Store the current table size.
        self.size = size

        # Create the table.
        #
        # This version uses chaining, so each index starts
        # with an empty list.
        self.table = []

        for _ in range(size):
            self.table.append([])

        # Track how many key-value pairs are stored.
        self.count = 0

        # Resize when the table is 70% full.
        self.max_load_factor = 0.7

    def hash_function(self, key):
        # Convert the key into an index.
        #
        # Formula:
        #   index = key % table_size
        return key % self.size

    def load_factor(self):
        # Calculate how full the table is.
        #
        # Formula:
        #   load_factor = number_of_items / table_size
        return self.count / self.size

    def insert(self, key, value):
        # Before inserting, check if the table is getting too full.
        #
        # We check what the load factor would be after adding
        # one more item.
        future_load_factor = (self.count + 1) / self.size

        # If the future load factor is too high, resize first.
        if future_load_factor >= self.max_load_factor:
            self.resize()

        # Find the index for this key.
        index = self.hash_function(key)

        # Get the chain at that index.
        chain = self.table[index]

        # If the key already exists, update it.
        for pair in chain:
            if pair[0] == key:
                pair[1] = value
                return

        # Otherwise, add a new key-value pair.
        chain.append([key, value])

        # Increase the number of stored items.
        self.count += 1

    def get(self, key):
        # Find the index where the key should be.
        index = self.hash_function(key)

        # Search the chain at that index.
        chain = self.table[index]

        for pair in chain:
            stored_key = pair[0]
            stored_value = pair[1]

            if stored_key == key:
                return stored_value

        return None

    def remove(self, key):
        # Find the index where the key should be.
        index = self.hash_function(key)

        # Search the chain at that index.
        chain = self.table[index]

        for pair_index in range(len(chain)):
            if chain[pair_index][0] == key:
                chain.pop(pair_index)
                self.count -= 1
                return True

        return False

    def resize(self):
        # Save the old table so we can reinsert its values.
        old_table = self.table

        # Double the table size.
        old_size = self.size
        self.size = self.size * 2

        # Create a new empty table with the larger size.
        self.table = []

        for _ in range(self.size):
            self.table.append([])

        # Reset count because insert will rebuild the table.
        self.count = 0

        # Reinsert every key-value pair from the old table.
        #
        # This is called rehashing because each key gets a new
        # index based on the new table size.
        for chain in old_table:
            for pair in chain:
                key = pair[0]
                value = pair[1]

                self.insert(key, value)

    def print_table(self):
        print("Resizing Hash Table")
        print("-" * 50)
        print(f"Table size: {self.size}")
        print(f"Number of items: {self.count}")
        print(f"Load factor: {self.load_factor():.2f}")
        print("-" * 50)

        for index in range(self.size):
            print(f"Index {index}: {self.table[index]}")


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

employee_table = ResizingHashTable(5)

# ------------------------------------------------------------
# Real example: Employee badge lookup with resizing
# ------------------------------------------------------------

employee_table = ResizingHashTable(5)

print("Employee Badge Hash Table - Resizing")
print("=" * 60)
print("Starting table size: 5")
print("Resize rule: resize when load factor reaches 0.7")
print()


# ------------------------------------------------------------
# Insert first employee
# ------------------------------------------------------------

print("Insert badge 10")
print("-" * 60)
print("10 % 5 = 0")
print('Store [10, "Trevonte"] at index 0.')
employee_table.insert(10, "Trevonte")
employee_table.print_table()
print()


# ------------------------------------------------------------
# Insert second employee
# ------------------------------------------------------------

print("Insert badge 15")
print("-" * 60)
print("15 % 5 = 0")
print("Index 0 already has badge 10.")
print("Because this table uses chaining, add badge 15 to index 0's chain.")
employee_table.insert(15, "Jordan")
employee_table.print_table()
print()


# ------------------------------------------------------------
# Insert third employee
# ------------------------------------------------------------

print("Insert badge 21")
print("-" * 60)
print("21 % 5 = 1")
print('Store [21, "Alex"] at index 1.')
employee_table.insert(21, "Alex")
employee_table.print_table()
print()


# ------------------------------------------------------------
# Insert fourth employee, causing resize
# ------------------------------------------------------------

print("Insert badge 22")
print("=" * 60)
print("Before inserting badge 22:")
print(f"Current number of items: {employee_table.count}")
print(f"Current table size: {employee_table.size}")
print()

print("Check what the load factor would become:")
print("future_load_factor = (current_items + 1) / table_size")
print(f"future_load_factor = ({employee_table.count} + 1) / {employee_table.size}")
print(f"future_load_factor = {employee_table.count + 1} / {employee_table.size}")
print(f"future_load_factor = {(employee_table.count + 1) / employee_table.size:.2f}")
print()

print("Resize limit: 0.70")
print("0.80 is greater than or equal to 0.70, so resize happens first.")
print()

print("Resize step:")
print("Old table size: 5")
print("New table size: 10")
print()

print("Rehash existing employees using the new table size:")
print("10 % 10 = 0  -> Trevonte moves to index 0")
print("15 % 10 = 5  -> Jordan moves to index 5")
print("21 % 10 = 1  -> Alex moves to index 1")
print()

print("Now insert the new employee:")
print("22 % 10 = 2  -> Morgan goes to index 2")
print()

employee_table.insert(22, "Morgan")

print("Table after resize, rehash, and inserting badge 22:")
employee_table.print_table()
print()


# ------------------------------------------------------------
# Insert fifth employee
# ------------------------------------------------------------

print("Insert badge 33")
print("=" * 60)
print("The table size is now 10.")
print("33 % 10 = 3")
print('Store [33, "Casey"] at index 3.')
employee_table.insert(33, "Casey")
employee_table.print_table()
print()


# ------------------------------------------------------------
# Lookup employees
# ------------------------------------------------------------

print("Lookup Employees")
print("=" * 60)

print("Lookup badge 10")
print("10 % 10 = 0")
print("Check index 0.")
print(f"Result: {employee_table.get(10)}")
print()

print("Lookup badge 15")
print("15 % 10 = 5")
print("Check index 5.")
print(f"Result: {employee_table.get(15)}")
print()

print("Lookup badge 22")
print("22 % 10 = 2")
print("Check index 2.")
print(f"Result: {employee_table.get(22)}")
print()


# ------------------------------------------------------------
# Remove employee
# ------------------------------------------------------------

print("Remove Employee")
print("=" * 60)

print("Remove badge 21")
print("Current table size = 10")
print("21 % 10 = 1")
print("Check index 1 and remove [21, \"Alex\"].")

removed = employee_table.remove(21)

print(f"Removed badge 21: {removed}")
print()
employee_table.print_table()
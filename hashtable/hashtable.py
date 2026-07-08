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
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        self.table[index] = [key, value]

    def get(self, key):
        index = self.hash_function(key)

        if self.table[index] is None:
            return None

        stored_key = self.table[index][0]
        stored_value = self.table[index][1]

        if stored_key == key:
            return stored_value

        return None

    def remove(self, key):
        index = self.hash_function(key)

        if self.table[index] is None:
            return False

        stored_key = self.table[index][0]

        if stored_key == key:
            self.table[index] = None
            return True

        return False

    def print_table(self):
        print("Hash Table")
        print("-" * 40)

        for index in range(self.size):
            print(f"Index {index}: {self.table[index]}")
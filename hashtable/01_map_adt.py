# ============================================================
# Map ADT
# ============================================================
#
# ADT means Abstract Data Type.
#
# A Map ADT stores key-value pairs.
#
# Simple idea:
#
#   Use a key to find a value.
#
# Examples:
#
#   student_id -> student_name
#   username   -> email
#   word       -> definition
#
# A key should be unique.
#
# That means:
#
#   One key maps to one value.
#
# If we add the same key again, we update the value.
#
# ------------------------------------------------------------
# COMMON MAP OPERATIONS
# ------------------------------------------------------------
#
# put(key, value)
#   Add a new key-value pair.
#   If the key already exists, update the value.
#
# get(key)
#   Return the value connected to the key.
#
# remove(key)
#   Delete a key-value pair.
#
# contains_key(key)
#   Check if a key exists.
#
# print_map()
#   Print all key-value pairs.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# This simple version uses a list.
#
# Search:
#   O(n)
#
# Speed:
#   Can be slow as the map grows.
#
# Why?
#   We may need to check each key one by one.
#
# Insert:
#   O(n)
#
# Speed:
#   Can be slow if we need to check whether the key already exists.
#
# Remove:
#   O(n)
#
# Speed:
#   Can be slow because we may need to search through the list.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   O(n)
#
# Why?
#   We store n key-value pairs.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# This file explains the Map ADT concept.
#
# It does not use hashing yet.
#
# Later, a hash table will make map operations faster by using
# a hash function to jump directly to an index.
# ============================================================
# ------------------------------------------------------------
# SimpleMap class
# ------------------------------------------------------------
#
# This class stores key-value pairs using a list.
#
# Each pair is stored as a small list:
#
#   [key, value]
#
# Example:
#
#   ["A123", "Trevonte"]
# ------------------------------------------------------------

class SimpleMap:
    def __init__(self):
        # Start with an empty list.
        #
        # This list will store all key-value pairs.
        self.items = []

    # --------------------------------------------------------
    # put
    # --------------------------------------------------------
    #
    # Add or update a key-value pair.
    #
    # If the key does not exist:
    #   Add the new key-value pair.
    #
    # If the key already exists:
    #   Update the existing value.
    # --------------------------------------------------------

    def put(self, key, value):
        # Loop through the existing key-value pairs.
        for pair in self.items:

            # pair[0] is the key.
            # pair[1] is the value.
            if pair[0] == key:
                # Key already exists, so update the value.
                pair[1] = value
                return

        # If the loop finishes, the key was not found.
        # Add a new key-value pair.
        self.items.append([key, value])

    # --------------------------------------------------------
    # get
    # --------------------------------------------------------
    #
    # Find a value by key.
    #
    # If the key exists:
    #   Return the value.
    #
    # If the key does not exist:
    #   Return None.
    # --------------------------------------------------------

    def get(self, key):
        # Search through each key-value pair.
        for pair in self.items:

            # If the key matches, return the value.
            if pair[0] == key:
                return pair[1]

        # Key was not found.
        return None

    # --------------------------------------------------------
    # remove
    # --------------------------------------------------------
    #
    # Remove a key-value pair.
    #
    # If the key exists:
    #   Remove it and return True.
    #
    # If the key does not exist:
    #   Return False.
    # --------------------------------------------------------

    def remove(self, key):
        # Use an index so we can remove the item from the list.
        for index in range(len(self.items)):

            # Check if the key matches.
            if self.items[index][0] == key:
                # Remove the pair at this index.
                self.items.pop(index)
                return True

        # Key was not found.
        return False

    # --------------------------------------------------------
    # contains_key
    # --------------------------------------------------------
    #
    # Check whether a key exists in the map.
    # --------------------------------------------------------

    def contains_key(self, key):
        # Search through each key-value pair.
        for pair in self.items:

            # If the key matches, the key exists.
            if pair[0] == key:
                return True

        # Key was not found.
        return False

    # --------------------------------------------------------
    # print_map
    # --------------------------------------------------------
    #
    # Print the current map in a readable way.
    # --------------------------------------------------------

    def print_map(self):
        print("Current Map")
        print("-" * 40)

        # If the map is empty, show that clearly.
        if len(self.items) == 0:
            print("Map is empty.")
            return

        # Print each key-value pair.
        for pair in self.items:
            print(f"{pair[0]} -> {pair[1]}")

# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

student_map = SimpleMap()

print("Map ADT Example")
print("=" * 50)
print("A map stores key-value pairs.")
print()

print("Regular Operations")
print("-" * 50)

student_map.put("A123", "Trevonte")
student_map.put("B456", "Jordan")
student_map.put("C789", "Alex")

student_map.print_map()

print()
print(f"Get A123: {student_map.get('A123')}")
print(f"Contains B456: {student_map.contains_key('B456')}")

print()
print("Update A123")
print("-" * 50)

student_map.put("A123", "Trevonte Wigfall")
student_map.print_map()

print()
print("Remove C789")
print("-" * 50)

student_map.remove("C789")
student_map.print_map()

# ============================================================
# Python Set Class
# ============================================================
#
# Python has a built-in set class.
#
# A set stores unique values.
#
# Unique means:
#
#   No duplicates allowed.
#
# Example:
#
#   numbers = {10, 5, 15}
#
# If we try to add 10 again, the set does not store another 10.
#
# ------------------------------------------------------------
# IMPORTANT IDEA
# ------------------------------------------------------------
#
# Python set is not a BST.
#
# Python set uses hashing.
#
# That means it is closer to the hash table chapter than the
# tree chapter.
#
# But it is included here because the chapter compares Set ADT
# ideas with different implementations.
#
# ------------------------------------------------------------
# SET ADT VS PYTHON SET
# ------------------------------------------------------------
#
# Set ADT:
#
#   The idea of a collection with unique values.
#
# Python set:
#
#   Python's built-in version of a set.
#
# A Set ADT tells us what operations a set should support:
#
#   add
#   remove
#   contains
#   size
#
# Python set gives us those operations already.
#
# ------------------------------------------------------------
# COMMON PYTHON SET OPERATIONS
# ------------------------------------------------------------
#
# Add:
#
#   numbers.add(10)
#
# Remove:
#
#   numbers.remove(10)
#
# Search / contains:
#
#   10 in numbers
#
# Size:
#
#   len(numbers)
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Python set add:
#
#   Average case: O(1)
#
# Speed:
#   Very fast.
#
# Python set search:
#
#   Average case: O(1)
#
# Speed:
#   Very fast.
#
# Python set remove:
#
#   Average case: O(1)
#
# Speed:
#   Very fast.
#
# Why?
#   Python set uses hashing.
#
# ------------------------------------------------------------
# WORST CASE
# ------------------------------------------------------------
#
# Python set operations can be O(n) in rare worst cases.
#
# Why?
#   Hash collisions can happen.
#
# But average case is usually O(1).
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Storing a set:
#
#   O(n)
#
# Why?
#   The set stores n unique values.
#
# ------------------------------------------------------------
# PYTHON SET VS BST SET
# ------------------------------------------------------------
#
# Python set:
#
#   Uses hashing.
#   Average add/search/remove is O(1).
#   Does not keep values sorted.
#
# BST set:
#
#   Uses a binary search tree.
#   Balanced add/search/remove is O(log n).
#   Can return values in sorted order with inorder traversal.
#
# ------------------------------------------------------------
# MAIN TAKEAWAY
# ------------------------------------------------------------
#
# A set stores unique values.
#
# Python's built-in set is usually faster than a BST set for
# add, search, and remove.
#
# But a BST set can naturally give sorted order.
# ============================================================


print("Python Set Class")
print("=" * 60)
print()

print("A Python set stores unique values.")
print("That means duplicates are not allowed.")
print()


# ------------------------------------------------------------
# Create a set
# ------------------------------------------------------------

print("Create a Set")
print("-" * 60)

numbers = set()

print("numbers = set()")
print(f"Current set: {numbers}")
print()


# ------------------------------------------------------------
# Add values
# ------------------------------------------------------------

print("Add Values")
print("-" * 60)

# Add 10.
# 10 is not in the set yet, so it is added.
numbers.add(10)
print("numbers.add(10)")
print(f"Current set: {numbers}")
print()

# Add 5.
# 5 is not in the set yet, so it is added.
numbers.add(5)
print("numbers.add(5)")
print(f"Current set: {numbers}")
print()

# Add 15.
# 15 is not in the set yet, so it is added.
numbers.add(15)
print("numbers.add(15)")
print(f"Current set: {numbers}")
print()


# ------------------------------------------------------------
# Try to add duplicates
# ------------------------------------------------------------

print("Try To Add Duplicates")
print("-" * 60)

print("Current set before duplicates:")
print(numbers)
print()

# Add 10 again.
# Since 10 already exists, the set does not change.
numbers.add(10)
print("numbers.add(10)")
print("10 already exists, so it is not added again.")
print(f"Current set: {numbers}")
print()

# Add 5 again.
# Since 5 already exists, the set does not change.
numbers.add(5)
print("numbers.add(5)")
print("5 already exists, so it is not added again.")
print(f"Current set: {numbers}")
print()

print("Main point:")
print("Even after adding duplicates, each value appears only once.")
print()


# ------------------------------------------------------------
# Contains / search
# ------------------------------------------------------------

print("Contains / Search")
print("-" * 60)

# Python uses the word "in" to check if a value exists.
#
# This is like contains(value) in a Set ADT.
print("Check if 10 is in the set:")
print("10 in numbers")
print(f"Result: {10 in numbers}")
print()

print("Check if 99 is in the set:")
print("99 in numbers")
print(f"Result: {99 in numbers}")
print()


# ------------------------------------------------------------
# Remove values
# ------------------------------------------------------------

print("Remove Values")
print("-" * 60)

print("Before removing 5:")
print(numbers)
print()

# Remove 5 from the set.
numbers.remove(5)

print("numbers.remove(5)")
print("5 was removed.")
print(f"Current set: {numbers}")
print()


# ------------------------------------------------------------
# Size
# ------------------------------------------------------------

print("Set Size")
print("-" * 60)

print("len(numbers)")
print(f"Size: {len(numbers)}")
print()


# ------------------------------------------------------------
# Set order warning
# ------------------------------------------------------------

print("Set Order Warning")
print("-" * 60)

print("Python sets do not guarantee sorted order.")
print("The values may not print in the same order you added them.")
print()

print("Current set:")
print(numbers)
print()

print("If you need sorted output, use sorted(numbers):")
print(sorted(numbers))
print()


# ------------------------------------------------------------
# Compare with BST Set
# ------------------------------------------------------------

print("Python Set vs BST Set")
print("=" * 60)

print("Python set:")
print("Uses hashing.")
print("Average add/search/remove: O(1)")
print("Does not naturally keep values sorted.")
print()

print("BST set:")
print("Uses a binary search tree.")
print("Balanced add/search/remove: O(log n)")
print("Can give sorted order with inorder traversal.")
print()


# ------------------------------------------------------------
# Main takeaway
# ------------------------------------------------------------

print("Main Takeaway")
print("=" * 60)

print("A Python set stores unique values.")
print("Duplicates are ignored.")
print()
print("Python set is usually very fast because it uses hashing.")
print()
print("A BST set is useful for understanding trees and sorted order.")
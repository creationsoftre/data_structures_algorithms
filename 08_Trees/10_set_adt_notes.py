# ============================================================
# Set ADT Notes
# ============================================================
#
# A Set is a collection of unique values.
#
# Unique means:
#
#   No duplicates allowed.
#
# Example:
#
#   {5, 10, 15}
#
# If we try to add 10 again, the set does not change.
#
# ------------------------------------------------------------
# REAL-LIFE EXAMPLES
# ------------------------------------------------------------
#
# Set of usernames:
#
#   {"trevonte", "alex", "jordan"}
#
# A username should only appear once.
#
# Set of student IDs:
#
#   {1021, 1022, 1023}
#
# A student ID should only appear once.
#
# Set of game players online:
#
#   {"player1", "player2", "player3"}
#
# A player should not be listed twice.
#
# ------------------------------------------------------------
# COMMON SET OPERATIONS
# ------------------------------------------------------------
#
# add(value):
#
#   Add a value if it does not already exist.
#
# contains(value):
#
#   Check if a value exists in the set.
#
# remove(value):
#
#   Remove a value from the set.
#
# size():
#
#   Return how many unique values are stored.
#
# ------------------------------------------------------------
# SET RULE
# ------------------------------------------------------------
#
# A set does not allow duplicates.
#
# Example:
#
#   add(10)
#   add(10)
#   add(10)
#
# The set still only stores:
#
#   {10}
#
# ------------------------------------------------------------
# HOW A BST CAN IMPLEMENT A SET
# ------------------------------------------------------------
#
# A Binary Search Tree can be used to build a set.
#
# BST rule:
#
#   smaller values go left
#   larger values go right
#
# Set rule:
#
#   duplicates are not allowed
#
# So when inserting into a BST set:
#
#   if value is smaller:
#       go left
#
#   if value is larger:
#       go right
#
#   if value already exists:
#       do not insert it again
#
# ------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------
#
# Add these values:
#
#   10, 5, 15, 5, 10, 20
#
# Step-by-step:
#
#   add(10)
#       10 is new, insert it.
#
#   add(5)
#       5 is new, insert it.
#
#   add(15)
#       15 is new, insert it.
#
#   add(5)
#       5 already exists, skip it.
#
#   add(10)
#       10 already exists, skip it.
#
#   add(20)
#       20 is new, insert it.
#
# Final set:
#
#   {5, 10, 15, 20}
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# BST Set add:
#
#   Balanced tree:   O(log n)
#   Unbalanced tree: O(n)
#
# BST Set contains:
#
#   Balanced tree:   O(log n)
#   Unbalanced tree: O(n)
#
# BST Set remove:
#
#   Balanced tree:   O(log n)
#   Unbalanced tree: O(n)
#
# Speed:
#
#   Fast if the tree is balanced.
#   Slow if the tree becomes a chain.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Storing the set:
#
#   O(n)
#
# Why?
#   The set stores n unique values.
#
# Recursive operations:
#
#   O(h)
#
# h = height of the tree.
#
# Balanced tree:
#
#   h = log n
#
# Unbalanced tree:
#
#   h = n
#
# ------------------------------------------------------------
# PYTHON SET NOTE
# ------------------------------------------------------------
#
# Python already has a built-in set class.
#
# Example:
#
#   numbers = set()
#   numbers.add(10)
#   numbers.add(5)
#   numbers.add(10)
#
# Result:
#
#   {10, 5}
#
# Python's built-in set uses hashing, not a BST.
#
# Average speed for Python set:
#
#   add:      O(1)
#   contains: O(1)
#   remove:   O(1)
#
# ------------------------------------------------------------
# BST SET VS PYTHON SET
# ------------------------------------------------------------
#
# BST Set:
#
#   Uses tree structure.
#   Can give sorted order with inorder traversal.
#   Speed depends on tree height.
#
# Python set:
#
#   Uses hash table structure.
#   Very fast average lookup.
#   Does not guarantee sorted order.
#
# ------------------------------------------------------------
# MAIN TAKEAWAY
# ------------------------------------------------------------
#
# A set stores unique values.
#
# A BST can implement a set by refusing duplicates.
#
# Python's built-in set is usually faster because it uses hashing.
# ============================================================


print("Set ADT Notes")
print("=" * 60)
print()

print("A set stores unique values.")
print("That means duplicates are not allowed.")
print()

print("Example:")
print("Add values: 10, 5, 15, 5, 10, 20")
print()

print("Step-by-step:")
print("add(10) -> 10 is new, insert it.")
print("add(5)  -> 5 is new, insert it.")
print("add(15) -> 15 is new, insert it.")
print("add(5)  -> 5 already exists, skip it.")
print("add(10) -> 10 already exists, skip it.")
print("add(20) -> 20 is new, insert it.")
print()

print("Final unique values:")
print("{5, 10, 15, 20}")
print()

print("How a BST can act like a set:")
print("-" * 60)
print("If value is smaller, go left.")
print("If value is larger, go right.")
print("If value already exists, do not insert it again.")
print()

print("BST Set Complexity:")
print("-" * 60)
print("Balanced BST add/search/remove:   O(log n)")
print("Unbalanced BST add/search/remove: O(n)")
print()

print("Python Built-in Set:")
print("-" * 60)
print("Python set uses hashing.")
print("Average add/search/remove: O(1)")
print()

print("Main Takeaway")
print("=" * 60)
print("A set stores unique values.")
print("A BST can implement a set by rejecting duplicates.")
print("Python's built-in set is usually faster because it uses hashing.")
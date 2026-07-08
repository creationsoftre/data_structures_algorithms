# ============================================================
# Longest Path in a Binary Tree
# ============================================================
#
# The longest path in this example means:
#
#   The longest path from the root node down to a leaf node.
#
# A leaf node is a node with no children.
#
# Example:
#
#              13
#            /    \
#           7      21
#         /  \    /  \
#        4   10  18  25
#       /              \
#      2                30
#
# Longest root-to-leaf paths:
#
#   13 -> 7 -> 4 -> 2
#   13 -> 21 -> 25 -> 30
#
# Both paths have 4 nodes.
#
# The longest path length is 4.
#
# ------------------------------------------------------------
# BIG O / TIME COMPLEXITY
# ------------------------------------------------------------
#
# Time Complexity:
#   O(n)
#
# Why?
#   We may need to visit every node in the tree once.
#
#   n = number of nodes
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Recursive version:
#   O(h)
#
# Why?
#   The recursive calls use the call stack.
#
#   h = height of the tree
#
# In a balanced tree:
#   O(log n)
#
# In an unbalanced tree:
#   O(n)
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# This version finds the longest path from the root to a leaf.
#
# This is different from the diameter of a tree.
#
# Root-to-leaf longest path:
#
#   Starts at the root.
#   Ends at a leaf.
#
# Tree diameter:
#
#   Can start at any node.
#   Can end at any node.
#   Does not have to pass through the root.
# ============================================================


# ------------------------------------------------------------
# Step 1: Create a Node class
# ------------------------------------------------------------
#
# Each node stores:
#
#   1. A value
#   2. A left child
#   3. A right child
# ------------------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ------------------------------------------------------------
# Step 2: Insert values into the Binary Search Tree
# ------------------------------------------------------------
#
# We are using the same insert logic from the BST search example.
#
# Smaller values go left.
# Larger values go right.
# ------------------------------------------------------------

def insert(root, value):
    # If the tree is empty, create the first node.
    if root is None:
        return Node(value)

    # Start at the root.
    current = root

    # Keep moving until we find an empty spot.
    while True:

        # Smaller values go left.
        if value < current.value:

            # If the left side is empty, insert here.
            if current.left is None:
                current.left = Node(value)
                break

            # Otherwise, keep moving left.
            current = current.left

        # Larger values go right.
        elif value > current.value:

            # If the right side is empty, insert here.
            if current.right is None:
                current.right = Node(value)
                break

            # Otherwise, keep moving right.
            current = current.right

        # Do not insert duplicate values.
        else:
            break

    return root


# ------------------------------------------------------------
# Step 3: Find the longest path length
# ------------------------------------------------------------
#
# This function returns the longest path length from the current
# node down to a leaf node.
#
# The idea:
#
#   1. Find the longest path on the left side.
#   2. Find the longest path on the right side.
#   3. Choose the larger one.
#   4. Add 1 for the current node.
#
# Base case:
#
#   If the current node is None, return 0.
#
# Why return 0?
#
#   None means there is no node there.
#   So that path has a length of 0.
# ------------------------------------------------------------

def longest_path_length(root):
    # Base case:
    # An empty tree has a path length of 0.
    if root is None:
        return 0

    # Find the longest path on the left side.
    left_path = longest_path_length(root.left)

    # Find the longest path on the right side.
    right_path = longest_path_length(root.right)

    # Choose the longer side and add 1 for the current node.
    return 1 + max(left_path, right_path)


# ------------------------------------------------------------
# Step 4: Find the longest path values
# ------------------------------------------------------------
#
# The previous function returns only the length.
#
# This function returns the actual path as a list.
#
# Example:
#
#   [13, 7, 4, 2]
#
# The idea:
#
#   1. Get the longest path from the left side.
#   2. Get the longest path from the right side.
#   3. Choose the longer path.
#   4. Add the current node to the front.
# ------------------------------------------------------------

def longest_path_values(root):
    # Base case:
    # If there is no node, return an empty path.
    if root is None:
        return []

    # Get the longest path from the left child.
    left_path = longest_path_values(root.left)

    # Get the longest path from the right child.
    right_path = longest_path_values(root.right)

    # If the left path is longer, use the left path.
    if len(left_path) > len(right_path): # This example has two longest paths we just chose the right side. If you want the left changee this line to if len(left_path) >= len(right_path):
        return [root.value] + left_path

    # Otherwise, use the right path.
    return [root.value] + right_path


# ------------------------------------------------------------
# Step 5: Trace the longest path
# ------------------------------------------------------------
#
# This version prints what is happening.
#
# It helps us see:
#
#   Which node is being checked
#   The longest path on the left
#   The longest path on the right
#   Which side gets chosen
# ------------------------------------------------------------

def longest_path_with_trace(root):
    # Base case:
    # If there is no node, return an empty path.
    if root is None:
        return []

    print(f"Checking node: {root.value}")

    # Find the longest path from the left side.
    left_path = longest_path_with_trace(root.left)

    # Find the longest path from the right side.
    right_path = longest_path_with_trace(root.right)

    print(f"Node {root.value}")
    print(f"Left path:  {left_path}")
    print(f"Right path: {right_path}")

    # Choose the longer path.
    if len(left_path) > len(right_path):
        chosen_path = [root.value] + left_path
        print(f"Choose left path: {chosen_path}")
    else:
        chosen_path = [root.value] + right_path
        print(f"Choose right path: {chosen_path}")

    print()

    return chosen_path


# ------------------------------------------------------------
# Step 6: Build a sample tree
# ------------------------------------------------------------
#
# We will build this tree:
#
#              13
#            /    \
#           7      21
#         /  \    /  \
#        4   10  18  25
#       /              \
#      2                30
# ------------------------------------------------------------

root = None

values = [13, 7, 21, 4, 10, 18, 25, 2, 30]

for value in values:
    root = insert(root, value)


# ------------------------------------------------------------
# Step 7: Test longest path length
# ------------------------------------------------------------

length = longest_path_length(root)

print(f"Longest path length: {length}")


# ------------------------------------------------------------
# Step 8: Test longest path values
# ------------------------------------------------------------

path = longest_path_values(root)

print(f"Longest path values: {path}")


# ------------------------------------------------------------
# Step 9: Test longest path with trace
# ------------------------------------------------------------

print()
print("Trace:")
print("-" * 40)

trace_path = longest_path_with_trace(root)

print(f"Final longest path: {trace_path}")
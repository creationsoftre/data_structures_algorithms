# ============================================================
# Binary Search Tree Search
# ============================================================
#
# A Binary Search Tree, also called a BST, stores values using
# a simple rule:
#
#   Smaller values go to the left.
#   Larger values go to the right.
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
# Searching for 18:
#
#   Start at 13.
#   18 is larger than 13, so move right.
#   Now we are at 21.
#   18 is smaller than 21, so move left.
#   Now we are at 18.
#   Found it.
#
# The main idea:
#
#   We do not always need to check every node.
#   Each comparison tells us which side of the tree to ignore.
#
# ------------------------------------------------------------
# TIME COMPLEXITY
# ------------------------------------------------------------
#
# Best case:
#   O(1)
#   The target is found at the root node.
#
# Average case:
#   O(log n)
#   The tree is balanced, so each step removes part of the tree.
#
# Worst case:
#   O(n)
#   The tree is unbalanced and behaves like a linked list.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Iterative search:
#   O(1)
#
# The search only uses a few variables:
#
#   current
#   target
#
# It does not create another list or copy the tree.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Binary Search Tree search is only fast when the tree is balanced.
#
# Balanced tree:
#
#              13
#            /    \
#           7      21
#         /  \    /  \
#        4   10  18  25
#
# Search is faster because the tree branches.
#
# Unbalanced tree:
#
#      2
#       \
#        4
#         \
#          7
#           \
#            10
#             \
#              13
#
# Search is slower because the tree starts to act like a list.
# ============================================================


# ------------------------------------------------------------
# Step 1: Create a Node class
# ------------------------------------------------------------
#
# Each node stores:
#
# 1. A value
# 2. A left child
# 3. A right child
#
# The left child stores smaller values.
# The right child stores larger values.
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
# This function adds a new value to the tree.
#
# Rules:
#
# - If the tree is empty, the new value becomes the root.
# - If the new value is smaller than the current node, go left.
# - If the new value is larger than the current node, go right.
# - Repeat until we find an empty spot.
# ------------------------------------------------------------

def insert(root, value):
    # If the tree is empty, create the first node.
    if root is None:
        return Node(value)

    # Start at the root node.
    current = root

    # Keep moving through the tree until we insert the value.
    while True:

        # If the new value is smaller, it belongs on the left side.
        if value < current.value:

            # If there is no left child, insert the new node here.
            if current.left is None:
                current.left = Node(value)
                break

            # Otherwise, move to the left child and keep checking.
            current = current.left

        # If the new value is larger, it belongs on the right side.
        elif value > current.value:

            # If there is no right child, insert the new node here.
            if current.right is None:
                current.right = Node(value)
                break

            # Otherwise, move to the right child and keep checking.
            current = current.right

        # If the value already exists, we will not insert it again.
        else:
            break

    # Return the root so we still have access to the full tree.
    return root


# ------------------------------------------------------------
# Step 3: Search for a value in the Binary Search Tree
# ------------------------------------------------------------
#
# This function searches for a target value.
#
# It returns True if the value is found.
# It returns False if the value is not found.
#
# Search rules:
#
# - Start at the root.
# - If the target equals the current node, we found it.
# - If the target is smaller, move left.
# - If the target is larger, move right.
# - If we reach None, the value is not in the tree.
# ------------------------------------------------------------

def search(root, target):
    # Start searching from the root node.
    current = root

    # Keep searching while there is still a node to check.
    while current is not None:

        # If the current node has the target value, return True.
        if current.value == target:
            return True

        # If the target is smaller, search the left side.
        elif target < current.value:
            current = current.left

        # If the target is larger, search the right side.
        else:
            current = current.right

    # If we reach None, the value was not found.
    return False


# ------------------------------------------------------------
# Step 4: Search with a trace
# ------------------------------------------------------------
#
# This version prints what is happening at each step.
#
# This is useful for learning because we can see:
#
# - Which node is being checked
# - Why we move left
# - Why we move right
# - When the search stops
# ------------------------------------------------------------

def search_with_trace(root, target):
    # Start at the root node.
    current = root

    print(f"Searching for: {target}")
    print("-" * 40)

    # Continue while there is a node to check.
    while current is not None:

        # Show the current node being checked.
        print(f"Checking node: {current.value}")

        # Case 1: The current node is the target.
        if current.value == target:
            print(f"Found {target}!")
            return True

        # Case 2: The target is smaller than the current node.
        elif target < current.value:
            print(f"{target} is smaller than {current.value}. Move left.")
            current = current.left

        # Case 3: The target is larger than the current node.
        else:
            print(f"{target} is larger than {current.value}. Move right.")
            current = current.right

        print()

    # If the loop ends, we reached an empty spot.
    print(f"{target} was not found in the tree.")
    return False


# ------------------------------------------------------------
# Step 5: Build a sample tree
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
# Step 6: Test regular search
# ------------------------------------------------------------

print(search(root, 18))  # True
print(search(root, 99))  # False


# ------------------------------------------------------------
# Step 7: Test search with trace
# ------------------------------------------------------------

print()
search_with_trace(root, 18)

print()
search_with_trace(root, 99)
# ============================================================
# Binary Tree Basics
# ============================================================
#
# A binary tree is a tree where each node has at most two children.
#
# The two children are usually called:
#
#   left child
#   right child
#
# Example:
#
#              A
#            /   \
#           B     C
#          / \     \
#         D   E     F
#
# A is the root.
# B is A's left child.
# C is A's right child.
# D and E are children of B.
# F is the right child of C.
#
# ------------------------------------------------------------
# BINARY TREE RULE
# ------------------------------------------------------------
#
# A binary tree does not have to be sorted.
#
# The only rule is:
#
#   Each node can have at most two children.
#
# This is different from a Binary Search Tree.
#
# Binary Tree:
#
#   At most two children.
#
# Binary Search Tree:
#
#   At most two children,
#   AND smaller values go left,
#   AND larger values go right.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Searching a normal binary tree:
#
#   O(n)
#
# Speed:
#   Can be slow.
#
# Why?
#   A regular binary tree has no sorting rule.
#   The value could be anywhere.
#   We may need to check every node.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Storing the tree:
#
#   O(n)
#
# Why?
#   A tree with n nodes stores n node objects.
#
# Recursive traversal:
#
#   O(h)
#
# Why?
#   Recursive calls use the call stack.
#
# h = height of the tree
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
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# A binary tree is a structure.
#
# A binary search tree is a structure plus an ordering rule.
#
# Do not assume a binary tree is sorted.
# ============================================================

# ------------------------------------------------------------
# Node class
# ------------------------------------------------------------
#
# A node stores:
#
#   1. A value
#   2. A left child
#   3. A right child
#
# If a child does not exist, it is stored as None.
# ------------------------------------------------------------

class Node:
    def __init__(self, value):
        # Store the value inside the node.
        #
        # Example:
        #   "A"
        #   10
        #   "Trevonte"
        self.value = value

        # Store the left child.
        #
        # This starts as None because the node does not have
        # a left child yet.
        self.left = None

        # Store the right child.
        #
        # This starts as None because the node does not have
        # a right child yet.
        self.right = None

# ------------------------------------------------------------
# Build a simple binary tree manually
# ------------------------------------------------------------
#
# We will build this tree:
#
#              A
#            /   \
#           B     C
#          / \     \
#         D   E     F
#
# This is not a Binary Search Tree.
#
# It is just a regular binary tree.
# ------------------------------------------------------------

root = Node("A")

root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")

root.right.right = Node("F")

# ------------------------------------------------------------
# Print root and children
# ------------------------------------------------------------
#
# This helps us see how the nodes are connected.
# ------------------------------------------------------------

print("Binary Tree Basics")
print("=" * 50)

print("Tree structure:")
print()
print("             A")
print("           /   \\")
print("          B     C")
print("         / \\     \\")
print("        D   E     F")
print()

print("Root:")
print(f"root.value = {root.value}")
print()

print("Root's children:")
print(f"root.left.value = {root.left.value}")
print(f"root.right.value = {root.right.value}")
print()

print("B's children:")
print(f"root.left.left.value = {root.left.left.value}")
print(f"root.left.right.value = {root.left.right.value}")
print()

print("C's children:")
print("root.right.left = None")
print(f"root.right.right.value = {root.right.right.value}")

# ------------------------------------------------------------
# Check if a node is a leaf
# ------------------------------------------------------------
#
# A leaf node has no children.
#
# That means:
#
#   left is None
#   right is None
# ------------------------------------------------------------

def is_leaf(node):
    # If the node does not exist, it cannot be a leaf.
    if node is None:
        return False

    # A node is a leaf if both children are None.
    return node.left is None and node.right is None


print()
print("Leaf Checks")
print("-" * 50)

print(f"Is A a leaf? {is_leaf(root)}")
print(f"Is D a leaf? {is_leaf(root.left.left)}")
print(f"Is E a leaf? {is_leaf(root.left.right)}")
print(f"Is F a leaf? {is_leaf(root.right.right)}")

# ------------------------------------------------------------
# Count nodes
# ------------------------------------------------------------
#
# This function counts how many nodes are in the tree.
#
# Since a normal binary tree is not sorted, we may need to visit
# every node.
#
# Time Complexity:
#
#   O(n)
#
# Why?
#   We count each node one time.
# ------------------------------------------------------------

def count_nodes(node):
    # Base case:
    # If there is no node, count 0.
    if node is None:
        return 0

    # Count the current node.
    current_node = 1

    # Count the nodes on the left side.
    left_count = count_nodes(node.left)

    # Count the nodes on the right side.
    right_count = count_nodes(node.right)

    # Total = current node + left side + right side.
    return current_node + left_count + right_count


print()
print("Count Nodes")
print("-" * 50)

total_nodes = count_nodes(root)

print("This tree has 6 nodes:")
print("A, B, C, D, E, F")
print(f"Total nodes counted: {total_nodes}")


# ------------------------------------------------------------
# Find height
# ------------------------------------------------------------
#
# Height is the longest path from a node down to a leaf.
#
# In this example:
#
#              A
#            /   \
#           B     C
#          / \     \
#         D   E     F
#
# Longest path:
#
#   A -> B -> D
#
# or
#
#   A -> C -> F
#
# These paths have 2 edges.
#
# So the height is 2.
#
# Time Complexity:
#
#   O(n)
#
# Why?
#   We may need to check every node.
# ------------------------------------------------------------

def height(node):
    # Base case:
    # An empty tree has height -1.
    #
    # Why -1?
    # A leaf node should have height 0.
    #
    # If a leaf's left and right children return -1:
    #
    #   height = 1 + max(-1, -1)
    #   height = 0
    if node is None:
        return -1

    # Find the height of the left subtree.
    left_height = height(node.left)

    # Find the height of the right subtree.
    right_height = height(node.right)

    # The height is 1 plus the taller side.
    return 1 + max(left_height, right_height)


print()
print("Tree Height")
print("-" * 50)

tree_height = height(root)

print("Height counts edges from root to deepest leaf.")
print(f"Tree height: {tree_height}")
print()

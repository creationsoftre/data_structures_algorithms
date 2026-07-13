# ============================================================
# Treap - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A treap is a tree that combines:
#
#   Binary Search Tree
#
# and:
#
#   Heap
#
# The name treap comes from:
#
#   Tree + Heap
#
# Each node stores:
#
#   Key:
#       Used for the Binary Search Tree rule.
#
#   Priority:
#       Used for the heap rule.
#
#   Left:
#       A reference to the left child.
#
#   Right:
#       A reference to the right child.
#
#
# TWO RULES
# ------------------------------------------------------------
#
# A treap must follow two rules:
#
#   1. Binary Search Tree Rule
#
#   2. Heap Priority Rule
#
#
# BINARY SEARCH TREE RULE
# ------------------------------------------------------------
#
# The node keys follow the normal BST rule:
#
#   Smaller keys go left.
#
#   Larger keys go right.
#
# Example:
#
#           50
#         /    \
#       30      70
#      /  \    /  \
#    20   40  60   80
#
#
# HEAP PRIORITY RULE
# ------------------------------------------------------------
#
# This implementation uses a min-heap priority rule.
#
# Smaller priority numbers represent higher priority.
#
# Every parent must have a priority less than or equal to the
# priorities of its children.
#
# Example:
#
#              50 (10)
#             /       \
#        30 (20)      70 (30)
#
# Keys:
#
#   30 < 50 < 70
#
# Priorities:
#
#   10 < 20
#   10 < 30
#
# The tree follows both the BST rule and the heap rule.
#
#
# NODE FORMAT
# ------------------------------------------------------------
#
# Nodes will be displayed as:
#
#   key (priority)
#
# Example:
#
#   Brake Repair (10)
#
# The repair name is the key.
#
# The number is the priority.
#
#
# WHY TREAPS EXIST
# ------------------------------------------------------------
#
# A normal Binary Search Tree can become unbalanced.
#
# Example:
#
# Insert:
#
#   10, 20, 30, 40
#
# Normal BST:
#
#   10
#     \
#      20
#        \
#         30
#           \
#            40
#
# This becomes a chain.
#
# Search can become:
#
#   O(n)
#
# A treap uses priorities and rotations to help keep the tree
# balanced.
#
# Priorities are commonly generated randomly.
#
# Random priorities make a badly unbalanced tree unlikely.
#
#
# HOW INSERTION WORKS
# ------------------------------------------------------------
#
# Treap insertion has two phases:
#
#   1. Insert the key using the BST rule.
#
#   2. Use rotations to restore the heap priority rule.
#
#
# INSERTION EXAMPLE
# ------------------------------------------------------------
#
# Original treap:
#
#       50 (20)
#
# Insert:
#
#   30 (10)
#
# First, use the BST rule:
#
#       50 (20)
#       /
#   30 (10)
#
# The priority rule is violated because:
#
#   10 < 20
#
# The child has a higher priority than the parent.
#
# Perform a right rotation:
#
#       30 (10)
#          \
#          50 (20)
#
# Both rules are now restored.
#
#
# ROTATIONS
# ------------------------------------------------------------
#
# Rotations rearrange nodes without breaking the BST order.
#
#
# RIGHT ROTATION
# ------------------------------------------------------------
#
# Before:
#
#           50
#          /
#        30
#          \
#           40
#
# After:
#
#        30
#          \
#           50
#          /
#        40
#
#
# LEFT ROTATION
# ------------------------------------------------------------
#
# Before:
#
#        30
#          \
#           50
#          /
#        40
#
# After:
#
#           50
#          /
#        30
#          \
#           40
#
#
# HOW DELETION WORKS
# ------------------------------------------------------------
#
# To delete a node:
#
#   1. Find the node using the BST rule.
#
#   2. Rotate the node downward.
#
#   3. Continue until the node becomes a leaf.
#
#   4. Remove the leaf node.
#
# The child with the higher priority is rotated upward.
#
# In this min-heap implementation, the child with the smaller
# priority number is rotated upward.
#
#
# MAIN TREAP OPERATIONS
# ------------------------------------------------------------
#
# insert(key, priority)
#     Adds a new node and restores both treap rules.
#
# search(key)
#     Searches for a node using the BST rule.
#
# delete(key)
#     Removes a node and restores both treap rules.
#
# find_min()
#     Returns the smallest key.
#
# find_max()
#     Returns the largest key.
#
# inorder()
#     Returns all keys in sorted order.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
#   Operation       Average Case       Worst Case
#   ------------------------------------------------
#   insert()          O(log n)            O(n)
#   search()          O(log n)            O(n)
#   delete()          O(log n)            O(n)
#   find_min()        O(log n)            O(n)
#   find_max()        O(log n)            O(n)
#   inorder()         O(n)                O(n)
#
# Random priorities usually keep the treap balanced.
#
# This gives insert, search, and delete an expected time of:
#
#   O(log n)
#
# The worst case is still possible if the tree becomes
# completely unbalanced.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(n)
#
# The treap stores one node for every key.
#
# Each node stores:
#
#   - A key
#   - A priority
#   - A left-child reference
#   - A right-child reference
#
#
# ============================================================
# NODE CLASS
# ============================================================
class Node:
    def __init__(self, key, priority):
        # Store the key used for the Binary Search Tree rule.
        self.key = key
        # Store the priority used for the heap rule.
        self.priority = priority
        # Point to the left child.
        self.left = None
        # Point to the right child.
        self.right = None
# ============================================================
# TREAP IMPLEMENTATION
# ============================================================
class Treap:
    def __init__(self):
        # The root points to the first node in the treap.
        #
        # None means the treap is currently empty.
        self.root = None
    def _rotate_right(self, node):
        # Save the node's left child.
        new_root = node.left
        # Move the left child's right subtree.
        node.left = new_root.right
        # Make the original node the right child.
        new_root.right = node
        # Return the new root of this subtree.
        return new_root
    def _rotate_left(self, node):
        # Save the node's right child.
        new_root = node.right
        # Move the right child's left subtree.
        node.right = new_root.left
        # Make the original node the left child.
        new_root.left = node
        # Return the new root of this subtree.
        return new_root
    def insert(self, key, priority):
        # Insert the new key and priority into the treap.
        self.root = self._insert(self.root, key, priority)
    def _insert(self, node, key, priority):
        # Create a new node when an empty position is found.
        if node is None:
            return Node(key, priority)
        # Move left when the new key is smaller.
        if key < node.key:
            node.left = self._insert(node.left, key, priority)
            # Restore the min-heap priority rule.
            #
            # A smaller number represents a higher priority.
            if node.left.priority < node.priority:
                node = self._rotate_right(node)
        # Move right when the new key is larger.
        elif key > node.key:
            node.right = self._insert(node.right, key, priority)
            # Restore the min-heap priority rule.
            if node.right.priority < node.priority:
                node = self._rotate_left(node)
        else:
            # Duplicate keys are not inserted.
            return node
        # Return the updated subtree root.
        return node
    def search(self, key):
        # Start searching from the root.
        current = self.root
        # Continue until the key is found or the search reaches
        # an empty position.
        while current is not None:
            # Return the node when the key matches.
            if key == current.key:
                return current
            # Move left when the key is smaller.
            if key < current.key:
                current = current.left
            # Move right when the key is larger.
            else:
                current = current.right
        # Return None when the key is not found.
        return None
    def delete(self, key):
        # Remove the key from the treap.
        self.root = self._delete(self.root, key)
    def _delete(self, node, key):
        # Stop when the key is not found.
        if node is None:
            return None
        # Search the left subtree.
        if key < node.key:
            node.left = self._delete(node.left, key)
        # Search the right subtree.
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # The node has been found.
            #
            # Remove it immediately when it has no children.
            if node.left is None and node.right is None:
                return None
            # Replace the node with its right child when there
            # is no left child.
            if node.left is None:
                return node.right
            # Replace the node with its left child when there
            # is no right child.
            if node.right is None:
                return node.left
            # Both children exist.
            #
            # Rotate the child with the smaller priority number
            # upward.
            if node.left.priority < node.right.priority:
                node = self._rotate_right(node)
                node.right = self._delete(node.right, key)
            else:
                node = self._rotate_left(node)
                node.left = self._delete(node.left, key)
        # Return the updated subtree root.
        return node
    def find_min(self):
        # Return None when the treap is empty.
        if self.root is None:
            return None
        # The smallest key is the leftmost node.
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key
    def find_max(self):
        # Return None when the treap is empty.
        if self.root is None:
            return None
        # The largest key is the rightmost node.
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key
    def inorder(self):
        # Create a list for keys in sorted order.
        result = []
        # Visit every node using inorder traversal.
        self._inorder(self.root, result)
        return result
    def _inorder(self, node, result):
        # Stop when an empty position is reached.
        if node is None:
            return
        # Visit the left subtree.
        self._inorder(node.left, result)
        # Visit the current key.
        result.append(node.key)
        # Visit the right subtree.
        self._inorder(node.right, result)
# ============================================================
# CODE EXAMPLE - CAR REPAIR JOBS
# ============================================================
#
# Create a treap for car repair jobs.
repair_jobs = Treap()
#
# Keys are repair job names.
#
# Smaller priority numbers represent more urgent jobs.
#
# Insert:
#
#   Wheel Cleaning (40)
repair_jobs.insert("Wheel Cleaning", 40)
#
# Insert:
#
#   Brake Failure (10)
#
# Brake Failure has a smaller key alphabetically and a higher
# priority than Wheel Cleaning.
#
# A rotation may move Brake Failure upward.
repair_jobs.insert("Brake Failure", 10)
#
# Insert:
#
#   Flat Tire (20)
repair_jobs.insert("Flat Tire", 20)
#
# Insert:
#
#   Engine Overheating (5)
#
# Priority 5 is the highest priority currently stored.
repair_jobs.insert("Engine Overheating", 5)
#
# Insert:
#
#   Oil Change (30)
repair_jobs.insert("Oil Change", 30)
#
# inorder() returns the keys in alphabetical order because the
# treap still follows the Binary Search Tree rule.
print("Jobs in sorted order:", repair_jobs.inorder())
#
# Search for a specific repair job.
found_job = repair_jobs.search("Flat Tire")
#
# Display the job's priority when it is found.
if found_job is not None:
    print("Flat Tire priority:", found_job.priority)
#
# find_min() returns the smallest key alphabetically.
print("First job alphabetically:", repair_jobs.find_min())
#
# find_max() returns the largest key alphabetically.
print("Last job alphabetically:", repair_jobs.find_max())
#
# Delete Oil Change from the treap.
repair_jobs.delete("Oil Change")
#
# Display the remaining keys.
print("After deletion:", repair_jobs.inorder())
#
# ============================================================
# EXPECTED OUTPUT
# ============================================================
#
# Jobs in sorted order: ['Brake Failure', 'Engine Overheating',
# 'Flat Tire', 'Oil Change', 'Wheel Cleaning']
# Flat Tire priority: 20
# First job alphabetically: Brake Failure
# Last job alphabetically: Wheel Cleaning
# After deletion: ['Brake Failure', 'Engine Overheating',
# 'Flat Tire', 'Wheel Cleaning']
# ============================================================
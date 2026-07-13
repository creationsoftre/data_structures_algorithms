# ============================================================
# Heap - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A heap is a specialized tree-based data structure.
#
# A heap is usually stored inside an array.
#
# It must follow two main rules:
#
#   1. Complete Binary Tree Rule
#
#   2. Heap-Order Rule
#
#
# COMPLETE BINARY TREE RULE
# ------------------------------------------------------------
#
# Every level must be completely filled except possibly the
# final level.
#
# Nodes on the final level must be filled from left to right.
#
# Example:
#
#           10
#         /    \
#       20      30
#      /  \    /
#    40   50  60
#
# This is a complete binary tree.
#
#
# TYPES OF HEAPS
# ------------------------------------------------------------
#
# Min-Heap:
#
#   The smallest value is stored at the root.
#
#   Every parent must be less than or equal to its children.
#
# Example:
#
#           10
#         /    \
#       20      30
#      /  \    /
#    40   50  60
#
#
# Max-Heap:
#
#   The largest value is stored at the root.
#
#   Every parent must be greater than or equal to its children.
#
# Example:
#
#           60
#         /    \
#       50      40
#      /  \    /
#    20   10  30
#
#
# IMPORTANT
# ------------------------------------------------------------
#
# A heap is not the same as a Binary Search Tree.
#
# In a Binary Search Tree:
#
#   Smaller values go left.
#   Larger values go right.
#
# In a heap:
#
#   Only the parent-child relationship matters.
#
# Sibling nodes do not need to be sorted.
#
#
# ARRAY REPRESENTATION
# ------------------------------------------------------------
#
# A heap is commonly stored in an array.
#
# Example min-heap:
#
#           10
#         /    \
#       20      30
#      /  \    /
#    40   50  60
#
# Array:
#
#   [10, 20, 30, 40, 50, 60]
#
# Indexes:
#
#   [ 0,  1,  2,  3,  4,  5]
#
#
# INDEX FORMULAS
# ------------------------------------------------------------
#
# For a node stored at index i:
#
#   Parent index:
#
#       (i - 1) // 2
#
#   Left child index:
#
#       (2 * i) + 1
#
#   Right child index:
#
#       (2 * i) + 2
#
#
# EXAMPLE
# ------------------------------------------------------------
#
# Node 20 is stored at index 1.
#
# Left child:
#
#   (2 * 1) + 1 = 3
#
# Index 3 contains 40.
#
# Right child:
#
#   (2 * 1) + 2 = 4
#
# Index 4 contains 50.
#
#
# MAIN HEAP OPERATIONS
# ------------------------------------------------------------
#
# insert(item)
#     Adds a new value to the heap.
#
# remove()
#     Removes and returns the root value.
#
# peek()
#     Returns the root value without removing it.
#
# is_empty()
#     Checks whether the heap contains no values.
#
# size()
#     Returns the number of values currently in the heap.
#
#
# HEAPIFY UP
# ------------------------------------------------------------
#
# When a value is inserted:
#
#   1. Add it to the end of the array.
#
#   2. Compare it with its parent.
#
#   3. Swap it upward until the heap property is restored.
#
# Example:
#
# Original min-heap:
#
#   [10, 20, 30, 40, 50]
#
# Insert:
#
#   15
#
# Add 15 to the end:
#
#   [10, 20, 30, 40, 50, 15]
#
# Compare 15 with its parent, 30.
#
# Swap:
#
#   [10, 20, 15, 40, 50, 30]
#
# The min-heap property is restored.
#
#
# HEAPIFY DOWN
# ------------------------------------------------------------
#
# When the root is removed:
#
#   1. Move the final value to the root.
#
#   2. Compare it with its children.
#
#   3. Swap it downward until the heap property is restored.
#
# Example:
#
# Original min-heap:
#
#   [10, 20, 15, 40, 50, 30]
#
# Remove 10.
#
# Move 30 to the root:
#
#   [30, 20, 15, 40, 50]
#
# Compare 30 with its smaller child, 15.
#
# Swap:
#
#   [15, 20, 30, 40, 50]
#
# The min-heap property is restored.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
#   Operation       Time Complexity
#   -------------------------------
#   insert()             O(log n)
#   remove()             O(log n)
#   peek()               O(1)
#   is_empty()           O(1)
#   size()               O(1)
#   search()             O(n)
#
# insert() may move a value from the bottom of the tree to
# the root.
#
# remove() may move a value from the root to the bottom.
#
# A complete binary tree has a height of:
#
#   O(log n)
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(n)
#
# The heap stores one array element for every value.
#
#
# ============================================================
# MIN-HEAP IMPLEMENTATION
# ============================================================


class MinHeap:
    def __init__(self):
        # Create an empty list to store the heap's values.
        self.items = []

    def insert(self, item):
        # Add the new value to the end of the array.
        self.items.append(item)

        # Find the index of the newly added value.
        current_index = len(self.items) - 1

        # Move the new value upward until the min-heap
        # property is restored.
        self._heapify_up(current_index)

    def _heapify_up(self, index):
        # Continue while the current node is not the root.
        while index > 0:
            # Find the current node's parent index.
            parent_index = (index - 1) // 2

            # Stop if the parent is already smaller than or
            # equal to the current value.
            if self.items[parent_index] <= self.items[index]:
                break

            # Swap the current value with its parent.
            self.items[parent_index], self.items[index] = (
                self.items[index],
                self.items[parent_index],
            )

            # Continue checking from the parent's old position.
            index = parent_index

    def remove(self):
        # A value cannot be removed from an empty heap.
        if self.is_empty():
            return None

        # Save the smallest value stored at the root.
        removed_item = self.items[0]

        # Remove the final value from the array.
        last_item = self.items.pop()

        # If values remain, move the final value to the root.
        if not self.is_empty():
            self.items[0] = last_item

            # Move the new root downward until the min-heap
            # property is restored.
            self._heapify_down(0)

        # Return the smallest value that was removed.
        return removed_item

    def _heapify_down(self, index):
        # Store the number of values currently in the heap.
        heap_size = len(self.items)

        while True:
            # Calculate the left and right child indexes.
            left_child = (2 * index) + 1
            right_child = (2 * index) + 2

            # Assume the current node contains the smallest value.
            smallest = index

            # Check whether the left child exists and is smaller.
            if (
                left_child < heap_size
                and self.items[left_child] < self.items[smallest]
            ):
                smallest = left_child

            # Check whether the right child exists and is smaller.
            if (
                right_child < heap_size
                and self.items[right_child] < self.items[smallest]
            ):
                smallest = right_child

            # Stop when the current node is already the smallest.
            if smallest == index:
                break

            # Swap the current value with its smaller child.
            self.items[index], self.items[smallest] = (
                self.items[smallest],
                self.items[index],
            )

            # Continue checking from the child's old position.
            index = smallest

    def peek(self):
        # An empty heap does not have a root value.
        if self.is_empty():
            return None

        # Return the smallest value without removing it.
        return self.items[0]

    def is_empty(self):
        # The heap is empty when the list contains no values.
        return len(self.items) == 0

    def size(self):
        # Return the number of values currently in the heap.
        return len(self.items)


# ============================================================
# CODE EXAMPLE - CAR REPAIR PRIORITY
# ============================================================
#
# Smaller numbers represent more urgent repair jobs.
#
# Priority:
#
#   1 = Emergency
#   2 = High
#   3 = Medium
#   4 = Low
#
# Create a min-heap for repair priorities.
repair_queue = MinHeap()

# Add a low-priority wheel cleaning job.
#
# Heap:
#
#   [4]
repair_queue.insert(4)

# Add a medium-priority tire replacement.
#
# Heap:
#
#   [3, 4]
repair_queue.insert(3)

# Add an emergency brake failure.
#
# Before heapify up:
#
#   [3, 4, 1]
#
# After heapify up:
#
#   [1, 4, 3]
repair_queue.insert(1)

# Add a high-priority wheel bearing repair.
#
# Before heapify up:
#
#   [1, 4, 3, 2]
#
# After heapify up:
#
#   [1, 2, 3, 4]
repair_queue.insert(2)

# peek() returns the most urgent priority.
print("Most urgent priority:", repair_queue.peek())

# size() returns the number of repair jobs.
print("Repair jobs:", repair_queue.size())

# remove() removes the smallest priority number.
completed_priority = repair_queue.remove()

# Priority 1 was removed first.
print("Completing priority:", completed_priority)

# Priority 2 is now the smallest value.
print("Next priority:", repair_queue.peek())

# Display the heap's internal array.
print("Heap:", repair_queue.items)

# ============================================================
# EXPECTED OUTPUT
# ============================================================
#
# Most urgent priority: 1
# Repair jobs: 4
# Completing priority: 1
# Next priority: 2
# Heap: [2, 4, 3]
# ============================================================
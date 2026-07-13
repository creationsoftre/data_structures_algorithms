# ============================================================
# Priority Queue - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A priority queue stores items based on priority.
#
# Items with a higher priority are removed before items with
# a lower priority.
#
# A priority queue does not always follow:
#
#   First In, First Out
#
# Instead, it follows:
#
#   Highest Priority Out First
#
# When two items have the same priority, they can be removed
# in the order they were added.
#
#
# EXAMPLE - CAR REPAIR SHOP
# ------------------------------------------------------------
#
# A repair shop may receive these jobs:
#
#   Priority 3: Wheel cleaning
#   Priority 1: Brake failure
#   Priority 2: Flat tire
#   Priority 1: Engine overheating
#
# Smaller priority numbers represent more urgent repairs.
#
# Removal order:
#
#   1. Brake failure
#   2. Engine overheating
#   3. Flat tire
#   4. Wheel cleaning
#
# The emergency jobs are handled before the less urgent jobs.
#
#
# PRIORITY LEVELS
# ------------------------------------------------------------
#
# In this example:
#
#   1 = Emergency
#   2 = High
#   3 = Medium
#   4 = Low
#
# Smaller numbers represent higher priority.
#
#
# HOW A PRIORITY QUEUE WORKS
# ------------------------------------------------------------
#
# A priority queue is commonly implemented using a heap.
#
# Python provides the heapq module.
#
# heapq creates a min-heap.
#
# This means the smallest value is stored at the root.
#
# Each item can be stored as a tuple:
#
#   (priority, order, item)
#
# Example:
#
#   (1, 0, "Brake failure")
#
#   Priority:
#       1
#
#   Order:
#       0
#
#   Item:
#       Brake failure
#
# The order value keeps items with the same priority in the
# order they were added.
#
#
# MAIN PRIORITY QUEUE OPERATIONS
# ------------------------------------------------------------
#
# enqueue(item, priority)
#     Adds an item with a priority value.
#
# dequeue()
#     Removes and returns the highest-priority item.
#
# peek()
#     Returns the highest-priority item without removing it.
#
# is_empty()
#     Checks whether the priority queue is empty.
#
# size()
#     Returns the number of items currently stored.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
#   Operation       Time Complexity
#   -------------------------------
#   enqueue()            O(log n)
#   dequeue()            O(log n)
#   peek()               O(1)
#   is_empty()           O(1)
#   size()               O(1)
#
# enqueue() may move a new item upward through the heap.
#
# dequeue() may move an item downward through the heap.
#
# peek() is O(1) because the highest-priority item is stored
# at index 0.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(n)
#
# The priority queue stores one heap entry for every item.
#
#
# ============================================================
# PRIORITY QUEUE IMPLEMENTATION
# ============================================================


import heapq


class PriorityQueue:
    def __init__(self):
        # Create an empty list for the heap.
        self.items = []

        # Track the order in which items are added.
        #
        # This allows items with the same priority to remain
        # in First In, First Out order.
        self.order = 0

    def enqueue(self, item, priority):
        # Create a tuple containing:
        #
        #   priority
        #   insertion order
        #   item
        entry = (priority, self.order, item)

        # Add the entry to the heap.
        #
        # heappush() automatically restores the min-heap.
        heapq.heappush(self.items, entry)

        # Increase the order value for the next item.
        self.order += 1

    def dequeue(self):
        # A value cannot be removed from an empty queue.
        if self.is_empty():
            return None

        # Remove the tuple with the smallest priority value.
        priority, order, item = heapq.heappop(self.items)

        # Return only the stored item.
        return item

    def peek(self):
        # An empty priority queue does not have a front item.
        if self.is_empty():
            return None

        # Index 0 contains the highest-priority entry.
        priority, order, item = self.items[0]

        # Return the item without removing it.
        return item

    def is_empty(self):
        # The priority queue is empty when the heap has no items.
        return len(self.items) == 0

    def size(self):
        # Return the number of items currently stored.
        return len(self.items)


# ============================================================
# CODE EXAMPLE - CAR REPAIR PRIORITY
# ============================================================
#
# Create a priority queue for repair jobs.
repair_queue = PriorityQueue()

# Add a medium-priority wheel cleaning job.
#
# Priority:
#
#   3 = Medium
repair_queue.enqueue("Wheel cleaning", 3)

# Add an emergency brake failure.
#
# Priority:
#
#   1 = Emergency
repair_queue.enqueue("Brake failure", 1)

# Add a high-priority flat tire.
#
# Priority:
#
#   2 = High
repair_queue.enqueue("Flat tire", 2)

# Add another emergency repair.
#
# This job has the same priority as Brake failure.
#
# Brake failure remains ahead because it was added first.
repair_queue.enqueue("Engine overheating", 1)

# Add a low-priority interior cleaning job.
#
# Priority:
#
#   4 = Low
repair_queue.enqueue("Interior cleaning", 4)

# peek() returns the most urgent repair without removing it.
print("Next repair:", repair_queue.peek())

# size() returns the number of repair jobs waiting.
print("Repairs waiting:", repair_queue.size())

# dequeue() removes the highest-priority repair.
completed_repair = repair_queue.dequeue()

# Brake failure is removed first.
print("Repairing:", completed_repair)

# Engine overheating is now the highest-priority repair.
print("Next repair:", repair_queue.peek())

# Remove and display every remaining repair.
while not repair_queue.is_empty():
    print("Repairing:", repair_queue.dequeue())

# ============================================================
# EXPECTED OUTPUT
# ============================================================
#
# Next repair: Brake failure
# Repairs waiting: 5
# Repairing: Brake failure
# Next repair: Engine overheating
# Repairing: Engine overheating
# Repairing: Flat tire
# Repairing: Wheel cleaning
# Repairing: Interior cleaning
# ============================================================
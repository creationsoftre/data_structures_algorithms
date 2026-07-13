# ============================================================
# Queue Using an Array - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A queue can be built using an array.
#
# In Python, a list can be used to represent the array.
#
# The queue keeps track of:
#
#   Front:
#       The index of the first item in the queue.
#
#   Rear:
#       The index where the next item will be added.
#
#   Count:
#       The number of items currently in the queue.
#
# Queue rule:
#
#   First In, First Out
#
# This is commonly called:
#
#   FIFO
#
#
# EXAMPLE - CUSTOMER CHECKOUT LINE
# ------------------------------------------------------------
#
#   Front                                      Rear
#     |                                          |
#     v                                          v
#
#   [Customer A, Customer B, Customer C, Customer D]
#
# Customer A entered the line first.
#
# Customer A will be helped and removed first.
#
# New customers are added at the rear of the queue.
#
#
# CIRCULAR ARRAY
# ------------------------------------------------------------
#
# This implementation uses a circular array.
#
# When the rear reaches the end of the array, it moves back
# to the beginning if an empty position is available.
#
# Example:
#
#   Array capacity: 5
#
#   [Customer E, Empty, Customer C, Customer D, Customer E]
#        ^
#        |
#   Rear wraps back to the beginning.
#
# The modulo operator keeps the indexes inside the array:
#
#   next_index = (current_index + 1) % capacity
#
#
# MAIN QUEUE OPERATIONS
# ------------------------------------------------------------
#
# enqueue(item)
#     Adds an item at the rear of the queue.
#
# dequeue()
#     Removes and returns the item at the front of the queue.
#
# peek()
#     Returns the front item without removing it.
#
# is_empty()
#     Checks whether the queue contains no items.
#
# is_full()
#     Checks whether the array has reached its capacity.
#
# size()
#     Returns the number of items currently in the queue.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
#   Operation       Time Complexity
#   -------------------------------
#   enqueue()            O(1)
#   dequeue()            O(1)
#   peek()               O(1)
#   is_empty()           O(1)
#   is_full()            O(1)
#   size()               O(1)
#
# enqueue() and dequeue() are O(1) because no items need to
# shift inside the array.
#
# Searching through the entire queue requires:
#
#   O(n)
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(n)
#
# The array reserves space based on the queue's capacity.
#
#
# ============================================================
# ARRAY QUEUE IMPLEMENTATION
# ============================================================


class ArrayQueue:
    def __init__(self, capacity):
        # Create an array with a fixed number of empty positions.
        self.items = [None] * capacity

        # Store the maximum number of items the queue can hold.
        self.capacity = capacity

        # Front points to the first item in the queue.
        self.front = 0

        # Rear points to the position where the next item
        # will be added.
        self.rear = 0

        # Keep track of how many items are currently stored.
        self.count = 0

    def enqueue(self, item):
        # An item cannot be added when the queue is full.
        if self.is_full():
            return False

        # Store the new item at the rear index.
        self.items[self.rear] = item

        # Move rear forward by one position.
        #
        # The modulo operator moves rear back to index 0 when
        # it reaches the end of the array.
        self.rear = (self.rear + 1) % self.capacity

        # Increase the number of items in the queue.
        self.count += 1

        # Return True to show that the item was added.
        return True

    def dequeue(self):
        # A value cannot be removed from an empty queue.
        if self.is_empty():
            return None

        # Save the front item before removing it.
        removed_item = self.items[self.front]

        # Clear the position where the item was stored.
        self.items[self.front] = None

        # Move front forward by one position.
        #
        # The modulo operator moves front back to index 0 when
        # it reaches the end of the array.
        self.front = (self.front + 1) % self.capacity

        # Decrease the number of items in the queue.
        self.count -= 1

        # Return the value that was removed.
        return removed_item

    def peek(self):
        # An empty queue does not have a front item.
        if self.is_empty():
            return None

        # Return the front item without removing it.
        return self.items[self.front]

    def is_empty(self):
        # The queue is empty when it contains zero items.
        return self.count == 0

    def is_full(self):
        # The queue is full when count reaches capacity.
        return self.count == self.capacity

    def size(self):
        # Return the number of items currently in the queue.
        return self.count


# ============================================================
# CODE EXAMPLE - CUSTOMER CHECKOUT LINE
# ============================================================
#
# Create an array queue that can hold four customers.
checkout_line = ArrayQueue(4)

# Customer A enters the checkout line.
#
# Array:
#
#   Front / Rear
#        |
#        v
#
#   [Customer A, None, None, None]
checkout_line.enqueue("Customer A")

# Customer B enters behind Customer A.
#
# Array:
#
#   Front                    Rear
#     |                         |
#     v                         v
#
#   [Customer A, Customer B, None, None]
checkout_line.enqueue("Customer B")

# Customer C enters behind Customer B.
#
# Array:
#
#   Front                                Rear
#     |                                     |
#     v                                     v
#
#   [Customer A, Customer B, Customer C, None]
checkout_line.enqueue("Customer C")

# Customer D enters at the rear of the line.
#
# Array:
#
#   Front
#     |
#     v
#
#   [Customer A, Customer B, Customer C, Customer D]
#
# The queue is now full.
checkout_line.enqueue("Customer D")

# peek() returns the next customer without removing them.
print("Next customer:", checkout_line.peek())

# size() returns the number of customers currently in line.
print("Customers in line:", checkout_line.size())

# The cashier helps the customer at the front of the line.
#
# dequeue() removes Customer A because Customer A entered first.
helped_customer = checkout_line.dequeue()

# Customer A was removed from the queue.
print("Helping:", helped_customer)

# Customer B is now at the front of the queue.
print("Next customer:", checkout_line.peek())

# Customer E enters the line.
#
# Rear wraps around and adds Customer E at index 0.
#
# Array:
#
#   Rear      Front
#     |         |
#     v         v
#
#   [Customer E, Customer B, Customer C, Customer D]
checkout_line.enqueue("Customer E")

# Display the number of customers after Customer E joins.
print("Customers in line:", checkout_line.size())

# ============================================================
# EXPECTED OUTPUT
# ============================================================
#
# Next customer: Customer A
# Customers in line: 4
# Helping: Customer A
# Next customer: Customer B
# Customers in line: 4
# ============================================================
# ============================================================
# Queue ADT - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A queue stores data using:
#
#   First In, First Out
#
# This is commonly called:
#
#   FIFO
#
# The first item added is the first item removed.
#
#
# EXAMPLE - CUSTOMER CHECKOUT LINE
# ------------------------------------------------------------
#
#   Front                                      Rear
#     |                                          |
#     v                                          v
#
#   Customer A <- Customer B <- Customer C <- Customer D
#
# Customer A entered the line first.
#
# Customer A will be helped and removed first.
#
# New customers are added at the rear of the queue.
#
#
# MAIN QUEUE OPERATIONS
# ------------------------------------------------------------
#
# enqueue(item)
#     Adds an item to the rear of the queue.
#
# dequeue()
#     Removes and returns the item at the front of the queue.
#
# peek()
#     Returns the front item without removing it.
#
# is_empty()
#     Checks whether the queue is empty.
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
#   dequeue()            O(n)
#   peek()               O(1)
#   is_empty()           O(1)
#   size()               O(1)
#
# enqueue() is fast because the new item is added to the end
# of the list.
#
# dequeue() is O(n) when using list.pop(0).
#
# Removing the first item causes every remaining item to shift
# one position to the left.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(n)
#
# The queue needs space for every item it stores.
#
#
# ============================================================
# QUEUE IMPLEMENTATION
# ============================================================


class Queue:
    def __init__(self):
        # Create an empty list to store the queue's items.
        self.items = []

    def enqueue(self, item):
        # Add the new item to the rear of the queue.
        #
        # The end of the list represents the rear.
        self.items.append(item)

    def dequeue(self):
        # An item cannot be removed from an empty queue.
        if self.is_empty():
            return None

        # Remove and return the item at the front of the queue.
        #
        # Index 0 represents the first item in the list.
        return self.items.pop(0)

    def peek(self):
        # An empty queue does not have a front item.
        if self.is_empty():
            return None

        # Return the front item without removing it.
        return self.items[0]

    def is_empty(self):
        # The queue is empty when the list contains no items.
        return len(self.items) == 0

    def size(self):
        # Return the number of items currently in the queue.
        return len(self.items)


# ============================================================
# CODE EXAMPLE - CUSTOMER CHECKOUT LINE
# ============================================================
#
# Create a queue for a customer checkout line.
checkout_line = Queue()

# Customer A enters the checkout line.
#
# Queue:
#
#   Front
#     |
#     v
#
#   Customer A
checkout_line.enqueue("Customer A")

# Customer B enters behind Customer A.
#
# Queue:
#
#   Front               Rear
#     |                    |
#     v                    v
#
#   Customer A <- Customer B
checkout_line.enqueue("Customer B")

# Customer C enters behind Customer B.
#
# Queue:
#
#   Front                            Rear
#     |                                |
#     v                                v
#
#   Customer A <- Customer B <- Customer C
checkout_line.enqueue("Customer C")

# Customer D enters at the rear of the line.
#
# Queue:
#
#   Front                                          Rear
#     |                                              |
#     v                                              v
#
#   Customer A <- Customer B <- Customer C <- Customer D
checkout_line.enqueue("Customer D")

# peek() returns the next customer without removing them.
print("Next customer:", checkout_line.peek())

# size() returns the number of customers currently in line.
print("Customers in line:", checkout_line.size())

# The cashier helps the customer at the front of the line.
#
# dequeue() removes Customer A because Customer A entered first.
helped_customer = checkout_line.dequeue()

# Display the customer who was removed from the queue.
print("Helping:", helped_customer)

# Customer B is now at the front of the queue.
print("Next customer:", checkout_line.peek())

# ============================================================
# EXPECTED OUTPUT
# ============================================================
#
# Next customer: Customer A
# Customers in line: 4
# Helping: Customer A
# Next customer: Customer B
# ============================================================
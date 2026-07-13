# ============================================================
# Queue Using a Linked List - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A queue can be built using a linked list.
#
# Each item is stored inside a node.
#
# Each node contains:
#
#   Data:
#       The value being stored.
#
#   Next:
#       A reference to the node behind it.
#
# The queue keeps track of two references:
#
#   Front:
#       Points to the first node in the queue.
#
#   Rear:
#       Points to the last node in the queue.
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
#   Customer A -> Customer B -> Customer C -> Customer D -> None
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
#     Creates a new node and adds it to the rear of the queue.
#
# dequeue()
#     Removes and returns the node at the front of the queue.
#
# peek()
#     Returns the front node's data without removing it.
#
# is_empty()
#     Checks whether the front reference is None.
#
# size()
#     Returns the number of nodes currently in the queue.
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
#   size()               O(1)
#
# enqueue() is O(1) because the rear reference points directly
# to the last node.
#
# dequeue() is O(1) because the front reference points directly
# to the first node.
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
# The queue stores one node for every item.
#
# Each node stores:
#
#   - The item's data
#   - A reference to the next node
#
#
# ============================================================
# NODE CLASS
# ============================================================


class Node:
    def __init__(self, data):
        # Store the value inside the node.
        self.data = data

        # Point to the next node in the queue.
        #
        # None means there is no next node yet.
        self.next = None


# ============================================================
# LINKED-LIST QUEUE IMPLEMENTATION
# ============================================================


class LinkedListQueue:
    def __init__(self):
        # The front points to the first node in the queue.
        #
        # None means the queue is currently empty.
        self.front = None

        # The rear points to the last node in the queue.
        #
        # None means the queue is currently empty.
        self.rear = None

        # Keep track of how many items are in the queue.
        self.count = 0

    def enqueue(self, item):
        # Create a new node containing the item.
        new_node = Node(item)

        # Check whether the queue is currently empty.
        if self.is_empty():
            # The new node becomes both the front and rear.
            self.front = new_node
            self.rear = new_node
        else:
            # Connect the current rear node to the new node.
            self.rear.next = new_node

            # Make the new node the rear of the queue.
            self.rear = new_node

        # Increase the queue size.
        self.count += 1

    def dequeue(self):
        # A value cannot be removed from an empty queue.
        if self.is_empty():
            return None

        # Save the front node's data before removing the node.
        removed_item = self.front.data

        # Move the front reference to the next node.
        self.front = self.front.next

        # Decrease the queue size.
        self.count -= 1

        # If the queue is now empty, reset the rear reference.
        if self.front is None:
            self.rear = None

        # Return the value that was removed.
        return removed_item

    def peek(self):
        # An empty queue does not have a front item.
        if self.is_empty():
            return None

        # Return the front item's data without removing it.
        return self.front.data

    def is_empty(self):
        # The queue is empty when front does not reference a node.
        return self.front is None

    def size(self):
        # Return the number of items currently in the queue.
        return self.count


# ============================================================
# CODE EXAMPLE - CUSTOMER CHECKOUT LINE
# ============================================================
#
# Create a linked-list queue for a customer checkout line.
checkout_line = LinkedListQueue()

# Customer A enters the checkout line.
#
# Queue:
#
#   Front / Rear
#        |
#        v
#
#   Customer A -> None
checkout_line.enqueue("Customer A")

# Customer B enters behind Customer A.
#
# Queue:
#
#   Front               Rear
#     |                    |
#     v                    v
#
#   Customer A -> Customer B -> None
checkout_line.enqueue("Customer B")

# Customer C enters behind Customer B.
#
# Queue:
#
#   Front                            Rear
#     |                                |
#     v                                v
#
#   Customer A -> Customer B -> Customer C -> None
checkout_line.enqueue("Customer C")

# Customer D enters at the rear of the line.
#
# Queue:
#
#   Front                                          Rear
#     |                                              |
#     v                                              v
#
#   Customer A -> Customer B -> Customer C -> Customer D -> None
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

# ============================================================
# EXPECTED OUTPUT
# ============================================================
#
# Next customer: Customer A
# Customers in line: 4
# Helping: Customer A
# Next customer: Customer B
# ============================================================
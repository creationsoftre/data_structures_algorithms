# ============================================================
# Singly Linked List Insertion - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Insertion adds a new node to the linked list.
#
# Common insertion locations:
#
#   Head
#
#   Tail
#
#   Specific position
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Insert at head:
#
#   O(1)
#
# Insert at tail with a tail reference:
#
#   O(1)
#
# Insert at a specific position:
#
#   O(n)
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
# One insertion:
#
#   O(1)
#
# Complete linked list:
#
#   O(n)
#
#
# ============================================================
# IMPLEMENTATION
# ============================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#
#
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
#
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
#
        if self.tail is None:
            self.tail = new_node
#
        self.count += 1
#
    def insert_at_tail(self, data):
        new_node = Node(data)
#
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
#
        self.count += 1
#
    def insert_at_position(self, data, position):
        if position < 0 or position > self.count:
            raise IndexError("Position is outside the list.")
#
        if position == 0:
            self.insert_at_head(data)
            return
#
        if position == self.count:
            self.insert_at_tail(data)
            return
#
        current = self.head
#
        for _ in range(position - 1):
            current = current.next
#
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        self.count += 1
#
    def display(self):
        values = []
        current = self.head
#
        while current is not None:
            values.append(current.data)
            current = current.next
#
        print(" -> ".join(values) + " -> None")
#
#
# ============================================================
# CODE EXAMPLE
# ============================================================
vehicles = SinglyLinkedList()
vehicles.insert_at_tail("Skyline")
vehicles.insert_at_tail("RX-7")
#
print("Starting list:")
vehicles.display()
#
vehicles.insert_at_head("Supra")
print("\nAfter inserting Supra at the head:")
vehicles.display()
#
vehicles.insert_at_position("NSX", 2)
print("\nAfter inserting NSX at position 2:")
vehicles.display()

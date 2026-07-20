# ============================================================
# Doubly Linked List Insertion - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Every inserted node must update both:
#
#   next
#
#   prev
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
# Insert at tail:
#
#   O(1)
#
# Insert at position:
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
# Complete list:
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
        self.prev = None
        self.next = None
#
#
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
#
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
#
        if self.head is None:
            self.tail = new_node
        else:
            self.head.prev = new_node
#
        self.head = new_node
        self.count += 1
#
    def insert_at_tail(self, data):
        new_node = Node(data)
        new_node.prev = self.tail
#
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
#
        self.tail = new_node
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
        for _ in range(position):
            current = current.next
#
        new_node = Node(data)
        previous = current.prev
#
        new_node.prev = previous
        new_node.next = current
        previous.next = new_node
        current.prev = new_node
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
        print(" <-> ".join(values))
#
#
# ============================================================
# CODE EXAMPLE
# ============================================================
vehicles = DoublyLinkedList()
vehicles.insert_at_tail("Skyline")
vehicles.insert_at_tail("RX-7")
vehicles.insert_at_head("Supra")
vehicles.insert_at_position("NSX", 2)
#
print("Final list:")
vehicles.display()

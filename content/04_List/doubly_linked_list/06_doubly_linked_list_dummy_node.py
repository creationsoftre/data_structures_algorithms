# ============================================================
# Doubly Linked List Dummy Nodes - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A doubly linked list can use two permanent dummy nodes:
#
#   Head sentinel
#
#   Tail sentinel
#
# Real data nodes are always stored between them.
#
# This removes many special cases for empty-list, head, and
# tail operations.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Insert at front:
#
#   O(1)
#
# Insert at back:
#
#   O(1)
#
# Remove known node:
#
#   O(1)
#
# Search:
#
#   O(n)
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
# Two dummy nodes:
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
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None
#
#
class SentinelDoublyLinkedList:
    def __init__(self):
        self.head_dummy = Node()
        self.tail_dummy = Node()
#
        self.head_dummy.next = self.tail_dummy
        self.tail_dummy.prev = self.head_dummy
#
    def append(self, data):
        new_node = Node(data)
        previous = self.tail_dummy.prev
#
        new_node.prev = previous
        new_node.next = self.tail_dummy
        previous.next = new_node
        self.tail_dummy.prev = new_node
#
    def remove(self, target):
        current = self.head_dummy.next
#
        while current != self.tail_dummy:
            if current.data == target:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
#
            current = current.next
#
        return False
#
    def display(self):
        values = []
        current = self.head_dummy.next
#
        while current != self.tail_dummy:
            values.append(current.data)
            current = current.next
#
        print(" <-> ".join(values))
#
#
# ============================================================
# CODE EXAMPLE
# ============================================================
vehicles = SentinelDoublyLinkedList()
#
for vehicle in ["Supra", "Skyline", "RX-7"]:
    vehicles.append(vehicle)
#
print("Before removal:")
vehicles.display()
#
vehicles.remove("Supra")
#
print("\nAfter removing the first real node:")
vehicles.display()

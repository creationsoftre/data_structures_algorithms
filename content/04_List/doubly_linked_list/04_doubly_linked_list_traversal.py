# ============================================================
# Doubly Linked List Traversal - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A doubly linked list can be traversed:
#
#   Forward from the head
#
#   Backward from the tail
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Forward traversal:
#
#   O(n)
#
# Backward traversal:
#
#   O(n)
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
# Iterative traversal:
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
#
    def append(self, data):
        new_node = Node(data)
#
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
#
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
#
    def traverse_forward(self):
        current = self.head
#
        while current is not None:
            print(current.data)
            current = current.next
#
    def traverse_backward(self):
        current = self.tail
#
        while current is not None:
            print(current.data)
            current = current.prev
#
#
# ============================================================
# CODE EXAMPLE
# ============================================================
vehicles = DoublyLinkedList()
#
for vehicle in ["Supra", "Skyline", "RX-7", "NSX"]:
    vehicles.append(vehicle)
#
print("Forward traversal:")
vehicles.traverse_forward()
#
print("\nBackward traversal:")
vehicles.traverse_backward()

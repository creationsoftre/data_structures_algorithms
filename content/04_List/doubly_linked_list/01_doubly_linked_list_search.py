# ============================================================
# Doubly Linked List Search - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A doubly linked list stores next and previous references.
#
# Search can begin at the head or tail.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Best case:
#
#   O(1)
#
# Average and worst case:
#
#   O(n)
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
# Search operation:
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
    def search_forward(self, target):
        current = self.head
        position = 0
#
        while current is not None:
            print(f"Checking forward: {current.data}")
#
            if current.data == target:
                return current, position
#
            current = current.next
            position += 1
#
        return None, -1
#
    def search_backward(self, target):
        current = self.tail
#
        while current is not None:
            print(f"Checking backward: {current.data}")
#
            if current.data == target:
                return current
#
            current = current.prev
#
        return None
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
print("Forward search for RX-7:")
node, position = vehicles.search_forward("RX-7")
print("Found at position:", position)
#
print("\nBackward search for Skyline:")
node = vehicles.search_backward("Skyline")
print("Found:", node.data if node else None)

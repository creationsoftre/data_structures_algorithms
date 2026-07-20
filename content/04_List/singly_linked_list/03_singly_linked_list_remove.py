# ============================================================
# Singly Linked List Removal - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Removal deletes a node and reconnects the surrounding links.
#
# In a singly linked list, the node before the removed node is
# usually needed so its next reference can be updated.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Remove head:
#
#   O(1)
#
# Remove by value:
#
#   O(n)
#
# Remove tail:
#
#   O(n)
#
# The node before the tail must be located first.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
# Removal operation:
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
#
    def append(self, data):
        new_node = Node(data)
#
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
#
        self.tail.next = new_node
        self.tail = new_node
#
    def remove(self, target):
        if self.head is None:
            return False
#
        if self.head.data == target:
            self.head = self.head.next
#
            if self.head is None:
                self.tail = None
#
            return True
#
        previous = self.head
        current = self.head.next
#
        while current is not None:
            if current.data == target:
                previous.next = current.next
#
                if current == self.tail:
                    self.tail = previous
#
                return True
#
            previous = current
            current = current.next
#
        return False
#
    def display(self):
        current = self.head
        values = []
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
#
for vehicle in ["Supra", "Skyline", "RX-7", "NSX"]:
    vehicles.append(vehicle)
#
print("Before removal:")
vehicles.display()
#
removed = vehicles.remove("RX-7")
print("\nRemoved RX-7:", removed)
vehicles.display()
#
removed = vehicles.remove("Supra")
print("\nRemoved head Supra:", removed)
vehicles.display()

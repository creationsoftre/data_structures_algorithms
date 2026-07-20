# ============================================================
# Singly Linked List Dummy Node - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A dummy node is a temporary node placed before the real head.
#
# It simplifies insertion and removal because the real head
# always has a previous node during the operation.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Remove by value:
#
#   O(n)
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
# Dummy node:
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
#
    def append(self, data):
        dummy = Node(None)
        dummy.next = self.head
        current = dummy
#
        while current.next is not None:
            current = current.next
#
        current.next = Node(data)
        self.head = dummy.next
#
    def remove(self, target):
        dummy = Node(None)
        dummy.next = self.head
        previous = dummy
        current = self.head
#
        while current is not None:
            if current.data == target:
                previous.next = current.next
                self.head = dummy.next
                return True
#
            previous = current
            current = current.next
#
        self.head = dummy.next
        return False
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
#
for vehicle in ["Supra", "Skyline", "RX-7"]:
    vehicles.append(vehicle)
#
print("Before removing the head:")
vehicles.display()
#
vehicles.remove("Supra")
#
print("\nAfter removing the head with a dummy node:")
vehicles.display()

# ============================================================
# Doubly Linked List Removal - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Removal reconnects both the previous and next neighboring
# nodes.
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
# Remove tail:
#
#   O(1)
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
# Removal operation:
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
    def remove(self, target):
        current = self.head
#
        while current is not None:
            if current.data == target:
                if current.prev is None:
                    self.head = current.next
                else:
                    current.prev.next = current.next
#
                if current.next is None:
                    self.tail = current.prev
                else:
                    current.next.prev = current.prev
#
                return True
#
            current = current.next
#
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
        print(" <-> ".join(values))
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
print("Before removal:")
vehicles.display()
#
vehicles.remove("RX-7")
print("\nAfter removing RX-7:")
vehicles.display()
#
vehicles.remove("NSX")
print("\nAfter removing the tail NSX:")
vehicles.display()

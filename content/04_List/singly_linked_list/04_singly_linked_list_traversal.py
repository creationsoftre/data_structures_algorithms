# ============================================================
# Singly Linked List Traversal - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Traversal visits every node from the head to the tail.
#
# The current reference moves forward using:
#
#   current = current.next
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Traverse all nodes:
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
    def traverse(self):
        current = self.head
        position = 0
#
        while current is not None:
            print(
                f"Position {position}: {current.data}"
            )
            current = current.next
            position += 1
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
print("=" * 60)
print("TRAVERSING THE LIST")
print("=" * 60)
vehicles.traverse()

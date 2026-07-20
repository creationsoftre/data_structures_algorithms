# ============================================================
# Singly Linked List Search - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Searching checks each node from the head until the target
# value is found or the end of the list is reached.
#
# A singly linked list cannot jump directly to an index.
#
# Each node only stores:
#
#   Data
#
#   A reference to the next node
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
# The target is stored at the head.
#
# Average case:
#
#   O(n)
#
# Worst case:
#
#   O(n)
#
# The target is at the tail or is not in the list.
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
    def search(self, target):
        current = self.head
        position = 0
#
        while current is not None:
            print(
                f"Checking position {position}: "
                f"{current.data}"
            )
#
            if current.data == target:
                return current, position
#
            current = current.next
            position += 1
#
        return None, -1
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
print("SEARCH FOR RX-7")
print("=" * 60)
#
node, position = vehicles.search("RX-7")
#
if node is not None:
    print(f"\nFound {node.data} at position {position}.")
else:
    print("\nTarget was not found.")

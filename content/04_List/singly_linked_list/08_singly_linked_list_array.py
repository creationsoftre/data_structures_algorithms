# ============================================================
# Singly Linked List Using an Array - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A linked list can be simulated inside an array by storing
# node records and using indexes instead of object references.
#
# Each array record stores:
#
#   Data
#
#   Index of the next node
#
# The value -1 represents:
#
#   No next node
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Append with a tail index:
#
#   O(1)
#
# Traversal:
#
#   O(n)
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
# Array-backed list:
#
#   O(n)
#
#
# ============================================================
# IMPLEMENTATION
# ============================================================
class ArraySinglyLinkedList:
    def __init__(self):
        self.nodes = []
        self.head_index = -1
        self.tail_index = -1
#
    def append(self, data):
        new_index = len(self.nodes)
#
        self.nodes.append(
            {
                "data": data,
                "next": -1,
            }
        )
#
        if self.head_index == -1:
            self.head_index = new_index
            self.tail_index = new_index
            return
#
        self.nodes[self.tail_index]["next"] = new_index
        self.tail_index = new_index
#
    def traverse(self):
        current_index = self.head_index
#
        while current_index != -1:
            node = self.nodes[current_index]
#
            print(
                f"Index {current_index}: "
                f"data={node['data']}, "
                f"next={node['next']}"
            )
#
            current_index = node["next"]
#
#
# ============================================================
# CODE EXAMPLE
# ============================================================
vehicles = ArraySinglyLinkedList()
#
for vehicle in ["Supra", "Skyline", "RX-7"]:
    vehicles.append(vehicle)
#
print("=" * 60)
print("ARRAY-BACKED SINGLY LINKED LIST")
print("=" * 60)
vehicles.traverse()

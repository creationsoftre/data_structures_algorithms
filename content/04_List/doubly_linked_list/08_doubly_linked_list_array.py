# ============================================================
# Doubly Linked List Using an Array - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A doubly linked list can be simulated inside an array.
#
# Each node record stores:
#
#   Data
#
#   Previous node index
#
#   Next node index
#
# The value -1 represents no connected node.
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
# Array-backed list:
#
#   O(n)
#
#
# ============================================================
# IMPLEMENTATION
# ============================================================
class ArrayDoublyLinkedList:
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
                "prev": self.tail_index,
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
    def traverse_forward(self):
        current_index = self.head_index
#
        while current_index != -1:
            node = self.nodes[current_index]
#
            print(
                f"Index {current_index}: "
                f"data={node['data']}, "
                f"prev={node['prev']}, "
                f"next={node['next']}"
            )
#
            current_index = node["next"]
#
    def traverse_backward(self):
        current_index = self.tail_index
#
        while current_index != -1:
            node = self.nodes[current_index]
#
            print(
                f"Index {current_index}: "
                f"data={node['data']}"
            )
#
            current_index = node["prev"]
#
#
# ============================================================
# CODE EXAMPLE
# ============================================================
vehicles = ArrayDoublyLinkedList()
#
for vehicle in ["Supra", "Skyline", "RX-7"]:
    vehicles.append(vehicle)
#
print("Forward traversal:")
vehicles.traverse_forward()
#
print("\nBackward traversal:")
vehicles.traverse_backward()

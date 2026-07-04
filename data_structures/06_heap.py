## TIME COMPLEXITY:
# Big O describes how the work grows as the amount of data grows.
#
# From fastest to slower:
# O(1)     -> Constant time
#             The operation takes about the same amount of work no matter how much data exists.
#
# O(log n) -> Logarithmic time
#             The operation gets faster than O(n) because the data is split into smaller parts.
#
# O(n)     -> Linear time
#             The operation gets slower as the amount of data grows because you may need to check each item.
#
# Simple rule:
# O(1) is usually better/faster than O(log n), and O(log n) is usually better/faster than O(n).
#
# HEAP TIME COMPLEXITY:
#
# - Peek at min/max item: O(1)
#   The highest-priority item is always at the top of the heap.
#
# - Insert/push item: O(log n)
#   The heap may need to move the new item up to keep the heap order.
#
# - Remove/pop min or max item: O(log n)
#   The heap removes the top item, then reorganizes itself.
#
# - Search for a specific item: O(n)
#   A heap is not designed for searching by name or value.
#
# - Build heap from existing list: O(n)
#   Python can turn a list into a heap efficiently.
#
# - Loop through all items: O(n)
#   You must visit every item once.

# A heap is a priority-based data structure.
#
# In Python, heapq gives us a min-heap.
#
# Min-heap rule:
# The smallest value stays at the top.
#
# For this project:
# The wheel with the lowest price will be treated as the highest-priority item.

from dataclasses import dataclass
import heapq

# =========================================
# RECORD
# =========================================

# RECORD:
# Represents one wheel.
#
# This is the same Wheel record used in the previous examples.
# The heap will store Wheel records, but it needs a number to sort by.
#
# In this example, we sort by price.

@dataclass
class Wheel:
    name: str           # The name of the wheel
    diameter: int       # The diameter of the wheel in inches
    width: float        # The width of the wheel in inches
    bolt_pattern: str   # The bolt pattern of the wheel, e.g., "5x114.3"
    color: str          # The color of the wheel
    price: float        # The price of the wheel in dollars
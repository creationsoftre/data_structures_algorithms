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

# =========================================
# HELPER FUNCTIONS
# =========================================

# Print the title of the section for visual separation.
def show_section_title(title):
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title) + "\n")

# =========================================
# CREATE HEAP
# =========================================

# CREATE HEAP:
# This function creates and returns our starting heap.
#
# A heap is usually stored as a normal Python list,
# but heapq controls how items are added and removed.
#
# Each item in the heap is a tuple:
#
# (priority, value)
#
# In this project:
# priority = wheel price
# value    = Wheel record
#
# Since this is a min-heap, the lowest price comes out first.

def create_inventory_heap():
    inventory = []

    heapq.heappush(inventory,(3500.00, Wheel("Volk Racing TE37", 18, 9.5, "5x114.3", "Matte Bronze", 3500.00)))
    heapq.heappush(inventory,(4500.00, Wheel("Work VSKF", 18, 10.0, "5x114.3", "Silver", 4500.00)))
    heapq.heappush(inventory,(5500.00, Wheel("Work Emitz", 18, 11.5, "5x114.3", "Gold", 5500.00)))
    heapq.heappush(inventory,(7500.00, Wheel("BBS LM", 18, 10.5, "5x114.3", "Polished Silver", 7500.00)))

    return inventory

# =========================================
# DISPLAY
# =========================================

# DISPLAY:
# Show the current heap.
#
# Important:
# A heap is not the same as a sorted list.
#
# The first item is guaranteed to be the smallest.
# The rest of the items are arranged in a way that keeps the heap working,
# but they may not appear fully sorted.

def display_heap(inventory, title):
    show_section_title(title)

    for index, item in enumerate(inventory):
        price, wheel = item

        print(f"Heap Index: {index}")
        print(f"Priority Price: ${price:.2f}")
        print(f"Model: {wheel.name}")
        print(f"Color: {wheel.color}")
        print(f"Price: ${wheel.price:.2f}")
        print()

# =========================================
# INSERT
# =========================================

# INSERT:
# Add a new wheel to the heap.
#
# heappush() adds the item and automatically reorganizes the heap
# so the lowest price stays near the top.

def add_inventory_item(inventory, wheel):
    show_section_title("2. INSERT INTO HEAP")

    heapq.heappush(inventory, (wheel.price, wheel)) # Use wheel.price as priority and store the wheel object as the value.

    print(f"Added wheel to heap: {wheel.name}")
    print(f"Priority price: ${wheel.price:.2f}")
    print(f"Heap count is now: {len(inventory)}")

# =========================================
# PEEK
# =========================================

# PEEK:
# Look at the highest-priority item without removing it.
#
# In a min-heap, the highest-priority item is the smallest value.
#
# Since we are using price as the priority,
# the top item is the cheapest wheel.

def peek_cheapest_wheel(inventory):
    show_section_title("3. PEEK AT CHEAPEST WHEEL")

    if len(inventory) == 0:
        print("Heap is empty.")
        return

    price, wheel = inventory[0] # This line is 0(1)becase the top of the heap is always at index 0

    print("Cheapest wheel currently in heap:")
    print(f"Model: {wheel.name}")
    print(f"Price: ${price:.2f}")

# =========================================
# REMOVE (POP)
# =========================================

# REMOVE (POP):
# Remove and return the highest-priority item.
#
# In this min-heap, that means removing the cheapest wheel.
#
# After removing the top item, heapq reorganizes the heap
# so the next cheapest wheel moves to the top.

def remove_cheapest_wheel(inventory):
    show_section_title("4. POP CHEAPEST WHEEL FROM HEAP")

    if len(inventory) == 0:
        print("Heap is empty.")
        return None

    price, wheel = heapq.heappop(inventory)

    print(f"Removed cheapest wheel: {wheel.name}")
    print(f"Price: ${price:.2f}")
    print(f"Heap count is now: {len(inventory)}")

    return wheel
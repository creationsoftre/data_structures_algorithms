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


# MIN-HEAP VISUAL:
#
# A heap is a priority-based data structure.
#
# In a min-heap, the smallest value has the highest priority.
# That means the cheapest wheel stays at the top.
#
# Example using wheel prices:
#
#                 $3000
#                /     \
#            $3500     $5500
#           /    \
#       $7500    $4500
#
# Important:
# A heap is not fully sorted.
# It only guarantees that the smallest item is at the top.
#
# In this project:
#
# Lower price = higher priority
#
# Mental model:
#
# A priority line where the most important item comes out first.
#
# Min-Heap = smallest value comes out first

# MAX-HEAP NOTE:
#
# Python's heapq is a min-heap by default.
#
# Min-heap:
# - Smallest value comes out first.
# - Good for finding the cheapest wheel.
#
# Max-heap:
# - Largest value comes out first.
# - Good for finding the most expensive wheel.
#
# Python does not have a separate max-heap tool in heapq.
# The common trick is to multiply the priority by -1.
#
# Example:
#
# Min-heap priority:
# (3000, Wheel(...))
#
# Max-heap priority:
# (-3000, Wheel(...))
#
# Why does this work?
#
# Python still removes the smallest number first.
# Since -7500 is smaller than -3000,
# the $7500 wheel comes out before the $3000 wheel.
#
# Original prices:
# 3000, 3500, 7500
#
# Negative priorities:
# -3000, -3500, -7500
#
# Smallest negative number:
# -7500
#
# Result:
# $7500 comes out first.

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

# =========================================
# SEARCH
# =========================================

# SEARCH:
# Search for a wheel by name.
#
# Important:
# A heap is not designed for fast searching by name.
#
# Even though the cheapest item is easy to find,
# a specific name could be anywhere in the heap.
#
# That means we may need to check every item.

def search_heap_by_name(inventory, search_name):
    show_section_title("5. SEARCH HEAP BY NAME")

    found_wheel = None

    for price, wheel in inventory:
        if wheel.name == search_name:
            found_wheel = wheel
            break

    print(f"Search Result for '{search_name}':")

    if found_wheel:
        print(f"Wheel found: {found_wheel.name}")
        print(f"Color: {found_wheel.color}")
        print(f"Price: ${found_wheel.price:.2f}")
    else:
        print("Wheel not found.")

# =========================================
# MAIN PROGRAM
# =========================================

# Create the starting heap inventory.
inventory = create_inventory_heap()


# SECTION 1:
# Display the internal heap.
#
# Remember:
# It may not look fully sorted.
# Only the first item is guaranteed to be the cheapest.
display_heap(inventory, "1. DISPLAY HEAP INVENTORY")


# SECTION 2:
# Insert a new wheel into the heap.
new_wheel = Wheel("Enkei RPF1", 18, 9.0, "5x114.3", "Hyper Silver", 3600.00)
add_inventory_item(inventory, new_wheel)


# SECTION 3:
# Peek at the cheapest wheel without removing it.
peek_cheapest_wheel(inventory)


# SECTION 4:
# Remove the cheapest wheel from the heap.
remove_cheapest_wheel(inventory)


# SECTION 5:
# Search for a wheel by name.
#
# This works, but it is not what heaps are best at.
search_heap_by_name(inventory, "Work VSKF")


# SECTION 6:
# Display the final heap after all changes.
display_heap(inventory, "6. FINAL HEAP INVENTORY")
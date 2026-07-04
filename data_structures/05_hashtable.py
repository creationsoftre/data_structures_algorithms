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
# HASH TABLE TIME COMPLEXITY:
#
# - Insert/add key-value pair: O(1) average, O(n) worst case
#   Usually fast because the key is converted into a direct storage location.
#
# - Search/lookup by key: O(1) average, O(n) worst case
#   Usually fast because the key takes you directly to the value.
#
# - Update by key: O(1) average, O(n) worst case
#   Updating is fast when you already know the key.
#
# - Delete by key: O(1) average, O(n) worst case
#   Removing is fast when you already know the key.
#
# - Loop through all items: O(n)
#   You must visit every key-value pair once.
#
# Note:
# Worst case can become O(n) if many keys collide,
# but Python dictionaries are highly optimized for normal use.

# A hash table stores as key-value pairs.
#
# In Python, a dictionary is a built-in hash table
# Example:
# Key -> Work Emitz
# Value -> Wheel("Work Emitz", 18, 11.5, "5x114.3", "Gold", 5500.00)

from dataclasses import dataclass

# ================================
# RECORD
#=================================

# RECORD:
# Represents one wheel.
@dataclass
class Wheel:
    name: str           # The name of the wheel
    diameter: int       # The diameter of the wheel in inches 
    width: float        # The width of the wheel in inches
    bolt_pattern: str   # The bolt pattern of the wheel, e.g., "5x114.3"
    color: str          # The color of the wheel
    price: float        # The price of the wheel in dollars

#===========================================
# HELPER FUNCTIONS
# ===========================================

# Print the title of the section for visual separation.
def show_section_title(title):
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title) + "\n")
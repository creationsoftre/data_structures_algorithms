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

#===========================================
# CREATE HASH TABLE
# ==========================================

# CREATEHASH TABLE:
# This function creates and returns our starting has table.
#
# The key is the wheel name.
# The value is the wheel record.
#
# This lets us quickly find a wheel if we know it's name. 

def create_inventory():
    inventory = {
        "Volk Racing TE37": Wheel("Volk Racing TE37", 18, 9.5, "5x114.3", "Matte Bronze", 3500.00),
        "Work VSKF": Wheel("Work VSKF", 18, 10.0, "5x114.3", "Silver", 4500.00),
        "Work Emitz": Wheel("Work Emitz", 18, 11.5, "5x114.3", "Gold", 5500.00),
        "BBS LM": Wheel("BBS LM", 18, 10.5, "5x114.3", "Polished Silver", 7500.00),
    }

    return inventory

#===========================================
# DISPLAY
# ==========================================

# DISPLAY
# Loop through all of the key-value pairs in the hash table.
#
# Key = the name used to find the wheel
# Value = the wheel record stored under that key

def display_inventory(inventory):
    show_section_title("1. DISPLAY HASH TABLE INVENTORY")

    for key, wheel in inventory.items():
        print(f"Key: {key}")
        print(f"Model: {wheel.name}")
        print(f"Diameter: {wheel.diameter} inches")
        print(f"Width: {wheel.width} inches")
        print(f"Bolt Pattern: {wheel.bolt_pattern}")
        print(f"Color: {wheel.color}")
        print(f"Price: ${wheel.price:.2f}")
        print()

#===========================================
# INSERT
# ==========================================

# INSERT:
# Add a new key-value pair to the hash table.
#
# If the key does not exist, Python adds it.
# If the key already exists, Python replaces the old value. 

def add_inventory_item(inventory, wheel):
    show_section_title("2. INSERT INTO HASH TABLE")

    # The wheel name becomes the key.
    # The full wheel record becomes the value
    inventory[wheel.name] = Wheel

    print(f"Added wheel using key: {wheel.name}")
    print(f"Inventory count is now: {len(inventory)}")

#===========================================
# SEARCH
# ==========================================


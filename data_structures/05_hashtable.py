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

# SEARCH: 
# Search for a wheel by key.
#
# Hash tables are great when you know the key. 
# Instead of checking every wheel one by one,
# Python uses the key to quickly find the value.

def search_inventory_by_name(inventory, search_name):
    show_section_title("3. SEARCH HASH TABLE")

    # get() safely looks for the key
    #
    # If the key exist, it returns the value.
    # If the key does not exist, it returns None.

    result = inventory.get(search_name)

    print(f"Search Result for '{search_name}':")

    if result:
        print(f"Wheel found: {result.name}")
        print(f"Color: {result.color}")
        print(f"Price: ${result.price:.2f}")
    else:
        print("Wheel not found.")

# UPDATE:
# Update an existing wheel in the hash table.
#
# Since we know the key, we can access the wheel directly.

def update_inventory_item_color(inventory, wheel_name, new_color):
    show_section_title("4. UPDATE HASH TABLE VALUE")

    # Check if the key exists before trying to update it.
    if wheel_name in inventory:
        inventory[wheel_name].color = new_color

        print(f"Updated {wheel_name}")
        print(f"New color: {new_color}")
    else:
        print(f"Wheel '{wheel_name}' not found.")


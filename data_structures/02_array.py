# An array is a data structure that stores multiple values in order.

from dataclasses import dataclass


# A record for one wheel.
@dataclass
class Wheel:
    # Each variable below is a field in the record.
    # A field stores one piece of information about the wheel.

    name: str           # The name of the wheel
    diameter: int       # The diameter of the wheel in inches
    width: float        # The width of the wheel in inches
    bolt_pattern: str   # The bolt pattern of the wheel, e.g., "5x114.3"
    color: str          # The color of the wheel
    price: float        # The price of the wheel in dollars


# Creates and returns our starting array.
def create_inventory():
    # An array/list of wheels.
    # This lets us store multiple wheels in one variable.
    # Each wheel is a record, and the array stores all of them together.
    inventory = [
        Wheel("Volk Racing TE37", 18, 9.5, "5x114.3", "Matte Bronze", 3500.00),
        Wheel("Work VSKF", 18, 10.0, "5x114.3", "Silver", 4500.00),
        Wheel("Work Emitz", 18, 11.5, "5x114.3", "Gold", 5500.00),
        Wheel("BBS LM", 18, 10.5, "5x114.3", "Polished Silver", 7500.00),
    ]

    return inventory


# Print the title of the section for visual separation.
def show_section_title(title):
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title) + "\n")


# READ:
# Access individual wheels in the array using their index.
# The first wheel is at index 0, the second wheel is at index 1, and so on.
def display_wheel_specs(inventory):
    show_section_title("1. READ FROM ARRAY")

    # Go through every item in the array one at a time.
    for index, wheel in enumerate(inventory):
        print(f"Array Index: {index}")  # Shows that array indexes start at 0.
        print(f"Wheel {index + 1}:")
        print(f"Model: {wheel.name}")
        print(f"Diameter: {wheel.diameter} inches")
        print(f"Width: {wheel.width} inches")
        print(f"Bolt Pattern: {wheel.bolt_pattern}")
        print(f"Color: {wheel.color}")
        print(f"Price: ${wheel.price:.2f}")
        print()


# APPEND:
# Add a new item to the end of the array.
def add_new_inventory_item(inventory, new_wheel):
    show_section_title("2. APPEND TO ARRAY")

    inventory.append(new_wheel)

    print(f"Added new wheel to inventory: {new_wheel.name}")
    print(f"Inventory count is now: {len(inventory)}")


# SEARCH:
# Search for a wheel by name in the inventory.
def search_inventory_by_name(inventory, search_name):
    show_section_title("3. SEARCH IN ARRAY")

    # This starts as None because we have not found a matching wheel yet.
    found_wheel = None

    for wheel in inventory:
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


# REMOVE:
# Remove the last item from the array.
def remove_last_inventory_item(inventory):
    show_section_title("4. REMOVE FROM ARRAY")

    # pop() removes and returns the last item in the array.
    removed_wheel = inventory.pop()

    print(f"Removed Wheel: {removed_wheel.name}")
    print(f"Inventory count is now: {len(inventory)}")


# Display the final inventory after all operations.
def display_final_inventory(inventory):
    show_section_title("5. FINAL INVENTORY")

    print("Final Inventory:")

    for index, wheel in enumerate(inventory):
        print(f"Array Index: {index}")
        print(f"Wheel {index + 1}:")
        print(f"Model: {wheel.name}")
        print(f"Diameter: {wheel.diameter} inches")
        print(f"Width: {wheel.width} inches")
        print(f"Bolt Pattern: {wheel.bolt_pattern}")
        print(f"Color: {wheel.color}")
        print(f"Price: ${wheel.price:.2f}")
        print()


# ============================================================
# Main program execution
# ============================================================

inventory = create_inventory()

display_wheel_specs(inventory)

add_new_inventory_item(inventory, Wheel("Enkei RPF1", 18, 9.0, "5x114.3", "Hyper Silver", 3000.00))

search_inventory_by_name(inventory, "Work VSKF")

remove_last_inventory_item(inventory)

display_final_inventory(inventory)
# A array is a data strucucture that stores multiple values in order. 

from dataclasses import dataclass

# A record for one wheel
@dataclass
class Wheel:
    # Each variable below is a field in the record.
    # A field stores one piece of information about the wheel.

    name:str                                      # The name of the wheel
    diameter: int                                 # The diameter of the wheel in inches
    width: float                                  # The width of the wheel in inches
    bolt_pattern: str                             # The bolt pattern of the wheel, e.g., "5x114.3"
    color: str                                    # The color of the wheel
    price: float                                  # The price of the wheel in dollars

# An array of wheels
# This lets us store multiiple wheels in one variable. Each wheel is a record, and the array stores all of them together.
inventory = [
    Wheel("Volk Racing TE37", 18, 9.5, "5x114.3", "Matte Bronze", 3500.00),
    Wheel("Work VSKF", 18, 10, "5x114.3", "Silver", 4500.00),
    Wheel("Work Emitz", 18, 11.5, "5x114.3", "Gold", 5500.00),
    Wheel("BBS LM", 18, 10.5, "5x114.3", "Polished Silver", 7500.00),
]

# Access individual wheels in the array using their index
# The first wheel in the array is at index 0, the second wheel is at index 1, and so on.

def display_wheel_specs(wheel:Wheel):
    for index, wheel in enumerate(inventory):
        print(f"Array Index: {index}") # shows the array index of the wheel in the inventory and that it starts at 0.
        print(f"Wheel {index + 1}:")
        print(f"Model: {wheel.name}")
        print(f"Diameter: {wheel.diameter} inches")
        print(f"Width: {wheel.width} inches")
        print(f"Bolt Pattern: {wheel.bolt_pattern}")
        print(f"Color: {wheel.color}")
        print(f"Price: ${wheel.price:.2f}")
        print()  # Print a blank line between wheels

# Display the specifications of all wheels in the inventory
display_wheel_specs(inventory)
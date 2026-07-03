from dataclasses import dataclass

## TIME COMPLEXITY:
# Big O describes how the work grows as the amount of data grows.
#
# From fastest to slower:
# O(1)  -> Constant time
#          The operation takes about the same amount of work no matter how much data exists.
#
# O(n)  -> Linear time
#          The operation gets slower as the amount of data grows because you may need to check each item.
#
# Simple rule:
# O(1) is usually better/faster than O(n).
#
# RECORD TIME COMPLEXITY:
#
# - Access a field: O(1)
#   You can access a field directly by name, such as wheel.color.
#
# - Update a field: O(1)
#   You can update a field directly, such as wheel.color = "Bronze".
#
# - Create a record: O(1)
#   Creating one record takes a fixed amount of work when the number of fields is fixed.
#
# - Compare two records: O(1)
#   Usually constant time if the record has a fixed number of fields.

# A record stores related data together
# This record represents a vehicle wheel
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


# Create one wheel record
volk_racing_te37 = Wheel(
        name = "Volk Racing TE37",
        diameter = 18,
        width = 9.5,
        bolt_pattern = "5x114.3",
        color = "Matte Bronze",
        price = 2500.00
    )

# Access individual fields using dot notation
# Better method to print the wheel information. A function that takes a wheel record as an argument and prints its specifications.
def display_wheel_specs(wheel:Wheel):
    print(f"Model: {wheel.name}")
    print(f"Diameter: {wheel.diameter} inches")
    print(f"Width: {wheel.width} inches")
    print(f"Bolt Pattern: {wheel.bolt_pattern}")
    print(f"Color: {wheel.color}")
    print(f"Price: ${wheel.price:.2f}")


# Display the specifications of the wheel
display_wheel_specs(volk_racing_te37)

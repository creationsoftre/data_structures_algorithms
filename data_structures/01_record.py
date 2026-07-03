from dataclasses import dataclass

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

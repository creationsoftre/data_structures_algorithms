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
print(f"Model: {volk_racing_te37.name}")          # Output: Model: Volk Racing TE37
print(f"Diameter: {volk_racing_te37.diameter}")      # Output: Diameter: 18
print(f"Width: {volk_racing_te37.width}")         # Output: Width: 9.5
print(f"Bolt Pattern: {volk_racing_te37.bolt_pattern}")  # Output: Bolt Pattern: 5x114.3
print(f"Color: {volk_racing_te37.color}")         # Output: Color: Matte Bronze
print(f"Price: ${volk_racing_te37.price:.2f}")         # Output: Price: $3500.00


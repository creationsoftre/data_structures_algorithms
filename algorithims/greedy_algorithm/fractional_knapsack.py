# ============================================================
# Fractional Knapsack - Greedy Algorithm
# ============================================================
#
# Fractional knapsack is a greedy problem.
#
# Problem:
#
#   We have a bag with a weight limit.
#   We have items with a value and a weight.
#   We want to get the most value possible.
#
# The important rule:
#
#   We are allowed to take part of an item.
#
# This is why it is called fractional knapsack.
#
# Example:
#
#   Item A:
#       value = 60
#       weight = 10
#
#   Item B:
#       value = 100
#       weight = 20
#
#   Item C:
#       value = 120
#       weight = 30
#
#   capacity = 50
#
# ------------------------------------------------------------
# GREEDY IDEA
# ------------------------------------------------------------
#
# For each item, calculate:
#
#   value_per_weight = value / weight
#
# Then:
#
#   Take the item with the highest value_per_weight first.
#
# Why?
#
#   It gives us the most value for each unit of weight.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Time Complexity:
#   O(n log n)
#
# Speed:
#   Usually fast.
#
# Why?
#   We sort the items by value_per_weight.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   O(n)
#
# Why?
#   We store the selected items.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Greedy works for fractional knapsack because we can take part
# of an item.
#
# Greedy does not always work for 0/1 knapsack because we cannot
# split items.
#
# Fractional knapsack:
#
#   Take all of an item, or take part of it.
#
# 0/1 knapsack:
#
#   Take the whole item, or skip it.
# ============================================================
# ------------------------------------------------------------
# Fractional knapsack
# ------------------------------------------------------------
#
# Each item has:
#
#   name
#   value
#   weight
#
# The greedy rule:
#
#   Sort by value_per_weight.
#   Take the best value_per_weight first.
# ------------------------------------------------------------

def fractional_knapsack(items, capacity):
    # Add value_per_weight to each item.
    for item in items:
        item["value_per_weight"] = item["value"] / item["weight"]

    # Sort items from best value_per_weight to lowest.
    items.sort(key=lambda item: item["value_per_weight"], reverse=True)

    # Store what we take.
    selected_items = []

    # Track total value collected.
    total_value = 0

    # Track remaining space in the bag.
    remaining_capacity = capacity

    # Go through each item from best value_per_weight to lowest.
    for item in items:

        # If the bag is full, stop.
        if remaining_capacity == 0:
            break

        # If the full item can fit, take all of it.
        if item["weight"] <= remaining_capacity:
            selected_items.append({
                "name": item["name"],
                "amount_taken": "full",
                "weight_taken": item["weight"],
                "value_taken": item["value"]
            })

            total_value += item["value"]
            remaining_capacity -= item["weight"]

        # If the full item cannot fit, take only the part that fits.
        else:
            fraction = remaining_capacity / item["weight"]
            value_taken = item["value"] * fraction

            selected_items.append({
                "name": item["name"],
                "amount_taken": f"{fraction:.2f}",
                "weight_taken": remaining_capacity,
                "value_taken": value_taken
            })

            total_value += value_taken
            remaining_capacity = 0

    return total_value, selected_items


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

items = [
    {"name": "A", "value": 60, "weight": 10},
    {"name": "B", "value": 100, "weight": 20},
    {"name": "C", "value": 120, "weight": 30}
]

capacity = 50

print("Fractional Knapsack Example")
print("=" * 60)
print(f"Bag capacity: {capacity}")
print()

print("Available items:")
print("-" * 60)
print(f"{'Item':<8}{'Value':<10}{'Weight':<10}")
print("-" * 60)

for item in items:
    print(f"{item['name']:<8}{item['value']:<10}{item['weight']:<10}")

print()
print("Regular Greedy Result")
print("=" * 60)

total_value, selected_items = fractional_knapsack(
    [item.copy() for item in items],
    capacity
)

print(f"Total value: {total_value:.2f}")
print("Items selected:")

for selected in selected_items:
    print(
        f"  {selected['name']} -> "
        f"amount_taken={selected['amount_taken']}, "
        f"weight_taken={selected['weight_taken']}, "
        f"value_taken={selected['value_taken']:.2f}"
    )
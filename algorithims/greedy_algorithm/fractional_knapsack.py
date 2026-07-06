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


def fractional_knapsack_with_trace(items, capacity):
    for item in items:
        item["value_per_weight"] = item["value"] / item["weight"]

    items.sort(key=lambda item: item["value_per_weight"], reverse=True)

    selected_items = []
    total_value = 0
    remaining_capacity = capacity

    print("Fractional Knapsack Trace")
    print("=" * 60)
    print(f"Goal: Fill a bag with capacity {capacity} and get the most value.")
    print()
    print("Greedy rule:")
    print("  Take the item with the highest value per weight first.")
    print("  If the whole item does not fit, take the fraction that fits.")
    print()

    print("Items sorted by value per weight:")
    print("-" * 60)
    print(f"{'Item':<8}{'Value':<10}{'Weight':<10}{'Value/Weight':<15}")
    print("-" * 60)

    for item in items:
        print(
            f"{item['name']:<8}"
            f"{item['value']:<10}"
            f"{item['weight']:<10}"
            f"{item['value_per_weight']:<15.2f}"
        )

    print()
    print("Greedy Choices")
    print("=" * 60)

    for item in items:
        if remaining_capacity == 0:
            print("Bag is full. Stop checking items.")
            break

        print(f"Checking item {item['name']}")
        print("-" * 60)
        print(f"Remaining capacity before choice: {remaining_capacity}")
        print(f"{item['name']} value per weight: {item['value_per_weight']:.2f}")

        if item["weight"] <= remaining_capacity:
            print(f"Decision: Take all of item {item['name']}.")

            weight_taken = item["weight"]
            value_taken = item["value"]
            amount_taken = "full"

            selected_items.append({
                "name": item["name"],
                "amount_taken": amount_taken,
                "weight_taken": weight_taken,
                "value_taken": value_taken
            })

            total_value += value_taken
            remaining_capacity -= weight_taken

        else:
            fraction = remaining_capacity / item["weight"]
            weight_taken = remaining_capacity
            value_taken = item["value"] * fraction
            amount_taken = f"{fraction:.2f}"

            print(f"Decision: Item {item['name']} does not fully fit.")
            print(f"Take {weight_taken} out of {item['weight']} weight.")
            print(f"Fraction taken: {fraction:.2f}")

            selected_items.append({
                "name": item["name"],
                "amount_taken": amount_taken,
                "weight_taken": weight_taken,
                "value_taken": value_taken
            })

            total_value += value_taken
            remaining_capacity = 0

        print(f"Value added: {value_taken:.2f}")
        print(f"Total value so far: {total_value:.2f}")
        print(f"Remaining capacity after choice: {remaining_capacity}")
        print()

    print("Final Summary")
    print("=" * 60)
    print(f"{'Item':<8}{'Amount':<12}{'Weight Taken':<15}{'Value Taken':<15}")
    print("-" * 60)

    for selected in selected_items:
        print(
            f"{selected['name']:<8}"
            f"{selected['amount_taken']:<12}"
            f"{selected['weight_taken']:<15}"
            f"{selected['value_taken']:<15.2f}"
        )

    print("-" * 60)
    print(f"Total value: {total_value:.2f}")
    print(f"Unused capacity: {remaining_capacity}")

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

print()
fractional_knapsack_with_trace([item.copy() for item in items], capacity)
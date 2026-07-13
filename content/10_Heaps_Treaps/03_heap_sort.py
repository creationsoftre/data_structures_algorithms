# ============================================================
# Heap Sort - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Heap sort is a comparison-based sorting algorithm.
#
# It uses a heap to arrange values in sorted order.
#
# Heap sort is commonly performed using a max-heap when sorting
# values from smallest to largest.
#
# A max-heap stores the largest value at the root.
#
# Example max-heap:
#
#           90
#         /    \
#       70      80
#      /  \    /
#    20   50  40
#
# Array:
#
#   [90, 70, 80, 20, 50, 40]
#
#
# HOW HEAP SORT WORKS
# ------------------------------------------------------------
#
# Heap sort has two main phases:
#
#   1. Build a max-heap.
#
#   2. Move the largest values to the end of the array.
#
#
# PHASE 1 - BUILD A MAX-HEAP
# ------------------------------------------------------------
#
# The original array is rearranged into a max-heap.
#
# Example:
#
# Original array:
#
#   [40, 10, 30, 50, 20]
#
# Max-heap:
#
#   [50, 40, 30, 10, 20]
#
# Tree:
#
#           50
#         /    \
#       40      30
#      /  \
#    10   20
#
# The largest value is now stored at index 0.
#
#
# PHASE 2 - SORT THE ARRAY
# ------------------------------------------------------------
#
# The root is swapped with the final unsorted value.
#
# Example:
#
# Before swap:
#
#   [50, 40, 30, 10, 20]
#
# Swap 50 with 20:
#
#   [20, 40, 30, 10, 50]
#
# The value 50 is now in its final sorted position.
#
# The heap size is reduced so 50 is no longer included.
#
# Heapify down restores the max-heap:
#
#   [40, 20, 30, 10, 50]
#
# This process repeats until the entire array is sorted.
#
#
# FINAL RESULT
# ------------------------------------------------------------
#
# Original array:
#
#   [40, 10, 30, 50, 20]
#
# Sorted array:
#
#   [10, 20, 30, 40, 50]
#
#
# IMPORTANT
# ------------------------------------------------------------
#
# Heap sort sorts the array in place.
#
# It does not need a second array to store all the values.
#
# Heap sort is not stable.
#
# Equal values may change their original order during sorting.
#
#
# ARRAY INDEX FORMULAS
# ------------------------------------------------------------
#
# For a value stored at index i:
#
#   Parent index:
#
#       (i - 1) // 2
#
#   Left child index:
#
#       (2 * i) + 1
#
#   Right child index:
#
#       (2 * i) + 2
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
#   Case              Time Complexity
#   ----------------------------------
#   Best case              O(n log n)
#   Average case           O(n log n)
#   Worst case             O(n log n)
#
# Building the heap requires:
#
#   O(n)
#
# Removing the largest value repeatedly requires:
#
#   O(n log n)
#
# The overall time complexity is:
#
#   O(n log n)
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(1)
#
# Heap sort rearranges the values inside the original array.
#
# Only a small number of extra variables are required.
#
#
# ============================================================
# HEAP SORT IMPLEMENTATION
# ============================================================


def heap_sort(values):
    # Store the number of values in the array.
    array_size = len(values)

    # Build a max-heap from the original array.
    #
    # The final parent node is located at:
    #
    #   (array_size // 2) - 1
    #
    # Nodes after this index are leaf nodes and do not need
    # to be heapified.
    for index in range((array_size // 2) - 1, -1, -1):
        heapify_down(values, array_size, index)

    # Move the largest value to the end of the array.
    #
    # The root of the max-heap is always stored at index 0.
    for end_index in range(array_size - 1, 0, -1):
        # Swap the largest value with the final unsorted value.
        values[0], values[end_index] = (
            values[end_index],
            values[0],
        )

        # Restore the max-heap using only the unsorted section.
        #
        # end_index becomes the new heap size because the value
        # at end_index is already in its final sorted position.
        heapify_down(values, end_index, 0)

    # Return the sorted array.
    return values


def heapify_down(values, heap_size, index):
    # Continue moving the current value downward until the
    # max-heap property is restored.
    while True:
        # Assume the current index contains the largest value.
        largest = index

        # Calculate the left and right child indexes.
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2

        # Check whether the left child exists and contains a
        # larger value.
        if (
            left_child < heap_size
            and values[left_child] > values[largest]
        ):
            largest = left_child

        # Check whether the right child exists and contains a
        # larger value.
        if (
            right_child < heap_size
            and values[right_child] > values[largest]
        ):
            largest = right_child

        # Stop when the current value is already larger than
        # both children.
        if largest == index:
            break

        # Swap the current value with its larger child.
        values[index], values[largest] = (
            values[largest],
            values[index],
        )

        # Continue checking from the child's previous position.
        index = largest


# ============================================================
# CODE EXAMPLE - CAR PART PRICES
# ============================================================
#
# Create a list containing different car part prices.
car_part_prices = [1200, 450, 800, 2000, 300, 950]

# Original array:
#
#   [1200, 450, 800, 2000, 300, 950]
#
# Sort the prices from lowest to highest.
heap_sort(car_part_prices)

# Display the sorted prices.
print("Sorted prices:", car_part_prices)

# ============================================================
# EXPECTED OUTPUT
# ============================================================
#
# Sorted prices: [300, 450, 800, 950, 1200, 2000]
# ============================================================
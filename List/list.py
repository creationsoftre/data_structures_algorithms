# Time Complexity
# Python lists are implemented as dynamic arrays, which means their time complexity for various operations can be summarized as follows:

# Accessing an element by index: O(1)O(1) (constant time) because you can directly access any element.
# Appending an element: O(1)O(1) on average. However, occasionally, when the list needs to resize, it can take O(n)O(n) time, where nn is the number of elements in the list.
# Inserting or deleting an element at the end: O(1)O(1) for deletion and O(1)O(1) on average for insertion (similar to appending).
# Inserting or deleting an element at the beginning or middle: O(n)O(n) because elements need to be shifted to accommodate the new element or fill the gap left by the removed element.
# Searching for an element: O(n)O(n) because, in the worst case, you might need to check each element.
# Space Complexity
# The space complexity of a Python list is primarily determined by the number of elements it contains:

# Space for the elements: O(n)O(n), where nn is the number of elements in the list.
# Overhead for dynamic resizing: Python lists over-allocate to reduce the frequency of resizing operations. This means the actual space used can be more than O(n)O(n), but the over-allocation is generally a constant factor, so it doesn't affect the overall space complexity.


# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing an element
print(my_list[2])  # O(1)

# Appending an element
my_list.append(6)  # O(1) on average

# Inserting an element at the beginning
my_list.insert(0, 0)  # O(n)

# Deleting an element from the end
my_list.pop()  # O(1)

# Searching for an element
print(3 in my_list)  # O(n)
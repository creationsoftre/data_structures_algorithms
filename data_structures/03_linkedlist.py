# A linked list is a data structure where each item points to the next item in a linear order.
# Each item is called a node, and each node contains data and a reference to the next node in the list.

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
# LINKED LIST TIME COMPLEXITY:
#
# - Access by position/search: O(n)
#   You must start at the head and move node by node.
#
# - Insert at head: O(1)
#   You only update the new node to point to the old head, then update head.
#
# - Insert at tail without a tail pointer: O(n)
#   You must traverse the list to find the last node.
#
# - Insert at tail with a tail pointer: O(1)
#   If the list tracks the tail, you can add directly to the end.
#
# - Delete from head: O(1)
#   You only move the head to the next node.
#
# - Delete by value/search: O(n)
#   You must traverse the list to find the node to remove.
#
# - Delete a known node with previous node reference: O(1)
#   If you already have the node and previous node reference, relinking is constant time.

from dataclasses import dataclass

# RECORD represents one wheel
# We will store this record in each node of the linked list node.

@dataclass
class Wheel:
    name: str           # The name of the wheel
    diameter: int       # The diameter of the wheel in inches 
    width: float        # The width of the wheel in inches
    bolt_pattern: str   # The bolt pattern of the wheel, e.g., "5x114.3"
    color: str          # The color of the wheel
    price: float        # The price of the wheel in dollars


# NODE: 
# A node stores two things:
# 1. The data (in this case, a Wheel record)
# 2. A reference to the next node in the list (or None if it's the last node)

class Node: 
    def __init__(self,data):
        self.data = data  # Store the wheel record in the node
        self.next = None  # Initialize the next reference to None


# LINKED LIST:
# The linked list keeps track of the first node in the list known as the head

class LinkedList:
    # Initialize the head of the list to None (empty list)
    def __init__(self):
        self.head = None 
    
    # APPEND: Add a new node to the end of the list
    def append(self, data):
        new_node = Node(data) # Create a new node with the given data

        if self.head is None: # If the list is empty, set the new node as the head
            self.head = new_node
            return
        
        # Start at the head and move through the list until we find the last node
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next # Move to the next node

        # connect the last node to the new node
        current_node.next = new_node

    # DISPLAY: Print all the nodes in the list
    def display(self):
        current_node = self.head # Start at the head of the list
        index = 0 # Initialize an index to keep track of the node position

        while current_node is not None:
            wheel = current_node.data # Get the wheel record from the current node

            print(f"Node Index: {index}")  # Shows the node position as we walk through the list.
            print(f"Wheel {index + 1}:")
            print(f"Model: {wheel.name}")
            print(f"Diameter: {wheel.diameter} inches")
            print(f"Width: {wheel.width} inches")
            print(f"Bolt Pattern: {wheel.bolt_pattern}")
            print(f"Color: {wheel.color}")
            print(f"Price: ${wheel.price:.2f}")
            print()

            # Move to the next node in the list
            current_node = current_node.next
            index += 1 # Increment the index for the next node
    
    # SEARCH: Search for a wheel by name in the linked list
    def search_by_name(self, search_name):
        current_node = self.head # Start at the head of the list

        while current_node is not None:
            wheel = current_node.data # Get the wheel record from the current node

            if wheel.name == search_name: # Check if the wheel name matches the search name
                return wheel # Return the wheel if we find it

            current_node = current_node.next # Move to the next node in the list

        return None # Return None if the wheel was not found
    
    # REMOVE: Remove a node by name from the linked list
    def remove_by_name(self, name_to_remove):
        current_node = self.head # Start at the head of the list
        previous_node = None # Keep track of the previous node

        while current_node is not None:
            wheel = current_node.data # Get the wheel record from the current node

            if wheel.name == name_to_remove: # Check if the wheel name matches the name to remove
                # If the node we are removing is the head,
                # move the head to the next node
                if previous_node is None:
                    self.head = current_node.next
                else:
                    # skipping the current node BIGGEST CONCEPT: so TE37 -> Work VSKF -> Work Emitz -> BBS LM becomes TE37 -> Work Emitz -> BBS LM
                    previous_node.next = current_node.next

                return wheel # Return the removed wheel record
            
            previous_node = current_node # Move the previous node to the current node
            current_node = current_node.next # Move to the next node in the list

        return None # Return None if the wheel was not found in the list
        

# =========================================
# HELPER FUNCTIONS
# ========================================

# Print the title of the section for visual separation.
def show_section_title(title):
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title) + "\n")


def create_inventory():
    inventory = LinkedList() # Create an empty linked list for the inventory

    inventory.append(Wheel("Volk Racing TE37", 18, 9.5, "5x114.3", "Matte Bronze", 3500.00))
    inventory.append(Wheel("Work VSKF", 18, 10.0, "5x114.3", "Silver", 4500.00))
    inventory.append(Wheel("Work Emitz", 18, 11.5, "5x114.3", "Gold", 5500.00))
    inventory.append(Wheel("BBS LM", 18, 10.5, "5x114.3", "Polished Silver", 7500.00))

    return inventory


# =========================================
# MAIN PROGRAM
# =========================================

inventory = create_inventory() # Create an inventory of wheels

show_section_title("1. Display Linked List Inventory")
inventory.display() # Display the linked list inventory


show_section_title("2. Append to Linked List Inventory")
new_wheel = Wheel("Enkei RPF1", 18, 9.0, "5x114.3", "Hyper Silver", 3000.00)
inventory.append(new_wheel) # Append a new wheel to the linked list inventory   
print(f"Added new wheel to inventory: {new_wheel.name}" )

show_section_title("3. Search in Linked List Inventory")

search_name = "Work VSKF"
result = inventory.search_by_name(search_name)

print(f"Search Result for '{search_name}':")

if result:
    print(f"Wheel found: {result.name}")
    print(f"Color: {result.color}")
    print(f"Price: ${result.price:.2f}")
else:
    print("Wheel not found.")


show_section_title("4. Remove from Linked List Inventory")
remove_name = "Work Emitz"
removed_wheel = inventory.remove_by_name(remove_name) # Remove a wheel by name from the linked list inventory
if removed_wheel:
    print(f"Removed wheel from inventory: {removed_wheel.name}")
else:
    print(f"Wheel '{remove_name}' not found in inventory.")

show_section_title("5. Display Linked List Inventory After Removal")
inventory.display() # Display the linked list inventory after removal







from ArrayList import ArrayList

num_list = ArrayList()

# Insert various items using append(), prepend(), and insert_after()
num_list.append(14)           # List: 14
num_list.append(2)            # List: 14, 2
num_list.append(20)           # List: 14, 2, 20
num_list.prepend(31)          # List: 31, 14, 2, 20
num_list.insert_after(2, 16)  # List: 31, 14, 2, 16, 20
num_list.insert_after(20, 55) # List: 31, 14, 2, 16, 20, 55

# Output list
print("List after adding items: ", end="")
num_list.print(", ", "\n")

# Remove the last and first items
num_list.remove(55) # List: 31, 14, 2, 16, 20
num_list.remove(31) # List: 14, 2, 16, 20

# Output list again
print("List after removing first and last items: ", end="")
num_list.print(", ", "\n")

# Insert three more items
num_list.prepend(67)          # List: 67, 14, 2, 16, 20
num_list.insert_after(20, 58) # List: 67, 14, 2, 16, 20, 58
num_list.append(89)           # List: 67, 14, 2, 16, 20, 58, 89
   
# Output final list
print("List after inserting three more items: ", end="")
num_list.print(", ", "\n")
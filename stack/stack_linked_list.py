# Singly-linked-list-based

numbers = [ 76, 81, 91, 34, 62, 88, 77, 21, 18 ]

# Initialize a new Stack and add numbers
num_stack = Stack()
for number in numbers:
    num_stack.push(number)

# Show the stack before any pop operations occur
print("Stack: ", end="")
num_stack.print(", ", "\n")

# Pop until stack is empty, printing each popped item and remaining stack
while not num_stack.is_empty():
    print(f"Popped {num_stack.pop()}")
    print("Stack: ", end="")
    num_stack.print(", ", "\n")
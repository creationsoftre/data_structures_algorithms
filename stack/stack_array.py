from Stack import Stack

# Make two stacks, one bounded to 4 items and the other unbounded
bounded_stack = Stack(4)
unbounded_stack = Stack()

# Push 8 items to each
values_to_push = list(range(1, 9))
print("Pushing values 1 through 8 to each stack")
for i in values_to_push:
    bounded_stack.push(i)
    unbounded_stack.push(i)

# Pop two items off each stack
print("Popping twice")
for i in range(2):
    bounded_stack.pop()
    unbounded_stack.pop()

# Push 4 more items onto each stack
values_to_push = list(range(10, 50, 10))
print(f"Pushing values to each stack: {values_to_push}")
for i in values_to_push:
    bounded_stack.push(i)
    unbounded_stack.push(i)

# Display contents of each stack
print(f"Bounded stack (max_length={bounded_stack.max_length}) contents:")
while len(bounded_stack) > 0:
    print(f"  {bounded_stack.pop()}")
print("Unbounded stack contents:")
while len(unbounded_stack) > 0:
    print(f"  {unbounded_stack.pop()}")
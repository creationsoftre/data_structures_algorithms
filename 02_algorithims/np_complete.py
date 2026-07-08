# ============================================================
# NP-Complete Problems
# ============================================================
#
# NP-Complete is a category of problems that are hard to solve
# quickly when the input gets large.
#
# The simple idea:
#
#   Finding the answer can be slow.
#   Checking an answer can be fast.
#
# Example:
#
#   If someone asks you to solve a hard puzzle, it may take a
#   long time to find the answer.
#
#   But if someone gives you a completed answer, checking it may
#   be much faster.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Faster Big O examples:
#
#   O(1)       Very fast
#   O(log n)   Very fast
#   O(n)       Usually okay
#   O(n log n) Usually okay
#   O(n^2)     Slower, but can still work for smaller inputs
#
# Slower Big O examples:
#
#   O(2^n)     Very slow as input grows
#   O(n!)      Extremely slow as input grows
#
# Many NP-Complete problems are solved with brute force.
#
# Brute force means:
#
#   Try every possible answer.
#
# This is why they can become slow.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space complexity depends on the solution.
#
# Some solutions only store a few variables.
# Some solutions store many possible answers.
#
# Storing more possible answers uses more memory.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# NP-Complete does not mean impossible.
#
# It means:
#
#   We do not currently know a fast way to solve every version
#   of the problem.
#
# Small inputs may still be easy to solve.
# Large inputs can become very slow.
#
# ============================================================


# ------------------------------------------------------------
# Example: Subset Sum
# ------------------------------------------------------------
#
# Question:
#
#   Can we choose some numbers that add up to a target?
#
# Example:
#
#   numbers = [3, 5, 7, 10]
#   target = 15
#
# Answer:
#
#   True
#
# Why?
#
#   5 + 10 = 15
#
# Finding that answer may take time.
# Checking that answer is fast.
# ------------------------------------------------------------



def check_subset_answer(possible_answer, target):
    # Checking an answer is fast.
    # We only add the numbers and compare the total to the target.
    return sum(possible_answer) == target


# ------------------------------------------------------------
# Brute force subset sum
# ------------------------------------------------------------
#
# This tries many possible combinations.
#
# For each number, we have two choices:
#
#   Use the number
#   Skip the number
#
# This grows like:
#
#   O(2^n)
#
# O(2^n) is slow because the number of combinations doubles
# every time we add another number.
# ------------------------------------------------------------


def subset_sum(numbers, target):
    # Start with an empty combination.
    combinations = [[]]

    # Go through each number.
    for number in numbers:

        # Store combinations that include the current number.
        new_combinations = []

        # Try adding the current number to each existing combination.
        for combo in combinations:
            new_combo = combo + [number]

            # If the new combination matches the target, we found an answer.
            if sum(new_combo) == target:
                return True

            # Save the new combination so future numbers can be added to it.
            new_combinations.append(new_combo)

        # Add the new combinations to the full list.
        combinations.extend(new_combinations)

    # No combination matched the target.
    return False


# ------------------------------------------------------------
# Trace version
# ------------------------------------------------------------
#
# This prints the combinations being checked.
# It helps show why brute force gets slow.
# ------------------------------------------------------------


def subset_sum_with_trace(numbers, target):
    combinations = [[]]

    print("Subset Sum Trace")
    print("-" * 40)
    print(f"Numbers: {numbers}")
    print(f"Target: {target}")
    print(f"Goal: Find a combination that adds up to {target}")
    print("-" * 40)

    for number in numbers:
        print(f"Current number: {number}")

        new_combinations = []

        for combo in combinations:
            new_combo = combo + [number]

            print(f"Checking: {new_combo}")

            if sum(new_combo) == target:
                print(f"Found answer: {new_combo}")
                return True

            new_combinations.append(new_combo)

        combinations.extend(new_combinations)

        print(f"Combinations so far: {len(combinations)}")
        print()

    print("No answer found.")
    return False


# ------------------------------------------------------------
# Test examples
# ------------------------------------------------------------

numbers = [3, 5, 7, 10]
target = 15

print("Subset Sum Example")
print("-" * 40)
print(f"Numbers: {numbers}")
print(f"Target: {target}")
print(f"Goal: Find a combination of numbers that adds up to {target}")
print()

print("Checking possible answers:")
print(f"Does [5, 10] add up to {target}?")
print(check_subset_answer([5, 10], target))  # True

print(f"Does [3, 7] add up to {target}?")
print(check_subset_answer([3, 7], target))   # False

print()
print("Running brute force search:")
print(f"Trying to find any combination that adds up to {target}")
print(subset_sum(numbers, target))           # True

print()
print("Running brute force search with trace:")
subset_sum_with_trace(numbers, target)

# ------------------------------------------------------------
# Why use brute force here?
# ------------------------------------------------------------
#
# We are not using brute force because it is the best solution.
#
# We are using brute force because it clearly shows the problem:
#
#   Each number gives us two choices:
#
#       Use it
#       Skip it
#
#   This causes the number of combinations to double.
#
# That is what makes this type of problem slow as the input grows.
#
# Later, smarter solutions can use pruning, caching, or dynamic
# programming to avoid checking unnecessary combinations.
# ------------------------------------------------------------
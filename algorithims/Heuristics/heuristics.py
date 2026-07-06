# ============================================================
# Heuristics
# ============================================================
#
# A heuristic is a smart guess used to make a search faster.
#
# Simple idea:
#
#   Instead of checking every possible option,
#   use a rule that helps guide the search.
#
# A heuristic does not always guarantee the perfect answer.
#
# But it can help find a good answer faster.
#
# ------------------------------------------------------------
# EXAMPLE: GRID PATHFINDING
# ------------------------------------------------------------
#
# Problem:
#
#   Find a path from a start position to a target position.
#
# Example grid:
#
#   S . . .
#   . X . .
#   . X . .
#   . . . T
#
# S = start
# T = target
# X = blocked cell
# . = open cell
#
# A simple heuristic:
#
#   Choose the move that gets closer to the target.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Time Complexity:
#   Depends on the heuristic and the problem.
#
# Speed:
#   Usually faster than brute force.
#
# Why?
#   A heuristic tries to avoid checking every possible path.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   Depends on what the algorithm stores.
#
# In this simple example:
#   O(n)
#
# Why?
#   We store the path and visited positions.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Heuristics are useful when:
#
#   The perfect answer is expensive to find.
#   A good answer is acceptable.
#   We want to guide the search instead of trying everything.
#
# Heuristic does not mean random.
#
# It means:
#
#   Use a rule or estimate to make a better choice.
#
# In this example, our heuristic is distance to the target.
# ============================================================

# ------------------------------------------------------------
# Heuristic function
# ------------------------------------------------------------
#
# This function estimates how far a position is from the target.
#
# We use Manhattan distance.
#
# Manhattan distance means:
#
#   How many row moves plus column moves are needed
#   if we cannot move diagonally?
#
# Example:
#
#   position = (0, 0)
#   target   = (3, 3)
#
#   distance = abs(0 - 3) + abs(0 - 3)
#   distance = 3 + 3
#   distance = 6
#
# Smaller distance means closer to the target.
# ------------------------------------------------------------

def heuristic(position, target):
    row, col = position
    target_row, target_col = target

    return abs(row - target_row) + abs(col - target_col)

# ------------------------------------------------------------
# Get valid neighbors
# ------------------------------------------------------------
#
# This function returns the valid moves from the current position.
#
# We allow four directions:
#
#   up
#   down
#   left
#   right
#
# We do not allow:
#
#   diagonal moves
#   moves outside the grid
#   moves into blocked cells
# ------------------------------------------------------------

def get_neighbors(grid, position):
    row, col = position

    possible_moves = [
        (row - 1, col),  # up
        (row + 1, col),  # down
        (row, col - 1),  # left
        (row, col + 1)   # right
    ]

    neighbors = []

    for move_row, move_col in possible_moves:
        # Check if the move is inside the grid.
        inside_rows = 0 <= move_row < len(grid)
        inside_cols = 0 <= move_col < len(grid[0])

        if inside_rows and inside_cols:
            # Check if the cell is not blocked.
            if grid[move_row][move_col] != "X":
                neighbors.append((move_row, move_col))

    return neighbors










# ------------------------------------------------------------
# Print grid
# ------------------------------------------------------------
#
# This helper prints the grid in a readable way.
# ------------------------------------------------------------

def print_grid(grid):
    for row in grid:
        print(" ".join(row))


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

grid = [
    ["S", ".", ".", "."],
    [".", "X", ".", "."],
    [".", "X", ".", "."],
    [".", ".", ".", "T"]
]

start = (0, 0)
target = (3, 3)

print("Heuristics Example")
print("=" * 60)
print("Grid:")
print_grid(grid)
print()
print(f"Goal: Find a path from {start} to {target}.")
print()
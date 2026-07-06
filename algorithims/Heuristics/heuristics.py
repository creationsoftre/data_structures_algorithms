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
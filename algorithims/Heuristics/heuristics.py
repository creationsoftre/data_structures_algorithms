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
# ============================================================
# BST Height and Insertion Order
# ============================================================
#
# A Binary Search Tree can be fast or slow depending on its shape.
#
# The shape depends on the order values are inserted.
#
# ------------------------------------------------------------
# IMPORTANT IDEA
# ------------------------------------------------------------
#
# Same values, different insert order, different tree shape.
#
# Values:
#
#   1, 2, 3, 4, 5, 6, 7
#
# Bad insertion order:
#
#   1, 2, 3, 4, 5, 6, 7
#
# Better insertion order:
#
#   4, 2, 6, 1, 3, 5, 7
#
# ------------------------------------------------------------
# BAD INSERTION ORDER
# ------------------------------------------------------------
#
# Insert values in sorted order:
#
#   1, 2, 3, 4, 5, 6, 7
#
# The BST becomes:
#
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#          \
#           5
#            \
#             6
#              \
#               7
#
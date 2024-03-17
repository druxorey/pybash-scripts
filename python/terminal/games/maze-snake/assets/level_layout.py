from config import WALL, SPACE
import random

first_map = """\
# ########## ########## #
#                       #
# ## ## #### #### ## ## #
# #   #           #   # #
# #   # #### #### #   # #
# #   # #       # #   # #
# #   # # ## ## # #   # #
# #   # # #   # # #   # #
# #   # # #   # # #   # #
# #   # # #   # # #   # #
# ## ## # #   # # ## ## #
                         
# #   #           #   # #
                         
# ## ## # #   # # ## ## #
# #   # # #   # # #   # #
# #   # # #   # # #   # #
# #   # # #   # # #   # #
# #   # # ## ## # #   # #
# #   # #       # #   # #
# #   # # ## ## # #   # #
# #   #           #   # #
# ## ## #### #### ## ## #
#                       #
# ########## ########## #\
"""

second_map = """\
# ########## ########## #
#                       #
# ### ###       ### ### #
# #                   # #
#       # ## ## #       #
# #     # #   # #     # #
# ### ### #   # ### ### #
#                       #
# ### ### ##### ### ### #
#                       #
# ##### #  ###  # ##### #
# #     #       #     # #
                         
# #     #       #     # #
# ##### #  ###  # ##### #
#                       #
# ### ### ##### ####### #
#                       #
# ### ### #   # ### ### #
# #     # #   # #     # #
#       # ## ## #       #
# #                   # #
# ### ###       ### ### #
#                       #
# ########## ########## #\
"""

def get_obstacle_definition():
    aleatory_map = random.randint(1,2)

    if aleatory_map == 1:
        obstacle_definition = first_map
    elif aleatory_map == 2:
        obstacle_definition = second_map
    
    return [list(row) for row in obstacle_definition.split("\n")]


def get_map_size(obstacle_definition):
    MAP_WIDTH = len(obstacle_definition[0])
    MAP_HEIGHT = len(obstacle_definition)
    return [MAP_WIDTH, MAP_HEIGHT]


def main():
    pass


if __name__ == "__main__":
    main()

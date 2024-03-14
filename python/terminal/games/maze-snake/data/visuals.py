import os
import random

WALL = "███"
SPACE = "   "
score = None

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


def print_tutorial_screen(MAP_SIZE):
    MAP_WIDTH = MAP_SIZE[0]

    os.system("clear")
    
    print_blank_spaces(6, MAP_WIDTH, "top")
    print_text("Tutorial\n Controles: wasd\nSalir: q\n󰉛: Vale 1 punto y añade 1 de largo a la cola\n: Vale 5 puntos y resta 1 de largo a la cola\n\nPresiona ENTER para continuar", MAP_WIDTH)
    print_blank_spaces(6, MAP_WIDTH, "bottom")

    input("")


def print_game_over_screen(score, MAP_SIZE):
    MAP_WIDTH = MAP_SIZE[0]

    os.system("clear")
    
    print_blank_spaces(10, MAP_WIDTH, "top")
    print_text(f"GAME OVER\n\nTu puntuación {score}", MAP_WIDTH)
    print_blank_spaces(10, MAP_WIDTH, "bottom")


def print_text(text, MAP_WIDTH):
    text = text.split("\n")
    for row in text:
        print(WALL + row.center(MAP_WIDTH * 3) + WALL) 


def print_blank_spaces(lines, MAP_WIDTH, position):
    if position == "top":
        print(WALL + (WALL * MAP_WIDTH) + WALL)
    else:
        pass
    for _ in range (lines):
        print(WALL + (SPACE * MAP_WIDTH) + WALL) 
    if position == "bottom":
        print(WALL + (WALL * MAP_WIDTH) + WALL)


def main():
    pass


if __name__ == "__main__":
    main()

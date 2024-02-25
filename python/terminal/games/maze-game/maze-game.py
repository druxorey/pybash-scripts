import readchar
import os

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

character_position = [19,14]

while True:

    os.system("clear")

    print("╔" + "═" * MAP_WIDTH * 3 + "╗")

    for coordinate_y in range(MAP_HEIGHT):
        print("║", end="")
        for coordinate_x in range(MAP_WIDTH):
            if character_position[POS_X] == coordinate_x and character_position[POS_Y] == coordinate_y:
                print("  ", end="")
            else:
                print("   ", end="")
        print("║")

    print("╚" + "═" * MAP_WIDTH * 3 + "╝")

    direction = readchar.readchar()

    if direction == "w":
        character_position[POS_Y] -= 1
        if character_position[POS_Y] < 0:
            character_position[POS_Y] = (MAP_HEIGHT - 1)
    elif direction == "s":
        character_position[POS_Y] += 1
        if character_position[POS_Y] > MAP_HEIGHT:
            character_position[POS_Y] = (0)
    elif direction == "a":
        character_position[POS_X] -= 1
        if character_position[POS_X] < 0:
            character_position[POS_X] = (MAP_WIDTH - 1)
    elif direction == "d":
        character_position[POS_X] += 1
        if character_position[POS_X] > (MAP_WIDTH -1):
            character_position[POS_X] = (0)
    elif direction == "Q":
        exit()

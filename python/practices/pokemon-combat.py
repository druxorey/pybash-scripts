import os
from random import randint
from colorama import Fore, Style

# Color variables
yellow = (Fore.YELLOW)
blue = (Fore.BLUE)
red = (Fore.RED)
green = (Fore.GREEN)
reset = (Style.RESET_ALL)

# Initial values
pikachu_initial_life = randint(70,140)
pikachu_life = pikachu_initial_life

squirtle_initial_life = randint(100,160)
squirtle_life = squirtle_initial_life

os.system("clear")
print(f"\n¡¡ Inicial el combate pokemon !!\n")

print(f"La vida inicial de Pikachu es de {yellow}{pikachu_initial_life} pts{reset}")
print(f"La vida inicial de Squirtle es de {blue}{squirtle_initial_life} pts{reset}")

while pikachu_life > 0 and squirtle_life > 0:   
    
    # Turno de Pikachu
    input(f"\n{yellow}Es el turno de Pikachu{reset} (Presiona enter)")
    os.system("clear")
    pikachu_atack = randint(1,2)
    if pikachu_atack == 1:
        # Bola voltio
        squirtle_life -= 10
        print(f"\nPikachu ataca con {yellow}Bola Voltio{reset}\n")
    elif pikachu_atack == 2:
        # Onda trueno
        squirtle_life -= 12
        print(f"\nPikachu ataca con {yellow}Onda Trueno{reset}\n")

    if squirtle_life < 0:
        squirtle_life = 0

    # squirtle life calculator
    squirtle_life_proportion = int(squirtle_life / squirtle_initial_life * 10)
    squirtle_life_bar = '#' * squirtle_life_proportion + " " * (10 - squirtle_life_proportion)
    print(f"{blue}Vida de Squirtle:{reset} [{squirtle_life_bar}] ({squirtle_life}/{squirtle_initial_life})")
    
    # pikachu life calculator
    pikachu_life_proportion = int(pikachu_life / pikachu_initial_life * 10)
    pikachu_life_bar = '#' * pikachu_life_proportion + " " * (10 - pikachu_life_proportion)
    print(f"{yellow}Vida de Pikachu:{reset}  [{pikachu_life_bar}] ({pikachu_life}/{pikachu_initial_life})")

    # Turno de Squirtle 
    input(f"\n{blue}Es el turno de Squirtle{reset} (Presiona enter)")

    squirtle_atack = None
    while squirtle_atack not in [1,2,3]:
        print(f"\n¿Qué ataque quieres hacer?")
        squirtle_atack = int(input("(1)Placaje, (2)Burbuja (3)Nada: "))
    if squirtle_atack == 1:
        # Placaje
        pikachu_life -= 2
        os.system("clear")
        print(f"\nSquirtle ataca con {blue}Placaje{reset}\n")
    elif squirtle_atack == 2:
        # Burbuja
        pikachu_life -= 25
        os.system("clear")
        print(f"\nSquirtle ataca con {blue}Burbuja{reset}\n")
    elif squirtle_atack == 3:
        # No hacer nada 
        pikachu_life -= 0
        os.system("clear")
        print(f"\nSquirtle no hace nada\n")
    
    if pikachu_life < 0:
        pikachu_life = 0

    # squirtle life calculator
    squirtle_life_proportion = int(squirtle_life / squirtle_initial_life * 10)
    squirtle_life_bar = '#' * squirtle_life_proportion + " " * (10 - squirtle_life_proportion)
    print(f"{blue}Vida de Squirtle:{reset} [{squirtle_life_bar}] ({squirtle_life}/{squirtle_initial_life})")

    # pikachu life calculator
    pikachu_life_proportion = int(pikachu_life / pikachu_initial_life * 10)
    pikachu_life_bar = '#' * pikachu_life_proportion + " " * (10 - pikachu_life_proportion)
    print(f"{yellow}Vida de Pikachu:{reset}  [{pikachu_life_bar}] ({pikachu_life}/{pikachu_initial_life})")

if pikachu_life > squirtle_life:
    print(f"{yellow}Pikachu ha ganado{reset}")
else:
    print(f"{blue}Squirtle ha ganado{reset}")

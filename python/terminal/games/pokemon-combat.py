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

print(f"\n¡¡ Inicial el combate pokemon !!\n")

print(f"La vida inicial de Pikachu es de {yellow}{pikachu_initial_life} pts{reset}")
print(f"La vida inicial de Squirtle es de {blue}{squirtle_initial_life} pts{reset}")

while pikachu_life > 0 and squirtle_life > 0:   
    
    # Turno de Pikachu
    input(f"\n{yellow}Es el turno de Pikachu{reset} (Presiona enter)")
    pikachu_atack = randint(1,2)
    if pikachu_atack == 1:
        # Bola voltio
        squirtle_life -= 10
        print(f"\nPikachu ataca con {yellow}Bola Voltio{reset}")
    elif pikachu_atack == 2:
        # Onda trueno
        squirtle_life -= 12
        print(f"\nPikachu ataca con {yellow}Onda Trueno{reset}")

    # squirtle life calculator
    squirtle_life_proportion = int(squirtle_life / squirtle_initial_life * 10)
    squirtle_life_bar = '#' * squirtle_life_proportion + " " * (10 - squirtle_life_proportion)
    
    print(f"{blue}Vida de Squirtle:{reset} [{squirtle_life_bar}] {squirtle_life}pts")
    
    # Turno de Squirtle 
    input(f"\n{blue}Es el turno de Squirtle{reset} (Presiona enter)")
    
    squirtle_atack = None
    while squirtle_atack != 1 and squirtle_atack != 2:
        print(f"\n¿Qué ataque quieres hacer?")
        squirtle_atack = int(input("(1)Placaje o (2)Burbuja: "))
    if squirtle_atack == 1:
        # Placaje
        pikachu_life -= 12
        print(f"\nSquirtle ataca con {blue}Placaje{reset}")
    elif squirtle_atack == 2:
        # Burbuja
        pikachu_life -= 14
        print(f"\nSquirtle ataca con {blue}Burbuja{reset}")

    # pikachu life calculator
    pikachu_life_proportion = int(pikachu_life / pikachu_initial_life * 10)
    pikachu_life_bar = '#' * pikachu_life_proportion + " " * (10 - pikachu_life_proportion)
    
    print(f"{yellow}Vida de Pikachu:{reset} [{pikachu_life_bar}] {pikachu_life}pts")

if pikachu_life > squirtle_life:
    print(f"{yellow}Pikachu ha ganado{reset}")
else:
    print(f"{blue}Squirtle ha ganado{reset}")

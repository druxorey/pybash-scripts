from colorama import Fore, Style

RESET = f"{Style.RESET_ALL}"
RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE

MAP_LAYOUT = """\
#################
###    #####@####
### ## ##### ####
###@##       ####
###### ##########
###    ##########
### #####@    ###
### ######### ###
###           ###
#######   #######
#######   #######
#######   #######
#################\
"""

HELP_SCREEN = f"""\
█████████████████████████████████████████████████████████
███                                                   ███
███                                                   ███
███                   {YELLOW}MENÚ DE AYUDA{RESET}                   ███
███                                                   ███
███             WASD o FLECHAS : Moverte              ███
███                Q : Salir del juego                ███
███              E:  Menú de estadísticas             ███
███               H: Muestra este menú                ███
███                                                   ███
███                                                   ███
███            {YELLOW}(Para salir presiona ENTER){RESET}            ███
███                                                   ███
███                                                   ███
█████████████████████████████████████████████████████████\
"""

WIN_SCREEN = f"""\
█████████████████████████████████████████████████████████
███                                                   ███
███                                                   ███
███                                                   ███
███                                                   ███
███                   {YELLOW}HAS GANADO{RESET}                      ███
███                                                   ███
███          Tus estadísticas han aumentado           ███
███          revisa el menú de Estadísticas           ███
███                                                   ███
███                {YELLOW}(presiona ENTER){RESET}                   ███
███                                                   ███
███                                                   ███
███                                                   ███
█████████████████████████████████████████████████████████\
"""

LOSE_SCREEN = F"""\
█████████████████████████████████████████████████████████
███                                                   ███
███                                                   ███
███                                                   ███
███                                                   ███
███                                                   ███
███                   {RED}HAS PERDIDO{RESET}                     ███
███                 {YELLOW}(presiona ENTER){RESET}                  ███
███                                                   ███
███                                                   ███
███                                                   ███
███                                                   ███
███                                                   ███
███                                                   ███
█████████████████████████████████████████████████████████\
"""

WINNER_SCREEN = f"""\
█████████████████████████████████████████████████████████
███{YELLOW}                  _______________                  {RESET}███
███{YELLOW}                 \@@@@|     |####/                 {RESET}███
███{YELLOW}                  \@@@|     |###/                  {RESET}███
███{YELLOW}                   `@@|_____|##'                   {RESET}███
███{YELLOW}                        (O)                        {RESET}███
███{YELLOW}                     .-'''''-.                     {RESET}███
███{YELLOW}                   .'  * * *  `.                   {RESET}███
███{YELLOW}                  :  *       *  :                  {RESET}███
███{YELLOW}                 : ~  CAMPEÓN  ~ :                 {RESET}███
███{YELLOW}                 : ~  POKEMÓN  ~ :                 {RESET}███
███{YELLOW}                  :  *       *  :                  {RESET}███
███{YELLOW}                   `.  * * *  .'                   {RESET}███
███{YELLOW}                     `-.....-'                     {RESET}███
█████████████████████████████████████████████████████████\
"""


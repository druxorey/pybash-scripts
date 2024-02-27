# programa en el que habra puntos y al llegar a esos puntos son batallas pokemon
# paso1 crear constantes y datos a cargar en el programa asi como
# crear vida y distintos ataques de los personajes
# paso2 cargar el mapa y hacer el mapa
# paso3 crear los puntos aleatorios en el mapa se me ocurre un modo facil uno normal y uno dificil
# pao4 meter las peleas

import random
import readchar
import os

# para saber que tipo de juego
game_tipe = None
while game_tipe != "1" and game_tipe != "2" and game_tipe != "3":
    game_tipe = input("¿Que tipo de juego deseas jugar? \n"
                      "Facil[1], Normal[2], Dificil[3]\n")

# paso 1
# creare una lista para almacenar las vidas de los personajes y los ataques de los mismos
# variables para la vida de los poke
vidas = [80, 90, 95]
vid_temp = 1
vid_temp1 = 1
grafic_vida = 0
grafic_vida1 = 0
pika = vidas[1]
vida_personajes = []  # darse cuenta que puedo crear N personajes si lo deseo...
numero_personajes = 0
if game_tipe == "1":
    numero_personajes = 2
elif game_tipe == "2":
    numero_personajes = 4
else:
    numero_personajes = 7
# aca se agrega la vida de los personajes
while numero_personajes > len(vida_personajes):
    vida_personajes.append(vidas[random.randint(0, 2)])
# nombre de los pokemon y ataques
pokemon = ["Pikachu", "Charmander", "Tortuga", "Raichu", "Gato", "Piedra", "Goku", "Yisus"]
ataques = [5, 8, 10, 16]
temp_atac = 0
string_atac = ""
# mapa
my_position = [1, 1]  # (x,y) empieza desde 0,0
pos_x = 0
pos_y = 1
barrera = """\
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x                               x
xxxxxx x xx x x x x  x  x x x  xx
x                               x
xxxxx x      x xxxxxxxx      xxxx
x                               x
xxxx xxxxx xxxxxx xxxxx xxxx xxxx
x                               x
xxx xx xxxx x  x x   x x x   x  x 
x                               x
xx x x xx xxx x xxxxxxxx x x xx x
x                               x
x x x xxx x xx x  x xx x x x x xx 
x                               x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\
"""
barrera = [list(row) for row in barrera.split("\n")]
map_width = len(barrera[0])  # ancho de mapa
map_height = len(barrera)  # largo

# aca se creara los elementos que se muestran en pantalla o los otros maestros pokemon
maestros = []
while (len(maestros)) < numero_personajes:
    new_pos = ([random.randint(0, (map_width - 1)), random.randint(0, (map_height - 1))])

    if new_pos not in maestros and new_pos != my_position and \
            barrera[new_pos[pos_y]][new_pos[pos_x]] != "x":
        maestros.append(new_pos)
num_poke = 0  # va diciendo que pokemon ataca
# lineas para el movimiento del personaje (paso 3 y 4)
while True:  # creo que es mas conveniente si lo pongo con un hasta qe maestros sea 0
    os.system("clear")
    print("[W(arriba) S(abajo) A(izquierda) D(derecha)] \n"
          "X[para salir]")
    print(maestros)  # muesta la ubi de los maestros pokemon
    print("+" + "-" * (map_width * 3) + "+")  # parte de arriba (techo)
    for coordinate_y in range(map_height):  # va creando laa filas
        print("|", end="")  # los inicios de linea
        for coordinate_x in range(map_width):  # lo de adentro de las lineas
            char_to_draw = " "  # este valor de un espacio toma la variable char mas abajo se entiende mejor
            objet_in_cell = None  # objetos en la celda
            for map_objet in maestros:  # objeto en el mapa en maestros en el mapa
                if map_objet[pos_x] == coordinate_x and map_objet[pos_y] == coordinate_y:  # si estan en el mismo lugar
                    char_to_draw = "◙"  # pondra un asterisco cuado este detecte un maestro del mapa
                    objet_in_cell = map_objet  # si estan en el mismo luigar objet in cell toma la posision de los objetos en el mapa
            """▣ ▃ ☱ ▓ ◍ ▞ ⊗ ◙ ◀ ▪ ♡
        aca se va a paralizar y empezara el combate no se como hacer un pokemon con
        simbolos del sistema pero algo se me ocurrira
            """
            # paso4 creando las batallas

            if my_position[pos_x] == coordinate_x and \
                    my_position[pos_y] == coordinate_y:  # mi posision "o"
                char_to_draw = "◀"  # caracter de la cara
                if objet_in_cell:  # si objeto de celda es igual a my position entonces removera el objeto [a,b]

                    # aki tiene que ir el paso 4
                    vid_temp = pika
                    vid_temp1 = vida_personajes[num_poke]  # empieza desde cero
                    input("Entrando al campo de batalla... \n "
                          "[presiona enter para continuar]")
                    while True:
                        os.system("clear")  # borra la pantalla anterior
                        # aca abajo se ven las graficas de las vidas bueno la operacion para que se muestren
                        grafic_vida = int((vid_temp / pika) * 20)
                        grafic_vida1 = int((vid_temp1 / vida_personajes[num_poke]) * 20)
                        # pokemon pika 0, charmander 1, tortuga 2, raichu 3, gato 4, piedra 5, goku 6, yisus 7
                        print(pokemon[0] + " vs " + pokemon[num_poke + 1])
                        print("Vida " + pokemon[0] + " ({})".format(vid_temp))
                        print("♡" * grafic_vida)
                        print("Vida " + pokemon[num_poke + 1] + " ({})".format(vid_temp1))
                        print("♡" * grafic_vida1)
                        if game_tipe == "1":
                            temp_atac = ataques[random.randint(0, 1)]
                        elif game_tipe == "2":
                            temp_atac = ataques[random.randint(0, 2)]
                        else:
                            temp_atac = ataques[random.randint(2, 3)]
                        vid_temp -= temp_atac
                        if temp_atac == ataques[0]:
                            string_atac = "puñetazo"
                        elif temp_atac == ataques[1]:
                            string_atac = "patada"
                        elif temp_atac == ataques[2]:
                            string_atac = "pistola"
                        else:
                            string_atac = "bombaaa"
                        print(pokemon[num_poke + 1] + " ataco con " + string_atac)
                        temp_atac = 0
                        while string_atac not in ["4", "3", "2", "1", "F", "f"]:
                            string_atac = input("Elige un ataque:\n"
                                                "[1] [2] [3] [4] \n"
                                                "[F] (pasar turno)")
                        if string_atac == "1":
                            temp_atac = ataques[0]
                        elif string_atac == "2":
                            temp_atac = ataques[1]
                        elif string_atac == "3":
                            temp_atac = ataques[2]
                        elif string_atac == "4":
                            temp_atac = ataques[3]
                        else:
                            pass
                        vid_temp1 -= temp_atac
                        if temp_atac == ataques[0]:
                            string_atac = "puñetazo"
                        elif temp_atac == ataques[1]:
                            string_atac = "patada"
                        elif temp_atac == ataques[2]:
                            string_atac = "pistola"
                        elif temp_atac == 0:
                            string_atac = ", ¡nada! Pasaste turno."
                        else:
                            string_atac = "bombaaa"
                        print(pokemon[0] + " ataco con " + string_atac)
                        input("Presiona enter para continuar")
                        #aca vera como van de vida y decedira si saldra del ciclo
                        #vid_temp es la vida del pikachu o de mi jugador
                        if vid_temp <= 0 or vid_temp1 <= 0:
                            break
                    if vid_temp1 <= 0 and num_poke == (numero_personajes - 1):
                        os.system("clear")
                        input("¡Felicidades! siempre supe que lo lograrias. \n"
                              "¡Eres el/la mejor! \n"
                              "Presiona enter para salir mi ¡Crack!")
                        break
                    elif vid_temp1 <= 0:

                        input("¡Felicidades sigue asi! ¡Ya falta poco! \n"
                              "[Presiona enter para continuar]")
                        os.system("clear")
                        vid_temp1 = 6
                        vid_temp = 6

                    elif vid_temp <= 0:
                        os.system("clear")
                        input("¡Rayos! Hemos Perdido \n"
                              "Espero la proxima tengas mas suerte..."
                              "[Presiona enter para continuar]")
                        break

                    maestros.remove(objet_in_cell)

                    num_poke += 1

            # los obsraculos en el mapa o las barreras

            if barrera[coordinate_y][coordinate_x] == "x":
                char_to_draw = "☱"
            print(" {} ".format(char_to_draw), end="")  # sabe que caracter poner
        print("|")
    print("+" + "-" * (map_width * 3) + "+")  # final de linea

    """por si alguien esta leyendo mi codigo tuve problemas para salir del
    while por eso repeti esta linea de codigo otra vez"""
    if vid_temp1 <= 0 and num_poke == (numero_personajes - 1):
        os.system("clear")
        break

    elif vid_temp <= 0:
        os.system("clear")
        break

    direction = readchar.readchar()  # devuelve bytes .decode convierte

    new_pos = None

    # aka vas menso asi no te confundes
    if direction in ["W", "w"]:
        new_pos = [my_position[pos_x], (my_position[pos_y] - 1)]
    elif direction in ["s", "S"]:
        new_pos = [my_position[pos_x], (my_position[pos_y] + 1)]
    elif direction in ["a", "A"]:
        new_pos = [(my_position[pos_x] - 1), (my_position[pos_y])]
    elif direction in ["D", "d"]:
        new_pos = [(my_position[pos_x] + 1), (my_position[pos_y])]
    elif direction in ["X", "x"]:
        break
    else:
        pass
    if new_pos:
        if barrera[new_pos[pos_y]][new_pos[pos_x]] != "x":
            my_position = new_pos

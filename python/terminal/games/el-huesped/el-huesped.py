from colorama import Fore, Style
from datetime import datetime
import random

# Color variables

character = (Fore.YELLOW)
danger = (Fore.RED)
reset = (Style.RESET_ALL)
decision = (Fore.BLUE)
success = (Fore.GREEN)

# Initial variables

name = "Jugador"
initial_object = "None"
master_key = False
game_continue = False

# Game

name = str(input("\nAntes de empezar, ¿Cómo te llamas?: "))
name = (character + name + reset)

print(f"""\n Te despiertas en una nave espacial abandonada. Estás en la sala de control, donde hay varios paneles dañados y pantallas rotas. Hay sangre y escombros por todas partes. Te duele la cabeza y tienes un corte profundo en el brazo. No sabes qué ha pasado ni dónde están los demás. Lo único que escuchas es un zumbido constante y un pitido ocasional.

Te levantas con dificultad y buscas algo que te sirva de ayuda. Ves dos objetos que podrían ser útiles: una linterna y una pistola. Sin embargo con el brazo en ese estado sólo podrías llevar uno de los dos. ¿Qué eliges?
      
      1) La linterna
      2) La pistola""")

first_decision = int(input(f"\n{decision}¿Cuál de los dos decides llevar contigo? [1 o 2]: {reset}"))

if first_decision == 1:
    initial_object = "linterna"
    print(f"""\n Eliges la linterna, la luz te permite ver mejor el estado de la nave. También te hace sentir más seguro, aunque sabes que podría atraer la atención de algo o alguien. La recoges del suelo, la limpias y sigues caminando decides salir de la sala de control.""")

elif first_decision == 2:
    initial_object = "pistola"
    print(f"""\n  Eliges la pistola. La recoges y la compruebas. Tiene seis balas en el cargador. No sabes si habrá más munición en la nave, así que decides ahorrarlas. Cargas una bala en la recámara y decides salir de la sala de control.""")

print(f"""\n Mientras caminas ves que todo está destruido, pareciera como si algo hubiera destrozado el metal a golpes, ves también rastros de sangre, era una escena terrorífica, habían chispas y cables rotos por todos lados por lo que intentas tener cuidado ya que podrías electrocutate muy fácilmente si no prestas atención. Mientras avanzas por el pasillo ves un pequeño rio de sangre que llama tu atención, viene desde un lado de la nave opuesto a dónde se encontraban las cápsulas de escape.""")

second_decision = int(input(f"\n{decision}¿Decides seguir el rastro de sangre [1] o continúas tu camino [2]?: {reset}"))

if second_decision == 1:
    master_key = True
    print(f"""\n Sigues el rastro de sangre sólo para encontrar a uno de tus compañeros muerto en el suelo, se veía como si se estuviera arrastrando hacia las cápsulas de escape, le falta una pierna, pero te parece curioso que la herida pareciera ser una mordida, aunque puede se que fuera mala suerte nada más, lo revisas para ver si tiene algo útil y consigues una llave de acceso de alguna parte, podría ser útil así que la recoges y la guardas en el bolsillo de tu camisa.""")

if initial_object == "pistola":

    print(f"""\n Sigues caminando por el pasillo hacia la sala de cápsulas de escape. Sabes que es tu única esperanza de salir de esta nave maldita. Sin embargo, el camino directo está oscuro y es peligroso. Ves cables de electricidad sueltos que chispean y amenazan con electrocutarte. No sabes si podrás pasar sin tocarlos. Sin embargo, hay otro pasillo que es más largo pero sirve para rodear este otro. Está iluminado y parece más seguro, pero también te hará perder tiempo. No sabes qué hacer. ¿Qué eliges?""")

    third_decision = int(input(f"\n{decision}¿Decides ir por el pasillo oscuro [1] o continúas por el pasillo con luz [2]?: {reset}"))

    if third_decision == 2:

        print("\n Decides ir por el pasillo con luz y escuchas un sonido a lo lejos. Es el alien que te persigue. Corres hacia la sala de cápsulas de escape, pero el alien se acerca rápidamente. Tienes dos opciones: o le disparas o no le disparas. Si le disparas, quizás puedas detenerlo o al menos retrasarlo. Si no le disparas, quizás puedas averiguar que quiere. No sabes qué hacer. ¿Qué eliges?")

        fourth_decision = int(input(f"\n{decision}¿Decides dispararle [1] o prefieres intentar una comunicación pacífica [2]?: {reset}"))

        if fourth_decision == 1:
            print(f"\n Le disparas al alien con la pistola que recogiste antes. Esperas que las balas lo hieran o lo maten. Sin embargo, no le afectan. El alien tiene una piel muy dura que resiste las balas. Se molesta y se enfurece. Te lanza un rugido y te salta encima..")
            print(f"{danger}\n Te atrapa y te muerde el cuello. Te desangras.... HAS MUERTO{reset}")
            exit()
        elif fourth_decision == 2: 
            print(f"\n No le disparas al alien con la pistola que recogiste antes. Piensas que quizás puedas razonar con él o al menos no provocarlo. El alien se detiene y te mira. Parece sorprendido por tu actitud. Luego, te habla con una voz telepática. Te explica que él y su especie vinieron a la Tierra en busca de un contacto pacífico. Te explica que los demás miembros de la tripulación los atacaron y que él se defendió. Te explica que tú eres el único que puede entenderlo, porque tienes una conexión especial con él. Te pide que lo acompañes a su planeta, donde podrán vivir en armonía. Te dice que es tu destino."

            "\nTe quedas pensando en lo que te dice el alien. Te das cuenta de que ha habido un malentendido entre las dos especies. Te sientes culpable por lo que han hecho tus compañeros. Te sientes curioso por conocer el planeta del alien. Decides aceptar su propuesta y confiar en él. El alien se alegra y te abraza. Te lleva a su nave, que está oculta en la otra parte de la nave espacial. Te subes a la nave y despegas. El alien te dice que te llevará a su mundo, donde serás bienvenido. Te dice que juntos podrán crear una alianza entre las dos especies. Te dice que todo será mejor.")

            print(f"{success}\n Has llegado a el mejor final bueno del juego. Has sobrevivido por no disparar al alien. Has logrado volver al planeta del alien y descubrir la verdad. ¡Felicidades, has ganado el juego!{reset}")

    elif third_decision == 1:
        possibility_to_die = random.randint(1,2)
        if possibility_to_die == 1:

            print(f"""\n Te arriesgas y eliges el camino directo, oscuro y peligroso. Corres por el pasillo, esquivando los cables de electricidad. Esperas llegar a la sala de cápsulas de escape antes de que sea demasiado tarde. Sin embargo, no lo logras. Uno de los cables te roza el brazo y te electrocuta. Sientes un dolor agudo y caes al suelo. La pistola se te cae de la mano y se dispara. Una bala te atraviesa el pecho.""")

            print(f"{danger}\n Te quedas sin aire y sin vida.... HAS MUERTO{reset}")
            exit()

        else:
            print(f"""\n Te arriesgas y eliges el camino directo, oscuro y peligroso. Corres por el pasillo, esquivando los cables de electricidad. Esperas llegar a la sala de cápsulas de escape antes de que sea demasiado tarde. Por suerte, lo logras.""")
            game_continue = True

elif initial_object == "linterna":
    print(f"""\n Sigues caminando por el pasillo hacia la sala de cápsulas de escape. Sabes que es tu única esperanza de salir de esta nave maldita. Sin embargo, el camino directo está oscuro y es peligroso. Ves cables de electricidad sueltos que chispean y amenazan con electrocutar. Te arriesgas y corres por el pasillo, iluminando el camino con la linterna que recogiste antes. Gracias a la luz, puedes ver los cables de electricidad y evitarlos. Esperas llegar a la sala de cápsulas de escape antes de que sea demasiado tarde. Por suerte, lo logras. Llegas a la sala y ves a través de la ventanilla varias cápsulas de escape intactas.""")
    game_continue = True

if game_continue == True:
    if master_key == True:
        print(f"""\n Llegas a la puerta que conduce a la sala de cápsulas de escape. Está cerrada con un sistema de seguridad. Afortunadamente, tienes la llave de acceso que obtuviste de tu compañero muerto. La insertas en la ranura y la giras. La puerta se abre y entras en la sala. Ves varias cápsulas de escape, y encuentras la que tiene el nombre {name}. Te metes en ella y la activas. La cápsula se desprende de la nave y se dirige hacia la Tierra.""")
        
        print(f"{success}\n Has llegado al final del juego. Has sobrevivido gracias a la llave de acceso. Has logrado volver a la Tierra. ¡Felicidades, has ganado el juego!{reset}")

    elif master_key == False:
        mission_start_date = random.randint(2400,3600)
        mission_actual_date = mission_start_date + 5
        print(f"""\n Llegas a la puerta que conduce a la sala de cápsulas de escape. Está cerrada con un sistema de seguridad. Desafortunadamente, no tienes la llave de acceso. Sin embargo, hay otro método para abrir la puerta. Tienes que poner tu huella dactilar y resolver una operación aritmética sencilla. Te aparece en una pantalla la siguiente pregunta: Si esta nave partió en el año {mission_start_date}, y han pasado ya 5 años desde que empezó la misión, ¿En que año estamos?""")

        mission_answer = int(input(f"\n{decision}Ingresa el año en el que estamos: {reset}"))

        if mission_answer == mission_actual_date:
            print(f"\n La puerta se abre y entras en la sala. Ves varias cápsulas de escape, y encuentras la que tiene el nombre {name}. Te metes en ella y la activas. La cápsula se desprende de la nave y se dirige hacia la Tierra.")

            print(f"{success}\n Has llegado al final del juego. Has sobrevivido gracias a que respondiste correctamente. Has logrado volver a la Tierra. ¡Felicidades, has ganado el juego!{reset}")
        else:
            print("\n Has fallado. No has podido resolver la operación aritmética. La puerta no se abre y la pantalla te muestra una cuenta atrás de 30 segundos. Sabes que es el tiempo que te queda de vida. Escuchas un sonido a lo lejos. Es el alien que te persigue. Te ha encontrado y viene a por ti. No tienes escapatoria.")

            print(f"{danger}\n El alien te atrapa.... HAS MUERTO{reset}")
            exit()
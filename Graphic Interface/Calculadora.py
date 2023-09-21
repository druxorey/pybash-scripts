from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title("Calculadora")
root.iconbitmap("folder-apps.ico")
root.geometry('300x520')
root.config(bg='#FF0')

# Estilo del Frame

style = ttk.Style()
style.configure('mainFrame.TFrame', background="#F00")
style.theme_use('clam')

# Estilos de los Labels

style_label_1 = ttk.Style()
style_label_1.configure('label_1.TLabel', font='arial 20', anchor='e', background='#0F0')

style_label_2 = ttk.Style()
style_label_2.configure('label_2.TLabel', font='arial 40', anchor='e', background='#F00')

# Estilos de los Buttons

style_button = ttk.Style()
style_button.configure('button.TButton', font='arial 15', background='#00F', width=5, relief='flat')

# Calculadora

mainFrame = ttk.Frame(root, style="mainFrame.TFrame")
mainFrame.grid(column=0, row=0)

entry_1 = StringVar()
label_entry_1 = ttk.Label(mainFrame, textvariable=entry_1, style='label_1.TLabel')
label_entry_1.grid(column=0, row=0, columnspan=4, sticky=(W,E))

entry_2 = StringVar()
label_entry_2 = ttk.Label(mainFrame, textvariable=entry_2, style='label_2.TLabel')
label_entry_2.grid(column=0, row=1, columnspan=4, sticky=(W,E))

button0 = ttk.Button(mainFrame, text="0", style='button.TButton')
button1 = ttk.Button(mainFrame, text="1", style='button.TButton')
button2 = ttk.Button(mainFrame, text="2", style='button.TButton')
button3 = ttk.Button(mainFrame, text="3", style='button.TButton')
button4 = ttk.Button(mainFrame, text="4", style='button.TButton')
button5 = ttk.Button(mainFrame, text="5", style='button.TButton')
button6 = ttk.Button(mainFrame, text="6", style='button.TButton')
button7 = ttk.Button(mainFrame, text="7", style='button.TButton')
button8 = ttk.Button(mainFrame, text="8", style='button.TButton')
button9 = ttk.Button(mainFrame, text="9", style='button.TButton')

button_borrar = ttk.Button(mainFrame, text=chr(9003), style='button.TButton')
button_borrar_todo = ttk.Button(mainFrame, text="C", style='button.TButton')
button_parentesis1 = ttk.Button(mainFrame, text="(", style='button.TButton')
button_parentesis2 = ttk.Button(mainFrame, text=")", style='button.TButton')
button_punto = ttk.Button(mainFrame, text=".", style='button.TButton')

button_division = ttk.Button(mainFrame, text=chr(247), style='button.TButton')
button_multipicacion = ttk.Button(mainFrame, text="x", style='button.TButton')
button_resta = ttk.Button(mainFrame, text="-", style='button.TButton')
button_suma = ttk.Button(mainFrame, text="+", style='button.TButton')

button_igual = ttk.Button(mainFrame, text="=",  style='button.TButton')
button_raiz = ttk.Button(mainFrame, text="√", style='button.TButton')

# Botones en pantalla

button_parentesis1.grid(column=0, row=2)
button_parentesis2.grid(column=1, row=2)
button_borrar_todo.grid(column=2, row=2)
button_borrar.grid(column=3, row=2)

button7.grid(column=0, row=3)
button8.grid(column=1, row=3)
button9.grid(column=2, row=3)
button_division.grid(column=3, row=3)

button4.grid(column=0, row=4)
button5.grid(column=1, row=4)
button6.grid(column=2, row=4)
button_multipicacion.grid(column=3, row=4)

button1.grid(column=0, row=5)
button2.grid(column=1, row=5)
button3.grid(column=2, row=5)
button_suma.grid(column=3, row=5)

button0.grid(column=0, row=6, columnspan=2, sticky=(W, E))
button_punto.grid(column=2, row=6)
button_resta.grid(column=3, row=6)

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, E))
button_raiz.grid(column=3, row=7)

for child in mainFrame.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

mainFrame.pack()


root.mainloop()



# dividendo = input("Ingrese el dividendo: ")
# divisor = input("Ingrese el divisor: ")

# if dividendo == "Messi" and divisor == "Dios":
#     print("Efectivamente, Messi es el mejor del mundo")
# if divisor == "0":
#     print("El divisor no puede ser 0")
# else:
#     try:
#         dividendo = float(dividendo)
#         divisor = float(divisor)
#         cociente = dividendo // divisor
#         residuo = dividendo % divisor

#         print(
#             f"El cociente de dividir {dividendo} entre {divisor} es: ", cociente)
#         print(
#             f"El residuo de dividir {dividendo} entre {divisor} es: ", residuo)

#     except:
#         print("Hubo un error, intente nuevamente")

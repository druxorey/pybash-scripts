from tkinter import *
from tkinter import ttk
import math

def ValueInput(key):
    if key >= '0' and key <='9' or key=='(' or key==')' or key=='.':
        entry_2.set(entry_2.get() + key)

    if key == '*' or key == '/' or key == '+' or key == '-':
        if key ==  '*':
            entry_1.set(entry_2.get() + '*')
        elif key ==  '/':
            entry_1.set(entry_2.get() + '/')
        elif key ==  '+':
            entry_1.set(entry_2.get() + '+')
        elif key ==  '-':
            entry_1.set(entry_2.get() + '-')

        entry_2.set('')

# Root Window

root = Tk()
root.title("Calculadora")
root.config(bg='#282a36')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Frame Style

style = ttk.Style()
style.theme_use('clam')
style.configure('mainFrame.TFrame', background="#282a36")

# Labels Style

style_label_1 = ttk.Style()
style_label_1.configure('label_1.TLabel', font='arial 20', anchor='e', background='#282a36', foreground='#f8f8f2')

style_label_2 = ttk.Style()
style_label_2.configure('label_2.TLabel', font='arial 40', anchor='e', background='#282a36', foreground='#f8f8f2')

# Buttons Style

style_button = ttk.Style()
style_button.configure('button.TButton', font='arial 15', background='#44475a', foreground='#f8f8f2', width=5, relief="flat")
style_button.map('button.TButton', background=[('active','#606580')], foreground=[('active','#f8f8f2')])

# Grid Configure

mainFrame = ttk.Frame(root, style="mainFrame.TFrame")
mainFrame.grid(column=0, row=0, sticky=(W, N, E, S))

mainFrame.columnconfigure(0, weight=1)
mainFrame.columnconfigure(1, weight=1)
mainFrame.columnconfigure(2, weight=1)
mainFrame.columnconfigure(3, weight=1)

mainFrame.rowconfigure(0, weight=1)
mainFrame.rowconfigure(1, weight=1)
mainFrame.rowconfigure(2, weight=1)
mainFrame.rowconfigure(3, weight=1)
mainFrame.rowconfigure(4, weight=1)
mainFrame.rowconfigure(5, weight=1)
mainFrame.rowconfigure(6, weight=1)
mainFrame.rowconfigure(7, weight=1)

entry_1 = StringVar()
label_entry_1 = ttk.Label(mainFrame, textvariable=entry_1, style='label_1.TLabel')
label_entry_1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

entry_2 = StringVar()
label_entry_2 = ttk.Label(mainFrame, textvariable=entry_2, style='label_2.TLabel')
label_entry_2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))

button0 = ttk.Button(mainFrame, text="0", style='button.TButton', command=lambda: ValueInput('0'))
button1 = ttk.Button(mainFrame, text="1", style='button.TButton', command=lambda: ValueInput('1'))
button2 = ttk.Button(mainFrame, text="2", style='button.TButton', command=lambda: ValueInput('2'))
button3 = ttk.Button(mainFrame, text="3", style='button.TButton', command=lambda: ValueInput('3'))
button4 = ttk.Button(mainFrame, text="4", style='button.TButton', command=lambda: ValueInput('4'))
button5 = ttk.Button(mainFrame, text="5", style='button.TButton', command=lambda: ValueInput('5'))
button6 = ttk.Button(mainFrame, text="6", style='button.TButton', command=lambda: ValueInput('6'))
button7 = ttk.Button(mainFrame, text="7", style='button.TButton', command=lambda: ValueInput('7'))
button8 = ttk.Button(mainFrame, text="8", style='button.TButton', command=lambda: ValueInput('8'))
button9 = ttk.Button(mainFrame, text="9", style='button.TButton', command=lambda: ValueInput('9'))

button_delete = ttk.Button(mainFrame, text=chr(9003), style='button.TButton')
button_delete_todo = ttk.Button(mainFrame, text="C", style='button.TButton')
button_parenthesis_1 = ttk.Button(mainFrame, text="(", style='button.TButton', command=lambda: ValueInput('('))
button_parenthesis_2 = ttk.Button(mainFrame, text=")", style='button.TButton', command=lambda: ValueInput(')'))
button_point = ttk.Button(mainFrame, text=".", style='button.TButton', command=lambda: ValueInput('.'))

button_divide = ttk.Button(mainFrame, text=chr(247), style='button.TButton', command=lambda: ValueInput('/'))
button_multiplication = ttk.Button(mainFrame, text="x", style='button.TButton', command=lambda: ValueInput('*'))
button_subtraction = ttk.Button(mainFrame, text="-", style='button.TButton', command=lambda: ValueInput('-'))
button_addition = ttk.Button(mainFrame, text="+", style='button.TButton', command=lambda: ValueInput('+'))

button_equal = ttk.Button(mainFrame, text="=",  style='button.TButton')
button_square_root = ttk.Button(mainFrame, text="√", style='button.TButton')

# Buttons on Screen

button_parenthesis_1.grid(column=0, row=2, sticky=(W, N, E, S))
button_parenthesis_2.grid(column=1, row=2, sticky=(W, N, E, S))
button_delete_todo.grid(column=2, row=2, sticky=(W, N, E, S))
button_delete.grid(column=3, row=2, sticky=(W, N, E, S))

button7.grid(column=0, row=3, sticky=(W, N, E, S))
button8.grid(column=1, row=3, sticky=(W, N, E, S))
button9.grid(column=2, row=3, sticky=(W, N, E, S))
button_divide.grid(column=3, row=3, sticky=(W, N, E, S))

button4.grid(column=0, row=4, sticky=(W, N, E, S))
button5.grid(column=1, row=4, sticky=(W, N, E, S))
button6.grid(column=2, row=4, sticky=(W, N, E, S))
button_multiplication.grid(column=3, row=4, sticky=(W, N, E, S))

button1.grid(column=0, row=5, sticky=(W, N, E, S))
button2.grid(column=1, row=5, sticky=(W, N, E, S))
button3.grid(column=2, row=5, sticky=(W, N, E, S))
button_addition.grid(column=3, row=5, sticky=(W, N, E, S))

button0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
button_point.grid(column=2, row=6, sticky=(W, N, E, S))
button_subtraction.grid(column=3, row=6, sticky=(W, N, E, S))

button_equal.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S))
button_square_root.grid(column=3, row=7, sticky=(W, N, E, S))

for child in mainFrame.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.mainloop()

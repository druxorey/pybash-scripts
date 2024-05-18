QUIT = "EXIT"
LISTING = "LIST"
DEFAULT_LIST = ["pollo", "pan", "pipas"]

def ask_user():
    return input("Introduce el producto: ")

def separate_list(shopping_list):
    return "\n".join(shopping_list)

def save_list(shopping_list):
    name = input("Como quieres que se llame el archivo?: ")
    with open(name + ".txt", "w") as save_file:
        save_file.write(separate_list(shopping_list))


def main():

    shopping_list = []

    print("{}: para salir, {}: para listar".format(QUIT, LISTING))

    item = ask_user()
    while item != QUIT:
        if item == LISTING:
            print(separate_list(shopping_list))
            item = ask_user()
        elif item.lower() not in DEFAULT_LIST:
            print("Su elemento no se encuentra en la lista")
            item = ask_user()
        else:
            shopping_list.append(item)
            item = ask_user()
    print("Se ha guardado la lista")
    save_list(shopping_list)    

if __name__ == "__main__":
    main()

QUIT = "Q"

def ask_user():
    return input("Introduce el producto: [{} para salir] ".format(QUIT))

def main():
    shopping_list = []
    item = ask_user()
    while item != "Q":
        shopping_list.append(item)
        print("\n".join(shopping_list))
        item = ask_user()

if __name__ == "__main__":
    main()

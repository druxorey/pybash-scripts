def main():

    def saludo_sectario(nombre):
        print("Hola {}".format(nombre[::-1]))

    def largo_string(mi_string):
        largo = 0
        for n in mi_string:
            largo += 1
        return largo


    saludo_sectario("Anuel")
    saludo_sectario("Felipe")
    saludo_sectario("Pablo")

    largo_input = input("Di algo: ")
    print(largo_string(largo_input))

if __name__ == "__main__":
    main()

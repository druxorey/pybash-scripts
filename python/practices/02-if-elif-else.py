print("""
    Welcome to the temperature unit converter, the options are as follows:

    1) Fahrenheit to Celsius
    2) Celsius to Fahrenheit
""")

option = int(input("Choose the option: "))

if option == 1:
    fahrenheit = float(input("Enter the temperature:"))
    celsius = (fahrenheit - 32) * 5/9
    print("The result of the operation is:", celsius)

elif option == 2:
    celsius = float(input("Enter the temperature: "))
    fahrenheit = (celsius * 9/5) + 32
    print("The result of the operation is:", fahrenheit)
else:
    print("There was an error, please try again")

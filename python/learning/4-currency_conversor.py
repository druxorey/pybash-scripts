usd_eur = 0.93
eur_ves = 39.05
usd_ves = 36.25

print("Welcome to the currency convertor.")
print("""
Qué moneda vas a convertir

1) Euro
2) Dólar
3) Bolívares
""")

first_option = int(input("Choose the option: "))

print("""
A qué moneda vas a convertir

1) Euro
2) Dólar
3) Bolívares
""")

second_option = int(input("Choose the option: "))

initial_conversion = float(input("¿Qué cantidad es la que vas a convertir?: "))

if first_option == second_option:
    print("There was an error, no puedes convertir a la misma moneda")

# Dolar Euro
elif first_option == 1 and second_option == 2:
    final_conversion = initial_conversion / usd_eur
    print(f"Tu conversión es: {final_conversion} $")
elif first_option == 2 and second_option == 1:
    final_conversion = initial_conversion * usd_eur
    print(f"Tu conversión es: {final_conversion} €")

# Dolar Bolívares
elif first_option == 2 and second_option == 3:
    final_conversion = initial_conversion * usd_ves
    print(f"Tu conversión es: {final_conversion} Bs")
elif first_option == 3 and second_option == 2:
    final_conversion = initial_conversion / usd_ves
    print(f"Tu conversión es: {final_conversion} $")

# Bolívares Euro
elif first_option == 1 and second_option == 3:
    final_conversion = initial_conversion * eur_ves
    print(f"Tu conversión es: {final_conversion} Bs")
elif first_option == 3 and second_option == 1:
    final_conversion = initial_conversion / eur_ves
    print(f"Tu conversión es: {final_conversion} €")

else:
    print("There was an error, please try again")

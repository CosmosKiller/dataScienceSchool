welcomeMsg = """
¡Hola! Bienvenido al conversor de unidades. 

Cuentanos..."""
menu = """¿Qué deseas convertir?

1 - Millas a kilómetros
2 - Kilómteros a millas

Elige una opción:
"""

milToKm = 1.609344
kmToMil = (1/1.609344)

def unitConversor(unitChoice, unitValue, exitUnit):
    unit = float(input("Ingrese el valor en " + unitChoice + " que desea convertir: "))
    value = unit * unitValue
    value = str(round(value, 2))
    print("El valor en " + unitChoice + " equivale a " + value + " " + exitUnit)
    

def main():
    print(welcomeMsg)
    option = 0
    while option != 1 and option != 2:
        option = int(input(menu))
        if option != 1 and option != 2:
            print("Has elegido una opción incorrecta (" + str(option) +"), por favor intentalo otra vez.")
    
    if option == 1:
        unitConversor("millas", milToKm, "kilómetros")
    else:
        unitConversor("kilómetros", kmToMil, "millas")



if __name__ == "__main__":
    main()
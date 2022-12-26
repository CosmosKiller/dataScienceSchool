welcomeMsg = """
¡Hola! Aquí te ayudaremos a calcular
el área de tu triangulo

Pero antes dinos..."""

menu = """
Tu triangulo:

1.-¿Tiene los 3 lados iguales?
2.-¿Tiene solo 2 lados iguales?
3.-¿Tiene los 3 lados distintos?

Elige una opción por favor: 
"""

def triangleArea():
    b = int(input("La base de tu triangulo es: "))
    h = int(input("La altura de tu triangulo es: "))

    area = str(((b*h))/2)

    return area
   

def main():
    print(welcomeMsg)
    option = 0
    while option != 1 and option != 2 and option != 3:
        menu
        option = int(input(menu))
        if option != 1 and option != 2 and option != 3:
            print("Has elegido una opción incorrecta (" + str(option) +"), por favor intentalo otra vez.")
    
    if option == 1:
        triangleType = "Equilatero"
        print("Tu triangulo es Equilatero")
    elif option == 2:
        triangleType = "Isoceles"
        print("Tu triangulo es Isoceles")
    else:
        triangleType = "Escaleno"
        print("Tu triangulo es Escaleno")
    
    print("Ahora completa los demas datos.")
    area = str(triangleArea())
    print("El área de tu triangulo " + triangleType + " es: " + area)

        

if __name__ == "__main__":
    main()
import math

welcomeMsg = """
¡Hola! Bienvenido al calculador de volúmen para superficies de revolución. 

Cuentanos..."""
menu = """¿De cuál superficie quiere conocer el volúmen?

1 - Esfera
2 - Cilindro recto
3 - Cono
4 - Cono truncado recto
5 - Toroide

Elige una opción:
"""

py = math.pi
r = 0
h = 0
r2 = 0

figureDictironary = {
    1 : "esfera",
    2 : "cilindro recto",
    3 : "cono",
    4 : "cono truncado recto",
    5 : "toroide"  
}

def volumeCalculator(figureChoice, figureName):
    r = int(input("Ingresa el valor del radio de tu " + figureName + ": "))
    if figureChoice == 1:
        volume = (4/3)*py*math.pow(r,3)
    elif figureChoice == 2:
        h = int(input("Ingresa el valor de la altura de tu " + figureName + ": "))
        volume = py*math.pow(r,2)*h
    elif figureChoice == 3:
        h = int(input("Ingresa el valor de la altura de tu " + figureName + ": "))
        volume = (1/3)*py*math.pow(r,2)*h
    elif figureChoice == 4:
        r2 = int(input("Ingresa el valor del radio Mayor altura de tu " + figureName + ": "))
        h = int(input("Ingresa el valor de la altura de tu " + figureName + ": "))
        volume = (1/3)*py*h*(math.pow(r,2)+math.pow(r2,2)+r*r2)
    else:
        r2 = int(input("Ingresa el valor del radio Mayor altura de tu " + figureName + ": "))
        volume = 2*math.pow(py,2)*r2*math.pow(r,2)

    volume = str(round(volume,4))
    print("El volúmen de tu " + figureName + " es: " + volume)
    

def main():
    print(welcomeMsg)
    option = 0
    while option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
        option = int(input(menu))
        if option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
            print("Has elegido una opción incorrecta (" + str(option) +"), por favor intentalo otra vez.")
    
    volumeCalculator(option, figureDictironary[option])



if __name__ == "__main__":
    main()
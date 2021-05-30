import random

def main():
    vidas = 3
    randNum = random.randint(1, 100)
    selNum = int(input("Ingresa un número del 1 al 100: "))
    while selNum != randNum:
        if selNum < randNum:
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")
        selNum = int(input("Ingresa otro número: "))
    print("Crack! Ganaste")
        


if __name__ == "__main__":
    main()
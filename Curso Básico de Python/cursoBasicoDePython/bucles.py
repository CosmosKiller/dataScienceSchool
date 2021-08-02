def main():
    LIMITE = int(input("¿Qué potencia de 2 desea calcular? "))
    contador = 0
    potencia = 2**contador
    while contador <= LIMITE:
        print("2 elevado a " + str(contador) + " es igual a " + str(potencia))
        contador = contador + 1
        potencia = 2**contador


if __name__ == "__main__":
    main()
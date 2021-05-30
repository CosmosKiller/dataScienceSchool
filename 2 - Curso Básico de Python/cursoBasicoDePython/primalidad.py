def esPrimo(numero):
    #contador = 0

    #for i in range(1, numero + 1):
    #    if i == 1 or i == numero:
    #        continue
    #    if numero % i == 0:
    #        contador += 1
    #if contador == 0:
    #    return True
    #else:
    #    return False

    #Teorema de Fermat: Si p es un número primo y a es un número entero positivo que no tiene factores comunes con p
    # (es decir, a y p son primos relativos), entonces el resto de la división de a^p-1 entre p es 1

    a = 2 
    fermat = (a**(numero-1)) % numero
    print(fermat)
    if fermat == 1:
        return True
    else:
        return False

def main():
    numero = int(input("Escribe un número: "))

    if numero == 1:
        print("No es primo")
    else:
        if esPrimo(numero):
            print("Es primo")
        else:
            print("No es primo")


if __name__ == "__main__":
    main()
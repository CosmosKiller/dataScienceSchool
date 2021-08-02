def esPalindromo(cadena):
    cadena = cadena.replace(" ","").lower()
    if cadena == cadena[::-1]:
        return True
    else:
        return False


def main():
    cadena = input("Escribe una palabra/frase: ")
    if esPalindromo(cadena) == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__== "__main__":
    main()
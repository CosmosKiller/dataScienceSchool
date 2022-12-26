def divisors(num):
    divisors = [ i for i in range(1, num + 1) if num % i == 0]
    
    return divisors


def main():
    while True:
        try:
            num = int(input("Ingresa un numero: "))
            if num < 0:
                raise TypeError("Solo se pueden ingresar numeros positivos")
            print(divisors(num))
            print("Programa finalizado")
            break
        except ValueError:
            print("Solo se pueden ingresar numeros")
        except TypeError as te:
            print(te)



if __name__ == '__main__':
    main()
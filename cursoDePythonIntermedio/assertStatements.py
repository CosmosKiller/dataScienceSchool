def divisors(num):
    divisors = [ i for i in range(1, num + 1) if num % i == 0]
    
    return divisors


def main():
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un número positivo"
    print(divisors(int(num)))
    print("Programa finalizado")



if __name__ == '__main__':
    main()
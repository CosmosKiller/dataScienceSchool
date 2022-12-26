def isPrime(number: int) -> bool:
    checkList = [i for i in range(2,number) if number % i == 0]
    return not checkList

def main():
    n = int(input("Ingresa un numeor entero: "))
    if isPrime(n):
        print(f"El numero {n}, es primo")
    else:
        print(f"El numero {n}, NO es primo")


if __name__ == "__main__":
    main()
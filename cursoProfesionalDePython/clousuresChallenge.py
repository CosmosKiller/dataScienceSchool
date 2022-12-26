def makeDivisionBy(n: int):
    def numerator(x: int) -> float:
        try:
            if type(n) != int or type(x) != int:
                raise ValueError("Solo puedes ingresar numeros enteros")
            return x/n
        except ValueError as ve:
            print(ve)
            return "Operación cancelada..."

    return numerator

def main():
    divisonBy3 = makeDivisionBy("A")
    print(divisonBy3(18))

    divisonBy5 = makeDivisionBy(5)
    print(divisonBy5(100))

    divisonBy18 = makeDivisionBy(18)
    print(divisonBy18(54))


if __name__ == "__main__":
    main()
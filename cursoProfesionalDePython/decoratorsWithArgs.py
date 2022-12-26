from random import randint

def customMessage(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{message} tu numero de la suerte es: ')
            func(*args, **kwargs)
        
        return wrapper

    return decorator



def main():
    name = str(input("¿Como te llamas? "))
    lucky_n = int(input("¿Cuantas caras tiene tu dado? "))

    @customMessage(name)
    def luckyNumber(n: int) -> int:
        print(randint(0, n))
    
    luckyNumber(lucky_n)

if __name__ == "__main__":
    main()
import random


def keyGenerator():
    mayus = ["A", "B", "C", "D", "E", "F", "G"]
    minus = ["a", "b", "c", "d", "e", "f", "g"]
    symbols = ["!", "#", "&", "/", "$", "(", ")", "?"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    characters = mayus + minus + symbols + numbers

    key = []

    for i in range(15):
        randChar = random.choice(characters)
        key.append(randChar)

    key = "".join(key)
    return key

def main():
    key = keyGenerator()
    print("Tu nueva contraseña es: " + key)


if __name__ == "__main__":
    main()
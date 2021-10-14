import os
import random

FORBIDDENCHARS = [" ", "", "!", "¡", "#", "&", "/", "$", "(", ")", "¿", "?", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

ASCIIART = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def wordSelector(filepath = '/home/nahirsamur/Dropbox/Platzi/DataScienceSchool/cursoDePythonIntermedio/testFiles/data.txt' ):
    with open(filepath, "r", encoding="UTF-8") as f: #File management
        words = [line for line in f] #Using list comprehensions
    randWord = random.choice(words).rstrip("\n")

    return randWord


def wordSeeker(word, myLetter, length):
    wordFound = False
    for index, character in enumerate(word):
        if character == myLetter:
            length[index] = myLetter
            wordFound = True

    return wordFound


def exitGame():
    while True:
        try:
            game_over = input("Presiona 'R' para reiniciar o 'E' para salir:\n").upper()
            if game_over == "E":
                break
            elif game_over == "R":
                #os.system("python3 hangmanGame.py") check functionallity
                pass
            else:
                raise TypeError("Por favor, seleccione una opción correcta")
        except TypeError as te:
            print(te)



def main():
    randWord = wordSelector()
    wordLength = ["_"] * len(randWord)
    tries = 0
    lives = 6

    while True:
        os.system("clear")
        print(f"Vidas disponibles: {'❤' * (lives)}")
        print("-----------------------------------")
        for character in wordLength:
            print(character, end=" ")
        print(ASCIIART[tries])

        try: #Error handling
            letter = input("Elige una letra: ").lower()
            for forbChar in FORBIDDENCHARS:
                if forbChar == letter:
                    raise ValueError("Solo puedes ingresar letras.")

            found = wordSeeker(randWord, letter, wordLength)
            
            if found == False:
                tries += 1
                lives -= 1

            if "_" not in wordLength:
                os.system("clear")
                print("¡Felicidades ganaste!")
                exitGame()
                break
            elif tries == 6:
                os.system("clear")
                print("¡Oh no perdiste!")
                print(f"Tu palabra era '{randWord}'")
                exitGame()
                break
        except ValueError as ve:
            print(ve)
            print(input("<Presiona cualquier tecla para continuar>"))
        except KeyboardInterrupt:
            print("\n")
            try:
                ki = input ("¿Realmente deseas salir? [Y/N]a\n").upper()
                if ki == "Y":
                    break
                elif ki == "N":
                    continue
                else:
                    raise TypeError("Por favor, seleccione una opción correcta")
            except TypeError as te:
                print(te)   



if __name__ == "__main__":
    main()
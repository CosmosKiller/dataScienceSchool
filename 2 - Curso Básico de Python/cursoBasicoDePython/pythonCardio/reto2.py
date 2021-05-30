choice ="""Elige tu opción:

1.- Piedra
2.- Papel
3.- Tijeras
"""


def main():
    player1Score = 0
    player2Score = 0

    name1 = input("¡Hola jugador 1! Ingresa tu nombre: ")
    name2 = input("¡Hola jugador 2! Ingresa tu nombre: ")

    round = 0
    while round < 3:
        print("Es tu turno " + name1)
        player1Choice = int(input(choice))
        print("Es tu turno " + name2)
        player2Choice = int(input(choice))

        if (player1Choice == 3 and player2Choice == 2) or (player1Choice == 2 and player2Choice == 1) or (player1Choice == 1 and player2Choice == 3):
            player1Score = player1Score + 1
            round += 1
            print(name1 + " gana la ronda")
        elif player1Choice == player2Choice:
            print("Empate")
        else:
            player2Score = player2Score + 1
            round += 1
            print(name2 + " gana la ronda")
    
    if player1Score > player2Score:
        print(name1 + " gana la parida")
    else:
        print(name2 + " gana la partida")



if __name__ == '__main__':
    main()
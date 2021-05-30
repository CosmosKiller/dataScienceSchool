def changeingRanges(lowerLimitm, upperLimit, comp):
    if comp >= lowerLimitm and comp <= upperLimit:
        print("¡Excelente! El numero " + str(comp) + " está dentro de los limites.")
        isOkay = True
    else:
        print("Ups... El numero " + str(comp) + " está fuera de los limites. Por favor intentalo otra vez.")
        isOkay = False

    return isOkay


def main():
    print("¡Bienvenido!")
    lowLim = int(input("Ingresa un valor entero para tu limite inferior: "))
    upLim = int(input("Ingresa un valor entero para tu limite superior: "))
        
    exitFlag = False

    while exitFlag == False:
        value = int(input("Ingresa un valor entero para usar como comparación: "))
        exitFlag = changeingRanges(lowLim, upLim, value)



if __name__ == "__main__":
    main()
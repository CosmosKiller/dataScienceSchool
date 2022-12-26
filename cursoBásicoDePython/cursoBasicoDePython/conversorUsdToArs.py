ars = 0.011

monOriginal = input("Ingrese el monto que desea convertir: ")
monOriginal = float(monOriginal)

monConvertida = monOriginal / ars
monConvertida = round(monConvertida, 2)
monConvertida = str(monConvertida)

print("El monto equivale a " + monConvertida + " pesos")
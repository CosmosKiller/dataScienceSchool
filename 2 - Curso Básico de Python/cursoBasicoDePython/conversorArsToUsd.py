# Variables
menu = """
Bienvenido al conversor de monedas

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """
opcion = int(input(menu))
ars = 92.25
col = 3657.28
mex = 20.15

# Funciones
def conversor(tipoPeso, valorDolar):
    monOriginal = input("Ingrese el monto en Pesos " + tipoPeso + " que desea convertir: ")
    monOriginal = float(monOriginal)
    monConvertida = monOriginal / valorDolar
    monConvertida = round(monConvertida, 2)
    monConvertida = str(monConvertida)
    print("El monto equivale a " + monConvertida + " dólares")

# Código
if opcion == 1:
    conversor("Argentinos", ars)
elif opcion == 2:
    conversor("Colombianos", col)
elif opcion == 3:
    conversor("Mexicanos", mex)
else:
    print("Ingrese una opción correcta, por favor")

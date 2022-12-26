# def decorator(func):
#     def wrapper():
#         func()
#         print("aaaahh, pero aquí sucede la magia...")
    
#     return wrapper

# @decorator
# def gretting():
#     print("Con este sencillo mensaje, te saludo!")


# if __name__ == "__main__":
#     gretting()

def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    
    return envoltura

@mayusculas
def mensaje(nombre):
    return f"{nombre}, recibiste un mensaje"


if __name__ == "__main__":
     print(mensaje("Nahir"))
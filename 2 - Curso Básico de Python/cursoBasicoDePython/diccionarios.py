def main():
    miDiccionario = {
        "llave1" : 1,
        "llave2" : 2,
        "llave3" : 3
    }
    poblaciónPaises = {
	'Argentina': 44_938_712,
	'Brasil': 210_147_125,
	'Colombia': 50_372_424
    }
    for pais, poblacion in poblaciónPaises.items():
        print(pais +  " tiene " + str(poblacion) + " habitantes")


if __name__ == "__main__":
    main()
def main():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Nahir", "lastname": "Samur"}

    super_list = [
        {"firstname": "Nahir", "lastname": "Samur"},
        {"firstname": "Leandro", "lastname": "Alvarez"},
        {"firstname": "Gabriel", "lastname": "Itterman"},
        {"firstname": "Franco", "lastname": "Aquistapace"},
        {"firstname": "Manuel", "lastname": "Ferreyra"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    #for key, value in super_dict.items():
    #    print(key, "-", value)

    for values in super_list:
        for key, value in values.items():
            print(f'{key}: {value}')



if __name__ == '__main__':
    main()
def read():
    numbers = []
    with open("/home/nahirsamur/Dropbox/Platzi/DataScienceSchool/cursoDePythonIntermedio/testFiles/numbers.txt", "r", encoding="utf-8" ) as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Nahir", "Leandro", "Gabriel", "Franco", "Manuel"]
    with open("/home/nahirsamur/Dropbox/Platzi/DataScienceSchool/cursoDePythonIntermedio/testFiles/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def main():
    #read()
    write()


if __name__ == '__main__':
    main()
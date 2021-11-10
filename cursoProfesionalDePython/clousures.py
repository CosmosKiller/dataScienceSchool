def makeRepeaterOf(n: int):
    def repeater(string: str) -> str:
        assert type(string) == str, "Solo puedes usar cadenas"
        return string * n
    
    return repeater

def main():
    repeat5 = makeRepeaterOf(5)
    repeat4 = makeRepeaterOf(4)

    print(repeat5('Holis'))
    print(repeat4('Nahir'))


if __name__ == "__main__":
    main()
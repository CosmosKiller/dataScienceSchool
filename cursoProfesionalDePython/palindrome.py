def isPalindrome(string: str) -> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def main():
    word = str(input("Ingresa una palabra: "))
    if isPalindrome(word):
        print(f"{word}, es palindromo")
    else:
        print(f"{word}, NO es palindromo")

if __name__ == "__main__":
    main()
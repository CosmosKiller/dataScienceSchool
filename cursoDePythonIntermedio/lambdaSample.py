def main():
    test_word = input("Enter the word you want to test: ")
    palindrome = lambda string : string == string[::-1]

    print(palindrome(test_word))



if __name__ == '__main__':
    main()
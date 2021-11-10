def removeDuplicates(randomList):
    return list(set(randomList))

def main():
    my_list = [1, 1, 2, 2, 4]
    print(removeDuplicates(my_list))

if __name__=='__main__':
    main()
from filtering_challenge_data import DATA


def main():
    #Creating allPythonDevs and allPlatziWorkers lists with high order functions
    allPythonDevs = list(filter(lambda workers: workers['language'] == 'python', DATA))
    allPythonDevs = list(map(lambda workers: workers['name'], allPythonDevs))

    allPlatziWorkers = list(filter(lambda workers: workers['organization'] == 'Platzi', DATA))
    allPlatziWorkers = list(map(lambda workers: workers['name'], allPlatziWorkers))

    #Creating allAdults and oldPeople lists with list comprehensions
    allAdults = [workers['name'] for workers in DATA if workers['age'] >= 18]

    oldPeople = [workers | {'old': workers['age'] >= 70} for workers in DATA]


    for worker in oldPeople:
        print(worker)


if __name__ == '__main__':
    main()
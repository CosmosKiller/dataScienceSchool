from filtering_challenge_data import DATA

def main():
    allPythonDev = [worker['name'] for worker in DATA if worker['language'] == 'python']
    allPlatziWorkers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    allAdults = list(filter(lambda worker: worker['age'] >= 18, DATA))
    allAdults = list(map(lambda worker: worker['name'], allAdults))
    oldPeople = list(map(lambda worker: worker | {'old': worker['age'] >= 70}, DATA))


    for worker in allAdults:
        print(worker)


if __name__ == '__main__':
    main()
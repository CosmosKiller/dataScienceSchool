from time import sleep

def fibonacci(max=None):
    
    n0, n1, aux = 0, 1, 0
    
    while not max or  aux < max:
        yield n0
        n0, n1 = n1, n0 + n1
        aux += 1


if __name__=='__main__':
    myFibo = fibonacci(10)
    for i in myFibo:
        print(i)
        sleep(0.5)
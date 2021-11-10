# from EvenNumbers import EvenNumbers

# n = EvenNumbers(18)

# myIter = n.__iter__()


# while True: #ciclo infinito
#   try:
#     element = n.__next__()
#     print(element)
#   except StopIteration:
#     break

from time import sleep
from Fibonacci import Fibonacci

for i in Fibonacci(10):
    print(i)
    sleep(0.5)
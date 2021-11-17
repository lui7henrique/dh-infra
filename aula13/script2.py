# generate random integer values
from random import seed
from random import randint

# ------------------------------------------

list = open("numbers.txt")
numberLines = list.readlines()

# reset values
if(len(numberLines) > 0):
    print("Cleaning the old numbers")
    open('numbers.txt', 'w').close()

# ------------------------------------------

primes = open("primes.txt")
primesLines = primes.readlines()

# reset values
if(len(primesLines) > 0):
    print("primes file is not empty")
    open('primes.txt', 'w').close()

# ------------------------------------------

for i in range(500):
    value = randint(0, 500)
    list = open("numbers.txt", "a")
    list.write(str(value) + "\n")

# compair numbers of files
newList = open("numbers.txt").read().split()
primes = open("primes.txt", "a")

for number in newList:
    number = int(number)
    divisores = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            divisores = divisores + 1
            if divisores > 1:
                break

    if divisores > 1 or number == 1 or number == 0:
        print(f"{number} isn't prime")
    else:
        primes.write(f"{str(number)}  \n")

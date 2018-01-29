def getCubesList(listLength: int) -> int:
    cubesList = []
    for num in range(1, listLength + 1):
        cubesList = cubesList + [num ** 3]
    return cubesList


def fibSequence(amount: int):
    x, y = 0, 1
    for i in range(0, amount):
        print(y)
        x, y = y, x + y

def isPrimeRange (num1: int, num2: int):
    for num in range(num1, num2 + 1):
        for test in range(2, num):
            if num % test == 0:
                print(str(num) + " is not a prime number ")
                break
        else:
            print(str(num) + " is a prime number")

#isPrimeRange(5, 10)

def factorization (number: int) -> list:
    factors = []
    for factor in range(1, number // 2):
        if number % factor == 0:
            factors.append(str(factor) + "x" + str(number / factor))
            #factors.extend([str(factor) + "x" + str(number / factor)])
    return factors

print(factorization(100))

def dontWantToCode():
    pass #Allows for empty class for completetion later

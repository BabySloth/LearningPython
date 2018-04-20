def problem1():
	"""
	Multiples of 3 and 5
	"""

	sum = 0;
	for number in range(0, 1000):  # Loops number between 0 to 1000 to add multiples
		if number % 3 == 0 or number % 5 == 0:
			sum += number

	return sum


print("Question 1: " + str(problem1()))  # Solution:  233168


def problem2():
	fibSequence = [1, 2]  # First two fibonacci numbers
	idx = 1  # Start at 1 so we add the last term to the penultimate term

	# Only add another element if the element is less than 4 million
	while fibSequence[-1] + fibSequence[-2] < 4000000:
		fibSequence.append(fibSequence[idx] + fibSequence[idx - 1])
		idx += 1

	sum = 0
	# Add all the even numbers to the sum and return it
	for number in fibSequence:
		if number % 2 == 0:
			sum += number

	return sum


print("Question 2: " + str(problem2()))  # Solution: 4613732


def problem3():
	number = 600851475143  # Number the question gave us
	factor = 2  # Tracker of what factor up to
	while number != 1:
		if number % factor == 0:
			number /= factor
		else:
			factor += 1

	return factor


print("Problem 3: " + str(problem3()))

# Helper to problem 4 checking if number is equal to itself reversed
def is_palindromic(number):
	return str(number) == str(number)[::-1]

def problem4():
	largest = 1
	# a * b = palindromic
	for a in range(100, 999):
		for b in range(100, 999):
			if is_palindromic(a * b) and a * b > largest:
				largest = a * b
	return largest


print("Question 4: " + str(problem4()))


# Helper function for determining lcm
def gcf(a, b):
	# Using Euclidean Algorithm
	# Already coded this in class
	if b > a:
		# Make sure a is always the largest number
		return gcf(b, a)
	else:
		if b == 0:
			return a
		else:
			return gcf(b, a % b)


def lcm(a, b):
	# Formula for lcm:
	return (a * b) / gcf(a, b)


def problem5():
	# If numbers are divisible by this range, it will be divisible by 1 to 10 inclusive
	factors = list(range(11, 21))  # Length of 11
	lowestMultiple = 1

	# Effectively finding the lcm of numbers from 11 to 20 inclusive
	index = 0
	while index < len(factors):
		lowestMultiple = lcm(lowestMultiple, factors[index])
		index += 1

	return lowestMultiple


print("Problem 5: " + str(problem5()))  # Solution: 232792560


def problem6():
	# Sum of the squares
	sumSquares = 0
	for number in range(0, 101): # Include 100
		sumSquares += number ** 2

	# Square of the sum
	sumNumbers = 0
	for number in range(0, 101):
		sumNumbers += number
	squareSum = sumNumbers ** 2

	return squareSum - sumSquares


print("Question 6: " + str(problem6()))

def is_prime(number):
	for factor in range(2, int(number ** .5) + 1):
		if number % factor == 0:
			return False
	return True


def problem7():
	pastPrimeCounter = 0
	largestPrime = 1
	counter = 2  # First prime number is 2
	while pastPrimeCounter < 10001: # Want the 10001st prime number, so do less than 10000
		if is_prime(counter):
			pastPrimeCounter += 1
			largestPrime = counter
		counter += 1

	return counter - 1  # Compensate for the fact that counter adds one in the end

# print("q7: " + str(problem7())) # S: 104743

def problem8():
	#All in the same
	QUESTION = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

	index = 0
	largestProduct = 1
	while index < len(QUESTION) - 13:
		digits = QUESTION[index:index+13]
		product = 1
		if '0' not in digits:
			for number in digits:
				product *= int(number)
			if product > largestProduct:
				largestProduct = product
		index += 1
	return largestProduct


print("p8 " + str(problem8()))  # 23514624000


def problem9():
	# a**2 + b**2 == c**2
	a = 1
	for a in range(1, 501):
		for b in range(a + 1, 501):
			c = (a ** 2 + b ** 2) ** (.5)

			if a + b + c == 1000:
				return a * b * c


print("Problem 9: {}" + str(problem9()))  # Solution: 31875000


def problem10():
	sum = 0
	for number in range(2, 2000000):
		if is_prime(number):
			sum += number
	return sum


print("P10: " + str(problem10()))  #Solution: 142913828922

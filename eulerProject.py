def problem1():
	"""
	Multiples of 3 and 5
	"""
	listOfProducts = []  # Stores all numbers 
	for number in range(0, 1000):  # Loops number between 0 to 1000 to add multiples
		if number % 3 == 0 or number % 5 == 0:
			listOfProducts.append(number)
	
	# Add all the numbers in the listOfProducts
	sum = 0
	for number in listOfProducts:
		sum += number

	return sum

print("Question 1: {}".format(problem1()))  # Solution:  233168

def problem2():
	fibSequence = [1, 2] # First two fibonacci numbers
	idx = 1
	while fibSequence[-1] < 4000000:  # Create the fib numbers until one number is greater than 4,000,000
		fibSequence.append(fibSequence[idx] + fibSequence[idx - 1])
		idx += 1
	
	sum = 0  # Holds the sum of even numbers	
	for number in fibSequence:
		if number % 2 == 0:
			sum += number

	return sum

print("Question 2: {}".format(problem2()))  # Solution: 4613732

def problem3():
	NUMBER = 600851475143
	

def problem9():
	# a**2 + b**2 == c**2
	a = 1
	for a in range(1, 500):
		for b in range(a + 1, 500):
			c = (a ** 2 + b ** 2) ** (.5)
			
			if a + b + c == 1000:
				return a * b * c

print("Problem 9: {}".format(problem9())) # Solution: 31875000






	


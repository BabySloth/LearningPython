import time
import random
import sys

sys.setrecursionlimit(1000000000)
startTime = time.time()

'''
Insert code here
'''

def problem9():
	# a**2 + b**2 == c**2
	a = 1
	for a in range(1, 500):
		for b in range(a + 1, 500):
			c = (a ** 2 + b ** 2) ** (.5)

			if a + b + c == 1000:
				return (a, b, c)


print("Problem 9: {}".format(problem9()))  # Solution: 31875000

# No code beyond this point
###########################

print("Program took {} seconds".format(time.time()-startTime))

index = 0
fruits = [('apples', 'william'), ('bananas', 'victoria')]

for item in list(range(len(fruits))):
	# item will have value of 0 or 1
	for x in fruits[item]:
		# you are now looping through the fruits using item which has the value of 0 or 1
		# fruits[0] = ('apples', 'william')
		# fruits[1] = ('bananas', 'victoria')
		print x
		# Prints:
		'''
		apples
		william
		bananas
		victoria
		''''
		
for item in fruits:
	'''
	item is now:
	('apples', 'william')
	('bananas', 'victoria')
	'''
	for x in item:
		'''
		x is now:
		apples
		william
		bananas
		victoria
		'''

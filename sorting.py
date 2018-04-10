# Slow sorting
def sortList(l):
	sortedList = []
	for _ in range(len(l)):	
		index = 0
		smallest = max(l)
		smallIndex = -1
		while index < len(l):
			if l[index] < smallest:
				smallest = l[index]
				smallIndex = index
			index += 1
		sortedList.append(smallest)
		l.pop(smallIndex)
	return sortedList

# print(sortList([3, 27, 17, 1]))

# Super fast one

def quickSort(l):
	if len(l) < 2:
		return l
	else: # 3 1
		# Partition step
		pivot = l[0] #3
		left = []  # Numbers smaller than pivot
		right = []  # Numbers greater than pivot
		index = 1
		while index < len(l):
			if l[index] > pivot:
				right.append(l[index])
			else:
				left.append(l[index])
			index += 1
		print("{} is left: ".format(left)) 
		print("{} is right: ".format(right))
		return quickSort(left) + [pivot] + quickSort(right)

print(quickSort([2, 3, 1]))

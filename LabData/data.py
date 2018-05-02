# William Cao
# Data Lab
# 4/23/18
# Intro Comp Sci 2, Period 10


def print_results():
	global FILE_PATH
	FILE_PATH = "result.csv"
	RAW_DATA_ARRAY = process_data(open(FILE_PATH, 'r'))
	print(RAW_DATA_ARRAY)

	# Print top school scores
	# Add \n to make it easier to read the list
	statement = "\nTop 10 schools with highest {} scores (greatest to least):"
	print(statement.format("reading"))
	print_top_ten(sorting('reading', RAW_DATA_ARRAY), 3)

	print(statement.format("math"))
	print_top_ten(sorting('math', RAW_DATA_ARRAY), 4)

	print(statement.format("writing"))
	print_top_ten(sorting('writing', RAW_DATA_ARRAY), 5)


def process_data(file_object):
	data_array = []
	for idx, line in enumerate(file_object.readlines()):
		# Ignores column names
		if idx != 0:
			# Removes commas that are in the name of the school
			new_line = line.replace(", ", "")
			# Removes \n if any
			new_line = new_line.strip()

			data_array.append(new_line.split(","))
	return data_array


def sorting(sort_type, array):
	"""Enter 'math', 'writing', 'reading' for parameters
	DBN, NAME, Num, Reading, Math, Writing

	Follows quick sort algorithm
	"""

	# Comparing arrays through certain elements from the array
	index_of_comparison = 0
	if sort_type == 'reading':
		index_of_comparison = 3
	elif sort_type == 'math':
		index_of_comparison = 4
	elif sort_type == 'writing':
		index_of_comparison = 5

	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		right_bound = []
		left_bound = []

		# [1:] to compensate for pivot being first element
		for element in array[1:]:
			pivot_score = pivot[index_of_comparison]
			comparison_score = element[index_of_comparison]

			# 's' is not a valid score
			if comparison_score == 's':
				comparison_score = 0
			if pivot_score == 's':
				pivot_score = 0

			if int(comparison_score) < int(pivot_score):
				left_bound.append(element)
			else:
				right_bound.append(element)
	# Right + pivot + left to organize from highest score to lowest score
	return sorting(sort_type, right_bound) + [pivot] + sorting(sort_type, left_bound)


def print_top_ten(top_list, position_score):
	# Only want first 10 schools
	for idx, detailedArray in enumerate(top_list[0:10]):
		'''
		detailedArray[1] gives name of the school
		detailedArray[position_score] gives score of reading/math/writing depending on list
		'''

		# Add one to idx to compensate for enumerate index beginning at 0
		print("{}. {} Score: {}".format(idx + 1, detailedArray[1], detailedArray[position_score]))

#print_results()

'''
Bad code for rewriting
'''

def write_data():
	data_array = []
	file_object = open('result.csv', 'r')
	for idx, line in enumerate(file_object.readlines()):
		# Removes commas that are in the name of the school
		new_line = line.replace(", ", "")
		# Removes \n if any
		new_line = new_line.strip()
		data_array.append(new_line.split(","))
		print(new_line)
	writing = open('test.csv', 'w')
	new_stuff = ""
	for idx, element in enumerate(data_array):
		array = element
		if idx == 0:
			new_stuff += fix(array)
		else:
			new_stuff += fix(array + [average(array)])
	
	print(new_stuff)
	writing.write(new_stuff)
	writing.close()

def average(array):
	if array[-2] == 's':
		return 's'
	else:
		sum = int(array[-1]) + int(array[-2]) + int(array[-3])
		return int(sum) / 3

def fix(array):
	string = ""
	for item in array:
		string += "{},".format(item)
	return string[:-1] + '\n'

write_data()

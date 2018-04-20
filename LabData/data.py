'''
Sometimes the data for score can be 's'

'''
class ReadSATData:
	filePath = "result.csv"
	rowOfData = []
	fileHandle = None
	
	def __init__(self):
		self.fileHandle = open(self.filePath, 'r')
		
		# Process data to put into self.rowOfData		
		self.sterializeData()
	
	def sterializeData(self):
		for idx, line in enumerate(self.fileHandle.readlines()):
			if idx != 0:
				newLine = str(line).strip()  # Remove \n if any
				# Turns string into an array				
				self.rowOfData.append(newLine.split(","))
		print(self.rowOfData)
	
	def get_top_writing_school(self):
		sortedData = self.sorting("writing", self.rowOfData)
		print(sortedData)
	
	def get_top_math_school(self):
		pass
	
	def get_top_reading_school(self):
		pass	


	def sorting(self, scoreType, array):
		'''
		Enter 'math', 'writing', 'reading' for parameters
		 DBN, NAME, Num, Reading, Math, Writing

		'''
		positionOfScore = 0
		if scoreType == 'math':
			positionOfScore = 4
		elif scoreType == 'writing':
			positionOfScore = 5
		else:
			positionOfScore == 3

		if len(array) < 2:
			return array
		else:
			pivot = array[0]
			left = []
			right = []
			
			for element in array[1:]:
				if element[positionOfScore] > pivot[positionOfScore]:
					right.append(element)
				else:
					left.append(element)
			
			return self.sorting(scoreType, left) + [pivot] + self.sorting(scoreType, right)
	
			










data = ReadSATData()
data.get_top_writing_school()

















def the_jungle():
	# Ask the user for information
	a = raw_input("Give me an animal \n")	
	f = raw_input("Give me a food \n")
	c = raw_input("Give me a city \n")
	
	text = open("jungle.txt", "r")
	
	o = text.read()	
	o = o.format(animal = a, food = f, city = c)

	write = open("jC.txt", 'w')
	write.write(o)

	write.close()
	text.close()
	
def the_newspaper():
	adj = raw_input("Give an adjective \n")
	n = raw_input("Give a noun \n")
	v = raw_input("Give a verb \n")
	c = raw_input("Give a color \n")
	e = raw_input("Give an exclamation \n")
	a = raw_input("Give an animal \n")

	text = open("newspaper.txt", "r")
	
	original = text.read()
	original = original.format(ADJECTIVE = adj, NOUN = n, VERB = v, COLOR = c, EXCLAMATION = e, ANIMAL = a)

	write = open("newC.txt", "w")
	write.write(original)

	write.close()
	text.close()

if __name__ == "__main__":
	the_newspaper()

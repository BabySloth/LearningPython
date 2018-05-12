def the_jungle():
    # Ask the user for information
    a = input("Give me an animal \n")
    f = input("Give me a food \n")
    c = input("Give me a city \n")

    text = open("jungle.txt", "r")

    o = text.read()
    o = o.format(animal=a, food=f, city=c)

    write = open("jC.txt", 'w')
    write.write(o)

    write.close()
    text.close()


def the_newspaper():
    adj = input("Give an adjective \n")
    n = input("Give a noun \n")
    v = input("Give a verb \n")
    c = input("Give a color \n")
    e = input("Give an exclamation \n")
    a = input("Give an animal \n")

    text = open("newspaper.txt", "r")

    original = text.read()
    original = original.format(ADJECTIVE=adj, NOUN=n, VERB=v, COLOR=c, EXCLAMATION=e, ANIMAL=a)

    write = open("newC.txt", "w")
    write.write(original)

    write.close()
    text.close()


if __name__ == "__main__":
	the_jungle()
	the_newspaper()

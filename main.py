def counts(datalists, targets):
    counter = []

    for list in datalists:
        counter.append(0)
        for item in list:
            if item in targets:
                counter[-1] += 1
    return counter


datalists = [[4000, 1100, 3600, 1000], [12, -10000], [13, 0, 13], []]
targets = [0, 12, -7, 13]

print("q2")
print(counts(datalists, targets))

def countdown_by_n(f, b):
    if f - b < 0:
        print(f)
    else:
        print(f)
        return countdown_by_n(f - b, b)

print("\n\nq3:")
print(countdown_by_n(21, 7))
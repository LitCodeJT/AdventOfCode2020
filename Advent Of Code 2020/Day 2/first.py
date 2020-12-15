listOfNumber = []
while(True):
    x = input("Enter something:")
    if x == "":
        break
    x = x.split(" ")
    numberOfReps = x[0].split("-")
    print(numberOfReps)
    x[0] = int(numberOfReps[0])
    x[1] = x[1][0]
    x.append(int(numberOfReps[1]))
    listOfNumber.append(x)

counter = 0


def checkIfValid(xs):
    count = 0
    for i in xs[2]:
        if (xs[1] == i):
            count = count + 1
    if (count >= xs[0] and count <= xs[3]):
        return True
    else:
        return False


for i in listOfNumber:
    if (checkIfValid(i)):
        counter = counter + 1
print(counter)

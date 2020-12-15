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
    password = xs[2]
    letterToCheck = xs[1]
    if (letterToCheck == password[xs[0] - 1] and letterToCheck == password[xs[3] - 1]):
        return False
    elif (letterToCheck == password[xs[0] - 1] or letterToCheck == password[xs[3] - 1]):
        return True
    else:
        return False


for i in listOfNumber:
    if (checkIfValid(i)):
        counter = counter + 1
print(counter)

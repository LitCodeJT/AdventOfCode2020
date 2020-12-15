import sys
# sort a list to find the two that give you 2020, and then multiply them
listOfNumber = []
while(True):
    x = input("Enter something:")

    if x == "":
        break
    listOfNumber.append(int(x))

# stringOfNumbers = "input("Enter your value: ")"
#listOfNumber = stringOfNumbers.split(" ")
#sortedListOfNumbers = sorted(listOfNumber)


def findThePair2(xs, firstNumber):
    for i in range(len(xs)):
        if (xs[firstNumber] + xs[i] == 2020):
            print(xs[firstNumber]*xs[i])
            sys.exit()
        else:
            continue

    return findThePair2(xs, firstNumber + 1)


print(len(listOfNumber))
findThePair2(listOfNumber, 0)

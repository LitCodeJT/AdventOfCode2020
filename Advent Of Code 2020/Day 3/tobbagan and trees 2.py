import sys
treeMap = []
while (True):
    x = input()
    if (x == ""):
        break
    treeMap.append(x)


def calcX(xs, x, changeInX):
    if (x + changeInX) >= len(xs[0]):
        x = (x + changeInX) - len(xs[0])
    else:
        x = x + changeInX
    return x


def countTheNumberOfTrees(xs, counter, x, y, changeInX, changeInY):
    x = calcX(xs, x, changeInX)
    y = y + changeInY
    if y >= len(xs):
        return counter
    else:
        if ("#" == xs[y][x]):
            counter = counter + 1
        return countTheNumberOfTrees(xs, counter, x, y, changeInX, changeInY)


def checkAllSlopes(xs):
    return countTheNumberOfTrees(xs, 0, 0, 0, 1, 1) * countTheNumberOfTrees(xs, 0, 0, 0, 3, 1) * countTheNumberOfTrees(xs, 0, 0, 0, 5, 1) * countTheNumberOfTrees(xs, 0, 0, 0, 7, 1) * countTheNumberOfTrees(xs, 0, 0, 0, 1, 2)


print(checkAllSlopes(treeMap))

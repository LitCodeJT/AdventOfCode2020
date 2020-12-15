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
        print(counter)
        sys.exit()
    else:
        if ("#" == xs[y][x]):
            counter = counter + 1
        return countTheNumberOfTrees(xs, counter, x, y, changeInX, changeInY)


print(len(treeMap))
countTheNumberOfTrees(treeMap, 0, 0, 0, 3, 1)

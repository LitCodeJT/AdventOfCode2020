# get input
listOfNumber = []
while(True):
    x = input("Enter something:")
    if x == "":
        break
    listOfNumber.append(int(x))

sum = 2020

# using nested loops
# 3 element sum
res = []
for i in range(0, len(listOfNumber)-2):
    for j in range(i + 1, len(listOfNumber)-1):
        for k in range(j + 1, len(listOfNumber)):
            if listOfNumber[i] + listOfNumber[j] + listOfNumber[k] == sum:
                temp = []
                temp.append(listOfNumber[i])
                temp.append(listOfNumber[j])
                temp.append(listOfNumber[k])
                res.append(tuple(temp))

# print result
listof3 = res
print(res[0][0])
print("The 3 sum element list is : " + str(listof3))
print(listof3[0][0] * listof3[0][1] * listof3[0][2])

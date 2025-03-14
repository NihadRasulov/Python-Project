list = []

for i in range(0,4):
    for j in range(0,4):
        if(i == 0 and j == 0):
            list.append("*")
        elif(i == 0 and j > 0):
            list.append(j)
        elif(j == 0 and i == 1):
            list.append("a")
        elif(j == 0 and i == 2):
            list.append("b")
        elif(j == 0 and i == 3):
            list.append("c")
        else:
            list.append("x")

newList = []
for i in range(0, len(list) // 4):
    newList.append(list[i * 4 : (i + 1) * 4])

for i in range(0, len(newList)):
    print(newList[i])


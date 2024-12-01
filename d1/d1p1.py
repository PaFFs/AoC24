with open('d1/input.txt') as file:
    lines = file.readlines()

leftList = []
rightList = []
for line in lines:
    leftList.append(int(line.split()[0]))
    rightList.append(int(line.split()[1]))
leftList.sort()
rightList.sort()

diffs = 0
for i in range(len(leftList)):
    if leftList[i] > rightList[i]:
        diffs += leftList[i] - rightList[i]
    else:
        diffs += rightList[i] - leftList[i]
print(diffs)
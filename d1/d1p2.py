with open('d1/input.txt') as file:
    lines = file.readlines()

leftList = []
rightList = []
for line in lines:
    leftList.append(int(line.split()[0]))
    rightList.append(int(line.split()[1]))
leftList.sort()
rightList.sort()

similarity = 0
for num in leftList:
    count = rightList.count(num)
    similarity += num * count
print(similarity)
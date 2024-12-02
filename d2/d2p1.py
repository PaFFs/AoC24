with open('d2/input.txt') as file:
    lines = file.readlines()

safe = 0
for line in lines:
    line = line.strip()
    line = line.split()
    lineNums = []
    for num in line:
        lineNums.append(int(num))
    
    diffs = []
    prevNum = lineNums[0]
    for i in range(1,len(lineNums)):
        currentNum = lineNums[i]
        diff = currentNum - prevNum
        diffs.append(str(diff))
        prevNum = currentNum
    
    posList = ["1","2","3"]
    negList = ["-1","-2","-3"]

    if "0" in diffs:
        continue
    check = True
    for e in diffs:
        if e not in posList:
            check = False
    if check:
        safe += 1
        continue
    check = True
    for e in diffs:
        if e not in negList:
            check = False
    if check:
        safe += 1
        continue
    else:
        continue
print(safe)
        
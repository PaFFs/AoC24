with open('d2/input.txt') as file:
    lines = file.readlines()

def is_safe(report):
    diffs = []
    prevNum = report[0]
    for i in range(1,len(report)):
        currentNum = report[i]
        diff = currentNum - prevNum
        diffs.append(str(diff))
        prevNum = currentNum
    
    posList = ["1","2","3"]
    negList = ["-1","-2","-3"]

    if "0" in diffs:
        return False
    
    check = True
    for e in diffs:
        if e not in posList:
            check = False
    if check:
        return True
    
    check = True
    for e in diffs:
        if e not in negList:
            check = False
    if check:
        return True
    
    else:
        return False

safe = 0
for line in lines:
    line = line.strip()
    line = line.split()
    lineNums = []
    for num in line:
        lineNums.append(int(num))
    
    if is_safe(lineNums):
        safe += 1
print(safe)
        
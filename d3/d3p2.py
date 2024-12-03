with open('d3/input.txt') as file:
    lines = file.readlines()

import re

compLine = ""
for line in lines:
    line.strip()
    compLine += line

def mulLine(line):
    muls = re.findall(r'mul\([0-9]+\,[0-9]+\)',line)

    sum = 0
    for mul in muls:
        mul = mul[4:-1]
        mul = mul.split(",")
        sum += int(mul[0]) * int(mul[1])
    return sum

def splitLine(baseline):
    splitLines = ["do()"+e for e in baseline.split("do()") if e]
    dos = []
    for line in splitLines:
        if "don't()" in line:
            do = line.split("don't()")[0]
            dos.append(do)
        else:
            dos.append(line)

    return dos

sums = 0
for do in splitLine(compLine):
    sums += mulLine(do)
print(sums)
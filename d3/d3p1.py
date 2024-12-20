with open('d3/input.txt') as file:
    lines = file.readlines()

import re

compLine = ""
for line in lines:
    line.strip()
    compLine += line

muls = re.findall(r'mul\([0-9]+\,[0-9]+\)',compLine)

sum = 0
for mul in muls:
    mul = mul[4:-1]
    mul = mul.split(",")
    sum += int(mul[0]) * int(mul[1])
print(sum)
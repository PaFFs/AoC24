with open('d5/input.txt') as file:
    lines = file.read().splitlines()

def parseLines(text):
    rules = []
    updates = []
    for line in text:
        line = line.strip()
        if line == "":
            continue
        elif line[2] == "|":
            # parse rule
            rules.append(line.split("|"))
        elif line[2] == ",":
            # parse update
            updates.append(line.split(","))
    return rules, updates

def parseUpdates(updates, rules):
    midNumbers = []
    for update in updates:
        safe = True
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    safe = False
        if safe:
            midNumbers.append(update[int((len(update)-1)/2)])
    return midNumbers

numsums = 0
for num in parseUpdates(parseLines(lines)[1],parseLines(lines)[0]):
    numsums += int(num)
print(numsums)
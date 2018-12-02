import collections

def day2part1():
    fileContents = open("input.txt", 'r').readlines()
    twos = 0
    threes = 0
    letterCount = {}
    for fc in fileContents:
        for letter in fc:
            if letterCount.has_key(letter):
                letterCount[letter] += 1
            else:
                letterCount[letter] = 1
        threeCount = False
        twoCount = False
        for entry in letterCount:
            if letterCount[entry] == 3:
                if (not threeCount):
                    threes += 1
                    threeCount = True
            elif letterCount[entry] == 2:
                if (not twoCount):
                    twos += 1
                    twoCount = True
            if (threeCount and twoCount):
                break
        letterCount = {}
    return twos * threes

def day2part2():
    fileContents = open("input.txt", 'r').readlines()
    for i in range(len(fileContents)):
        for j in range(1, len(fileContents)):
            t = oneOff(fileContents[i], fileContents[j])
            if t != None:
                return t
    return

def oneOff(string1, string2):
    changes = 0
    changeIndex = -1
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            changes += 1
            changeIndex = i
    if changes == 1:
        return string1[:changeIndex] + string1[changeIndex+1:]
    return None

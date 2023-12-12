from functools import cache
import re

def setDamaged(condition, truth, index):
    firstNum = re.findall(r"[0-9]+", truth)[0]
    length = int(firstNum)
    end = index+length
    for i in range(index, end):
        if i > len(condition)-1 or condition[i] == ".":
            return False
    if end <= len(condition)-1 and condition[end] == "#":
        return False
    return True

@cache
def recursiveAssignment(condition, truth, index):
    # termination conditions
    if index >= len(condition) and len(truth) == 0:
        return 1
    elif index >= len(condition):
        return 0
    elif index < len(condition) and len(truth) == 0:
        if "#" in condition[index:]:
            return 0
        return 1
    
    # recursive conditions
    sum = 0
    if condition[index] == "?":
        success = setDamaged(condition, truth, index)
        if success:
            firstNum = re.findall(r"[0-9]+", truth)[0]
            newIndex = index + int(firstNum) + 1
            sum += recursiveAssignment(condition, truth[len(firstNum)+1:], newIndex)
        sum += recursiveAssignment(condition, truth, index+1)
    elif condition[index] == ".":
        sum += recursiveAssignment(condition, truth, index+1)
    elif condition[index] == "#":
        success = setDamaged(condition, truth, index)
        if success:
            firstNum = re.findall(r"[0-9]+", truth)[0]
            newIndex = index + int(firstNum) + 1
            sum += recursiveAssignment(condition, truth[len(firstNum)+1:], newIndex)
    return sum

def countArrangements(lines, part):    
    lines = lines.strip().split("\n")
    sum = 0
    for line in lines:
        condition, truth = line.split(" ")
        if part == 2:
            condition = ("?".join([condition] * 5))
            truth = ((truth+",")*5)
        sum += recursiveAssignment(condition, truth, 0)
    print(sum)

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.read()

    countArrangements(lines, 1)
    countArrangements(lines, 2)
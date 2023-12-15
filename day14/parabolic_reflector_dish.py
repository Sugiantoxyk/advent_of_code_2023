
from functools import cache

@cache
def rotatePlatform(platform):
    platform = platform.strip().split("\n")
    return [''.join(row[i] for row in platform[::-1]) for i in range(len(platform[0]))]

@cache
def rollRoundedRocks(platform):
    platform = platform.strip().split("\n")
    for r in range(len(platform)):
        row = platform[r]
        row = list(row)
        rounded_count = 0
        for i in range(len(row)):
            if row[i] == "O":
                row[i] = "."
                rounded_count += 1
            elif row[i] == "#":
                temp_i = i-1
                for j in range(rounded_count):
                    row[temp_i] = "O"
                    temp_i -= 1
                rounded_count = 0
                
            if i == len(row)-1:
                temp_i = i
                for j in range(rounded_count):
                    row[temp_i] = "O"
                    temp_i -= 1
        platform[r] = "".join(row)
    return platform

def countWeight(platform):
    sum = 0
    for row in platform:
        for i in range(len(platform)):
            if row[i] == "O":
                sum += i+1
    return sum

def findPattern(outcomes):
    for start in range(1, len(outcomes)):
        for length in range(2, len(outcomes)-start):
            pattern = outcomes[start:start+length]
            
            matchCount = 0
            i = start+length
            while matchCount <= 3:
                if matchCount >= 3:
                    return True, start, length
                if pattern == outcomes[i:i+length]:
                    matchCount += 1
                else:
                    break
                i += length
    return False, None, None

def calculateLoadToNorth(inp, part):
    platformStr = inp
    if part == 1:
        platform = rotatePlatform(platformStr)
        platform = rollRoundedRocks("\n".join(platform))
        weight = countWeight(platform)
        print(weight)
    else:
        iterations = 1_000_000_000
        outcomes = []
        for i in range(iterations):
            for _ in range(4):
                platform = rotatePlatform(platformStr)
                platform = rollRoundedRocks("\n".join(platform))
                platformStr = "\n".join(platform)
            tempPlatform = rotatePlatform(platformStr)
            weight = countWeight(tempPlatform)
            outcomes.append(weight)
            
            if i % 200 == 0:
                pattern_found, start, length = findPattern(outcomes)
            
            if pattern_found:
                break
        
        weight = outcomes[((iterations-start)%length) + start - 1]
        print(weight)

if __name__ == "__main__":
    file = open("input.txt", "r")
    inp = file.read()

    calculateLoadToNorth(inp, 1)
    calculateLoadToNorth(inp, 2)

def differenceCount(line1, line2):
    return (sum(i != j for i, j in zip(line1, line2)))

def rotateMap(lines):
    return [''.join(row[i] for row in lines) for i in range(len(lines[0]))]

def checkHorMirror(lines, i, i2, part):
    smudgeCount = 0
    front_len = i+1
    back_len = len(lines)-i2
    length = min(front_len, back_len)
    for j2 in range(i2, i2+length):
        line1 = lines[j2]
        line2 = lines[i-(j2-i2)]
        if part == 1:
            if line1 != line2:
                return False
        elif part == 2:
            smudgeCount += differenceCount(line1, line2)
            if smudgeCount > 1:
                return False
            
    if part == 1:
        return True
    if part == 2 and smudgeCount == 1:
        return True
    else:
        return False            

def findHorMirror(lines, part):
    for i in range(len(lines)):
        i2 = i + 1
        if i2 < len(lines):
            if checkHorMirror(lines, i, i2, part):
                return i2
    return 0
                
def findMirror(inp, part):    
    maps = inp.strip().split("\n\n")
    sum = 0
    for map in maps:
        lines = map.split("\n")
        
        # find horizontal mirror
        rSum = findHorMirror(lines, part)
        rSum *= 100
        
        if rSum == 0:
            rotatedLines = rotateMap(lines)
            # find vertical mirror
            rSum = findHorMirror(rotatedLines, part)
            
        sum += rSum
    print(sum)

if __name__ == "__main__":
    file = open("input.txt", "r")
    inp = file.read()

    findMirror(inp, 1)
    findMirror(inp, 2)
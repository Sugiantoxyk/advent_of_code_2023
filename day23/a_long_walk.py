
import copy
import sys

def pathFinding(mat, cur, dest, part):
    steps = 0
    tempMat = copy.deepcopy(mat)
    slope = {">":(1,0),"<":(-1,0),"^":(0,-1),"v":(0,1)}
    next = [cur]
    while len(next) == 1:
        curX, curY = next[0]
        del next[0]
        tempMat[curY][curX] = "O"
        steps += 1
        # terminating condition
        if (curX, curY) == dest:
            return steps
        # when encountering slope, move to the next slot immediately
        if part == 1 and mat[curY][curX] in slope:
            newX = curX + slope[mat[curY][curX]][0]
            newY = curY + slope[mat[curY][curX]][1]
            next.append((newX, newY))
            continue
        for key in slope.keys():
            addX, addY = slope[key]
            newX = curX + addX
            newY = curY + addY
            if newX >= 0 and newY >= 0 and newX < len(mat[0]) and newY < len(mat) and (newX,newY) and tempMat[newY][newX] != "O":
                if part == 1 and mat[newY][newX] == "." or mat[newY][newX] == key:
                    next.append((newX, newY))
                elif part == 2 and mat[newY][newX] != "#":
                    next.append((newX, newY))
    if len(next) > 1:
        tempMat[curY][curX] = "O"
        maxSteps = 0
        for coord in next:
            tempSteps = pathFinding(tempMat, coord, dest, part)
            if tempSteps > maxSteps:
                maxSteps = tempSteps
        steps += maxSteps
    elif len(next) == 0:
        return 0
    return steps

def longWalk(mat):
    y = 0
    x = mat[y].index(".")
    dy = len(mat)-1
    dx = mat[dy].index(".")
    part1Steps = pathFinding(mat, (x, y), (dx, dy), 1)
    print("Part 1:", part1Steps-1)
    part2Steps = pathFinding(mat, (x, y), (dx, dy), 2)
    print("Part 2:", part2Steps-1)

if __name__ == "__main__":
    file = open("input.txt", "r")
    inp = file.read()
    rows = inp.strip().splitlines()
        
    sys.setrecursionlimit(10000)
    mat = [list(row) for row in rows]
    longWalk(mat)
    
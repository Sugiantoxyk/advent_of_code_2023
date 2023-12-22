
import copy
import re

def output(map):
    file = open("output.txt", "w")
    for row in map:
        file.writelines("".join(row) + "\n")

def fillMat(mat, i, lx, ly, lz, ux, uy, uz):
    for z in range(lz, uz+1):
        for y in range(ly, uy+1):
            for x in range(lx, ux+1):
                mat[z][y][x] = i

def part1(mat, rows):
    disintegrate = []
    data = {}
    # simulate dropping brick and store the "bot" and "top" information
    for i in range(len(rows)):
        disintegrate.append(0)
        data[i] = {"bot":[], "top":[], "lower":[], "upper":[]}
        lower, upper = rows[i].split("~")
        lx, ly, lz = tuple(map(int, lower.split(",")))
        ux, uy, uz = tuple(map(int, upper.split(",")))

        nextRow = False
        for z in range(lz-1, -1, -1):
            for y in range(ly, uy+1):
                for x in range(lx, ux+1):
                    if mat[z][y][x] != -1:
                        fillMat(mat, i, lx, ly, z+1, ux, uy, (uz-lz)+z+1)
                        data[i]["lower"] = [lx, ly, z+1]
                        data[i]["upper"] = [ux, uy, (uz-lz)+z+1]
                        if mat[z][y][x] != -2:
                            if i not in data[mat[z][y][x]]["top"]: data[mat[z][y][x]]["top"].append(i)
                            if mat[z][y][x] not in data[i]["bot"]: data[i]["bot"].append(mat[z][y][x])
                        nextRow = True
            if nextRow: break
    
    # use "bot" and "top" information to determine if other brick will fall
    for i in range(len(disintegrate)):
        if len(data[i]["top"]) == 0:
            disintegrate[i] = 1
        else:
            canDisintegrate = True
            for j in data[i]["top"]:
                if len(data[j]["bot"]) <= 1:
                    canDisintegrate = False
                    break
            if canDisintegrate: disintegrate[i] = 1

    print("Part 1:", sum(disintegrate))
    # return for use in part 2
    return disintegrate, data

def willFall(mat, lx, ly, lz, ux, uy, uz):
    for y in range(ly, uy+1):
        for x in range(lx, ux+1):
            if mat[lz-1][y][x] != -1:
                return False
    return removeMat(mat, lx, ly, lz, ux, uy, uz)
            
def removeMat(mat, lx, ly, lz, ux, uy, uz):
    for z in range(lz, uz+1):
        for y in range(ly, uy+1):
            for x in range(lx, ux+1):
                if mat[z][y][x] == -1:
                    return False
                mat[z][y][x] = -1
    return True

def part2(fullmat, disintegrate, data):
    dropCount = [0] * len(data)
    for i in range(len(disintegrate)-1, -1, -1):
        if disintegrate[i] == 0:
            mat = copy.deepcopy(fullmat)
            removeMat(mat, *(data[i]["lower"]), *(data[i]["upper"]))
            q = copy.deepcopy(data[i]["top"])
            while q:
                cur = q[0]
                del q[0]
                fallen = willFall(mat, *(data[cur]["lower"]), *(data[cur]["upper"]))
                if fallen:
                    dropCount[i] += 1
                    for j in data[cur]["top"]:
                        q.append(j)
            # fillMat(mat, i, *(data[i]["lower"]), *(data[i]["upper"]))

    # print(dropCount)
    print("Part 2:", sum(dropCount))

if __name__ == "__main__":
    file = open("input.txt", "r")
    inp = file.read()
    rows = inp.strip().splitlines()
    
    # sort inputs based on their lower z axis
    rows = sorted(rows, key=lambda row: int(re.findall(r"[0-9]+(?=~)", row)[0]))
    
    # get size of 3D matrix
    maxX = max([int(re.findall(r"(?<=~)[0-9]+", row)[0]) for row in rows])
    maxY = max([int(re.findall(r"(?<=,)[0-9]+(?=,)", row)[1]) for row in rows])
    maxZ = max([int(re.findall(r"[0-9]+$", row)[-1]) for row in rows])

    # create 3D matrix
    mat = []
    for z in range(maxZ+1):
        tempZ = []
        for y in range(maxY+1):
            tempY = [-1] * (maxX+1)
            if z == 0:
                tempY = [-2] * (maxX+1)
            tempZ.append(tempY)
        mat.append(tempZ)

    disintegrate, data = part1(mat, rows)
    part2(mat, disintegrate, data)
    
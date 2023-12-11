import re

def shortestDistance(lines, part):    
    lines = lines.strip().split("\n")
    
    # find indexes of rows and cols with no galaxy
    row_has_galaxy = [1] * len(lines)
    col_has_galaxy = [0] * len(lines[0])
    for i in range(len(lines)):
        line = lines[i]
        if len(re.findall(r"#", line)) == 0:
            row_has_galaxy[i] = 0
        for j in range(len(line)):
            symbol = line[j]
            if symbol == "#":
                col_has_galaxy[j] = 1
    
    # extract the index of rows and cols needed to expand
    index_row_expand = []
    index_col_expand = []
    for i in range(len(col_has_galaxy)-1, -1, -1):
        if col_has_galaxy[i] == 0:
            index_col_expand.append(i)
    for i in range(len(row_has_galaxy)-1, -1, -1):
        if row_has_galaxy[i] == 0:
            index_row_expand.append(i)

    # calculate distance for all pairs
    sum = 0
    galaxies_coord = []
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if line[x] == "#":
                for coord in galaxies_coord:
                    x2, y2 = coord
                    distance = abs(x-x2) + abs(y-y2)
                    # check if expansion row/col is between the 2 galaxies
                    # if it is in between, add the expansion distance
                    for ir in index_row_expand:
                        if y < ir < y2 or y2 < ir < y:
                            distance += (2 if part == 1 else 1000000)-1
                    for ic in index_col_expand:
                        if x < ic < x2 or x2 < ic < x:
                            distance += (2 if part == 1 else 1000000)-1
                    sum += distance
                galaxies_coord.append([x,y])
    
    print(sum)

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.read()

    shortestDistance(lines, 1)
    shortestDistance(lines, 2)
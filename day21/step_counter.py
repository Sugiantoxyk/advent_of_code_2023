
import copy

def output(map):
    file = open("output.txt", "w")
    for row in map:
        file.writelines("".join(row) + "\n")

def stepCounter(map, start, steps):
    map[start[1]][start[0]] = "O"
    even_map = copy.deepcopy(map)
    even_count = 1
    map[start[1]][start[0]] = "."
    odd_map = copy.deepcopy(map)
    odd_count = 0
    curs = [start]
    moves = [[0,1],[0,-1],[1,0],[-1,0]]
    for step in range(1, steps+1):
        new_curs = []
        for cur in curs:
            for addX, addY in moves:
                newX = cur[0] + addX
                newY = cur[1] + addY
                if newX < 0 or newY < 0 or newX >= len(map[0]) or newY >= len(map): continue
                if step%2 == 0: # update map on even_map
                    if even_map[newY][newX] != "O" and even_map[newY][newX] != "#":
                        even_map[newY][newX] = "O"
                        even_count += 1
                        new_curs.append((newX, newY))
                else: # update map on odd_map
                    if odd_map[newY][newX] != "O" and odd_map[newY][newX] != "#":
                        odd_map[newY][newX] = "O"
                        odd_count += 1
                        new_curs.append((newX, newY))
        curs = copy.deepcopy(new_curs)
    if steps%2 == 0: return even_count
    else: return odd_count

def part2(widen_map, start, row, middle):
    ans = []
    for i in range(4):
        level = row * i
        ans.append(stepCounter(widen_map, start, middle + level))
    print(ans)
    
    # level 0 (65 + 131 * 0 steps): 3720 plots
    # level 1 (65 + 131 * 1 steps): 33150 plots
    # level 2 (65 + 131 * 2 steps): 91890 plots
    # level 3 (65 + 131 * 3 steps): 179940 plots
    # let n be level number and f(n) be the plots,
    # n = f(n-1) + (n * 29310) + 120 
    plots = 3720 # at 65 steps
    multi = 29310
    constant = 120
    iteration = int((26501365-middle)/row)
    for i in range(iteration):
        plots += (i+1)*multi + constant
    print("Part 2:", plots)

if __name__ == "__main__":
    file = open("input.txt", "r")
    inp = file.read()
    rows = inp.strip().splitlines()
    
    map = []
    widen_map = []
    multiple = 7
    for i in range(len(rows)):
        row = rows[i]
        map.append(list(row))
        widen_map.append(list(row)*multiple)
        if "S" in row:
            x = row.index("S")
            y = i
            
    temp = copy.deepcopy(widen_map)
    for i in range(multiple-1):
        for row in temp:
            widen_map.append(list(row))
    
    widen_x = int(x + (multiple-1)/2 * len(map[0]))
    widen_y = int(y + (multiple-1)/2 * len(map))

    # part 1
    print("Part 1:", stepCounter(map, (x,y), 64))
    # part 2
    part2(widen_map, (widen_x,widen_y), len(map[0]), x)
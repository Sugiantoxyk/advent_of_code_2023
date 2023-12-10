
def findS(lines):
    x,y = 0,0
    for line in lines:
        if "S" in line:
            x = line.index("S")
            break
        y += 1
    return x,y

def pipeMaze(lines):
    # part 1
    up = ["|", "7", "F"]
    down = ["|", "L", "J"]
    left = ["-", "L", "F"]
    right = ["-", "7", "J"]
    movement_list = {"|":["up", "down"], "-":["left", "right"], "L":["up", "right"], "J":["up", "left"], "7":["down", "left"], "F":["down", "right"]}
    
    lines = lines.strip().split("\n")
    x,y = findS(lines)
    coords = [(x,y)]
    
    # initial move
    prev = None
    if lines[max(0, y-1)][x] in up:
        # can move up
        prev = "down"
        y = max(0, y-1)
    elif lines[min(len(lines)-1, y+1)][x] in down:
        # can move down
        prev = "up"
        y = min(len(lines)-1, y+1)
    elif lines[y][max(0, x-1)] in left:
        # can move left
        prev = "right"
        x = max(0, x-1)
    elif lines[y][min(len(lines[0]), x+1)] in right:
        # can move right
        prev = "left"
        x = min(len(lines[0])-1, x+1)

    # count the number of pipes until return back to 'S'
    steps = 1
    while lines[y][x] != "S":
        coords.append((x,y))
        movement = movement_list[lines[y][x]].copy()
        movement.remove(prev)
        movement = movement[0]
        if movement == "up":
            y -= 1
            prev = "down"
        elif movement == "down":
            y += 1
            prev = "up"
        elif movement == "left":
            x -= 1
            prev = "right"
        elif movement == "right":
            x += 1
            prev = "left"
        steps += 1
    
    print(int(steps/2))
    
    # part 2
    x,y = coords[0]
    start_movement = []
    
    if lines[max(0, y-1)][x] in up:
        start_movement.append("up")
    if lines[min(len(lines)-1, y+1)][x] in down:
        start_movement.append("down")
    if lines[y][max(0, x-1)] in left:
        start_movement.append("left")
    if lines[y][min(len(lines[0])-1, x+1)] in right:
        start_movement.append("right")
        
    # get the pipe shape for starting point 'S'
    for symbol, movement in movement_list.items():
        if movement == start_movement:
            start_movement = symbol
            break
    
    # replace 'S' with a correct pipe shape
    temp = list(lines[y])
    temp[x] = symbol
    lines[y] = "".join(temp)
    
    # count spaces within the pipe loop
    # explanation:
    # general step is to read the pipes row by row from left to right to determine the area enclosed by the loop
    # the variable 'draw' will determin if the next sequence is enclosed by the loop or not (0 means not enclosed, 1 means enclosed)
    # reading from left to right, if I find the pipes (part of the loop border) that is either "|" or "L7"(can be "L--7" as well) or "FJ" (can be "F---J" as well), the 'draw' variable will flip
    # if I find the pipes (part of the loop border) that is either "F7" (or "F---7") and "LJ" (or "L---J") I don't do anything
    # based on variable 'draw' I will increment count when encountering any pipe that is not part of the loop border
    count = 0
    for y in range(len(lines)):
        line_list = list(lines[y])
        draw = 0
        rule = ""
        for x in range(len(line_list)):
            if (x,y) in coords:
                if lines[y][x] == "|":
                    draw = (draw+1)%2
                elif lines[y][x] == "F" or lines[y][x] == "L":
                    rule = lines[y][x]
                elif lines[y][x] == "7" or lines[y][x] == "J":
                    rule += lines[y][x]
                    if rule == "L7" or rule == "FJ":
                        draw = (draw+1)%2
            else:
                if draw == 1:
                    count += 1
    print(count)

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.read()

    pipeMaze(lines)      
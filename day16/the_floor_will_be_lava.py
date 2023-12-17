
import sys

def move(puzzle, history, x, y, direction):
    # check if coordinate is out of puzzle size
    if x < 0 or y < 0 or x >= len(puzzle[0]) or y >= len(puzzle):
        return
    # check if this coordinate has already been explored with same direction
    if str(x)+","+str(y) in history and direction in history[str(x)+","+str(y)]:
        return
    
    dir_to_dir = {"up":{".":["up"],"|":["up"],"-":["left","right"],"/":["right"],"`":["left"]}, 
              "down":{".":["down"],"|":["down"],"-":["left","right"],"/":["left"],"`":["right"]}, 
              "left":{".":["left"],"|":["up","down"],"-":["left"],"/":["down"],"`":["up"]}, 
              "right":{".":["right"],"|":["up","down"],"-":["right"],"/":["up"],"`":["down"]}}
    dir_to_coord = {"up":[0,-1],"down":[0,1],"left":[-1,0],"right":[1,0]}
    if str(x)+","+str(y) not in history:
        history[str(x)+","+str(y)] = [direction]
    else:
        history[str(x)+","+str(y)].append(direction)
    next_dir = dir_to_dir[direction][puzzle[y][x]]
    for dir in next_dir:
        next_coord = dir_to_coord[dir]
        newX = x + next_coord[0]
        newY = y + next_coord[1]
        move(puzzle, history, newX, newY, dir)
    return

def part1(puzzle):
    history = {}
    move(puzzle, history, 0, 0, "right")
    print(len(history))
    
def part2(puzzle):
    results = []
    for y in range(len(puzzle)):
        for x in [0, len(puzzle[0])-1]:
            history = {}
            if x == 0:
                direction = "right"
            else:
                direction = "left"
            move(puzzle, history, x, y, direction)
            results.append(len(history))
    for x in range(len(puzzle)):
        for y in [0, len(puzzle)-1]:
            history = {}
            if x == 0:
                direction = "down"
            else:
                direction = "up"
            move(puzzle, history, x, y, direction)
            results.append(len(history))
    print(max(results))

if __name__ == "__main__":
    file = open("input.txt", "r")
    inp = file.read()
    puzzle = list(list(row) for row in inp.strip().replace("\\","`").split("\n"))

    sys.setrecursionlimit(5000)

    part1(puzzle)
    part2(puzzle)
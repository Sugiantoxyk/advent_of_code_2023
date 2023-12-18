from heapq import heappush, heappop
from math import inf

moves = {"right": ["down","up"],
        "left": ["down","up"],
        "up": ["right","left"],
        "down": ["right","left"],
        "initial": ["right","down"]}
coords = {"up":(0,-1),"down":(0,1),"left":(-1,0),"right":(1,0)}

def clumsyCrucible(puzzle, min, max):
    destination = (len(puzzle[0])-1, len(puzzle)-1)
    heap = [(0, (0,0), "initial")]
    heatMap = {(0,0): 0}
    visited = set()

    while heap:
        heatLoss, coord, direction = heappop(heap)

        # terminating condition
        if coord == destination: 
            break
        if (coord, direction) in visited: 
            continue
        visited.add((coord, direction))

        for newDir in moves[direction]:
            addX, addY = coords[newDir]
            newHeatLoss = heatLoss
            for steps in range(1, max + 1):
                newCoord = (coord[0] + steps * addX, coord[1] + steps * addY)
                # out of the puzzle border
                if newCoord[0] < 0 or newCoord[1] < 0 or newCoord[0] > destination[0] or newCoord[1] > destination[1]:
                    continue
                newHeatLoss = newHeatLoss + puzzle[newCoord[1]][newCoord[0]]
                if steps >= min:
                    newNode = (newCoord, newDir)
                    if heatMap.get(newNode, inf) <= newHeatLoss:
                        continue
                    heatMap[newNode] = newHeatLoss
                    heappush(heap, (newHeatLoss, newCoord, newDir))
    print (heatLoss)

if __name__ == "__main__":
    file = open("input.txt", "r")
    inp = file.read()
    puzzle = [[int(x) for x in row] for row in inp.strip().splitlines()]
    clumsyCrucible(puzzle, 1, 3)
    clumsyCrucible(puzzle, 4, 10)

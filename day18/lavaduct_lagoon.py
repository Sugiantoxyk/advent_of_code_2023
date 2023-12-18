
import re

def calculateLava(instructions, part):
    perimeter = 0
    prevX = 0
    prevY = 0
    x = 0
    y = 0
    over = 0
    under = 0
    if part == 1:
        dirCoord = {"U":[0,-1],"D":[0,1],"L":[-1,0],"R":[1,0]}
    else:
        dirCoord = {"3":[0,-1],"1":[0,1],"2":[-1,0],"0":[1,0]}
    for instruction in instructions:
        dir, length, color = instruction.split(" ")
        if part == 2:
            code = re.findall(r"[0-9a-z]+", color)[0]
            length = int(code[:-1], base=16)
            dir = code[-1]
        length = int(length)
        x += dirCoord[dir][0] * length
        y += dirCoord[dir][1] * length
        perimeter += length
        over += prevX * y
        under += prevY * x
        prevX = x
        prevY = y
    print(abs(over-under)/2 + perimeter/2 + 1)

if __name__ == "__main__":
    file = open("input.txt", "r")
    inp = file.read()
    puzzle = inp.strip().split("\n")

    calculateLava(puzzle, 1)
    calculateLava(puzzle, 2)
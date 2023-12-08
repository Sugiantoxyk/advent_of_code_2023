import re
import math

def stepsToEnd(instruction, mapping, cur, part):
    steps = 0
    while True:
        # check for terminating condition
        if part == 1 and cur == "ZZZ":
            break
        if part == 2 and cur[-1] == "Z":
            break
        cur_mapping = re.findall(cur+" = \([A-Z]+, [A-Z]+\)", mapping)
        left, right = re.findall(r"[A-Z]+", cur_mapping[0].split("=")[1])
        move = instruction[steps%len(instruction)]
        if move == "L":
            cur = left
        else:
            cur = right
        steps += 1
    return steps

def navigate(lines, part):
    instruction, mapping = lines.strip().split("\n\n")
    if part == 1:
        cur = "AAA"
        print(stepsToEnd(instruction, mapping, cur, part))
    else:
        # get all starting position that ends with 'A'
        curs = [x.split("=")[0].strip() for x in re.findall("[A-Z]+A =", mapping)]
        curs_loop_count = []
        for cur in curs:
            curs_loop_count.append(stepsToEnd(instruction, mapping, cur, part))
        print(math.lcm(*curs_loop_count))

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.read()

    navigate(lines, 1)
    navigate(lines, 2)
        
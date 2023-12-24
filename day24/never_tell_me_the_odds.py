
import copy
import sys
import re

def inPast(x, y, px, py, vx, vy):
    if (vx > 0 and x < px) or (vx < 0 and x > px):
        return True
    if (vy > 0 and y < py) or (vy < 0 and y > py):
        return True
    return False

def crossPath(rows, min, max):
    total = 0
    for i in range(len(rows)):
        px1, py1, pz1, vx1, vy1, vz1 = list(map(int, re.findall(r"[-]?[0-9]+", rows[i])))
        const1 = py1-(vy1/vx1)*px1
        a1 = vy1
        b1 = -vx1
        c1 = const1 * vx1
        for j in range(i+1, len(rows)):
            px2, py2, pz2, vx2, vy2, vz2 = list(map(int, re.findall(r"[-]?[0-9]+", rows[j])))
            const2 = py2-(vy2/vx2)*px2
            a2 = vy2
            b2 = -vx2
            c2 = const2 * vx2
            try:
                x, y = [(b1*c2-b2*c1)/(a1*b2-a2*b1), (a2*c1-a1*c2)/(a1*b2-a2*b1)]
                if x>=min and x<=max and y>=min and y<=max and not inPast(x, y, px1, py1, vx1, vy1) and not inPast(x, y, px2, py2, vx2, vy2):
                    total += 1
            except:
                continue
            
    print("Part 1:", total)

def rockThrow(rows):
    
    print()

if __name__ == "__main__":
    file = open("input copy.txt", "r")
    inp = file.read()
    rows = inp.strip().splitlines()
        
    # crossPath(rows, 200000000000000, 400000000000000)
    rockThrow(rows)
    
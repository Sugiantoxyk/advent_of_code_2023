import re    

def part1(lines):
    # part 1
    margin = 0
    datas = lines.split("Distance")
    time = re.findall(r"\d+" ,datas[0])
    distance = re.findall(r"\d+" ,datas[1])
    for i in range(0, len(time)):
        sum = 0
        min = 0
        for j in range(1, int(time[i])):
            if (j * (int(time[i])-j)) > int(distance[i]):
                min = j
                break
        sum = (((int(time[i])+1)/2)-min)*2
        if margin == 0:
            margin = sum
        else:
            margin *= sum
    print(margin)

def part2(lines):
    # part 2
    datas = lines.split("Distance")
    time = re.findall(r"\d+" ,datas[0])
    distance = re.findall(r"\d+" ,datas[1])
    time = "".join(time)
    distance = "".join(distance)

    min = 0
    for i in range(0, int(time)):
        if (i * (int(time)-i)) > int(distance):
            min = i
            break
        
    print((((int(time)+1)/2)-min)*2)            

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.read()
    
    part1(lines)
    part2(lines)
        
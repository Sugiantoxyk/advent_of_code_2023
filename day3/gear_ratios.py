import re

def part1(lines):
    # part 1
    sum = 0
    for i in range(len(lines)):
        # retrieving adjacent lines
        if i == 0:
            line_before = None
        else:
            line_before = lines[i-1]
        if i == len(lines)-1:
            line_after = None
        else:
            line_after = lines[i+1]
        line_cur = lines[i]
        
        # for all number in line
        nums = re.findall(r"\d+", line_cur)
        for num in nums:
            index = line_cur.find(num)
            line_cur = line_cur.replace(num, "."*len(num), 1)
            index_from = max(0, index-1)
            index_to = min(len(line_cur)-1, index+len(num)+1)
            # extract out adjacent cells into a string
            string = ""
            if line_before != None:
                string += line_before[index_from : index_to]
            string += line_cur[index_from : index_to]
            if line_after != None:
                string += line_after[index_from : index_to]
            # use regex to extract all symbols
            check = re.findall(r"[^.0123456789]", string)
            if len(check) != 0:
                sum += int(num)
    print(sum)
    
def part2(lines):
    sum = 0
    for i in range(len(lines)):
        # retrieving adjacent lines
        if i == 0:
            line_before = None
        else:
            line_before = lines[i-1]
        if i == len(lines)-1:
            line_after = None
        else:
            line_after = lines[i+1]
        line_cur = lines[i]
        
        # for all * in line
        gear_i = line_cur.find("*")
        while gear_i != -1:
            line_cur = line_cur.replace("*", ".", 1)
            part_nums = []
            if line_before != None:
                line_before_nums = re.finditer(r"\d+", line_before)
            if line_after != None:
                line_after_nums = re.finditer(r"\d+", line_after)
            line_cur_nums = re.finditer(r"\d+", line_cur)
            for match in line_cur_nums:
                num_range = [x for x in range(match.span()[0], match.span()[1])]
                for j in range(gear_i-1, gear_i+2):
                    if j in num_range:
                        part_nums.append(line_cur[match.span()[0] : match.span()[1]])
                        break
            for match in line_before_nums:
                num_range = [x for x in range(match.span()[0], match.span()[1])]
                for j in range(gear_i-1, gear_i+2):
                    if j in num_range:
                        part_nums.append(line_before[match.span()[0] : match.span()[1]])
                        break
            for match in line_after_nums:
                num_range = [x for x in range(match.span()[0], match.span()[1])]
                for j in range(gear_i-1, gear_i+2):
                    if j in num_range:
                        part_nums.append(line_after[match.span()[0] : match.span()[1]])
                        break
            if len(part_nums) == 2:
                sum += int(part_nums[0]) * int(part_nums[1])
            gear_i = line_cur.find("*")
    print(sum)

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    
    part1(lines)
    part2(lines)    
        
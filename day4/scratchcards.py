import re    

def part1(lines):
    # part 1
    sum = 0
    for line in lines:
        card_point = 0
        card_list = line.split(":")
        winning_nums, my_nums = card_list[1].split("|")
        winning_nums = re.findall(r"\d+", winning_nums)
        my_nums = re.findall(r"\d+", my_nums)
        for num in my_nums:
            if num in winning_nums:
                if card_point == 0:
                    card_point += 1
                else:
                    card_point *= 2
        sum += card_point
    print(sum)

def part2(lines):
    # part 2
    sc_num = [1] * len(lines)
    for i in range(len(lines)):
        line = lines[i]
        card_list = line.split(":")
        winning_nums, my_nums = card_list[1].split("|")
        winning_nums = re.findall(r"\d+", winning_nums)
        my_nums = re.findall(r"\d+", my_nums)
        temp_i = i
        for num in my_nums:
            if num in winning_nums:
                temp_i += 1
                sc_num[temp_i] += 1 * sc_num[i]
    print(sum(sc_num))
            

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    
    part1(lines)
    part2(lines)
        
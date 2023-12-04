import re
    
if __name__ == "__main__": 
    file = open("input.txt", "r")
    lines = file.readlines()

    # part 1
    # sum = 0
    # for line in lines:
    #     nums = re.findall("\d", line)
    #     sum += int(nums[0]) * 10 + int(nums[-1])
    # print(sum)

    # part 2
    sum = 0
    for line in lines:
        line = (line.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e"))
        nums = re.findall("\d", line)
        sum += int(nums[0]) * 10 + int(nums[-1])
    print(sum)
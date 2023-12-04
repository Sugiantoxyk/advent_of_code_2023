import re    

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    
    
    sum = 0
    for i in range(len(lines)):
        if i == 0:
            line_before = None
        else:
            line_before = lines[i-1]
        if i == len(lines)-1:
            line_after = None
        else:
            line_after = lines[i+1]
        line_cur = lines[i]
        
        nums = re.findall(r"\d+", line_cur)
        for num in nums:
            index = line_cur.find(num)
            line_cur = line_cur.replace(num, "."*len(num), 1)
            index_from = max(0, index-1)
            index_to = min(len(line_cur)-1, index+len(num)+1)
            string = ""
            if line_before != None:
                string += line_before[index_from : index_to]
            string += line_cur[index_from : index_to]
            if line_after != None:
                string += line_after[index_from : index_to]
            check = re.findall(r"[^.0123456789]", string)
            if len(check) != 0:
                sum += int(num)
    print(sum)
        
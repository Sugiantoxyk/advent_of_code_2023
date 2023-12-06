import re

def part1(lines):
    # part 1
    datas = lines.split("\n\n")
    data_blocks = datas[1:]
    seeds = list(map(int, re.findall(r"\d+", datas[0])))
    
    for data_block in data_blocks:
        range_list = []
        for line in data_block.splitlines()[1:]:
            range_list.append(list(map(int, re.findall(r"\d+", line))))
            
        new_seeds = []
        
        while len(seeds) > 0:
            seed = seeds.pop()
            
            for destination, source, length in range_list:            
                if seed >= source and seed <= source+length-1:
                    new_seeds.append((seed-source)+destination)
                    break
            else:
                new_seeds.append(seed)
                
        seeds = new_seeds
            
    print(min(seeds))

def part2(lines):
    # part 2
    datas = lines.split("\n\n")
    data_blocks = datas[1:]
    seed_inputs = list(map(int, re.findall(r"\d+", datas[0])))
    seeds = [] #store seed ranges
    
    for i in range(0, len(seed_inputs), 2):
        seeds.append([seed_inputs[i], seed_inputs[i] + seed_inputs[i + 1]])
        
    for data_block in data_blocks:
        range_list = []
        for line in data_block.splitlines()[1:]:
            range_list.append(list(map(int, re.findall(r"\d+", line))))
            
        new_seeds = []
        
        while len(seeds) > 0:
            start, end = seeds.pop()
            
            for destination, source, length in range_list:
                overlap_start = max(start, source)
                overlap_end = min(end, source+length)
            
                if overlap_start < overlap_end:
                    new_seeds.append([overlap_start - source + destination, overlap_end - source + destination])
                    if overlap_start > start:
                        seeds.append([start, overlap_start])
                    if overlap_end < end:
                        seeds.append([overlap_end, end])
                    break
            else:
                new_seeds.append([start, end])
                
        seeds = new_seeds
            
    print(min(seeds)[0])
            
if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.read()
    
    part1(lines)
    part2(lines)
        

def analize(lines, part):
    total = 0
    lines = lines.strip().split("\n")
    for line in lines:
        dataset = line.strip().split(" ")
        end_values = []
        
        while not all(v == 0 for v in dataset):
            if part == 1:
                end_values.append(int(dataset[-1]))
            elif part == 2:
                end_values.append(int(dataset[0]))
            new_dataset = []
            for i in range(len(dataset)-1):
                diff = int(dataset[i+1]) - int(dataset[i])
                new_dataset.append(diff)
            dataset = new_dataset
        
        if part == 1:
            total += sum(end_values)
        elif part == 2:
            new_value = end_values[0]
            temp = 1
            for val in end_values[1:]:
                if temp == 1:
                    new_value -= val
                    temp = 0
                else:
                    new_value += val
                    temp = 1
            total += new_value
    
    print(total)

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.read()

    analize(lines, 1)
    analize(lines, 2)
        
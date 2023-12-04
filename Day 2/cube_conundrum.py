import re



if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    
    # part 1
    # ground = {"red":12, "green":13, "blue":14}
    # sum = 0
    # for line in lines:
    #     texts = line.split(":")
    #     game_id = int(re.findall(r"\d+", texts[0])[0])
    #     red = re.findall(r"(\d+) red", texts[1])
    #     red = [eval(i) for i in red]
    #     green = re.findall(r"(\d+) green", texts[1])
    #     green = [eval(i) for i in green]
    #     blue = re.findall(r"(\d+) blue", texts[1])
    #     blue = [eval(i) for i in blue]
    #     if max(red) <= ground["red"] and max(green) <= ground["green"] and max(blue) <= ground["blue"]:
    #         sum += game_id
    # print(sum)
    
    # part 2
    sum = 0
    for line in lines:
        texts = line.split(":")
        red = re.findall(r"(\d+) red", texts[1])
        red = [eval(i) for i in red]
        green = re.findall(r"(\d+) green", texts[1])
        green = [eval(i) for i in green]
        blue = re.findall(r"(\d+) blue", texts[1])
        blue = [eval(i) for i in blue]
        sum += max(red) * max(green) * max(blue)
    print(sum)
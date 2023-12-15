
import re

def hash(word):
    value = 0
    for i in word:
        value += ord(i)
        value *= 17
        value %= 256
    return value

def sumHash(inp):
    sum = 0
    words = inp.strip().split(",")
    for word in words:
        sum += hash(word)
    print(sum)

def sumFocusPower(inp):
    words = inp.strip().split(",")
    boxes = {}
    for word in words:
        label = re.findall(r"[a-z]+", word)[0]
        l_hash = hash(label)
        if "-" in word:
            if l_hash in boxes.keys() and label in boxes[l_hash].keys():
                del boxes[l_hash][label]
        elif "=" in word:
            power = word.split("=")[1]
            if l_hash not in boxes.keys():
                boxes[l_hash] = {}
            boxes[l_hash][label] = power
    
    totalPower = 0
    for boxKey in boxes.keys():
        slot = 1
        for label in boxes[boxKey].keys():
            totalPower += (boxKey+1) * (slot) * int(boxes[boxKey][label])
            slot += 1
    print(totalPower)

if __name__ == "__main__":
    file = open("input.txt", "r")
    inp = file.read()

    sumHash(inp)
    sumFocusPower(inp)
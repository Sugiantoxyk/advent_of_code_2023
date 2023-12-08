
class Node:
    def __init__(self, hand, bid, type_strength):
        self.hand = hand
        self.bid = int(bid)
        self.type_strength = type_strength
        self.left = None
        self.right = None

def getTypeStrength(hand, part):
    # use a list to accumulate the counter of each card appear in the hand
    # calculate strength by the counter
    counter = {"2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "T":0, "J":0, "Q":0, "K":0, "A":0}
    strength = 0
    for card in hand:
        counter[card] += 1
        if part == 2 and card == "J":
            continue
        if counter[card] == 2:
            strength += 1
        elif counter[card] == 3:
            strength += 2
        elif counter[card] == 4:
            strength += 2
        elif counter[card] == 5:
            strength += 1
    
    # only applicable to part 2 of the question
    # add the counter of J's to the second highest card, and recalculate the strength
    if part == 2 and counter["J"] != 0:
        iter = counter["J"]
        counter["J"] = 0
        max_value = max(counter.values())
        for i in range(iter):
            max_value += 1
            if max_value == 2:
                strength += 1
            elif max_value == 3:
                strength += 2
            elif max_value == 4:
                strength += 2
            elif max_value == 5:
                strength += 1
    
    return strength

def isStronger(hand1, hand2, part):
    # if both hand are the same type
    # proceed to check which is stronger by checking card from left to right
    strength_map = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
    if part == 2:
        strength_map["J"] = 1
    for i in range(len(hand1)):
        if strength_map[hand1[i]] > strength_map[hand2[i]]:
            return True
        elif strength_map[hand1[i]] < strength_map[hand2[i]]:
            return False
    return True

def calculateBid(node, rank):
    sum = 0
    if node.left != None:
        total, rank = calculateBid(node.left, rank)
        sum += total
    sum += node.bid * rank
    rank += 1
    if node.right != None:
        total, rank = calculateBid(node.right, rank)
        sum += total
    return sum, rank

def getWinnings(lines, part):
    hand_bid_pairs = lines.split("\n")
    
    # tree sort
    head_node = None
    for hand_bid_pair in hand_bid_pairs:
        hand, bid = hand_bid_pair.split()
        node = Node(hand, bid, getTypeStrength(hand, part))
        if head_node == None: # only for 1st interation
            head_node = node
            continue
        
        cur_node = head_node
        while True:
            if node.type_strength > cur_node.type_strength:
                if cur_node.right == None:
                    cur_node.right = node
                    break
                else:
                    cur_node = cur_node.right
            elif node.type_strength < cur_node.type_strength:
                if cur_node.left == None:
                    cur_node.left = node
                    break
                else:
                    cur_node = cur_node.left
            else:
                if isStronger(node.hand, cur_node.hand, part):
                    if cur_node.right == None:
                        cur_node.right = node
                        break
                    else:
                        cur_node = cur_node.right
                else:
                    if cur_node.left == None:
                        cur_node.left = node
                        break
                    else:
                        cur_node = cur_node.left
                        
    # calculate bid using recursive function
    rank = 1
    sum, rank = calculateBid(head_node, rank)
    print(sum)

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.read()
    
    getWinnings(lines, 1)
    getWinnings(lines, 2)
        

import math

class Broadcast:
    def __init__(self, name, out):
        self.name = name
        self.cur = 0
        self.out = out

class FlipFlop:
    def __init__(self, name, out):
        self.type = "%"
        self.name = name
        self.cur = 0
        self.out = out
    
    def sendInp(self, inp_name, pulse):
        if pulse == 0:
            self.cur = (self.cur+1)%2
            return True
        return False

class Conjunction:
    def __init__(self, name, inp, inp_p, out):
        self.type = "&"
        self.name = name
        self.inp = inp
        self.inp_p = inp_p
        self.cur = 1
        self.out = out
    
    def insertInp(self, name):
        self.inp.append(name)
        self.inp_p.append(0)
        
    def sendInp(self, inp_name, pulse):
        i = self.inp.index(inp_name)
        self.inp_p[i] = pulse
        if sum(self.inp_p) == len(self.inp_p): self.cur = 0
        else: self.cur = 1
        return True
        
    def print(self):
        print("&",self.name,self.inp,"->",self.out)

def part1(mod_dict):    
    high = 0
    low = 0
    for _ in range(1_000):
        low += 1
        q = ["broadcaster"]
        while q:
            sender = q[0]
            del q[0]
            for receiver in mod_dict[sender].out:
                if mod_dict[sender].cur == 1: high += 1
                else: low += 1
                if receiver not in mod_dict: continue
                cont = mod_dict[receiver].sendInp(sender, mod_dict[sender].cur)
                if cont:
                    q.append(receiver)
    print("Part 1:", low * high)
    
def part2(mod_dict, last_mod):
    
    print()

if __name__ == "__main__":
    file = open("input.txt", "r")
    inp = file.read()
    modules = inp.strip().splitlines()
    
    mod_dict = {}
    conj_list = []
    last_mod = ""
    # create a dictionary for easy access
    for module in modules:
        name, outputs = module.split(" -> ")
        outputs = outputs.split(", ")
        if name[0] == "%":
            mod_dict[name[1:]] = FlipFlop(name[1:], outputs)
        elif name[0] == "&":
            mod_dict[name[1:]] = Conjunction(name[1:], [], [], outputs)
            conj_list.append(name[1:])
        else:
            mod_dict[name] = Broadcast(name, outputs)
    # another iteration to add all the input modules for Conjunction module
    for module in modules:
        name, outputs = module.split(" -> ")
        if name[0] == "%" or name[0] == "&": name = name[1:]
        outputs = outputs.split(", ")
        for output in outputs:
            if output == "rx":
                last_mod = name
            if output in conj_list:
                mod_dict[output].insertInp(name)
                        
    part1(mod_dict)
    part2(mod_dict, last_mod)
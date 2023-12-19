
import re
import copy

def part1(parts, workflows_dict):
    total = 0
    part_index = {"x":0, "m":1, "a":2, "s":3}
    # iterate through all parts
    for part in parts:
        part_nums = [eval(i) for i in re.findall(r"[0-9]+", part)]
        workflow_name = "in"
        while workflow_name != None:
            workflow_steps = workflows_dict[workflow_name]
            for step_i in range(len(workflow_steps)):
                if step_i == len(workflow_steps)-1:
                    # the last step
                    workflow_name = workflow_steps[step_i]
                else:
                    # the intermediate step
                    step, workflow_name = workflow_steps[step_i].split(":")
                    if step[1] == ">":
                        if part_nums[part_index[step[0]]] > int(step[2:]): 
                            break
                    elif step[1] == "<":
                        if part_nums[part_index[step[0]]] < int(step[2:]): 
                            break
            if workflow_name == "A":
                total += sum(part_nums)
                break
            elif workflow_name == "R":
                break
    print(total)

def combination(part_range):
    total = 1
    for lower, upper in part_range.values():
        total *= (upper+1-lower)
    return total

def getRange(range_list, workflows_dict, part_range, name):
    total = 0
    true_part_range = copy.deepcopy(part_range)
    false_part_range = copy.deepcopy(part_range)
    steps = workflows_dict[name]
    for step_num in range(len(steps)):
        true_part_range = copy.deepcopy(false_part_range)
        step = steps[step_num]
        if step_num == len(steps)-1:
            # the last step
            if step == "R":
                continue
            elif step == "A":
                total += combination(true_part_range)
            else:
                total += getRange(range_list, workflows_dict, true_part_range, step)
        else:
            # the intermediate step
            rule, result = step.split(":")
            num = int(rule[2:])
            if rule[1] == ">":
                true_part_range[rule[0]][0] = num+1
                false_part_range[rule[0]][1] = num
            elif rule[1] == "<":
                true_part_range[rule[0]][1] = num-1
                false_part_range[rule[0]][0] = num

            if result == "R":
                continue
            elif result == "A":
                total += combination(true_part_range)
            else:
                total += getRange(range_list, workflows_dict, true_part_range, result)
    return total

def part2(workflows_dict):    
    part_range = {"x":[1,4000], "m":[1,4000], "a":[1,4000], "s":[1,4000]}
    name = "in"
    range_list = []
    total = getRange(range_list, workflows_dict, part_range, name)
    print(total)

if __name__ == "__main__":
    file = open("input.txt", "r")
    inp = file.read()
    puzzle = inp.strip().split("\n\n")
    parts = puzzle[1].strip().splitlines()
    
    workflows_dict = {}
    # store workflows in a dictionary
    for workflow in puzzle[0].strip().splitlines():
        workflow_list = re.findall(r"[^{},]+", workflow)
        workflows_dict[workflow_list[0]] = workflow_list[1:]
    
    part1(parts, workflows_dict)
    part2(workflows_dict)
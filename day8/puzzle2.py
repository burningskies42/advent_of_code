import re


def exec_command(cmnd):
    global accumulator
    operation = cmnd.split(" ")[0]
    quantifier = int(re.findall(r"-?\d+", cmnd)[0])

    if operation == "acc":
        accumulator += quantifier
        return 1
    elif operation == "nop":
        return 1
    elif operation == "jmp":
        return quantifier


def run_app(line_id):
    past_steps = [0]
    i = 0

    fixed_list = commands_list.copy()
    if "nop" in fixed_list[line_id]:
        fixed_list[line_id] = fixed_list[line_id].replace("nop", "jmp")
    elif "jmp" in fixed_list[line_id]:
        fixed_list[line_id] = fixed_list[line_id].replace("jmp", "nop")
    else:
        return False

    while i < len(commands_list):
        step = exec_command(fixed_list[i])
        if i + step in past_steps:
            print(i+step)
            return False
        else:
            past_steps.append(i + step)
            i = i + step

    return True


commands_list = open("input.txt", "r").read().split("\n")
flag = False
cmnd_id = 0

while not flag:
    accumulator = 0
    cmnd_id += 1
    flag = run_app(cmnd_id)

print(cmnd_id-1)        
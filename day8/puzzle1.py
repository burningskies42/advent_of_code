import re

def exec_command(cmnd):
    global accumulator
    operation = cmnd.split(" ")[0]
    quantifier = int(re.findall(r"-?\d+", cmnd)[0])

    if operation == "acc":
        accumulator+= quantifier
        return 1
    elif operation == "nop":
        return 1
    elif operation == "jmp":
        return quantifier


accumulator = 0
past_steps = [0]
i = 0
commands_list = open("input.txt", "r").read().split("\n")

while True:
    step = exec_command(commands_list[i])
    if i + step in past_steps:
        print(i+step)
        break
    else:
        past_steps.append(i + step)
        i = i + step
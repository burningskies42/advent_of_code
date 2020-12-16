import re

raw_data = open("input.txt", "r").read().split("\n")

requirements_dict = {re.findall(r"^(.*) bags contain", line)[0]: re.findall(r"(\d)([\w\s]*) bag", line) for line in raw_data}
requirements_dict = {k: {v1[1].strip():v1[0] for v1 in v} for k, v in requirements_dict.items()}

def count_gold(color):
    if color == "shiny gold":
        return True
    else:
        return any([count_gold(k) for k in requirements_dict[color].keys()])

print(sum([count_gold(k) for k in requirements_dict.keys()])-1)
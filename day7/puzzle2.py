import re


raw_data = open("/home/leon/repos/advent_of_code/day7/input.txt", "r").read().split("\n")

requirements_dict = {re.findall(r"^(.*) bags contain", line)[0]: re.findall(r"(\d)([\w\s]*) bag", line) for line in raw_data}
requirements_dict = {k: {v1[1].strip():v1[0] for v1 in v} for k, v in requirements_dict.items()}

def count_contents(color):
    return 1 + sum([int(v)*count_contents(k) for k, v in requirements_dict[color].items()])

print(count_contents("shiny gold") -1)
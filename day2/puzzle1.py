import numpy as np

def check_rule(text):
    rule, pwd = text.split(":")
    rule_range, rule_letter = rule.split(" ")
    rule_range = rule_range.split("-")
    rule_range = list(map(int, rule_range))

    try:
        if rule_range[0] <= pwd.count(rule_letter) <= rule_range[1]:
            return True
        else:
            return False
    except Exception as e:
        raise e

data = open("input.txt", "r").read().split("\n")
print(sum(list(map(check_rule, data))))

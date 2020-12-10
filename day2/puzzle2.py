

def check_policy(text):
    rule, pwd = text.split(": ")
    rule_indices, rule_letter = rule.split(" ")
    rule_indices = list(map(int, rule_indices.split("-")))
    try:
        return sum([1 if pwd[i-1] == rule_letter else 0 for i in rule_indices ]) == 1
    except Exception as e:
        print(pwd)
        print(rule_indices)
        print([pwd[i-1] for i in rule_indices])
        raise e

data = open("input.txt", "r").read().split("\n")
print(sum(list(map(check_policy, data))))
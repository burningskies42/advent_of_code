from collections import Counter

data = open("input.txt", "r").read().split("\n")
data = sorted([int(d) for d in data if len(d) > 0])
data.insert(0, 0)
data.append(data[-1]+3)

sol = {0:1}
for line in sorted(data[1:]):
    sol[line] = 0
    if line - 1 in sol:
        sol[line] += sol[line-1]
    if line - 2 in sol:
        sol[line] += sol[line-2]
    if line - 3 in sol:
        sol[line] += sol[line-3]

print(sol[max(data)])

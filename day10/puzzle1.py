from collections import Counter


data = open("input.txt", "r").read().split("\n")
data = sorted([int(d) for d in data if len(d) > 0])
data.insert(0, 0)
data.append(data[-1]+3)
diffs = [data[i+1] - data[i] for i in range(len(data) - 1)]
diffs_dict = dict(Counter(diffs))
print(diffs_dict[1]*diffs_dict[3])


raw_data = open("input.txt", "r").read().split("\n\n")
data_list = [[set(r1) for r1 in r.split("\n")] for r in raw_data]
data_list = [(set.intersection(*r)) for r in data_list]
data_len_list = [len(list(r)) for r in data_list]

print(sum(data_len_list))

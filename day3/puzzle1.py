import math
import os

try:
    os.remove("output.txt")
except:
    pass

forest_list = open("input.txt", "r").read().split("\n")
cnt_trees = 0

for i, row in enumerate(forest_list):
    mult = math.ceil((1+i*3)/ (len(row)-1))
    full_row = list(row*mult)
    try:
        if full_row[i*3] == "#":
            full_row[i*3] = "X"
            cnt_trees+=1
        else:
            full_row[i*3] = "O"
        with open("output.txt", "a") as f:
            f.write("".join(full_row)+"\n")
    except Exception as e:
        print(full_row)
        print(1+(i*3))
        print(e)

print(cnt_trees)



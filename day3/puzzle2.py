import math
import os


forest = open("input.txt", "r").read().split("\n")

def check_slope(slope):
    try:
        os.remove("output.txt")
    except:
        pass
    
    right, down = slope 
    cnt_trees = 0
    for i, row in zip(range(0, len(forest), down), forest):
        mult = math.ceil((1+i*right)/ (len(row)-1))
        full_row = list(row*mult)
        try:
            if full_row[i*right] == "#":
                full_row[i*right] = "X"
                cnt_trees+=1
            else:
                full_row[i*right] = "O"
            with open("output.txt", "a") as f:
                f.write("".join(full_row)+"\n")
        except Exception as e:
            raise e
    return cnt_trees

slopes = [
    [1, 1],
    [3, 1], 
    [5, 1],
    [7, 1],
    [1, 2]
]

math.prod(list(map(check_slope, slopes)))


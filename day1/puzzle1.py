import os

# read in data as list and sort
data = open("input.csv", "r").read()
data = sorted([int(d) for d in data.split('\n') if len(d)>0])

for i, num in enumerate(data):
    for j in range(i, len(data), 1):
        if data[i] + data[j] == 2020:
            print(f"{data[i]} + {data[j]} == 2020")
            print(f"{data[i]} * {data[j]} == {data[i]*data[j]}")
        elif data[i] + data[j] > 2020:
            break



def is_valid(preamble):
    num = preamble[-1]
    preamble = sorted(preamble[:-1])
    for i in range(len(preamble)):
        for j in range(i+1, len(preamble), 1):
            if preamble[i] + preamble[j] == num:
                return True
    return False


raw_data = [int(i) for i in open("/home/leon/repos/advent_of_code/day9/input.txt", "r").read().split("\n")]

for i in range(len(raw_data)-24):
    if not is_valid(raw_data[i:i+26]):
        print(raw_data[i+25])
        break


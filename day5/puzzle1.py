

def assign_seat(half, seat_range):
    range_len = len(seat_range)
    if half in ["F", "L"]:
        return seat_range[:int(range_len/2)]
    elif half in ["B", "R"]:
        return seat_range[int(range_len/2):]

def deduce_seat(boarding_pass_str):
    seat_row = list(range(128))
    seat_col = list(range(8))

    for l in boarding_pass_str[:7]:
        seat_row = assign_seat(l, seat_row)

    for l in boarding_pass_str[7:]:
        seat_col = assign_seat(l, seat_col)

    return 8*seat_row[0] + seat_col[0]


all_boarding_passes = open("input.txt", "r").read().split("\n")
all_boarding_passes = sorted(list(map(deduce_seat, all_boarding_passes)))
puzzle1 = all_boarding_passes[-1]
print(f"puzzle1: {puzzle1}")

puzzle2 = set(range(all_boarding_passes[0], all_boarding_passes[-1])) - set(all_boarding_passes)
print(f"puzzle2: {list(puzzle2)[0]}")

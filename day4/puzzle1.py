
raw_data = open("input.txt", "r").read().split("\n\n")
necessary_fields ={"byr","iyr","eyr","hgt","hcl","ecl","pid"}
cnt = 0

for r in raw_data:
    r = r.replace('\n'," ")
    passport_data = [elem.split(":")[0] for elem in r.split(" ")]
    passport_keys_set = set(filter(lambda x: len(x)>0, passport_data))
    if len(necessary_fields - passport_keys_set) == 0:
        cnt+=1
    # else:
print(cnt)


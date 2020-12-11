import re


def valid_pass(passport_dict):

    if len({"byr","iyr","eyr","hgt","hcl","ecl","pid"} - set(passport_dict.keys())) > 0:
        return False
    try:
        byr = 1920 <= int(passport_dict["byr"]) <= 2002
        iyr = 2010 <= int(passport_dict["iyr"]) <= 2020
        eyr = 2020 <= int(passport_dict["eyr"]) <= 2030
        
        if "cm" in passport_dict["hgt"]:
            hgt = "".join([i for i in passport_dict["hgt"] if i.isdigit()])
            hgt = 150 <= int(hgt) <= 193
        elif "in" in passport_dict["hgt"]:
            hgt = "".join([i for i in passport_dict["hgt"] if i.isdigit()])
            hgt = 59 <= int(hgt) <= 76
        else:
            hgt = False

        hcl = re.match(r"#[a-zA-Z0-9]{6}", passport_dict["hcl"]) is not None
        ecl = re.match(r"amb|blu|brn|gry|grn|hzl|oth", passport_dict["ecl"]) is not None
        
        pid = (len(passport_dict["pid"]) == 9) and (passport_dict["pid"].isnumeric())

        return all([byr, iyr, eyr, hgt, hcl, ecl, pid])
    except Exception as e:
        print(passport_dict)
        raise(e)

def parse_passport(raw_text):
    raw_text = raw_text.replace('\n'," ")
    passport_data = [elem.split(":") for elem in raw_text.split(" ") if len(elem)>0]
    return {i[0]:i[1] for i in passport_data}


data = open("input.txt", "r").read().split("\n\n")
raw_data = open("input.txt", "r").read().split("\n\n")
print(sum([valid_pass(parse_passport(r)) for r in raw_data]))

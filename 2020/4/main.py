import data
import re

passports = data.input().split('\n\n')

pattern = '(\w+):([\w#]+)'

passport_values = [re.findall(pattern, passport_section) for passport_section in passports]
        
def validate_field(key: str, value: str):
    if (key == "byr"):
        return 1920 <= int(value) <= 2002
    elif (key == "iyr"):
        return 2010 <= int(value) <= 2020
    elif (key == "eyr"):
        return 2020 <= int(value) <= 2030
    elif (key == "hgt"):
        if (value.endswith("cm")):
            return 150 <= int(value.rstrip("cm")) <= 193
        elif (value.endswith("in")):
            return 59 <= int(value.rstrip("in")) <= 76
        else:
            return False
    elif (key == "hcl"):
        return re.match("""^#[0-9a-f]{6}$""", value) != None
    elif (key == "ecl"):
        return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    elif (key == "pid"):
        return re.match("""^\d{9}$""", value) != None
    elif (key == "cid"):
        return True
    else:
        raise ValueError(f"key not found: {key}")


valid_count_part_one = sum(all (required_fields in dict(passport_value) for required_fields in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")) 
                        for passport_value in passport_values)

print(valid_count_part_one)

valid_count_part_two = sum(  all (required_fields in dict(passport_value) for required_fields in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")) and 
                        (all (validate_field(key, value) for key, value in dict(passport_value).items()))
                        for passport_value in passport_values)

print(valid_count_part_two)



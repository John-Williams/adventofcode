import data
import re
from typing import List
from dataclasses import dataclass

@dataclass
class PasswordPolicy:
    min_count: int
    max_count: int
    char: str
    password: str


lines = iter(data.input().splitlines())
pattern = '(\d+)-(\d+)\s([a-z]):\s(\w+)'

all_policies = []


for line in lines:
    matches = re.search(pattern, line)
    if matches:
        all_policies.append(PasswordPolicy(min_count=int(matches.group(1)), max_count=int(matches.group(2)), char=matches.group(3), password=matches.group(4)))
    else:
        print(f"This line didn't match the regex: {line}")


def validate_policy_part_one(pol : PasswordPolicy):
    char_count = pol.password.count(pol.char)
    return ((char_count >= pol.min_count) and (char_count <= pol.max_count))

def validate_policy_part_two(pol : PasswordPolicy):
    first_char = pol.password[pol.min_count - 1]
    second_char = pol.password[pol.max_count - 1]
    #print(f"password: {pol.password} min_count: {pol.min_count} first_char: {first_char} max_count: {pol.max_count} second_char: {second_char}")    
    first_char_matches = first_char == pol.char
    second_char_matches = second_char == pol.char
    return (first_char_matches ^ second_char_matches) # ^ is XOR


valid_policy_count_part_one = 0
valid_policy_count_part_two = 0

for policy in all_policies:
    if (validate_policy_part_one(policy)):
        valid_policy_count_part_one += 1
    if (validate_policy_part_two(policy)):
        valid_policy_count_part_two += 1

print(valid_policy_count_part_one)
print(valid_policy_count_part_two)





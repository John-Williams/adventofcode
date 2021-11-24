import data
import re

input_lines = data.input().splitlines()

#input_lines = ["pale chartreuse bags contain 3 shiny gold bags.", "posh black bags contain 3 pale chartreuse bags, 3 mirrored coral bags, 1 dotted chartreuse bag."]

bag_rules = []

for line in input_lines:
    matches = re.match('^(\w+\s\w+)\sbags contain\s', line)
    if (not matches):
        raise ValueError("Regex didn't match")

    first_part_of_string = matches[0]
    first_bag_name = matches[1]

    rest_of_string = line[len(first_part_of_string):].rstrip('.')

    contains_bags = re.findall('(\d+)\s(\w+\s\w+)\s', rest_of_string)

    bag_rules.append((first_bag_name, contains_bags))


def get_parents(bag_name: str):
    return list(filter(lambda rule:  bag_name in [r[1] for r in rule[1]], bag_rules))

all_parents_names = []

def find_all(parent_name: str):
    parents = get_parents(parent_name)    
    all_parents_names.extend([parent[0] for parent in parents])    
    
    for parent in parents:
        find_all(parent[0])


find_all("shiny gold")

distinct_parents = set(all_parents_names)

print(f"part one: {len(distinct_parents)}")

#------------ part 2. not complete.

bag_count = 0
for parent_name in distinct_parents:
    children = [bag_rule[1] for bag_rule in bag_rules if bag_rule[0] == parent_name]
    bag_count = bag_count + 1 + sum([int(child[0]) for child in children[0]]) #this needs work

print(f"part two: {bag_count}")



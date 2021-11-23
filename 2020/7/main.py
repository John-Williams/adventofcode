import data
import re

input_lines = data.input().splitlines()

#input_lines = ["pale chartreuse bags contain 3 faded orange bags.", "posh black bags contain 3 dark lavender bags, 3 mirrored coral bags, 1 dotted chartreuse bag."]

bag_rules = []

for line in input_lines:
    matches = re.match('^(\w+\s\w+)\sbags contain\s', line)
    if (not matches):
        raise ValueError("Regex didn't match")

    first_part_of_string = matches[0]
    first_bag_name = matches[1]

    rest_of_string = line[len(first_part_of_string):].rstrip('.')

    #print(f"first_bag: {first_bag_name} rest of string: {rest_of_string}")

    contains_bags = re.findall('(\d+)\s(\w+\s\w+)\s', rest_of_string)

    #print(contains_bags)
    bag_rules.append((first_bag_name, contains_bags))

#print(bag_rules)
#print(dict(bag_rules[0][1]).values())


def get_parents(bag_name: str):
    return list(filter(lambda rule:  bag_name in dict(rule[1]).values(), bag_rules))

parent_count = 0


#recursive func goes here

while True:
    parents = get_parents('shiny gold')
    if (len(parents) == 0):
        break
    parent_count += len(parents)
    for parent in parents



print(parents)

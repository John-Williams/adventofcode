import data
from math import ceil
from dataclasses import dataclass
from operator import mul
from functools import reduce

input_lines = data.input().splitlines()

def expand_line(original_map: str, character_index_required: int):
    map_length = len(original_map)
    if (character_index_required <= (map_length -1)):
        return original_map
    else:
        number_of_copies = ceil((character_index_required + 1) / map_length)
        #print(f"number_of_copies: {number_of_copies} char_index_reqd:{character_index_required} map: {original_map}")
        return original_map * number_of_copies

@dataclass
class RouteDownMountain:
    right: int
    down: int = 1
    tree_count: int = 0


routes = [RouteDownMountain(1),
            RouteDownMountain(3),
            RouteDownMountain(5),
            RouteDownMountain(7),
            RouteDownMountain(1,2)]


for route in routes:
    line_number = 0
    char_index = 0
    tree_count = 0

    for line in input_lines:
        even_line_number = ((line_number % 2) == 0)
        check_row = (route.down == 1 or even_line_number)
        if check_row:
            expanded_line = expand_line(line, char_index)  
            char_at_index = expanded_line[char_index]
            if (char_at_index == "#"):
                tree_count += 1
            char_index += route.right
        line_number += 1

    route.tree_count = tree_count
    
totals = []
    
for route in routes:
    print(f"Route: {route} Tree count {route.tree_count}")
    totals.append(route.tree_count)

grand_total = reduce(mul, totals)
print(f"Total : {grand_total}")




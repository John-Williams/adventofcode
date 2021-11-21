import data

input_lines = data.input().splitlines()

#input_lines = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

def row_split(lower_half : bool, start_index: int, row_count: int):   
    if (lower_half):
        return start_index, row_count / 2
    row_count /= 2
    return start_index + row_count, row_count    

def get_place(code: str, max_count: int, lower_char: str):
    place_start_index = 0
    place_count = max_count

    for code_char in code:
        place_start_index, place_count = row_split((code_char == lower_char), place_start_index, place_count)

    return int(place_start_index)
    
def get_seats(line: str):
    row_id = get_place(line[0: 7], 128, "F")
    column_id = get_place(line[7:], 8, "L")
    seat_id = row_id * 8 + column_id
    return row_id, column_id, seat_id


seats = [get_seats(line) for line in input_lines]

print(f"Seat with max seat_id: {max(seats, key=lambda s: s[2])}")

#part two -----------------------------------------------------------------------------------------

for row_number in range(128):
    seats_in_this_row = list(filter(lambda s: (s[0] == row_number), seats))
    if (seats_in_this_row):
        print(sorted(seats_in_this_row, key=lambda s: s[1]))


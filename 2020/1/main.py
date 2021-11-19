import data

input = data.input()

def get_sum_for_two_numbers():
    for x in input:
        for y in input:
            if ((x + y) == 2020):
                return x * y


def get_sum_for_three_numbers():
    for x in input:
        for y in input:
            for z in input:
                if ((x + y + z) == 2020):
                    return x * y * z

print(get_sum_for_two_numbers())

print(get_sum_for_three_numbers())
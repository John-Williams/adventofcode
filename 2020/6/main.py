import data

input = data.input().split('\n\n')

def get_unique_answers(answers):
    answer_set = set(answers)
    answer_set.discard('\n')
    return len(answer_set)

answer_count_per_group = [get_unique_answers(answers) for answers in input]

print(f"Total: {sum(answer_count_per_group)}")

## part 2 ---------------------------

def get_duplicate_answers(answers: str):
    group_size = answers.count('\n') + 1
    answer_set = set(answers)
    answer_set.discard('\n')
    
    duplicate_answers = [answer for answer in answer_set if answers.count(answer) == group_size]

    return len(duplicate_answers)

duplicate_answers_in_group = [get_duplicate_answers(answers) for answers in input]

print(duplicate_answers_in_group)
print(f"Total: {sum(duplicate_answers_in_group)}")
'''
However, the TSP is unique in that we need to include all locations exactly one time.
To abide by this rule, we can use a special breeding function called ordered crossover.
In ordered crossover, we randomly select a subset of the first parent string.
'''
import random


def crossover_of_two(sol_one, sol_two):
    split_start = random.randint(0, 100)
    split_count = random.randint(15, 25)

    new_sol_two = []
    new_sol_one = []
    new_sol_one.extend(sol_one[split_start:split_start + split_count])
    new_sol_two.extend(sol_two[split_start:split_start + split_count])

    for two_elm in sol_two:
        for one_elm in sol_one[split_start:split_start + split_count]:
            if two_elm[0] == one_elm[0]:
                new_sol_one.append(two_elm)

    for one_elm in sol_one:
        for two_elm in sol_two[split_start:split_start + split_count]:
            if one_elm[0] == two_elm[0]:
                new_sol_two.append(one_elm)

    return [new_sol_one, new_sol_two]

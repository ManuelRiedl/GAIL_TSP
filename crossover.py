'''
However, the TSP is unique in that we need to include all locations exactly one time.
To abide by this rule, we can use a special breeding function called ordered crossover.
In ordered crossover, we randomly select a subset of the first parent string.
'''
import random

SPLIT_START = random.randint(0, 100)
SPLIT_COUNT = random.randint(15, 25)


def crossover_of_two(sol_one, sol_two):
    new_sol_two = []
    new_sol_one = []
    new_sol_one.extend(sol_one[SPLIT_START:SPLIT_START + SPLIT_COUNT])
    new_sol_two.extend(sol_two[SPLIT_START:SPLIT_START + SPLIT_COUNT])

    counter = SPLIT_START
    for two_elm in sol_two:
        for one_elm in sol_one[SPLIT_START:SPLIT_START + SPLIT_COUNT]:
            if two_elm[0] == one_elm[0]:
                new_sol_one.append(two_elm)
                counter += 1

    counter = SPLIT_START
    for one_elm in sol_one:
        for two_elm in sol_two[SPLIT_START:SPLIT_START + SPLIT_COUNT]:
            if one_elm[0] == two_elm[0]:
                new_sol_two.append(one_elm)
                counter += 1

    return sol_one, sol_two

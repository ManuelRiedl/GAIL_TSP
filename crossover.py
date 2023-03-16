'''
However, the TSP is unique in that we need to include all locations exactly one time.
To abide by this rule, we can use a special breeding function called ordered crossover.
In ordered crossover, we randomly select a subset of the first parent string
and then fill the remainder of the route with the genes from the second parent 
in the order in which they appear, without duplicating any genes in the selected subset
 from the first parent
'''
import random


def crossover_of_two(sol1, sol2):
    length = len(sol1)
    kept_cities = []
    new_cities_in_order = []
    split_start = random.randint(0, 99)
    split_end = split_start + random.randint(15, 25)

    # keep cities within split_start and split_end
    for i in range(split_start, split_end):
        kept_cities.append(sol1[i % length])

    # fill rest of the cities in order
    for item in sol2:
        if item not in kept_cities:
            new_cities_in_order.append(item)

    return kept_cities + new_cities_in_order

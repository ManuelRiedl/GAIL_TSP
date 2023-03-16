'''
    mutation.py
    mutate a solution by swapping two adjacent cities a random number of times 
'''
import random

MUTATION_RATE = 0.07    # 7%


def mutation(solutions):
    max_number_of_swaps = int(len(solutions) * MUTATION_RATE)
    for solution in solutions:
        number_of_swaps = random.randint(0, max_number_of_swaps)
        for _ in range(number_of_swaps):
            index1 = random.randint(0, len(solution) - 1)
            index2 = (index1 + 1) % len(solution)
            solution[index1], solution[index2] = solution[index2], solution[index1]

    return solutions

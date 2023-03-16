import csv
import random
import numpy as np
from geopy import distance

CITIES_FILE = './european_cities.csv'
NUMBER_OF_SOLUTIONS = 80
NUMBER_OF_SELECTED_SOLUTIONS = 4  # should be even (as of now)
NUMBER_OF_GENERATIONS = 300

MUTATION_RATE = 0.04  # 7%


def random_exponential_pdf(lam=8):
    return min(int(np.random.exponential(1 / lam) * 100), 99)


def distance_between_two_cities(city1, city2):
    return distance.geodesic((city1[1], city1[2]), (city2[1], city2[2])).km


def load_cities():
    cities = []
    with open(CITIES_FILE, 'r') as csvfile:
        # skip header
        csvfile.readline()
        for row in csv.reader(csvfile, delimiter=','):
            cities.append([row[0], float(row[1]), float(row[2])])
    return cities


def generate_random_solutions(cities, number_of_solutions):
    solutions = []
    for _ in range(number_of_solutions):
        solution = list(cities)
        random.shuffle(solution)
        solutions.append(solution)
    return solutions


def get_two_random_solutions(solutions):
    i_1 = random_exponential_pdf()
    while True:
        i_2 = random_exponential_pdf()
        if i_2 != i_1:
            break
    return solutions[i_1], solutions[i_2]


def fitness(solution, distance_matrix):
    score = 0
    for i in range(len(solution) - 2):
        score += distance_matrix[solution[i][0]][solution[i + 1][0]]
    score += distance_between_two_cities(solution[-1], solution[0])
    return score


def crossover(sol1, sol2):
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


def mutation(solutions):
    max_number_of_swaps = int(len(solutions) * MUTATION_RATE)
    for solution in solutions:
        number_of_swaps = random.randint(0, max_number_of_swaps)
        for _ in range(number_of_swaps):
            index1 = random.randint(0, len(solution) - 1)
            index2 = (index1 + 1) % len(solution)
            solution[index1], solution[index2] = solution[index2], solution[index1]

    return solutions

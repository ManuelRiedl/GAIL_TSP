import csv
from random_solution_generator import *
from mutation import *
from crossover import *
from numpy import random
from geopy import distance

CITIES_FILE = './european_cities.csv'
NUMBER_OF_SOLUTIONS = 80
NUMBER_OF_SELECTED_SOLUTIONS = 4  # should be even (as of now)
NUMBER_OF_GENERATIONS = 300


def get_two_random_solutions(solutions):
    i_1 = random_exponential_pdf()
    while True:
        i_2 = random_exponential_pdf()
        if i_2 != i_1:
            break
    return solutions[i_1], solutions[i_2]


def random_exponential_pdf(lam=8):
    return min(int(random.exponential(1 / lam) * 100), 99)


def distance_between_two_cities(city1, city2):
    return distance.geodesic((city1[1], city1[2]), (city2[1], city2[2])).km


def fitness(solution):
    score = 0
    for i in range(len(solution) - 2):
        score += distances[solution[i][0]][solution[i + 1][0]]
    score += distance_between_two_cities(solution[-1], solution[0])
    return score


def load_cities():
    cities = []
    with open(CITIES_FILE, 'r') as csvfile:
        # skip header
        csvfile.readline()
        for row in csv.reader(csvfile, delimiter=','):
            cities.append([row[0], float(row[1]), float(row[2])])
    return cities


cities = load_cities()
solutions = generate_solutions(cities, NUMBER_OF_SOLUTIONS)
''' prototype
N = number of solutions
n = number of top solutions to keep

repeat for X generations
    get random solutions
    determine fitness for each solution 
    selection
        selected = [n fittest solutions]
        repeat until len(selected) = N - n
            select 2 solutions
                the fitter the more likely to be chosen
                solutions already sorted by fitness => exponential PDF
            crossover for these 2 new solutions
            add these to selected
    mutate each solution
'''

# compute distance matrix as lookup table
distances = {}
for city1 in cities:
    # todo
    distances[city1[0]] = 0
    distances[city1[0]] = {}
    for city2 in cities:
        distances[city1[0]][city2[0]] = distance_between_two_cities(city1, city2)

for i in range(NUMBER_OF_GENERATIONS):
    # sort by fitness
    print("Generation ", i)
    solutions = sorted(solutions, key=lambda x: fitness(x))
    surviving_solutions = solutions[:NUMBER_OF_SELECTED_SOLUTIONS]
    print(f'Current Best: {fitness(surviving_solutions[0]):.2f} km')

    while (len(surviving_solutions) < 100):
        sol1, sol2 = get_two_random_solutions(solutions)
        cross_solutions = crossover_of_two(sol1, sol2)
        surviving_solutions.append(cross_solutions)

    solutions = mutation(surviving_solutions)

print('Best solution: {}'.format(solutions[0]))
print('Range: {}'.format(fitness(solutions[0])))

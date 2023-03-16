import csv
from geopy.geocoders import Nominatim

from fitness import *
from random_solution_generator import *
# from genetic_representation import *
from mutation import *
# from selection import *
from crossover import *

CITIES_FILE = './european_cities.csv'
NUMBER_OF_SOLUTIONS = 80
NUMBER_OF_SELECTED_SOLUTIONS = 5
NUMBER_OF_GENERATIONS = 100


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

for i in range(NUMBER_OF_GENERATIONS):
    # sort by fitness
    solutions = sorted(solutions, key=lambda x: fitness(x, cities))
    surviving_solutions = solutions[:NUMBER_OF_SELECTED_SOLUTIONS]
    # add crossovered solutions
    # crossovered_solutions = crossover(selected_solutions)
    # surviving_solutions.extend(crossover(surviving_solutions))
    mutated_solutions = mutation(surviving_solutions)

print('Best solution: {}'.format(solutions[0]))

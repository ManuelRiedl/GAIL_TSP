import csv
from geopy.geocoders import Nominatim

from fitness import *
from generate_solutions import *
from genetic_representation import *
from mutation import *
from selection import *
from crossover import *

CITIES_FILE = './european_cities.csv'
NUMBER_OF_SOLUTIONS = 15
NUMBER_OF_SELECTED_SOLUTIONS = 4


def load_cities():
    cities = []
    with open(CITIES_FILE, 'r') as csvfile:
        # skip header
        csvfile.readline()
        for row in csv.reader(csvfile, delimiter=','):
            cities.append([row[0], float(row[1]), float(row[2])])
    return cities


# prototype of first iteration
cities = load_cities()
solutions = generate_solutions(cities, NUMBER_OF_SOLUTIONS)
solutions = sorted(solutions, key=lambda x: fitness_function(x, cities))
selected_solutions = selection(solutions, NUMBER_OF_SELECTED_SOLUTIONS)
crossovered_solutions = crossover(selected_solutions)
mutated_solutions = mutation(crossovered_solutions)

print('Best solution: {}'.format(solutions[0]))

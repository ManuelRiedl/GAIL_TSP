import csv
from geopy.geocoders import Nominatim
import geopy.distance

from fitness import *
from random_solution_generator import *
# from genetic_representation import *
from mutation import *
# from selection import *
from crossover import *
import numpy as np
CITIES_FILE = './european_cities.csv'
NUMBER_OF_SOLUTIONS = 80
NUMBER_OF_SELECTED_SOLUTIONS = 10
NUMBER_OF_GENERATIONS = 20


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
    print("Generation ",i)
    solutions = sorted(solutions, key=lambda x: fitness(x))
    surviving_solutions = solutions[:NUMBER_OF_SELECTED_SOLUTIONS]
    print('Current Best: {}'.format(fitness(surviving_solutions[0])))
    while(len(surviving_solutions) < 100):
        i_1 = random.randint(0, NUMBER_OF_SELECTED_SOLUTIONS*2)
        while True:
            i_2 = random.randint(0, NUMBER_OF_SELECTED_SOLUTIONS*2)
            if i_2 != i_1:
                break

        cross_solutions = crossover_of_two(solutions[i_1],solutions[i_2])
        surviving_solutions.append(cross_solutions[0])
        surviving_solutions.append(cross_solutions[1])
    #selected_index = np.random.exponential(NUMBER_OF_SELECTED_SOLUTIONS, size=2)
    #crossover_solutions = crossover_of_two(surviving_solutions[selected_index[0]], surviving_solutions[selected_index[1]])
    # add crossovered solutions
    # crossovered_solutions = crossover(selected_solutions)
    # surviving_solutions.extend(crossover(surviving_solutions))
    mutated_solutions = mutation(surviving_solutions)
    solutions = mutated_solutions
print('Best solution: {}'.format(solutions[0]))
print('Range: {}'.format(fitness(solutions[0])))

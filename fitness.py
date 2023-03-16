'''
    fitness-function for TSP
    basic idea:
    sum of distances between all cities in the order they are visited
'''


def distance_between_two_cities(city1, city2):
    return ((city1[1] - city2[1]) ** 2 + (city1[2] - city2[2]) ** 2) ** 0.5


def fitness_function(solution, cities):
    fitness = 0
    for i in range(len(solution) - 2):
        fitness += distance_between_two_cities(
            cities[solution[i]], cities[solution[i + 1]])
    fitness += distance_between_two_cities(
        cities[solution[-1]], cities[solution[0]])
    # negate fitness => higher fitness (less distance) is better
    return fitness * -1

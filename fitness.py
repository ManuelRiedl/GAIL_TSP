'''
    fitness-function for TSP
    basic idea:
    sum of distances between all cities in the order they are visited
    maybe * -1 to get a maximization problem
'''


def distance_between_two_cities(city1, city2):
    return ((city1[2] - city2[2]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

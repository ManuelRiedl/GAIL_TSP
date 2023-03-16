'''
    fitness-function for TSP
    basic idea:
    sum of distances between all cities in the order they are visited
'''
import geopy.distance


def distance_between_two_cities(city1, city2):
    c_1 = (city1[1], city1[2])
    c_2 = (city2[1], city2[2])
    return geopy.distance.geodesic(c_1, c_2).km


def fitness(solution):
    score = 0
    for i in range(len(solution) - 2):
        score += distance_between_two_cities(solution[i], solution[i + 1])
    score += distance_between_two_cities(solution[-1], solution[0])
    return score

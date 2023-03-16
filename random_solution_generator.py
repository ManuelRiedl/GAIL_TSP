'''
    generate_solutions.py
    
    generates random solutions for the TSP problem
'''
import random


def generate_solutions(cities, number_of_solutions):
    solutions = []
    for _ in range(number_of_solutions):
        solution = list(cities)
        random.shuffle(solution)
        solutions.append(solution)
    return solutions

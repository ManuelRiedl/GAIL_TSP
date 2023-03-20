from helper_functions import *

CITIES_FILE = './european_cities.csv'
NUMBER_OF_GENERATIONS = 600
NUMBER_OF_SOLUTIONS = 700
NUMBER_OF_SELECTED_SOLUTIONS = 80
MUTATION_RATE = 0.01

if __name__ == '__main__':
    cities = load_cities(CITIES_FILE)
    solutions = generate_random_solutions(cities, NUMBER_OF_SOLUTIONS)

    best_solution = None
    best_score = np.Infinity

    # compute distance matrix as lookup table
    distance_matrix = {}
    for city1 in cities:
        distance_matrix[city1[0]] = 0
        distance_matrix[city1[0]] = {}
        for city2 in cities:
            distance_matrix[city1[0]][city2[0]] = distance.geodesic(
                (city1[1], city1[2]), (city2[1], city2[2])).km

    # training loop
    for i in range(NUMBER_OF_GENERATIONS):
        solutions = sorted(
            solutions, key=lambda x: fitness(x, distance_matrix))

        # store city names and score of best solution
        if fitness(solutions[0], distance_matrix) < best_score:
            best_solution = [city[0] for city in solutions[0]]
            best_score = fitness(solutions[0], distance_matrix)

        surviving_solutions = solutions[:NUMBER_OF_SELECTED_SOLUTIONS]
        print(
            f'\rGeneration {i + 1}: {fitness(surviving_solutions[0], distance_matrix):.2f} km', end='')

        # add new crossover solutions to the surviving solutions
        while (len(surviving_solutions) < NUMBER_OF_SOLUTIONS):
            sol1, sol2 = get_two_random_solutions(surviving_solutions)
            surviving_solutions.append(crossover(sol1, sol2))
        solutions = mutation(surviving_solutions, MUTATION_RATE)

    print(f'\n\nShortest route: {best_score:.2f} km')
    print(best_solution)

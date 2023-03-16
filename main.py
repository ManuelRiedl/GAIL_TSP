from helper_functions import *

if __name__ == '__main__':
    cities = load_cities()
    solutions = generate_random_solutions(cities, NUMBER_OF_SOLUTIONS)

    best_solution = None
    best_score = np.Infinity

    # compute distance matrix as lookup table
    distance_matrix = {}
    for city1 in cities:
        distance_matrix[city1[0]] = 0
        distance_matrix[city1[0]] = {}
        for city2 in cities:
            distance_matrix[city1[0]][city2[0]] = distance_between_two_cities(city1, city2)

    # training loop
    for i in range(NUMBER_OF_GENERATIONS):
        solutions = sorted(solutions, key=lambda x: fitness(x, distance_matrix))

        # store best solution
        if fitness(solutions[0], distance_matrix) < best_score:
            best_solution = solutions[0]
            best_score = fitness(solutions[0], distance_matrix)

        surviving_solutions = solutions[:NUMBER_OF_SELECTED_SOLUTIONS]
        print(f'Generation {i + 1}: {fitness(surviving_solutions[0]):.2f} km')

        # add new crossover solutions to the surviving solutions
        while (len(surviving_solutions) < 100):
            sol1, sol2 = get_two_random_solutions(solutions)
            cross_solutions = crossover(sol1, sol2)
            surviving_solutions.append(cross_solutions)
        solutions = mutation(surviving_solutions)

    print('Best solution: {}'.format(solutions[0]))
    print('Range: {}'.format(fitness(solutions[0])))

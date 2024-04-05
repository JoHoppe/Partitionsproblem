import back_end
def run_evolutionary_algorithm(initial_set, amount_solutions, generations, fitness_selection):
    # Initialize the population
    population = back_end.initialization(initial_set, amount_solutions)

    # Evolve the population for the specified number of generations
    for _ in range(generations):
        # Select the best individuals from the population
        population = back_end.best_fitness_selection(population, fitness_selection)

        # Apply mutation to the selected individuals
        population = back_end.mutate(population, mutation_factor=4)

        # Perform crossover to generate the next generation
        population = back_end.random_crossover(population, amount_solutions)

    # Sort the final population by fitness
    population.sort(key=lambda x: x.fitness, reverse=True)

    return population


def find_best_solution(initial_set, amount_solutions, generations, fitness_selection):
    # Run the evolutionary algorithm
    result_population = run_evolutionary_algorithm(initial_set, amount_solutions, generations, fitness_selection)

    # Select the best solution from the final population
    best_solution = back_end.best_fitness_selection(result_population, 1)[0]

    return best_solution


def main():
    initial_set = [20, 30, 15, 25, 10, 35, 40, 5, 50, 45]
    amount_solutions = 20
    generations = 50
    fitness_selection = 10

    best_solution = find_best_solution(initial_set, amount_solutions, generations, fitness_selection)

    print("Best solution so far:")
    print(best_solution)


if __name__ == "__main__":
    main()

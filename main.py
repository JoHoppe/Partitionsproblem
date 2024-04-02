import back_end


def run_evolutionary_algorithm(initial_set, amount_solutions, generations, fitness_selection=10, mutationfactor=4,
                               stagnation_threshhold=3):
    # Initialize the population
    population = back_end.initialization(initial_set, amount_solutions)
    best_solution = back_end.sort_by_fitness(population)[0]  # Get the best solution from the sorted population
    stagnation_tracker = 0

    # Evolve the population for the specified number of generations
    for _ in range(generations):
        population = back_end.sort_by_fitness(population)
        # if we achieved a good enough solution abort
        if best_solution.fitness >= 1:  # Check the fitness of the best solution
            print("found good enough solution")
            return best_solution
        if stagnation_tracker >= stagnation_threshhold:
            print("stagnation threshold reached")
            population = back_end.break_stagnation(population)
            stagnation_tracker = 0
        stagnation_tracker += 1
        # Select the best individuals fraction
        population = back_end.best_fitness_selection(population, fitness_selection)
        print(abs(best_solution.partial_sum - (best_solution.total_sum / 2)))
        print(best_solution.fitness)
        # Apply mutation to the selected individuals
        population = back_end.mutate(population, mutation_factor=mutationfactor)

        # Perform crossover to generate the next generation
        population = back_end.random_crossover(population, amount_solutions)
        population = back_end.sort_by_fitness(population)

        # Update the best solution if necessary
        if population[0].fitness > best_solution.fitness:  # Check the fitness of the best solution
            best_solution = population[0]

    # Sort the final population by fitness
    population = back_end.sort_by_fitness(population)

    return best_solution


def main():
    initial_set = [20, 30, 15, 26, 10, 35, 40, 10, 50, 45, 6, 5, 69, 420, 100, 5, 22, 52]
    generation_size = 100
    amount_generations = 50
    fitness_selection = 5
    mutation_factor = 4

    best_solution = run_evolutionary_algorithm(initial_set, generation_size, amount_generations, fitness_selection,
                                               mutation_factor)
    print("Best solution so far:")
    print(best_solution)
    print(best_solution.partial_sum)


if __name__ == "__main__":
    main()

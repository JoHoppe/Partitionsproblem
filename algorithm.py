import back_end


def run_evolutionary_algorithm(
        initial_set,
        amount_solutions,
        generations,
        fitness_selection=10,
        mutation_factor=4,
        stagnation_threshold=3,
):
    # Initialize the population
    population = back_end.initialization(initial_set, amount_solutions)
    best_solution = back_end.sort_by_fitness(population)[
        0
    ]  # Get the best solution from the sorted population
    stagnation_tracker = 0

    # Evolve the population for the specified number of generations
    for gen in range(generations):
        population = back_end.sort_by_fitness(population)
        # if we achieved a good enough solution abort
        if best_solution.fitness >= 99:  # Check the fitness of the best solution
            print("found good enough solution")
            return {"solution": best_solution, "generations_needed": gen + 1}
        if stagnation_tracker >= stagnation_threshold:
            print("stagnation threshold reached")
            population = back_end.break_stagnation(population)
            stagnation_tracker = 0
        stagnation_tracker += 1
        # Select the best individuals fraction
        population = back_end.best_fitness_selection(population, fitness_selection)
        print(f"Differenz: {abs(best_solution.partial_sum - (best_solution.total_sum / 2))};"
              f"best Score: {best_solution.fitness}")
        # Apply mutation to the selected individuals
        population = back_end.mutate(population, mutation_factor=mutation_factor)

        # Perform crossover to generate the next generation
        population = back_end.random_crossover(population, amount_solutions)
        population = back_end.sort_by_fitness(population)

        # Update the best solution if necessary
        if (
                population[0].fitness > best_solution.fitness
        ):  # Check the fitness of the best solution
            best_solution = population[0]

    return {"solution": best_solution, "generations_needed": generations}


def run_algorithm_multiple_times(
        initial_set,
        generation_size,
        amount_generations,
        fitness_selection,
        mutation_factor,
        stagnation_threshold,
        num_runs,
):
    results = []

    for _ in range(num_runs):
        result = run_evolutionary_algorithm(
            initial_set,
            generation_size,
            amount_generations,
            fitness_selection,
            mutation_factor,
            stagnation_threshold,
        )
        results.append(result)

    return results

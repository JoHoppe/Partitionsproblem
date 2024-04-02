import matplotlib.pyplot as plt

import back_end


def run_evolutionary_algorithm(initial_set, amount_solutions, generations, fitness_selection=10, mutationfactor=4,
                               stagnation_threshold=3):
    # Initialize the population
    population = back_end.initialization(initial_set, amount_solutions)
    best_solution = back_end.sort_by_fitness(population)[0]  # Get the best solution from the sorted population
    stagnation_tracker = 0

    # Evolve the population for the specified number of generations
    for gen in range(generations):
        population = back_end.sort_by_fitness(population)
        # if we achieved a good enough solution abort
        if best_solution.fitness >= 1:  # Check the fitness of the best solution
            print("found good enough solution")
            return {"solution": best_solution, "generations_needed": gen + 1}
        if stagnation_tracker >= stagnation_threshold:
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

    return {"solution": best_solution, "generations_needed": generations}


def run_algorithm_multiple_times(initial_set, generation_size, amount_generations, fitness_selection,
                                 mutation_factor, stagnation_threshold, num_runs):
    results = []

    for _ in range(num_runs):
        result = run_evolutionary_algorithm(initial_set, generation_size, amount_generations, fitness_selection,
                                            mutation_factor, stagnation_threshold)
        results.append(result)

    return results


def plot_generations_needed(results):
    generations_needed = [result["generations_needed"] for result in results]
    num_runs = len(results)

    # Count the frequency of each generation needed
    generation_counts = {gen: generations_needed.count(gen) for gen in set(generations_needed)}

    # Sort the generations by their counts
    sorted_generations = sorted(generation_counts.items(), key=lambda x: x[1], reverse=True)
    labels, counts = zip(*sorted_generations)

    max_generations = max(generations_needed)
    max_label = f"Max Gens: {max_generations}"

    # Create a dictionary to store the average fitness score for each generation
    average_fitness_scores = {
        gen: sum(result["solution"].fitness for result in results if result["generations_needed"] == gen) /
             generation_counts[gen]
        for gen in set(generations_needed)}

    # Create the pie chart
    plt.figure(figsize=(8, 8))
    patches, _, _ = plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 12})

    # Add the average fitness score inside each pie slice
    for patch, (gen, count) in zip(patches, sorted_generations):
        patch.set_label(f'{gen}\n(Avg. Fitness: {average_fitness_scores[gen]:.2f})')

    plt.title(f'Distribution of Generations Needed\nTotal Runs: {num_runs}\n{max_label}', fontsize=16)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1)  # Adjust layout

    plt.legend(title='Average Fitness Score', loc='center left', fontsize=10, bbox_to_anchor=(1, 0.5))

    plt.show()


def main():
    initial_set = [20, 30, 15, 26, 10, 35, 40, 10, 50, 45, 6, 5, 69, 420, 100, 5, 22, 52]
    generation_size = 100
    amount_generations = 50
    fitness_selection = 5
    mutation_factor = 4
    stagnation_threshold = 3
    num_runs = 10

    results = run_algorithm_multiple_times(initial_set, generation_size, amount_generations,
                                           fitness_selection, mutation_factor, stagnation_threshold,
                                           num_runs)
    plot_generations_needed(results)


if __name__ == "__main__":
    main()

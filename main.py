import algorithm
import util


def main():
    initial_set = util.random_set(100, 10, 400)
    print(initial_set)

    generation_size = 15
    amount_generations = 50
    fitness_selection = 5
    mutation_factor = 1
    stagnation_threshold = 1
    num_runs = 10
    # TODO: create a way to load and safe configs and initial sets
    # ToDO: mute_factor must be smaller then pop
    results = algorithm.run_algorithm_multiple_times(
        initial_set,
        generation_size,
        amount_generations,
        fitness_selection,
        mutation_factor,
        stagnation_threshold,
        num_runs,
    )
    util.plot_generations_needed(results)


if __name__ == "__main__":
    main()

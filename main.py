import algorithm
import util
import back_end


def main():
    # initial_set = util.random_set(100, 10, 400)
    # print(initial_set)
    # util.save_set(initial_set)
    print(util.get_all_configs())

    set_1 = util.load_set(1)
    # generation_size = 15
    # amount_generations = 50
    # fitness_selection = 5
    # mutation_factor = 1
    # stagnation_threshold = 1
    # num_runs = 10
    good_enough_number = 1
    # run_config = util.RunConfig(generation_size=generation_size, amount_generations=amount_generations,
    #                            fitness_selection=fitness_selection, mutation_factor=mutation_factor,
    #                           stagnation_threshold=stagnation_threshold, num_runs=num_runs, good_enough_number=good_enough_number)
    #util.save_config(run_config=run_config)
    run_config2 = util.load_config(1)
    results = algorithm.run_algorithm_multiple_times(set_1, *run_config2.values())
    util.plot_generations_needed(results)


if __name__ == "__main__":
    main()

# back_end enthält die Datenstrukturen und funktionen
import random


class Individual:
    def __str__(self):
        return (
            f"Solution: initial_set={self.initial_set}, solution={self.solution}, total_sum={self.total_sum},"
            f"partial_sum={self.partial_sum}, fitness={self.fitness}"
        )

    # first implementation of the fitness function
    def calculate_fitness(self):
        if (self.partial_sum - self.total_sum / 2) == 0:
            return 100
        fitness = 1 / (((abs(self.partial_sum - (self.total_sum / 2))) ** 3) * 100)
        return fitness

    def calculate_partial_sum(self):
        partial_sum = 0
        for i in range(len(self.initial_set)):
            if self.solution[i] == 1:
                partial_sum += self.initial_set[i]
        return partial_sum

    def generate_solution(self):
        return [random.choice([0, 1]) for _ in self.initial_set]

    # initial Set is always bigger 10 so no division by 0 possible in  fitness
    def __init__(self, initial_set):
        self.initial_set = initial_set
        self.solution = self.generate_solution()
        self.total_sum = sum(initial_set)
        self.partial_sum = self.calculate_partial_sum()
        self.fitness = self.calculate_fitness()


def initialization(initial_set, amount_solutions):
    return [Individual(initial_set) for _ in range(amount_solutions)]


def mutate(solutions, mutation_factor=1):
    # TODO: check if mutation from 1 to 1 should be possible, or to just flip values
    # chose a mutation_factor between 0 and length of the solution. we will then choose random positions of solution to
    # redraw the values,the amount based on the mutation_factor
    # we use range() plus len() to choose which positions of the solutions to change
    for solution in solutions:
        mutations = random.sample(range(len(solution.solution)), mutation_factor)
        for i in mutations:
            if solution.solution[i] == 1:
                solution.solution[i] = 0
            else:
                solution.solution[i] = 1
            # ensure mutations change the solution
            # solution.solution[i] = random.choice([0, 1])
    return solutions


def random_crossover(parent_solutions, num_children):
    """
    Perform random crossover between a list of parent solutions.

    This method randomly selects each gene from either parent with equal probability
    to produce a specified number of child solutions.

    Args:
    - parent_solutions (list): A list of parent solutions, where each solution is represented as a list.
    - num_children (int): The number of child solutions to generate.

    Returns:
    - list: A list of child solutions resulting from the crossover operation.
    """

    children = []
    for _ in range(num_children):
        # Randomly select parents
        parent1 = random.choice(parent_solutions)
        parent2 = random.choice(parent_solutions)

        # Perform random crossover
        child = Individual(initial_set=parent1.initial_set)
        child.solution = [
            random.choice(gene_pair)
            for gene_pair in zip(parent1.solution, parent2.solution)
        ]

        children.append(child)

    return children


def sort_by_fitness(solutions):
    sorted_list = sorted(solutions, key=lambda x: x.fitness, reverse=True)
    return sorted_list


def best_fitness_selection(solutions, output_amount):
    return sort_by_fitness(solutions)[:output_amount]


def break_stagnation(population, new_population_output=20):
    new_population = initialization(population[0].initial_set, new_population_output)
    population = population[
        :-new_population_output
    ]  # Remove the last new_population_output elements
    population.extend(new_population)  # Append the new_population to the population
    return population

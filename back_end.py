# back_end enthält die Datenstrukturen und funktionen
import random


def generate_solutions(initial_set):
    random_solution = []
    for i in initial_set:
        # we randomly create a solution
        random_solution.append(random.choice([0, 1]))
    return random_solution


class Solution:
    # initial Set is always bigger 10 so no division by 0 possible in  fitness
    def __init__(self, initial_set):
        self.initial_set = initial_set
        self.solution = generate_solutions(self.initial_set)
        self.total_sum = sum(initial_set)
        self.fitness = self.calculate_fitness()

    def __str__(self):
        return f"Solution: initial_set={self.initial_set}, solution={self.solution}, total_sum={self.total_sum}, fitness={self.fitness}"

    # first implementation of the fitness function
    def calculate_fitness(self):
        partition = [value for idx, value in enumerate(self.solution) if self.solution[idx] == 1]
        fitness = 1 / (abs(sum(partition) - (sum(self.initial_set) / 2)))
        return fitness


def initialization(initial_set, amount_solutions):
    initial_solutions = []
    for i in range(amount_solutions):
        initial_solutions.append(Solution(initial_set))
    return initial_solutions


def mutate(solutions, mutation_factor=1):
    # TODO: check if mutation from 1 to 1 should be possilbe, or to just flip values
    # chose a mutation_factor between 0 and length of the solution. we will then choose random positions of solution to
    # redraw the values,the amount based on the mutation_factor
    # we use range() plus len() to choose which positions of the solutions to change
    for solution in solutions:
        mutations = random.sample(range(len(solution.solution)), mutation_factor)
        for i in mutations:
            solution.solution[i] = random.choice([0, 1])
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
        child=Solution(initial_set=parent1.initial_set)
        child.solution = [random.choice(gene_pair) for gene_pair in zip(parent1.solution, parent2.solution)]

        children.append(child)

    return children


def best_fitness_selection(solutions, output_amount):
    return sorted(solutions,key=lambda x: x.fitness, reverse=True)[:output_amount]

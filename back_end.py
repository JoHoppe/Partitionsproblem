# back_end enthält die Datenstrukturen und funktionen
import random


def generate_solutions(initial_set):
    random_solution=[]
    for i in initial_set:
        # we randomly set the solution either
        random_solution.append(random.choice([0,1]))
    return random_solution

class Solution:
    def __init__(self, initial_set):
        self.initial_set = initial_set
        self.solution = []
        self.total_sum = sum(initial_set)
        self.fitness = self.calculate_fitness()

    def set_solution(self, solution_list):
        self.solution = generate_solutions(self.initial_set)

    def calculate_fitness(self):
        partition = [value for idx, value in enumerate(self.initial_set) if self.solution[idx] == 1]
        fitness = 1 / (abs(sum(partition) - (sum(self.initial_set) / 2)) + 1)  # Adding 1 to avoid division by zero
        return fitness





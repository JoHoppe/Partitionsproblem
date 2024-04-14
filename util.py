import random
import yaml
from dataclasses import dataclass
from matplotlib import pyplot as plt
from typing import List


def plot_generations_needed(results):
    generations_needed = [result["generations_needed"] for result in results]
    num_runs = len(results)

    # Count the frequency of each generation needed
    generation_counts = {
        gen: generations_needed.count(gen) for gen in set(generations_needed)
    }

    # Sort the generations by their counts
    sorted_generations = sorted(
        generation_counts.items(), key=lambda x: x[1], reverse=True
    )
    labels, counts = zip(*sorted_generations)

    max_generations = max(generations_needed)
    max_label = f"Max Gens: {max_generations}"

    # Create a dictionary to store the average fitness score for each generation
    average_fitness_scores = {
        gen: sum(
            result["solution"].fitness
            for result in results
            if result["generations_needed"] == gen
        ) / generation_counts[gen]
        for gen in set(generations_needed)
    }

    # Create the pie chart
    plt.figure(figsize=(8, 8))
    patches, _, _ = plt.pie(
        counts,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        textprops={"fontsize": 12},
    )

    # Add the average fitness score inside each pie slice
    for patch, (gen, count) in zip(patches, sorted_generations):
        patch.set_label(f"{gen}\n(Avg. Fitness: {average_fitness_scores[gen]:.2f})")

    plt.title(
        f"Distribution of Generations Needed\nTotal Runs: {num_runs}\n{max_label}",
        fontsize=16,
    )
    plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1)  # Adjust layout

    plt.legend(
        title="Average Fitness Score",
        loc="center left",
        fontsize=10,
        bbox_to_anchor=(1, 0.5),
    )

    plt.show()


def random_set(set_size: int, min_value: int, max_value: int) -> List[int]:
    return [random.randint(min_value, max_value) for _ in range(set_size)]


SetStorage = "set_storage.yaml"


def load_sets() -> List[List[int]]:
    with open(SetStorage, "r") as infile:
        return yaml.safe_load(infile) or []


def load_set(number: int) -> List[int]:
    sets = load_sets()
    if 0 <= number < len(sets):
        return sets[number]
    else:
        return None


def save_set(new_set: List[int]) -> None:
    sets = load_sets()
    sets.append(new_set)
    with open(SetStorage, "w") as outfile:
        yaml.dump(sets, outfile, default_flow_style=False, allow_unicode=True)


ConfigStorage = "config_storage.yaml"


def load_config(number: int) -> dict:
    with open(ConfigStorage, "r") as infile:
        configs = yaml.safe_load(infile)
        if configs and 0 <= number < len(configs):
            return configs[number]
        else:
            return {}

def save_config(run_config) -> None:
    config_to_save = run_config.to_dict()
    configs = get_all_configs()
    configs.append(config_to_save)

    with open(ConfigStorage, "w") as outfile:
        yaml.dump(configs, outfile, default_flow_style=False, allow_unicode=True)


def get_all_configs() -> List[dict]:
    with open(ConfigStorage, "r") as outfile:
        return yaml.safe_load(outfile) or []


def show_specific_config(number: int) -> dict:
    configs = load_config()
    if 0 <= number < len(configs):
        return configs[number]
    else:
        return None


def get_config_values(self):
    configs = self.load_config()
    return [config.values() for config in configs]


@dataclass
class RunConfig:
    generation_size: int
    amount_generations: int
    fitness_selection: int
    mutation_factor: int
    stagnation_threshold: int
    num_runs: int
    good_enough_number: int

    def to_dict(self) -> dict:
        return {
            "generation_size": self.generation_size,
            "amount_generations": self.amount_generations,
            "fitness_selection": self.fitness_selection,
            "mutation_factor": self.mutation_factor,
            "stagnation_threshold": self.stagnation_threshold,
            "num_runs": self.num_runs,
            "good_enough_number": self.good_enough_number,
        }

    def __str__(self) -> str:
        return (
            f"Generation Size: {self.generation_size}\n"
            f"Amount of Generations: {self.amount_generations}\n"
            f"Fitness Selection: {self.fitness_selection}\n"
            f"Mutation Factor: {self.mutation_factor}\n"
            f"Stagnation Threshold: {self.stagnation_threshold}\n"
            f"Number of Runs: {self.num_runs}\n"
            f"Good Enough Number: {self.good_enough_number}\n"
        )

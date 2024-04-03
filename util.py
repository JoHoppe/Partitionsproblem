import random
from matplotlib import pyplot as plt


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
        )
             / generation_counts[gen]
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


def random_set(set_size, min, max):
    return [random.randint(min, max) for i in range(set_size)]

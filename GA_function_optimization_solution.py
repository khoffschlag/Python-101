"""
You are tasked with implementing a genetic algorithm to optimize a mathematical function.
The goal is to find the optimal set of input values that minimizes the function.

Function to Optimize: f(x, y) = x^2 + y^2

You should implement the following steps in your genetic algorithm:

    1) Generate an initial population of individuals, where each individual represents a set of values for x and y.
    2) Evaluate the fitness of each individual in the population using the function to optimize.
    3) Select parents for reproduction using tournament selection.
       Implement a tournament selection mechanism where each individual competes at least against another individual.
       The one with the lowest fitness value is selected as a parent.
    4) Perform crossover and mutation to create offspring.
       Use a simple crossover operation, such as averaging the values of x and y from two parents.
       Apply a small random mutation to the offspring to introduce diversity.
    5) Replace the old population with the offspring.
    Repeat steps 2-5 for a specified number of generations.
    At the end of the specified number of generations, identify the best solution in the final population based on the lowest fitness value.

Note:

- The optimal solution for this problem is x = 0 and y = 0, which results in a fitness value of 0.
  Your program should aim to find this optimal solution using the genetic algorithm implementation.

- random.uniform(a,b) gives a float between a and b
- random.sample(list, k) takes k random entries of list
- min(list, key=lambda x: fx(x)) sort list based on function specified by key

"""

import random


# Define the function to optimize
def function_to_optimize(x, y):
    return x ** 2 + y ** 2  # Example function: f(x, y) = x^2 + y^2


# Genetic Algorithm parameters
population_size = 50
mutation_rate = 0.1
num_generations = 1_000

# Define the range of possible values for variables x and y
x_range = (-10, 10)
y_range = (-10, 10)


# Generate initial population
def generate_individual():
    x = random.uniform(x_range[0], x_range[1])
    y = random.uniform(y_range[0], y_range[1])
    return (x, y)


population = [generate_individual() for _ in range(population_size)]

# Genetic Algorithm main loop
for generation in range(num_generations):
    # Evaluate fitness for each individual in the population
    fitness_scores = [function_to_optimize(x, y) for x, y in population]

    # Select parents for reproduction (tournament selection)
    selected_parents = []
    for _ in range(population_size):
        # Randomly select two individuals for the tournament
        parent1, parent2 = random.sample(population, 2)

        # Choose the parent with the better fitness score
        if function_to_optimize(parent1[0], parent1[1]) < function_to_optimize(parent2[0], parent2[1]):
            selected_parents.append(parent1)
        else:
            selected_parents.append(parent2)

    # Perform crossover and mutation to create the offspring
    offspring = []
    for _ in range(population_size):
        parent1, parent2 = random.sample(selected_parents, 2)
        child = (
            (parent1[0] + parent2[0]) / 2,  # Crossover for x
            (parent1[1] + parent2[1]) / 2  # Crossover for y
        )
        child = (
            child[0] + random.uniform(-mutation_rate, mutation_rate),  # Mutation for x
            child[1] + random.uniform(-mutation_rate, mutation_rate)  # Mutation for y
        )
        offspring.append(child)

    # Replace the old population with the offspring
    population = offspring

# Find the best solution in the final population
best_solution = min(population, key=lambda ind: function_to_optimize(ind[0], ind[1]))
best_fitness = function_to_optimize(best_solution[0], best_solution[1])

# Print the results
print("Best solution:", best_solution)
print("Best fitness:", best_fitness)

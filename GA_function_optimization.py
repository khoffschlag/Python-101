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


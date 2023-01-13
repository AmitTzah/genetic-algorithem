# General function that works on any error function:

import numpy as np


def genetic_algorithm(pop_size, mutation_rate, max_generations,
                      error_threshold, error_function, ranges,
                      parent_prop, num_vars):
    """
    A function that uses genetic algorithm to optimize the value of x that minimizes the error_function.
    Args:
        pop_size (int): The size of the population of individuals that will be generated at the start of the algorithm
        mutation_rate (float): The degree of randomness that will be introduced to the x values of the new population each generation, as a value between 0 and 1
        max_generations (int): The number of iterations the algorithm will run for
        error_threshold (float): The minimum error value that, when reached, will stop the algorithm.
        error_function (function): The function that the algorithm will use to evaluate the fitness of each individual in the population, takes in *params optimization arguments.
        ranges (list): List of tuple of range of values for each parameter
        parent_prop (float): The proportion of the population size to use as parents for the next generation
        num_vars (int): The number of variables that need to be optimized by the error function

    Returns:
        list : The fittest individual and fitness value as a list
    """
    parent_size = int(parent_prop * pop_size)
    population = []

    # Generating the initial population
    for j in range(1, pop_size+1):
        individual = []
        for i in range(num_vars):
            min_range, max_range = ranges[i]
            random_float = np.random.uniform(min_range, max_range)
            individual.append(random_float)
        population.append([individual, error_function(*individual)])

    # Sorting the population based on fitness value
    population.sort(key=lambda x: x[1])

    for i in range(1, max_generations+1):
        print(f'Generation {i}...\n')
        new_population = []
        for k in range(1, pop_size+1):
            random_int = np.random.randint(1, parent_size-1)
            mutation = np.random.uniform(1-mutation_rate, 1+mutation_rate)
            child = []
            for p in range(num_vars):
                child.append(mutation*((population[random_int][0][p] +
                                        population[random_int+1][0][p] +
                                        population[random_int+2][0][p])/3))

            new_population.append([child, error_function(*child)])

        population = new_population.copy()
        population.sort(key=lambda x: x[1])
        if population[0][1] < error_threshold:
            print(f'Generation {i} did it!...\n')
            break

    print(f'Fittest individual:{population[0]}\n')
    return population[0]

# tests:


def error_function_1(*params):
    x, y, z, k = params
    return (3*x + y**2 + 5*z-k**10-300)**2


genetic_algorithm(10000, 0.1, 500, 0.01, error_function_1,
                  [(-100, 100), (-100, 100), (-100, 100), (-100, 100)], 0.1, 4)


def error_function_2(*params):

    x, y = params

    return (x ** 2 + y ** 2-40)**2


genetic_algorithm(10000, 0.2, 100, 0.00001, error_function_2,
                  [(0, 9), (-10, 10)], 0.1, 2)

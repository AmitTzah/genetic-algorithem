import numpy as np


def error_function(x):

    return (1231*x**6 + x**5 + 3*x**4+12*x**3+x**2+12*x - 32 - 32)**2


population = []

for j in range(1, 10000):
    random_float = np.random.uniform(-500, 500)
    population.append([random_float, error_function(random_float)])

population.sort(key=lambda x: x[1])

for i in range(1, 2000):
    print(f'Generation {i}...\n')
    new_population = []
    for k in range(1, 10000):
        random_int = np.random.randint(1, 99)
        x_child = np.random.uniform(0.9, 1.1)*((population[random_int][0] +
                                                population[random_int+1][0] +
                                                population[random_int+2][0])/3)

        new_population.append([x_child, error_function(x_child)])

    population = new_population.copy()
    population.sort(key=lambda x: x[1])
    if population[0][1] < 0.00000000001:
        print(f'Generation {i} did it!...\n')
        break

print('Fittest individual:')
print(population[0])

import numpy as np


# Recursive calculate total mass for a module
def compute_fuel(mass):
    fuel = int(np.floor(mass/3)-2)

    if fuel <= 0:
        return 0

    return fuel+compute_fuel(fuel)


# Examples
print("Result for examples:")
print(compute_fuel(14))
print(compute_fuel(1969))
print(compute_fuel(100756))


# my puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
modules = [int(mod[:-1]) for mod in file.readlines()]

# Calculate the solution
solutions = []
for mod in modules:
    solutions.append(compute_fuel(mod))

# Print the solution
print(sum(solutions))

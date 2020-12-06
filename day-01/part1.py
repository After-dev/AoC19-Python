import numpy as np


def compute_fuel(mass):
    fuel_required = int(np.floor(mass/3)-2)
    #print("Fuel requirements for a module with "+str(mass)+" of mass: "+str(fuel_required))
    return fuel_required


# Examples
print("Result for examples:")
print(compute_fuel(12))
print(compute_fuel(14))
print(compute_fuel(1969))
print(compute_fuel(100756))


# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
modules = [int(mod[:-1]) for mod in file.readlines()]

# Calculate the solution
solution = 0
for mod in modules:
    solution += compute_fuel(mod)

# Print the solution
print(solution)

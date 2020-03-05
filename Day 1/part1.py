import numpy as np


def compute_fuel(mass):
    fuel_required=np.floor(mass/3)-2
    print("Fuel requirements for a module with "+mass.__str__()+" of mass: "+fuel_required.__str__())
    return fuel_required


# Examples
print("Result for examples:")
compute_fuel(12)
compute_fuel(14)
compute_fuel(1969)
compute_fuel(100756)


# My puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
lines = file.readlines()
modules=[int(mod[:-1]) for mod in lines]

# Calculate the solution
solution=0
for mod in modules:
    solution += compute_fuel(mod)

# Print the solution
print("Solution: "+solution.__str__())
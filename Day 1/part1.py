import numpy as np


def compute_fuel(mass):
    fuel_required=np.floor(mass/3)-2
    print("Fuel requirements for a module with "+mass.__str__()+" of mass: "+fuel_required.__str__())
    return fuel_required


# examples
print("Result for examples:")
compute_fuel(12)
compute_fuel(14)
compute_fuel(1969)
compute_fuel(100756)


# my puzzle
print("Result for my puzzle:")
file = open('data/input.data', 'r')
lines = file.readlines()

solution=0
for mass in lines:
    solution += compute_fuel(int(mass))

print("Solution: "+solution.__str__())
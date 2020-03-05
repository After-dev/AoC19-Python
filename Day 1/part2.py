import numpy as np


# Recursive calculate total mass for a module
def compute_fuel2(mass):
    fuel=np.floor(mass/3)-2

    if(fuel <= 0):
        return 0

    return fuel+compute_fuel2(fuel)


# Examples
print("Result for examples:")
e1=compute_fuel2(14)
e2=compute_fuel2(1969)
e3=compute_fuel2(100756)
print("Fuel requirements for a module with 14 of mass: "+e1.__str__())
print("Fuel requirements for a module with 1969 of mass: "+e2.__str__())
print("Fuel requirements for a module with 100756 of mass: "+e3.__str__())


# my puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
lines = file.readlines()
modules=[int(mod[:-1]) for mod in lines]

# Calculate the solution
solution=0
for mod in modules:
    fuel_required=compute_fuel2(mod)
    print("Fuel requirements for a module with "+mod.__str__()+" of mass: "+fuel_required.__str__())
    solution += fuel_required

# Print the solution
print("Solution: "+solution.__str__())
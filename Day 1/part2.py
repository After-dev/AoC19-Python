import numpy as np


def compute_fuel2(mass):
    fuel=np.floor(mass/3)-2

    if(fuel <= 0):
        return 0

    return fuel+compute_fuel2(fuel)


# examples
print("Result for examples:")
e1=compute_fuel2(14)
e2=compute_fuel2(1969)
e3=compute_fuel2(100756)
print("Fuel requirements for a module with 14 of mass: "+e1.__str__())
print("Fuel requirements for a module with 1969 of mass: "+e2.__str__())
print("Fuel requirements for a module with 100756 of mass: "+e3.__str__())


# my puzzle
print("Result for my puzzle:")
file = open('data/input.data', 'r')
lines = file.readlines()

solution=0
for mass in lines:
    fuel_required=compute_fuel2(int(mass))
    print("Fuel requirements for a module with "+int(mass).__str__()+" of mass: "+fuel_required.__str__())
    solution += fuel_required

print("Solution: "+solution.__str__())
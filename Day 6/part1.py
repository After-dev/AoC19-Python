import numpy as np


def recursive_number_orbits(orbits,current,COM_distance):
    total=0
    if(current not in orbits):
        return COM_distance

    for object in orbits[current]:
        total+=recursive_number_orbits(orbits,object,COM_distance+1)

    return total+COM_distance



def get_number_orbits(map_data):
    orbits={}

    # Populate orbits
    for orbit in map_data:
        orbited=orbit.split(')')[0]
        orbiter=orbit.split(')')[1]

        if(orbited in orbits):
            orbits[orbited].append(orbiter)
        else:
            orbits.update({orbited : [orbiter]})

    # Compute direct and indirect orbits
    return recursive_number_orbits(orbits,'COM',0)






# My puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
lines = file.readlines()
map_data=[i[:-1] for i in lines]

# Calculate the solution
solution=get_number_orbits(map_data)

# Print the solution
print("Solution: "+solution.__str__())
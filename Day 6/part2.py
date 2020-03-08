import numpy as np


def get_parents(parents,orig,dest):
    path=[]

    next_parent=parents[orig]
    while(next_parent != dest):
        path.append(next_parent)
        next_parent=parents[next_parent]

    path.append(dest)
    return path


def get_number_of_transfers(map_data):
    parents={}

    # Populate orbits
    for orbit in map_data:
        [orbited,orbiter]=orbit.split(')')
        parents.update({orbiter : orbited})

    # Compute direct and indirect orbits
    from_YOU=get_parents(parents,'YOU','COM')
    from_SAN=get_parents(parents,'SAN','COM')

    complete_path=set(from_YOU).symmetric_difference(set(from_SAN))

    return len(complete_path)






# My puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
lines = file.readlines()
map_data=[i[:-1] for i in lines]

# Calculate the solution
solution=get_number_of_transfers(map_data)

# Print the solution
print("Solution: "+solution.__str__())
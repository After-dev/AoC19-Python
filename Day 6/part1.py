import numpy as np


def get_number_orbits(map_data):
    parents={}

    # Populate parents
    for orbit in map_data:
        [orbited,orbiter]=orbit.split(')')
        parents[orbiter]=orbited

    # Compute total (direct and indirect) orbits
    orbits=0
    for node in parents:
        # Count all orbits from current node until COM
        while(node in parents):
            node = parents[node]
            orbits += 1

    return orbits






# Examples
map_data=['COM)B',
          'B)C',
          'C)D',
          'D)E',
          'E)F',
          'B)G',
          'G)H',
          'D)I',
          'E)J',
          'J)K',
          'K)L'
]
print(get_number_orbits(map_data))




# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
lines = file.readlines()
map_data=[i[:-1] for i in lines]

# Calculate the solution
solution=get_number_orbits(map_data)

# Print the solution
print(solution)
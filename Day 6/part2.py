def get_path(parents,orig,dest):
    path=[]

    next_parent=parents[orig]
    while(next_parent != dest):
        path.append(next_parent)
        next_parent=parents[next_parent]

    path.append(dest)
    return path


def get_number_of_transfers(map_data):
    parents={}

    # Populate parents
    for orbit in map_data:
        [orbited,orbiter]=orbit.split(')')
        parents[orbiter]=orbited

    # Compute path from YOU and SAN to COM
    from_YOU_to_COM=get_path(parents,'YOU','COM')
    from_SAN_to_COM=get_path(parents,'SAN','COM')

    # Delete common objects to generate path between YOU and SAN
    from_YOU_to_SAN=set(from_YOU_to_COM).symmetric_difference(set(from_SAN_to_COM))

    return len(from_YOU_to_SAN)






# Examples
print("Result for examples:")
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
          'K)L',
          'K)YOU',
          'I)SAN'
]
print(get_number_of_transfers(map_data))




# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
lines = file.readlines()
map_data=[i[:-1] for i in lines]

# Calculate the solution
solution=get_number_of_transfers(map_data)

# Print the solution
print(solution)
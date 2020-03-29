def get_path(parents,orig):
    path=[]

    next_parent=parents[orig]
    while(next_parent != 'COM'):
        path.append(next_parent)
        next_parent=parents[next_parent]

    path.append('COM')
    return [i for i in reversed(path)]


def get_number_of_transfers(map_data):
    parents={}

    # Populate parents
    for orbit in map_data:
        [orbited,orbiter]=orbit.split(')')
        parents[orbiter]=orbited

    # Compute path from YOU and SAN to COM
    from_YOU_to_COM=get_path(parents,'YOU')
    from_SAN_to_COM=get_path(parents,'SAN')

    # Delete common objects to generate path between YOU and SAN
    prev_node = None
    while(from_YOU_to_COM[0] == from_SAN_to_COM[0]):
        prev_node = from_YOU_to_COM[0]
        from_YOU_to_COM.pop(0)
        from_SAN_to_COM.pop(0)

    from_YOU_to_SAN=['YOU']+[i for i in reversed(from_YOU_to_COM)]+[prev_node]+from_SAN_to_COM+['SAN']

    return len(from_YOU_to_SAN)-3






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
map_data=[i[:-1] for i in file.readlines()]

# Calculate the solution
solution=get_number_of_transfers(map_data)

# Print the solution
print(solution)

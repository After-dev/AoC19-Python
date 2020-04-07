import numpy as np
import datetime


def mapToGraph(map):
    graph = {}
    directions = {
        "north": (0, -1),
        "south": (0, 1),
        "west":  (-1, 0),
        "east":  (1, 0)
    }

    # Find start position
    pos_entrance = (-1, -1)
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == '@':
                pos_entrance = (row, col)
                map[row] = map[row].replace('@', '.')
                break

    # Populate graph
    queue = [[pos_entrance, pos_entrance, 0, '@']]
    while len(queue) > 0:
        # Get current
        [prev_pos, current_pos, current_distance, prev_node] = queue.pop()

        # For each direction
        for d in directions.values():
            # Get next pos
            next_pos = (current_pos[0]+d[0], current_pos[1]+d[1])

            # Always forward
            if next_pos != prev_pos:
                # Blank position
                if map[next_pos[0]][next_pos[1]] == '.':
                    queue.append([current_pos, next_pos, current_distance+1, prev_node])

                # Node position
                elif map[next_pos[0]][next_pos[1]].isalpha():
                    current_node = map[next_pos[0]][next_pos[1]]
                    # Add node to map
                    if prev_node not in graph:
                        graph[prev_node] = []
                    graph[prev_node].append([current_node, current_distance+1])
                    if current_node not in graph:
                        graph[current_node] = []
                    graph[current_node].append([prev_node, current_distance+1])

                    queue.append([current_pos, next_pos, 0, current_node])

    return graph


def get_keys(graph):
    keys = []

    for node in graph:
        if node.islower():
            keys.append(node)

    return keys


def collect_keys(map):
    sol = float('inf')

    # Get graph
    graph = mapToGraph(map)
    #print(graph)

    # Get keys
    keys = get_keys(graph)
    #print(keys)

    # Gen statuses
    queue = [['@', 0, [], []]]
    while len(queue) > 0:
        # Get current
        [current_node, current_distance, current_visited, current_keys] = queue.pop()
        #print(str(current_node)+" "+str(current_distance))

        # For each next node
        for [next_node, distance] in graph[current_node]:
            # If not visited
            if next_node not in current_visited:
                next_distance = current_distance+distance

                # If next_node is a key
                if next_node.islower():
                    # Visited key
                    if next_node in current_keys:
                        #current_visited.append(current_node)
                        queue.append([next_node, next_distance, current_visited[:]+[current_node], current_keys])

                    elif len(current_keys)+1 != len(keys):
                        #current_keys.append(next_node)
                        queue.append([next_node, next_distance, [], current_keys[:]+[next_node]])

                    # If it is last key, update solution
                    elif next_distance < sol:
                        #print next_distance
                        sol = next_distance

                # If next_node is '@'
                elif next_node == '@':
                    #current_visited.append(current_node)
                    queue.append([next_node, next_distance, current_visited[:]+[current_node], current_keys])

                # If next_node is a door and we have the key
                elif next_node.lower() in current_keys:
                    #print 'aqui '+next_node
                    #current_visited.append(current_node)
                    queue.append([next_node, next_distance, current_visited[:]+[current_node], current_keys])

    return sol


def collect_keys2(map):
    sol = float('inf')
    states = {}

    # Get graph
    graph = mapToGraph(map)
    #print(graph)

    # Get keys
    keys = get_keys(graph)
    #print(keys)

    # Gen statuses
    queue = [['@', 0, []]]
    while len(queue) > 0:
        # Get current
        [current_node, current_distance, current_keys] = queue.pop()

        # For each next node
        for [next_node, distance] in graph[current_node]:
            next_distance = current_distance+distance

            # If not visited
            if (next_node, str(current_keys)) not in states:
                states[(next_node, str(current_keys))] = float('inf')

            # Better path
            if next_distance < states[(next_node, str(current_keys))]:
                states[(next_node, str(current_keys))] = next_distance

                # If next_node is a key
                if next_node.islower():
                    # Visited key
                    if next_node in current_keys:
                        queue.append([next_node, next_distance, current_keys])

                    elif len(current_keys)+1 != len(keys):
                        #current_keys.append(next_node)
                        queue.append([next_node, next_distance, current_keys[:]+[next_node]])

                    # If it is last key, update solution
                    elif next_distance < sol:
                        print next_distance
                        sol = next_distance

                # If next_node is '@'
                elif next_node == '@':
                    #current_visited.append(current_node)
                    queue.append([next_node, next_distance, current_keys])

                # If next_node is a door and we have the key
                elif next_node.lower() in current_keys:
                    #print 'aqui '+next_node
                    #current_visited.append(current_node)
                    queue.append([next_node, next_distance, current_keys])

    return sol







# Examples
print("Result for examples:")
map = [
    '#########',
    '#b.A.@.a#',
    '#########'
]
print(collect_keys(map))

map = [
    '########################',
    '#f.D.E.e.C.b.A.@.a.B.c.#',
    '######################.#',
    '#d.....................#',
    '########################'
]
print(collect_keys(map))

map = [
    '########################',
    '#...............b.C.D.f#',
    '#.######################',
    '#.....@.a.B.c.d.A.e.F.g#',
    '########################'
]
print(collect_keys(map))

map = [
    '#################',
    '#i.G..c...e..H.p#',
    '########.########',
    '#j.A..b...f..D.o#',
    '########@########',
    '#k.E..a...g..B.n#',
    '########.########',
    '#l.F..d...h..C.m#',
    '#################'
]
print(collect_keys2(map))
"""
map = [
    '########################',
    '#@..............ac.GI.b#',
    '###d#e#f################',
    '###A#B#C################',
    '###g#h#i################',
    '########################'
]
pos_entrance = get_entrance(map)
keys = get_num_keys(map)
print(collect_keys(map, keys, pos_entrance, pos_entrance, 0))
"""




# My puzzle
"""
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
map = [i[:-1] for i in file.readlines()]

# Calculate the solution
solution = collect_keys(map)

# Print the solution
print(solution)
"""

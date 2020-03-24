def find_portals(maze):
    portals={}
    directions = {"north": ((0, -2), (0, -1)), "south": ((0, 1), (0, 2)),
                  "west": ((-2, 0), (-1, 0)), "east": ((1, 0), (2, 0))}

    for row in range(len(maze)):
        for col in range(len(maze[0])):
            # Get current_value from field
            current_value=maze[row][col]

            # If current_value is a empty field, check portal
            if(current_value == '.'):
                for d in directions:
                    dx1, dy1 = directions[d][0]
                    dx2, dy2 = directions[d][1]
                    c1, c2 = maze[row+dy1][col+dx1], maze[row+dy2][col+dx2]

                    # If c1 and c2 are letters, this is portal
                    if(c1.isalpha() and c2.isalpha()):
                        portal = c1+c2
                        pos = (row,col)
                        if(portal not in portals):
                            portals[portal]=[]
                        portals[portal].append(pos)

    return portals


def maze_to_graph(maze):
    directions = {"north": (0, -1), "south": (0, 1),
                  "west": (-1, 0), "east": (1, 0)}
    graph={}

    # Get portals and positions
    portals=find_portals(maze)

    # For each node, see reachable portals
    for current_portal in portals:
        for pos in portals[current_portal]:
            queue=[[pos,pos,0]]
            while(len(queue) != 0):
                # Get current pos
                [prev_pos,current_pos,current_steps]=queue.pop()

                # Generate adjacent pos
                for d in directions.values():
                    next_pos=(current_pos[0]+d[0],current_pos[1]+d[1])
                    next_field=maze[next_pos[0]][next_pos[1]]

                    # If next pos is portal, calculate next_pos again
                    if(next_field.isalpha()):
                        # Get portal name
                        if(d == (-1,0) or d == (0,-1)):
                            portal=maze[next_pos[0]+d[0]][next_pos[1]+d[1]]+maze[next_pos[0]][next_pos[1]]
                        else:
                            portal=maze[next_pos[0]][next_pos[1]]+maze[next_pos[0]+d[0]][next_pos[1]+d[1]]

                        # Get portal index
                        current_index = portals[current_portal].index(pos)
                        next_index = portals[portal].index(current_pos)

                        # Add portal to graph
                        if(portal != current_portal):
                            current_portal_name = current_portal+str(current_index)
                            next_portal_name = portal+str(next_index)
                            if(current_portal_name not in graph):
                                graph[current_portal_name]=[[next_portal_name,current_steps]]
                            else:
                                graph[current_portal_name].append([next_portal_name,current_steps])
                    # If next pos is empty
                    elif(next_pos != prev_pos and next_field == '.'):
                        queue.append([current_pos,next_pos,current_steps+1])

        # Add jump from portal 0 to 1
        if(len(portals[current_portal]) == 2):
            graph[current_portal+'0'].append([current_portal+'1',1])
            graph[current_portal+'1'].append([current_portal+'0',1])

    return graph


def fewest_path(maze):
    distances={}

    # Get graph
    graph=maze_to_graph(maze)

    distances['AA0']=0
    queue=['AA0']
    while(len(queue) > 0):
        # Get current node
        current_node=queue.pop()

        # Calculate next nodes
        for [next_node,distance] in graph[current_node]:
            new_distance=distances[current_node]+distance
            if(next_node not in distances or distances[next_node] > new_distance):
                distances[next_node] = new_distance
                queue.append(next_node)

    return distances['ZZ0']



# Examples
print("Result for examples:")
maze=[
    '         A           ',
    '         A           ',
    '  #######.#########  ',
    '  #######.........#  ',
    '  #######.#######.#  ',
    '  #######.#######.#  ',
    '  #######.#######.#  ',
    '  #####  B    ###.#  ',
    'BC...##  C    ###.#  ',
    '  ##.##       ###.#  ',
    '  ##...DE  F  ###.#  ',
    '  #####    G  ###.#  ',
    '  #########.#####.#  ',
    'DE..#######...###.#  ',
    '  #.#########.###.#  ',
    'FG..#########.....#  ',
    '  ###########.#####  ',
    '             Z       ',
    '             Z       '
]
print(fewest_path(maze))

maze=[
    '                   A               ',
    '                   A               ',
    '  #################.#############  ',
    '  #.#...#...................#.#.#  ',
    '  #.#.#.###.###.###.#########.#.#  ',
    '  #.#.#.......#...#.....#.#.#...#  ',
    '  #.#########.###.#####.#.#.###.#  ',
    '  #.............#.#.....#.......#  ',
    '  ###.###########.###.#####.#.#.#  ',
    '  #.....#        A   C    #.#.#.#  ',
    '  #######        S   P    #####.#  ',
    '  #.#...#                 #......VT',
    '  #.#.#.#                 #.#####  ',
    '  #...#.#               YN....#.#  ',
    '  #.###.#                 #####.#  ',
    'DI....#.#                 #.....#  ',
    '  #####.#                 #.###.#  ',
    'ZZ......#               QG....#..AS',
    '  ###.###                 #######  ',
    'JO..#.#.#                 #.....#  ',
    '  #.#.#.#                 ###.#.#  ',
    '  #...#..DI             BU....#..LF',
    '  #####.#                 #.#####  ',
    'YN......#               VT..#....QG',
    '  #.###.#                 #.###.#  ',
    '  #.#...#                 #.....#  ',
    '  ###.###    J L     J    #.#.###  ',
    '  #.....#    O F     P    #.#...#  ',
    '  #.###.#####.#.#####.#####.###.#  ',
    '  #...#.#.#...#.....#.....#.#...#  ',
    '  #.#####.###.###.#.#.#########.#  ',
    '  #...#.#.....#...#.#.#.#.....#.#  ',
    '  #.###.#####.###.###.#.#.#######  ',
    '  #.#.........#...#.............#  ',
    '  #########.###.###.#############  ',
    '           B   J   C               ',
    '           U   P   P               '
]
print(fewest_path(maze))





# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
maze = [l[:-1] for l in file.readlines()]

# Calculate the solution
solution=fewest_path(maze)

# Print the solution
print(solution)
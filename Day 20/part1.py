def find_portals(maze):
    portals={}

    for row in range(len(maze)-1):
        for col in range(len(maze[0])-1):
            # Get current_value from field
            current_value=maze[row][col]

            # If current_value is a letter, check portal
            if(current_value.isalpha()):
                portal=None
                # Get adjacent values
                down_value=maze[row+1][col]
                right_value=maze[row][col+1]

                # If down is a letter, there is a portal!
                if(down_value.isalpha()):
                    portal=current_value+down_value
                # If right is a letter, there is a portal!
                if(right_value.isalpha()):
                    portal=current_value+right_value

                # Add portal to portals
                if(portal != None):
                    # Get pos
                    pos=(-1,-1)
                    # Top
                    if(maze[(row-1)%len(maze)][col] == '.'):
                        pos=((row-1)%len(maze),col)
                    # Bot
                    elif(maze[(row+2)%len(maze)][col] == '.'):
                        pos=((row+2)%len(maze),col)
                    # Left
                    elif(maze[row][(col-1)%len(maze[0])] == '.'):
                        pos=(row,(col-1)%len(maze[0]))
                    # Right
                    elif(maze[row][(col+2)%len(maze[0])] == '.'):
                        pos=(row,(col+2)%len(maze[0]))

                    if(portal not in portals):
                        portals[portal]=[pos]
                    else:
                        portals[portal].append(pos)

    return portals


def maze_to_graph(maze):
    directions=[[1,0],[-1,0],[0,1],[0,-1]]
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
                for d in directions:
                    next_pos=(current_pos[0]+d[0],current_pos[1]+d[1])
                    next_field=maze[next_pos[0]][next_pos[1]]

                    # If next pos is portal, calculate next_pos again
                    if(next_field.isalpha()):
                        if(d == [-1,0] or d == [0,-1]):
                            portal=maze[next_pos[0]+d[0]][next_pos[1]+d[1]]+maze[next_pos[0]][next_pos[1]]
                        else:
                            portal=maze[next_pos[0]][next_pos[1]]+maze[next_pos[0]+d[0]][next_pos[1]+d[1]]
                        # Add portal to graph
                        if(portal != current_portal):
                            if(current_portal not in graph):
                                graph[current_portal]=[[portal,current_steps+1]]
                            else:
                                graph[current_portal].append([portal,current_steps+1])
                    # If next pos is empty
                    elif(next_pos != prev_pos and next_field == '.'):
                        queue.append([current_pos,next_pos,current_steps+1])

    return graph


def fewest_path(graph):
    distances={}

    distances['AA']=0
    queue=['AA']
    while(len(queue) > 0):
        # Get current node
        current_node=queue.pop()

        # Calculate next nodes
        for [next_node,distance] in graph[current_node]:
            new_distance=distances[current_node]+distance
            if(next_node not in distances or distances[next_node] > new_distance):
                distances[next_node] = new_distance
                queue.append(next_node)

    return distances['ZZ']-1



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
graph=maze_to_graph(maze)
print(fewest_path(graph))

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
graph=maze_to_graph(maze)
print(fewest_path(graph))





# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
maze = file.readlines()

# Calculate the solution
graph=maze_to_graph(maze)
solution=fewest_path(graph)

# Print the solution
print(solution)
# Get all portals and their position in the maze
def find_portals(maze):
    portals={}
    directions = {"north": ((0, -2), (0, -1)), "south": ((0, 1), (0, 2)),
                  "west": ((-2, 0), (-1, 0)), "east": ((1, 0), (2, 0))}

    for row in range(len(maze)):
        for col in range(len(maze[row])):
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


# Transform the maze into a graph, in which each node has (portal_name, list([next_portal, distance]))
def maze_to_graph(maze):
    directions = {"north": ((0, -2), (0, -1)), "south": ((0, 1), (0, 2)),
                  "west": ((-2, 0), (-1, 0)), "east": ((1, 0), (2, 0))}
    graph={}

    # Get portals and positions
    portals=find_portals(maze)

    # For each portal, see other reachable portals
    for current_portal in portals:
        for i,pos in enumerate(portals[current_portal]):
            queue=[[pos,pos,0]]
            while(len(queue) != 0):
                # Get current pos
                [prev_pos,current_pos,current_steps]=queue.pop()

                # Generate adjacent pos
                for d in directions:
                    dx1, dy1 = directions[d][0]
                    dx2, dy2 = directions[d][1]
                    c1, c2 = maze[current_pos[0]+dy1][current_pos[1]+dx1], maze[current_pos[0]+dy2][current_pos[1]+dx2]
                    next_pos = (current_pos[0]+dx1,current_pos[1]+dy1) if(d == "south" or d == "east") else (current_pos[0]+dx2,current_pos[1]+dy2)

                    # If c1 and c2 are letters, this is portal
                    if(c1.isalpha() and c2.isalpha() and c1+c2 != current_portal):
                        current_portal_name = current_portal+str(i)
                        next_portal_name = c1+c2+str(portals[c1+c2].index(current_pos))
                        if(current_portal_name not in graph):
                            graph[current_portal_name]=[]
                        graph[current_portal_name].append([next_portal_name,current_steps])
                    # If next pos is empty
                    elif(next_pos != prev_pos and maze[next_pos[0]][next_pos[1]] == '.'):
                        queue.append([current_pos,next_pos,current_steps+1])

        # Add jump from portal 0 to 1
        if(i == 1):
            graph[current_portal+'0'].append([current_portal+'1',1])
            graph[current_portal+'1'].append([current_portal+'0',1])

    return graph


def fewest_path(maze):
    distances={}

    # Get graph
    graph=maze_to_graph(maze)

    distances['AA0']=0
    queue=[['AA0',False]]
    while(len(queue) > 0):
        # Get current node
        [current_node,jump]=queue.pop()

        # Calculate next nodes
        for [next_node,distance] in graph[current_node]:
            if((jump and distance == 1) or (not jump and distance != 1)):
                new_distance=distances[current_node]+distance
                if(next_node not in distances or distances[next_node] > new_distance):
                    distances[next_node] = new_distance
                    queue.append([next_node, not jump])

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
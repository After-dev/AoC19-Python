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
    directions=[[1,0],[-1,0],[0,1],[0,-1]]
    graph={}

    # Get portals and positions
    portals=find_portals(maze)

    # For each node, see reachable portals
    for current_portal in portals:
        var_level = []
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
                        # Get portal name
                        if(d == [-1,0] or d == [0,-1]):
                            portal=maze[next_pos[0]+d[0]][next_pos[1]+d[1]]+maze[next_pos[0]][next_pos[1]]
                        else:
                            portal=maze[next_pos[0]][next_pos[1]]+maze[next_pos[0]+d[0]][next_pos[1]+d[1]]

                        # Get portal index
                        current_index = portals[current_portal].index(pos)
                        next_index = portals[portal].index(current_pos)

                        # Add portal to graph
                        if(portal != current_portal and portal != 'AA'):
                            current_portal_name = current_portal+str(current_index)
                            next_portal_name = portal+str(next_index)
                            if(current_portal_name not in graph):
                                graph[current_portal_name]=[[next_portal_name,current_steps,0]]
                            else:
                                graph[current_portal_name].append([next_portal_name,current_steps,0])
                    # If next pos is empty
                    elif(next_pos != prev_pos and next_field == '.'):
                        queue.append([current_pos,next_pos,current_steps+1])

            # Get level var
            if(pos[0] == 2 or pos[0] == len(maze)-3 or pos[1] == 2 or pos[1] == len(maze[0])-3):
                var_level.append(-1)
            else:
                var_level.append(1)

        # Add jump from portal 0 to 1
        if(len(portals[current_portal]) == 2):
            graph[current_portal+'0'].append([current_portal+'1',1,var_level[0]])
            graph[current_portal+'1'].append([current_portal+'0',1,var_level[1]])

    return graph


def fewest_path(maze,max_distance):
    fewest_distance=float('inf')

    # Get graph
    graph=maze_to_graph(maze)

    # Add initial nodes
    queue=[['AA0',0,0,False]]

    while(len(queue) > 0):
        # Get current state
        [current_node,current_distance,current_level,jump] = queue.pop()

        # If current_distance is higher than max_distance or current_level < 0, stop this path
        if(current_distance <= max_distance and current_level >= 0):
            # Calculate next nodes
            for [next_node,distance,var_level] in graph[current_node]:
                # If jump and next_level is equal to current, stop this path
                next_level = current_level+var_level
                if((jump and next_level != current_level) or (not jump and next_level == current_level)):
                    next_distance = current_distance+distance
                    # If next_node is ZZ and next_level is 0, this is a posible solution
                    if(next_node == 'ZZ0' and next_level == 0):
                        fewest_distance = next_distance if(next_distance < fewest_distance) else fewest_distance

                    # Continue search
                    elif(next_node != 'ZZ0'):
                        queue.append([next_node,next_distance,next_level,not jump])

    return fewest_distance



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
print(fewest_path(maze,500))

maze=[
    '             Z L X W       C                 ',
    '             Z P Q B       K                 ',
    '  ###########.#.#.#.#######.###############  ',
    '  #...#.......#.#.......#.#.......#.#.#...#  ',
    '  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  ',
    '  #.#...#.#.#...#.#.#...#...#...#.#.......#  ',
    '  #.###.#######.###.###.#.###.###.#.#######  ',
    '  #...#.......#.#...#...#.............#...#  ',
    '  #.#########.#######.#.#######.#######.###  ',
    '  #...#.#    F       R I       Z    #.#.#.#  ',
    '  #.###.#    D       E C       H    #.#.#.#  ',
    '  #.#...#                           #...#.#  ',
    '  #.###.#                           #.###.#  ',
    '  #.#....OA                       WB..#.#..ZH',
    '  #.###.#                           #.#.#.#  ',
    'CJ......#                           #.....#  ',
    '  #######                           #######  ',
    '  #.#....CK                         #......IC',
    '  #.###.#                           #.###.#  ',
    '  #.....#                           #...#.#  ',
    '  ###.###                           #.#.#.#  ',
    'XF....#.#                         RF..#.#.#  ',
    '  #####.#                           #######  ',
    '  #......CJ                       NM..#...#  ',
    '  ###.#.#                           #.###.#  ',
    'RE....#.#                           #......RF',
    '  ###.###        X   X       L      #.#.#.#  ',
    '  #.....#        F   Q       P      #.#.#.#  ',
    '  ###.###########.###.#######.#########.###  ',
    '  #.....#...#.....#.......#...#.....#.#...#  ',
    '  #####.#.###.#######.#######.###.###.#.#.#  ',
    '  #.......#.......#.#.#.#.#...#...#...#.#.#  ',
    '  #####.###.#####.#.#.#.#.###.###.#.###.###  ',
    '  #.......#.....#.#...#...............#...#  ',
    '  #############.#.#.###.###################  ',
    '               A O F   N                     ',
    '               A A D   M                     '
]
print(fewest_path(maze,500))





# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
maze = [l[:-1] for l in file.readlines()]

# Calculate the solution
solution=fewest_path(maze,6000)

# Print the solution
print(solution)
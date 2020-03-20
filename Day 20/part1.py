def find_portal(maze,portal,point=None):
    for row in range(len(maze)-1):
        for col in range(len(maze[0])-1):
            current_value=maze[row][col]
            down_value=maze[row+1][col]
            right_value=maze[row][col+1]

            # If current+down is equal to portal
            if(current_value+down_value == portal):
                # Verify top field
                if(row > 1 and maze[row-1][col] == '.'):
                    if((row-1,col) != point):
                        return (row-1,col)
                elif((row+2,col) != point):
                        return (row+2,col)

            # If current+right is equal to portal
            if(current_value+right_value == portal):
                if(col > 1 and maze[row][col-1] == '.'):
                    if((row,col-1) != point):
                        return (row,col-1)
                elif((row,col+2) != point):
                    return (row,col+2)
    return None


def fewest_path(maze):
    directions=[[1,0],[-1,0],[0,1],[0,-1]]
    visited={}

    # Get start pos
    start_pos=find_portal(maze,'AA')
    end_pos=find_portal(maze,'ZZ')
    visited[start_pos]=0

    # Populate graph
    queue=[start_pos]
    while(len(queue) != 0):
        # Get current pos
        current_pos=queue.pop(0)

        # Generate adjacent pos
        for d in directions:
            next_pos=(current_pos[0]+d[0],current_pos[1]+d[1])
            next_field=maze[next_pos[0]][next_pos[1]]

            # If next pos is portal, calculate next_pos again
            if(next_field != '#' and next_field != '.'):
                if(d == [-1,0] or d == [0,-1]):
                    portal=maze[next_pos[0]+d[0]][next_pos[1]+d[1]]+maze[next_pos[0]][next_pos[1]]
                else:
                    portal=maze[next_pos[0]][next_pos[1]]+maze[next_pos[0]+d[0]][next_pos[1]+d[1]]
                next_pos=find_portal(maze,portal,current_pos)

            if(next_pos != None and next_field != '#'):
                # If next_pos is visited
                if(next_pos in visited):
                    # Continue for highest path
                    if(visited[next_pos] > visited[current_pos]+1):
                        visited[next_pos]=visited[current_pos]+1
                        queue.append(next_pos)
                # Not visited
                else:
                    visited[next_pos]=visited[current_pos]+1
                    queue.append(next_pos)

    return visited[end_pos]



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
maze = file.readlines()

# Calculate the solution
solution=fewest_path(maze)

# Print the solution
print(solution)
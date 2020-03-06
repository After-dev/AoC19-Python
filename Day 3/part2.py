import numpy as np


def get_points(wire):
    wire_points={}

    # Set origin position (0,0)
    x = y = 0
    step=0

    # Split sequence in movements
    moves=wire.split(',')

    # Generate all points for each movement
    for move in moves:
        # Get direction and distance of movement
        direction=move[0]
        distance=int(move[1:])

        # Verify movement direction
        move_x = move_y = 0
        if(direction == 'U'):
            move_y = 1
        elif(direction == 'D'):
            move_y = -1
        elif(direction == 'R'):
            move_x = 1
        elif(direction == 'L'):
            move_x = -1

        # Do movement
        for _ in range(distance):
            x += move_x
            y += move_y

            point='('+x.__str__()+','+y.__str__()+')'
            step += 1

            # Add each point
            wire_points.update({point : step})

    return wire_points


def manhattan_distance(wire1,wire2):
    # Get all points for each wire path
    wire1_points=get_points(wire1)
    wire2_points=get_points(wire2)

    # Get cross points
    cross_points= list(set(wire1_points) & set(wire2_points))

    # Calculate distance between cross points and origin
    steps=[wire1_points[i] + wire2_points[i] for i in cross_points]

    # Return fewest steps
    solution=np.min(steps)
    print("Solution is: "+solution.__str__())
    return solution





# Examples
print("Result for examples:")
wire1='R8,U5,L5,D3'
wire2='U7,R6,D4,L4'
manhattan_distance(wire1,wire2)

wire1='R75,D30,R83,U83,L12,D49,R71,U7,L72'
wire2='U62,R66,U55,R34,D71,R55,D58,R83'
manhattan_distance(wire1,wire2)

wire1='R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
wire2='U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
manhattan_distance(wire1,wire2)



# My puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
lines = file.readlines()
wire1=lines[0][:-1]
wire2=lines[1][:-1]

# Calculate the solution
manhattan_distance(wire1,wire2)
import numpy as np


def get_points(wire):
    wire_points={}
    x=0
    y=0

    moves=wire.split(',')
    for move in moves:
        direction=move[0]
        displacement=int(move[1:])

        for step in range(displacement):
            if(direction == 'U'):
                y += 1
            elif(direction == 'D'):
                y -= 1
            elif(direction == 'R'):
                x += 1
            elif(direction == 'L'):
                x -= 1

            point='('+x.__str__()+','+y.__str__()+')'
            wire_points.update({point : '1'})

    return wire_points


def manhattan_distance(wire1,wire2):
    cross_points=[]
    wire1_points=get_points(wire1)
    wire2_points=get_points(wire2)

    for point in wire1_points:
        if(point in wire2_points):
            cross_points += [point]

    solution=999999
    for cross_point in cross_points:
        nums=cross_point.split(',')
        x=int(nums[0][1:])
        y=int(nums[1][0:-1])

        md=np.abs(x)+np.abs(y)

        if(md < solution):
            solution=md

    print("Solution is: "+solution.__str__())
    return solution




# examples
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



# my puzzle
print("Result for my puzzle:")
file = open('data/input.data', 'r')
lines = file.readlines()

wire1=lines[0][:-1]
wire2=lines[1][:-1]
manhattan_distance(wire1,wire2)
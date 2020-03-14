import numpy as np


def transform_coors(point):
    point.reverse()
    return point

def get_point_laser(map):
    rows=len(map)
    cols=len(map[0])

    for x in range(rows):
        for y in range(cols):
            if(map[x][y] == 'X'):
                return [x,y]

def get_point_asteroids(map):
    asteroids=[]
    rows=len(map)
    cols=len(map[0])

    for x in range(rows):
        for y in range(cols):
            if(map[x][y] == '#'):
                asteroids.append([x,y])

    return asteroids

def vaporization(asteroids,laser):
    targets=[]
    shoots=[]

    # Populate targets
    for asteroid in asteroids:
        # Calculate down of straight
        var_x=float(asteroid[1]-laser[1])
        var_y=float(asteroid[0]-laser[0])
        if(var_x != 0):
            p=var_y/var_x
        elif(var_y > 0):
            p=float('inf')
        else:
            p=float('-inf')

        # Calculate direction
        sign_x = '+' if var_x >= 0 else '-'
        sign_y = '+' if var_y >= 0 else '-'
        if(sign_y == '-' and sign_x == '+'):
            key=1
        elif(sign_y == '+' and sign_x == '+'):
            key=2
        elif(sign_y == '+' and sign_x == '-'):
            key=3
        elif(sign_y == '-' and sign_x == '-'):
            key=4

        # Calculate distance
        distance=np.sqrt(pow(var_x,2)+pow(var_y,2))

        # Add target
        targets.append([key,p,distance,asteroid])

    # Targets order by quadrant, straight and distance (down to up)
    targets.sort()

    # Gen shoots
    last_quadrant=last_straight=''
    cont=0
    while(len(targets) > 0):
        # Get next target
        target=targets.pop(0)
        cont+=1

        # Verify if last target was in the same quadrant and straight
        quadrant=str(target[0])
        straight=str(target[1])
        if(straight != last_straight or quadrant != last_quadrant):
            last_straight=straight
            last_quadrant=quadrant

            cont-=1
            shoots.append(target)
        else:
            targets.append(target)

        # If there are only targets from the same quadrant and straight
        if(cont == len(targets)):
            last_quadrant=last_straight=''
            cont=0

    return shoots



# Examples
asteroid_map=[
    '.#....#####...#..',
    '##...##.#####..##',
    '##...#...#.#####.',
    '..#.....X...###..',
    '..#.#.....#....##'
]
laser=get_point_laser(asteroid_map)
asteroids=get_point_asteroids(asteroid_map)
shoots=vaporization(asteroids,laser)
print(shoots)

asteroid_map=[
    '.#..##.###...#######',
    '##.############..##.',
    '.#.######.########.#',
    '.###.#######.####.#.',
    '#####.##.#.##.###.##',
    '..#####..#.#########',
    '####################',
    '#.####....###.#.#.##',
    '##.#################',
    '#####.##.###..####..',
    '..######..##.#######',
    '####.##.####...##..#',
    '.#####..#.######.###',
    '##...#.####X#####...',
    '#.##########.#######',
    '.####.#.###.###.#.##',
    '....##.##.###..#####',
    '.#.#.###########.###',
    '#.#.#.#####.####.###',
    '###.##.####.##.#..##'
]
laser=get_point_laser(asteroid_map)
asteroids=get_point_asteroids(asteroid_map)
shoots=vaporization(asteroids,laser)
print(transform_coors(shoots[0][3]))
print(transform_coors(shoots[1][3]))
print(transform_coors(shoots[2][3]))
print(transform_coors(shoots[9][3]))
print(transform_coors(shoots[19][3]))
print(transform_coors(shoots[49][3]))
print(transform_coors(shoots[99][3]))
print(transform_coors(shoots[198][3]))
print(transform_coors(shoots[199][3]))
print(transform_coors(shoots[200][3]))
print(transform_coors(shoots[298][3]))


# My puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
lines = file.readlines()
asteroid_map=[line[:-1] for line in lines]

# Calculate the solution
laser=[11, 11]
asteroids=get_point_asteroids(asteroid_map)
asteroids.remove(laser)
shoots=vaporization(asteroids,laser)
solution=transform_coors(shoots[199][3])

# Print the solution
print("Solution: "+solution.__str__())
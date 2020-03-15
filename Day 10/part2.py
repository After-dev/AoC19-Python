import numpy as np


def transform_coors(point):
    point.reverse()
    return point

# Traduce map to get points in which object appear
def get_points(map,object):
    objects=[]
    rows=len(map)
    cols=len(map[0])

    # Find object in each point of the map
    for x in range(rows):
        for y in range(cols):
            if(map[x][y] == object):
                objects.append([x,y])
    return objects

def vaporization(asteroids,laser):
    targets=[]
    shoots=[]

    # Populate targets
    for asteroid in asteroids:
        # Calculate straight
        var_x=float(asteroid[1]-laser[1])
        var_y=float(asteroid[0]-laser[0])
        if(var_x != 0):
            p=var_y/var_x
        elif(var_y > 0):
            p=float('inf')
        else:
            p=float('-inf')

        # Calculate angle from straight with arctan(p)
        angle=(np.degrees(np.arctan(p))+90)
        if(var_x < 0):
            angle += 180

        # Calculate distance
        distance=np.sqrt(pow(var_x,2)+pow(var_y,2))

        # Add target
        targets.append([angle,distance,asteroid])

    # Targets order by angle and distance (down to up)
    targets.sort()

    # Gen shoots
    last_angle=''
    cont=0
    while(len(targets) > 0):
        # Get next target
        target=targets.pop(0)

        # Verify if last target was in the same angle
        angle=str(target[0])
        if(angle != last_angle):
            last_angle=angle
            shoots.append(target)
            cont=0
        else:
            targets.append(target)
            cont+=1

        # If there are only targets from the same angle
        if(cont == len(targets)):
            last_angle=''

    return shoots



# Examples
print("Result for examples:")
asteroid_map=[
    '.#....#####...#..',
    '##...##.#####..##',
    '##...#...#.#####.',
    '..#.....X...###..',
    '..#.#.....#....##'
]
laser=get_points(asteroid_map,'X')[0]
asteroids=get_points(asteroid_map,'#')
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
laser=get_points(asteroid_map,'X')[0]
asteroids=get_points(asteroid_map,'#')
shoots=vaporization(asteroids,laser)
print(transform_coors(shoots[0][2]))
print(transform_coors(shoots[1][2]))
print(transform_coors(shoots[2][2]))
print(transform_coors(shoots[9][2]))
print(transform_coors(shoots[19][2]))
print(transform_coors(shoots[49][2]))
print(transform_coors(shoots[99][2]))
print(transform_coors(shoots[198][2]))
print(transform_coors(shoots[199][2]))
print(transform_coors(shoots[200][2]))
print(transform_coors(shoots[298][2]))


# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
lines = file.readlines()
asteroid_map=[line[:-1] for line in lines]

# Calculate the solution
laser=[11, 11]
asteroids=get_points(asteroid_map,'#')
asteroids.remove(laser)
shoots=vaporization(asteroids,laser)
solution=transform_coors(shoots[199][2])

# Print the solution
print(solution)
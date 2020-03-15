import numpy as np


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

def asteroids_detected(asteroids,station):
    sight_lines=[]

    for asteroid in asteroids:
        if(asteroid != station):
            # Calculate straight
            var_x=float(asteroid[0]-station[0])
            var_y=float(asteroid[1]-station[1])
            if(var_x != 0):
                p=var_y/var_x
            elif(var_y > 0):
                p=float('inf')
            else:
                p=float('-inf')

            # Get position inside the straight
            sign_x = '+' if var_x >= 0 else '-'
            sign_y = '+' if var_y >= 0 else '-'

            # Create key
            key=sign_x+sign_y+p.__str__()
            sight_lines.append(key)

    return len(set(sight_lines))


def get_best_asteroid(asteroids):
    solutions=[]

    # Get detected asteroids for each posible station
    for asteroid in asteroids:
            solutions.append(asteroids_detected(asteroids,asteroid))

    # Return best station and number of detected asteriods
    max_detections=np.max(solutions)
    best_asteroid=solutions.index(max_detections)
    return [asteroids[best_asteroid],max_detections]



# Examples
print("Result for examples:")
asteroid_map=[
    '.#..#',
    '.....',
    '#####',
    '....#',
    '...##'
]
asteroids=get_points(asteroid_map,'#')
print(get_best_asteroid(asteroids))


asteroid_map=[
    '......#.#.',
    '#..#.#....',
    '..#######.',
    '.#.#.###..',
    '.#..#.....',
    '..#....#.#',
    '#..#....#.',
    '.##.#..###',
    '##...#..#.',
    '.#....####'
]
asteroids=get_points(asteroid_map,'#')
print(get_best_asteroid(asteroids))


asteroid_map=[
    '#.#...#.#.',
    '.###....#.',
    '.#....#...',
    '##.#.#.#.#',
    '....#.#.#.',
    '.##..###.#',
    '..#...##..',
    '..##....##',
    '......#...',
    '.####.###.'
]
asteroids=get_points(asteroid_map,'#')
print(get_best_asteroid(asteroids))


asteroid_map=[
    '.#..#..###',
    '####.###.#',
    '....###.#.',
    '..###.##.#',
    '##.##.#.#.',
    '....###..#',
    '..#.#..#.#',
    '#..#.#.###',
    '.##...##.#',
    '.....#.#..'
]
asteroids=get_points(asteroid_map,'#')
print(get_best_asteroid(asteroids))


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
    '##...#.##########...',
    '#.##########.#######',
    '.####.#.###.###.#.##',
    '....##.##.###..#####',
    '.#.#.###########.###',
    '#.#.#.#####.####.###',
    '###.##.####.##.#..##'
]
asteroids=get_points(asteroid_map,'#')
print(get_best_asteroid(asteroids))


# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
lines = file.readlines()
asteroid_map=[line[:-1] for line in lines]

# Calculate the solution
asteroids=get_points(asteroid_map,'#')
solution=get_best_asteroid(asteroids)

# Print the solution
print(solution)
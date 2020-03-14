import numpy as np


def get_point_asteroids(map):
    asteroids=[]
    rows=len(map)
    cols=len(map[0])

    for x in range(rows):
        for y in range(cols):
            if(map[x][y] == '#'):
                asteroids.append([x,y])

    return asteroids

def asteroids_detected(asteroids,point):
    sight_lines=[]

    for asteroid in asteroids:
        if(asteroid != point):
            # Calculate down of a straight
            var_x=float(asteroid[0]-point[0])
            var_y=float(asteroid[1]-point[1])
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

    for asteroid in asteroids:
            solutions.append(asteroids_detected(asteroids,asteroid))

    best_asteroid=solutions.index(np.max(solutions))
    return [asteroids[best_asteroid],np.max(solutions)]



# Examples
asteroid_map=[
    '.#..#',
    '.....',
    '#####',
    '....#',
    '...##'
]
asteroids=get_point_asteroids(asteroid_map)
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
asteroids=get_point_asteroids(asteroid_map)
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
asteroids=get_point_asteroids(asteroid_map)
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
asteroids=get_point_asteroids(asteroid_map)
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
asteroids=get_point_asteroids(asteroid_map)
print(get_best_asteroid(asteroids))


# My puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
lines = file.readlines()
asteroid_map=[line[:-1] for line in lines]

# Calculate the solution
asteroids=get_point_asteroids(asteroid_map)
solution=get_best_asteroid(asteroids)

# Print the solution
print("Solution: "+solution.__str__())
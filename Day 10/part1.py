import numpy as np


# Traduce map to get points in which object appear
def get_points(map, object):
    objects = []

    # Find object in each point of the map
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == object:
                objects.append([x, y])

    return objects


def asteroids_detected(asteroids, station):
    slope_lines = []

    for asteroid in asteroids:
        if asteroid != station:
            # Calculate slope
            var_x = float(asteroid[0]-station[0])
            var_y = float(asteroid[1]-station[1])
            if var_x != 0:
                p = var_y/var_x
            elif var_y > 0:
                p = float('inf')
            else:
                p = float('-inf')

            # Get position inside the straight
            sign_x = '+' if var_x >= 0 else '-'
            sign_y = '+' if var_y >= 0 else '-'

            # Create key
            key = sign_x+sign_y+str(p)
            slope_lines.append(key)

    return len(set(slope_lines))


def get_best_asteroid(asteroid_map):
    solutions = []

    # Get asteroids
    asteroids = get_points(asteroid_map, '#')

    # Get detected asteroids for each posible station
    for asteroid in asteroids:
        solutions.append(asteroids_detected(asteroids, asteroid))

    # Return best station and number of detected asteriods
    max_detections = np.max(solutions)
    best_asteroid = solutions.index(max_detections)
    return [asteroids[best_asteroid], max_detections]



# Examples
print("Result for examples:")
asteroid_map = [
    '.#..#',
    '.....',
    '#####',
    '....#',
    '...##'
]
print(get_best_asteroid(asteroid_map))


asteroid_map = [
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
print(get_best_asteroid(asteroid_map))


asteroid_map = [
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
print(get_best_asteroid(asteroid_map))


asteroid_map = [
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
print(get_best_asteroid(asteroid_map))


asteroid_map = [
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
print(get_best_asteroid(asteroid_map))


# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
asteroid_map = [line[:-1] for line in file.readlines()]

# Calculate the solution
solution = get_best_asteroid(asteroid_map)

# Print the solution
print(solution)

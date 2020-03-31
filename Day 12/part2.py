import numpy as np
from copy import deepcopy


def print_state(moons_pos,moons_velocities,steps):
    print('After '+steps+' steps:')
    for i in range(len(moons_pos)):
        print('pos=<x='+str(moons_pos[i][0])+', y='+str(moons_pos[i][1])+', z='+str(moons_pos[i][2])+'>, vel=<x='+str(moons_velocities[i][0])+', y='+str(moons_velocities[i][0])+', z='+str(moons_velocities[i][0])+'>')
    print


def motion_simulation(init_pos_moons, init_vel_moons, steps):
    moons_pos = deepcopy(init_pos_moons)
    moons_velocities = deepcopy(init_vel_moons)

    # Print position and velocity of each moon at init
    #print_state(moons_pos, moons_velocities, '0')

    # Simulate each step
    for step in range(steps):
        # Update velocities (compare every pair of moons)
        for i,moon1 in enumerate(moons_pos,start=0):
            for moon2 in moons_pos:
                if moon1 != moon2:
                    for dim in range(3):
                        if moon1[dim] > moon2[dim]:
                            moons_velocities[i][dim] += -1
                        elif moon1[dim] < moon2[dim]:
                            moons_velocities[i][dim] += 1

        # Update positions
        for i in range(len(moons_pos)):
            for dim in range(3):
                moons_pos[i][dim] += moons_velocities[i][dim]

        # Print position and velocity of each moon
        #print_state(moons_pos, moons_velocities, str(step+1))

    return [moons_pos, moons_velocities]


def steps_to_cycle(init_pos_moons, init_vel_moons):
    steps = [0,0,0]

    # Find steps needed to reach initial position in each dimension
    for dim in range(3):
        # Get initial pos for dimension dim
        dim_init_pos = [moon[dim] for moon in init_pos_moons]

        current_pos_moons = init_pos_moons
        current_vel_moons = init_vel_moons
        while True:
            # Simulate one step
            [current_pos_moons, current_vel_moons] = motion_simulation(current_pos_moons, current_vel_moons, steps=1)
            steps[dim] += 1

            if [moon[dim] for moon in current_pos_moons] == dim_init_pos and [moon[dim] for moon in current_vel_moons] == [0,0,0,0]:
                break

    print(str(steps[0])+" "+str(steps[1])+" "+str(steps[2]))
    print(np.lcm(steps[1], steps[2]))
    print(np.lcm(steps[0], np.lcm(steps[1], steps[2])))

    # Calculate least common multiple to obtain total steps
    return np.lcm(steps[0], np.lcm(steps[1], steps[2]))



# Examples
print("Result for examples:")
init_pos_Io = [-1, 0, 2]
init_pos_Europa = [2, -10, -7]
init_pos_Ganymede = [4, -8, 8]
init_pos_Callisto = [3, 5, -1]
init_pos_moons = [
    init_pos_Io,
    init_pos_Europa,
    init_pos_Ganymede,
    init_pos_Callisto
]
init_vel_moons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(steps_to_cycle(init_pos_moons, init_vel_moons))


init_pos_Io = [-8, -10, 0]
init_pos_Europa = [5, 5, 10]
init_pos_Ganymede = [2, -7, 3]
init_pos_Callisto = [9, -8, -3]
init_pos_moons = [
    init_pos_Io,
    init_pos_Europa,
    init_pos_Ganymede,
    init_pos_Callisto
]
init_vel_moons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(steps_to_cycle(init_pos_moons, init_vel_moons))






# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
values = [line[:-1].replace(' ', '')[1:-1].replace('x', '').replace('y', '').replace('z', '').replace('=', '') for line in file.readlines()]
init_pos_moons = [[int(i) for i in v.split(',')] for v in values]
init_vel_moons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Calculate the solution
solution = steps_to_cycle(init_pos_moons, init_vel_moons)

# Print the solution
print(solution)

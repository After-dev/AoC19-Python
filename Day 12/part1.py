def print_state(moons_pos, moons_velocities, steps):
    print('After '+steps+' steps:')
    for i in range(len(moons_pos)):
        print('pos=<x='+str(moons_pos[i][0])+', y='+str(moons_pos[i][1])+', z='+str(moons_pos[i][2])+'>, vel=<x='+str(moons_velocities[i][0])+', y='+str(moons_velocities[i][0])+', z='+str(moons_velocities[i][0])+'>')
    print


def motion_simulation(moons_pos, steps):
    # Init moon velocities
    moons_velocities = [[0,0,0] for _ in moons_pos]

    # Print position and velocity of each moon at init
    #print_state(moons_pos, moons_velocities, '0')

    # Simulate each step
    for step in range(steps):
        # Update velocities (compare every pair of moons)
        for i,moon1 in enumerate(moons_pos, start=0):
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


def calculate_total_energy(moons_pos, moons_velocities):
    total_energy = 0

    for i in range(len(moons_pos)):
        pot_energy = kin_energy = 0
        for dim in range(3):
            pot_energy += abs(moons_pos[i][dim])
            kin_energy += abs(moons_velocities[i][dim])

        total_energy += pot_energy*kin_energy

    return total_energy



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
[moons_pos, moons_velocities] = motion_simulation(init_pos_moons, steps=10)
print(calculate_total_energy(moons_pos, moons_velocities))


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
[moons_pos, moons_velocities] = motion_simulation(init_pos_moons, steps=100)
print(calculate_total_energy(moons_pos, moons_velocities))




# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
values = [line[:-1].replace(' ', '')[1:-1].replace('x', '').replace('y', '').replace('z', '').replace('=', '') for line in file.readlines()]
init_pos_moons = [[int(i) for i in v.split(',')] for v in values]

# Calculate the solution
[moons_pos, moons_velocities] = motion_simulation(init_pos_moons, steps=1000)
solution = calculate_total_energy(moons_pos, moons_velocities)

# Print the solution
print(solution)

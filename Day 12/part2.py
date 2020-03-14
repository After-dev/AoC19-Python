import numpy as np
from copy import copy, deepcopy


def motion_simulation(init_pos_moons,init_vel_moons,steps):
    moons_pos=deepcopy(init_pos_moons)
    moons_velocities=deepcopy(init_vel_moons)

    # Print position and velocity of each moon at init
    """
    print('After 0 steps:')
    for i in range(len(moons_pos)):
        print('pos=<x='+str(moons_pos[i][0])+', y='+str(moons_pos[i][1])+', z='+str(moons_pos[i][2])+'>, vel=<x='+str(moons_velocities[i][0])+', y='+str(moons_velocities[i][0])+', z='+str(moons_velocities[i][0])+'>')
    print
    """

    # Simulate each step
    for step in range(steps):
        # Update velocities (compare every pair of moons)
        for i,moon1 in enumerate(moons_pos,start=0):
            for moon2 in moons_pos:
                if(moon1 != moon2):
                    for dim in range(3):
                        if(moon1[dim] > moon2[dim]):
                            moons_velocities[i][dim] += -1
                        elif(moon1[dim] < moon2[dim]):
                            moons_velocities[i][dim] += 1

        # Update positions
        for i in range(len(moons_pos)):
            for dim in range(3):
                moons_pos[i][dim] += moons_velocities[i][dim]

        # Print position and velocity of each moon
        """
        print('After '+str(step+1)+' steps:')
        for i in range(len(moons_pos)):
            print('pos=<x='+str(moons_pos[i][0])+', y='+str(moons_pos[i][1])+', z='+str(moons_pos[i][2])+'>, vel=<x='+str(moons_velocities[i][0])+', y='+str(moons_velocities[i][1])+', z='+str(moons_velocities[i][2])+'>')
        print
        """

    return [moons_pos,moons_velocities]

def calculate_total_energy(moons_pos,moons_velocities):
    total_energy=0

    for i in range(len(moons_pos)):
        pot_energy=kin_energy=0
        for dim in range(3):
            pot_energy += abs(moons_pos[i][dim])
            kin_energy += abs(moons_velocities[i][dim])

        total_energy += pot_energy*kin_energy

    return total_energy

def steps_to_cycle(init_pos_moons,init_vel_moons):
    steps=[0,0,0]

    # Find init pos for each dimension
    for dim in range(3):
        # Get initial pos for dimension dim
        dim_init_pos=[moon[dim] for moon in init_pos_moons]

        current_pos_moons=init_pos_moons
        current_vel_moons=init_vel_moons
        while(True):
            # Simulate one step
            [current_pos_moons,current_vel_moons]=motion_simulation(current_pos_moons,current_vel_moons,steps=1)
            steps[dim]+=1

            if([moon[dim] for moon in current_pos_moons] == dim_init_pos and [moon[dim] for moon in current_vel_moons] == [0,0,0,0]):
                break

    return np.lcm(steps[0], np.lcm(steps[1], steps[2]))



# Examples
init_pos_Io=[-1,0,2]
init_pos_Europa=[2,-10,-7]
init_pos_Ganymede=[4,-8,8]
init_pos_Callisto=[3,5,-1]
init_pos_moons=[init_pos_Io,init_pos_Europa,init_pos_Ganymede,init_pos_Callisto]
init_vel_moons=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
print(steps_to_cycle(init_pos_moons,init_vel_moons))


init_pos_Io=[-8,-10,0]
init_pos_Europa=[5,5,10]
init_pos_Ganymede=[2,-7,3]
init_pos_Callisto=[9,-8,-3]
init_pos_moons=[init_pos_Io,init_pos_Europa,init_pos_Ganymede,init_pos_Callisto]
init_vel_moons=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
print(steps_to_cycle(init_pos_moons,init_vel_moons))






# My puzzle
print("Result for my puzzle:")
# Input data
init_pos_moons=[
    [5,13,-3],
    [18,-7,13],
    [16,3,4],
    [0,8,8]
]
init_vel_moons=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

# Calculate the solution
solution=steps_to_cycle(init_pos_moons,init_vel_moons)

# Print the solution
print("Solution: "+solution.__str__())
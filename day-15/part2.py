import numpy as np


def intcode_program(state, max_size, n_read):
    output = []

    # Get state
    intcode_aux = state[0][:]
    inputs = state[1]
    pointer = state[2]
    relative_base = state[3]

    # Resize array (get more memory)
    intcode_aux = np.resize(intcode_aux, max_size)

    # Browse array by steps of 4
    while pointer < len(intcode):
        # Get opcode and mode of parameters
        opcode_instruction = str(intcode_aux[pointer])
        while len(opcode_instruction) < 5:
            opcode_instruction = '0'+opcode_instruction

        opcode = int(opcode_instruction[-2:])
        mode_params = [
            int(opcode_instruction[-3]),
            int(opcode_instruction[-4]),
            int(opcode_instruction[-5])
        ]

        # Get index of each parameter
        indexes = [-1, -1, -1]
        for i in range(len(indexes)):
            pos = pointer+1+i
            if pos < len(intcode_aux):
                if mode_params[i] == 0:
                    indexes[i] = intcode_aux[pos]
                elif mode_params[i] == 1:
                    indexes[i] = pos
                elif mode_params[i] == 2:
                    indexes[i] = relative_base+intcode_aux[pos]

        # Apply opcode operation
        # STOP
        if opcode == 99:
            break

        # ADDITION
        elif opcode == 1:
            op1 = intcode_aux[indexes[0]]
            op2 = intcode_aux[indexes[1]]
            intcode_aux[indexes[2]] = op1+op2
            pointer += 4

        # MULTIPLICATION
        elif opcode == 2:
            op1 = intcode_aux[indexes[0]]
            op2 = intcode_aux[indexes[1]]
            intcode_aux[indexes[2]] = op1*op2
            pointer += 4

        # INPUT
        elif opcode == 3:
            intcode_aux[indexes[0]] = inputs.pop(0)
            pointer += 2

        # OUTPUT
        elif opcode == 4:
            #print('Output: '+intcode_aux[indexes[0]].__str__())
            output.append(intcode_aux[indexes[0]])
            pointer += 2
            if len(output) == n_read:
                break

        # JUMP-IF-TRUE
        elif opcode == 5:
            if intcode_aux[indexes[0]] != 0:
                pointer = intcode_aux[indexes[1]]
            else:
                pointer += 3

        # JUMP-IF-FALSE
        elif opcode == 6:
            if intcode_aux[indexes[0]] == 0:
                pointer = intcode_aux[indexes[1]]
            else:
                pointer += 3

        # LESS-THAN
        elif opcode == 7:
            if intcode_aux[indexes[0]] < intcode_aux[indexes[1]]:
                intcode_aux[indexes[2]] = 1
            else:
                intcode_aux[indexes[2]] = 0
            pointer += 4

        # EQUAL-TO
        elif opcode == 8:
            if intcode_aux[indexes[0]] == intcode_aux[indexes[1]]:
                intcode_aux[indexes[2]] = 1
            else:
                intcode_aux[indexes[2]] = 0
            pointer += 4

        # ADJUST RELATIVE BASE
        elif opcode == 9:
            relative_base += intcode_aux[indexes[0]]
            pointer += 2

    return [output, intcode_aux, pointer, relative_base]


def get_full_map(intcode):
    pos = (0, 0)
    goal = (-1, -1)
    fields = {pos: 1}
    direction = -1
    movements = [
        (0, 1),
        (0, -1),
        (-1, 0),
        (1, 0)
    ]
    state = [intcode, [], 0, 0]
    path_from_start = [pos]

    while True:
        back = False

        # Get current pos
        pos = path_from_start[-1]

        # Get new direction when hit wall
        if direction == -1:
            # Search unvisited direction
            for i in range(4):
                new_pos = (pos[0]+movements[i][0], pos[1]+movements[i][1])
                if new_pos not in fields:
                    direction = i
                    break

            # If there is no available direction, turn back
            if direction == -1:
                # If root has not got available direction, break
                if len(path_from_start) == 1:
                    break

                back = True
                path_from_start.pop(-1)
                prev_pos = path_from_start[-1]
                direction = movements.index((prev_pos[0]-pos[0], prev_pos[1]-pos[1]))

        # Calculate new pos
        new_pos = (pos[0]+movements[direction][0], pos[1]+movements[direction][1])

        # Get repair droid status
        state[1].append(direction+1)
        [output, state[0], state[2], state[3]] = intcode_program(state, 2000, 1)
        status = output[0]

        # Analyze status
        fields[new_pos] = status
        if back:
            direction = -1
        else:
            if status == 0:
                direction = -1
            else:
                if status == 2:
                    #print('Goal reached')
                    goal = pos

                path_from_start.append(new_pos)

    return [fields, goal]


def oxygen(full_map, goal):
    minutes = 0
    directions = {
        "north": (0, -1),
        "south": (0, 1),
        "west": (-1, 0),
        "east": (1, 0)
    }

    queue = [[goal, minutes]]
    while len(queue) > 0:
        # Get next point
        [point, minutes] = queue.pop(0)

        # For each direction
        for d in directions:
            # Gen adjacent point
            p = (point[0]+directions[d][0], point[1]+directions[d][1])

            # Get status of each adjacent point
            s = full_map[p]

            # Add to queue points diferent from wall (0)
            if s != 0:
                full_map[p] = 0
                queue.append([p, minutes+1])

    return minutes+1






# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
intcode = [int(i) for i in file.readlines()[0][:-1].split(',')]

# Calculate the solution
[full_map, goal] = get_full_map(intcode)
solution = oxygen(full_map, goal)

# Print the solution
print(solution)

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
    state = [intcode, [], 0, 0]
    line = []
    full_map = []

    # Get all ASCII codes
    [ASCII_codes, _, _, _] = intcode_program(state, 5000, -1)
    #print(ASCII_codes)

    # Populate map
    for code in ASCII_codes:
        # New line (10)
        if code == 10:
            full_map.append(line)
            line = []
        # Scaffold (35), space (46) or robot (94)
        else:
            line.append(code)

    return full_map[:-1]


def print_map(full_map):
    print('Printing map...')
    # Get dims
    rows = len(full_map)
    cols = len(full_map[0])
    print('Rows: '+str(rows))
    print('Cols: '+str(cols))

    # Print map
    for row in range(rows):
        # Get complete line
        line = ''
        for col in range(cols):
            line += str(full_map[row][col])

        # Change: 94 --> ^ | 35 --> # | 46 --> . | 12 --> O
        line = line.replace('94', '^').replace('35', '#').replace('46', '.').replace('12', 'O')
        print(line)


def point_in_map(map, point):
    rows = len(map)
    cols = len(map[0])
    if point[0] >= rows or point[0] < 0 or point[1] >= cols or point[1] < 0:
        return False
    return True


def get_full_routine(full_map):
    rows = len(full_map)
    cols = len(full_map[0])
    full_routine = ''
    pos = (-1, -1)
    dir = 0
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    # Find robot position
    for row in range(rows):
        for col in range(cols):
            if full_map[row][col] == 94:
                pos=(row, col)
                break

    # Generate full routine
    turn = ''
    cont = 0
    while True:
        # Get next position
        next_pos = (pos[0]+directions[dir][0], pos[1]+directions[dir][1])
        next_pos_in_map = point_in_map(full_map, next_pos)

        # Verify if next_pos is space
        if not next_pos_in_map or full_map[next_pos[0]][next_pos[1]] == 46:
            # Do not store first turn
            if turn != '':
                full_routine += turn+','+str(cont)+','

            # Calculate turn
            dir1 = (dir-1)%len(directions)
            dir2 = (dir+1)%len(directions)
            pos_adj1 = (pos[0]+directions[dir1][0], pos[1]+directions[dir1][1])
            pos_adj2 = (pos[0]+directions[dir2][0], pos[1]+directions[dir2][1])
            pos_adj1_in_map = point_in_map(full_map, pos_adj1)
            pos_adj2_in_map = point_in_map(full_map, pos_adj2)

            # Turn Left if left point is inside map and is 35
            if pos_adj1_in_map and full_map[pos_adj1[0]][pos_adj1[1]] == 35:
                turn = 'L'
                dir = dir1
            # Turn Right if left point is inside map and is 35
            elif pos_adj2_in_map and full_map[pos_adj2[0]][pos_adj2[1]] == 35:
                turn = 'R'
                dir = dir2
            # End point
            else:
                break

            # Reset counter
            cont = 0
        else:
            pos = next_pos
            cont += 1

    return full_routine[:-1]


def get_functions(full_routine):
    functions = []

    cont1 = cont2 = cont3 = 1
    while True:
        # Copy full_routine
        copy_full_routine = full_routine[:]+','

        # Update counters
        if cont3 == 6:
            cont3 = 1
            cont2 += 1
        if cont2 == 6:
            cont2 = 1
            cont1 += 1
        if cont1 == 6:
            break

        # Get functions A, B and C
        # Function A
        index_A = copy_full_routine.replace(',', '-', cont1*2).replace('-', ',', cont1*2-1).index('-')
        func_A = copy_full_routine[:index_A]
        copy_full_routine = copy_full_routine[index_A+1:].replace(','+func_A, '')

        # Function B
        index_B = copy_full_routine.replace(',', '-', cont2*2).replace('-', ',', cont2*2-1).index('-')
        func_B = copy_full_routine[:index_B]
        copy_full_routine = copy_full_routine[index_B+1:].replace(','+func_B, '')

        # Function C
        index_C = copy_full_routine.replace(',', '-', cont3*2).replace('-', ',', cont3*2-1).index('-') if len(copy_full_routine) > 20 else 0
        func_C = copy_full_routine[:index_C]

        # Main routine
        main_routine = full_routine[:]
        # Replace from most to least restrictive
        ordered_functions = sorted([func_A, func_B, func_C], key=len, reverse=True)
        for f in ordered_functions:
            if f == func_A:
                main_routine = main_routine.replace(func_A, 'A')
            elif f == func_B:
                main_routine = main_routine.replace(func_B, 'B')
            else:
                main_routine = main_routine.replace(func_C, 'C')

        # RESULT
        is_solution = main_routine.replace('A', '').replace('B', '').replace('C', '').replace(',', '')
        if len(is_solution) == 0 and len(main_routine) <= 20 and len(func_A) <= 20 and len(func_B) <= 20 and len(func_C) <= 20:
            functions.append(main_routine)
            functions.append(func_A)
            functions.append(func_B)
            functions.append(func_C)
            break

        cont3 += 1

    return functions







# Examples
print("Result for examples:")
full_map = [
    [35, 35, 35, 35, 35, 35, 35, 46, 46, 46, 35, 35, 35, 35, 35],
    [35, 46, 46, 46, 46, 46, 35, 46, 46, 46, 35, 46, 46, 46, 35],
    [35, 46, 46, 46, 46, 46, 35, 46, 46, 46, 35, 46, 46, 46, 35],
    [46, 46, 46, 46, 46, 46, 35, 46, 46, 46, 35, 46, 46, 46, 35],
    [46, 46, 46, 46, 46, 46, 35, 46, 46, 46, 35, 35, 35, 46, 35],
    [46, 46, 46, 46, 46, 46, 35, 46, 46, 46, 46, 46, 35, 46, 35],
    [94, 35, 35, 35, 35, 35, 35, 35, 35, 46, 46, 46, 35, 46, 35],
    [46, 46, 46, 46, 46, 46, 35, 46, 35, 46, 46, 46, 35, 46, 35],
    [46, 46, 46, 46, 46, 46, 35, 35, 35, 35, 35, 35, 35, 35, 35],
    [46, 46, 46, 46, 46, 46, 46, 46, 35, 46, 46, 46, 35, 46, 46],
    [46, 46, 46, 46, 35, 35, 35, 35, 35, 35, 35, 35, 35, 46, 46],
    [46, 46, 46, 46, 35, 46, 46, 46, 35, 46, 46, 46, 46, 46, 46],
    [46, 46, 46, 46, 35, 46, 46, 46, 35, 46, 46, 46, 46, 46, 46],
    [46, 46, 46, 46, 35, 46, 46, 46, 35, 46, 46, 46, 46, 46, 46],
    [46, 46, 46, 46, 35, 35, 35, 35, 35, 46, 46, 46, 46, 46, 46]
]
print_map(full_map)
full_routine = get_full_routine(full_map)
print(get_functions(full_routine))





# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
line = file.readlines()[0][:-1].split(',')
intcode = [int(i) for i in line]

# Calculate the solution
full_map = get_full_map(intcode)
print_map(full_map)

full_routine = get_full_routine(full_map)
functions = get_functions(full_routine)

inputs = []
for func in functions:
    inputs += [ord(i) for i in func]+[10]

file = open('./input.data', 'r')
line = file.readlines()[0][:-1].split(',')
intcode = [int(i) for i in line]
intcode[0] = 2
[solutions, _, _, _] = intcode_program([intcode, inputs+[ord('y')]+[10], 0, 0], 10000, -1)
solution = solutions[-1]

# Print the solution
print(solution)

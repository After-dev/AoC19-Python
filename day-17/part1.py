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


# Mark intersections with 12
def mark_intersections(full_map):
    rows = len(full_map)
    cols = len(full_map[0])

    for row in range(1, rows-1):
        for col in range(1, cols-1):
            # Get adjacent codes
            c = full_map[row][col]
            c1 = full_map[row-1][col]
            c2 = full_map[row][col+1]
            c3 = full_map[row+1][col]
            c4 = full_map[row][col-1]

            # If all adjacent are not space (46)
            if c != 46 and c1 != 46 and c2 != 46 and c3 != 46 and c4 != 46:
                full_map[row][col] = 12


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

        # Change: 94 --> X | 35 --> # | 46 --> . | 12 --> O
        line = line.replace('94', 'X').replace('35', '#').replace('46', '.').replace('12', 'O')
        print(line)


def sum_alignment_parameters(full_map):
    sum = 0
    rows = len(full_map)
    cols = len(full_map[0])

    for row in range(1,rows-1):
        for col in range(1,cols-1):
            if full_map[row][col] == 12:
                sum += row*col

    return sum






# Examples
print("Result for examples:")
full_map=[
    [46, 46, 35, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46],
    [46, 46, 35, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46],
    [35, 35, 35, 35, 35, 35, 35, 46, 46, 46, 35, 35, 35],
    [35, 46, 35, 46, 46, 46, 35, 46, 46, 46, 35, 46, 35],
    [35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35],
    [46, 46, 35, 46, 46, 46, 35, 46, 46, 46, 35, 46, 46],
    [46, 46, 35, 35, 35, 35, 35, 46, 46, 46, 94, 46, 46]
]
mark_intersections(full_map)
print_map(full_map)
print(sum_alignment_parameters(full_map))





# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
intcode = [int(i) for i in file.readlines()[0][:-1].split(',')]

# Calculate the solution
full_map = get_full_map(intcode)
mark_intersections(full_map)
print_map(full_map)
solution = sum_alignment_parameters(full_map)

# Print the solution
print(solution)

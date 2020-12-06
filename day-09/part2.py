import numpy as np


def intcode_program(intcode, input):
    relative_base = 0

    # Copy array
    intcode_aux = intcode[:]
    intcode_aux = np.resize(intcode_aux, 2000)

    # Browse array by steps
    pointer = 0
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
            pos = pointer+i+1
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
            intcode_aux[indexes[0]] = input
            pointer += 2

        # OUTPUT
        elif opcode == 4:
            #print('Output: '+intcode_aux[indexes[0]].__str__())
            intcode_aux[0] = intcode_aux[indexes[0]]
            pointer += 2
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

    return intcode_aux[0]





# Examples
print("Result for examples:")
intcode = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
print(intcode_program(intcode, 0))

intcode = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
print(intcode_program(intcode, 0))

intcode = [104, 1125899906842624, 99]
print(intcode_program(intcode, 0))

# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
intcode = [int(i) for i in file.readlines()[0][:-1].split(',')]

# Calculate the solution
solution = intcode_program(intcode,2)

# Print the solution
print(solution)

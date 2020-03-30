import numpy as np
import itertools


def intcode_program(intcode,inputs):
    # Copy array
    intcode_aux=intcode[:]

    # Browse array by steps
    pointer=0
    while(True):
        # Get opcode and mode of parameters
        opcode_instruction=str(intcode_aux[pointer])
        while(len(opcode_instruction) < 5):
            opcode_instruction = '0'+opcode_instruction

        opcode=int(opcode_instruction[-2:])
        mode_params=[
            int(opcode_instruction[-3]),
            int(opcode_instruction[-4]),
            int(opcode_instruction[-5])
        ]

        # Get index of each parameter
        indexes=[
            intcode_aux[pointer+1] if mode_params[0] == 0 and pointer+1 < len(intcode_aux) else pointer+1,
            intcode_aux[pointer+2] if mode_params[1] == 0 and pointer+2 < len(intcode_aux) else pointer+2,
            intcode_aux[pointer+3] if mode_params[2] == 0 and pointer+3 < len(intcode_aux) else pointer+3
        ]

        # Apply opcode operation
        # STOP
        if(opcode == 99):
            break

        # ADDITION
        elif(opcode == 1):
            op1=intcode_aux[indexes[0]]
            op2=intcode_aux[indexes[1]]
            intcode_aux[indexes[2]]=op1+op2
            pointer+=4

        # MULTIPLICATION
        elif(opcode == 2):
            op1=intcode_aux[indexes[0]]
            op2=intcode_aux[indexes[1]]
            intcode_aux[indexes[2]]=op1*op2
            pointer+=4

        # INPUT
        elif(opcode == 3):
            intcode_aux[indexes[0]]=inputs.pop(0)
            pointer+=2

        # OUTPUT
        elif(opcode == 4):
            intcode_aux[0]=intcode_aux[indexes[0]]
            pointer+=2
            break

        # JUMP-IF-TRUE
        elif(opcode == 5):
            if(intcode_aux[indexes[0]] != 0):
                pointer=intcode_aux[indexes[1]]
            else:
                pointer+=3

        # JUMP-IF-FALSE
        elif(opcode == 6):
            if(intcode_aux[indexes[0]] == 0):
                pointer=intcode_aux[indexes[1]]
            else:
                pointer+=3

        # LESS-THAN
        elif(opcode == 7):
            if(intcode_aux[indexes[0]] < intcode_aux[indexes[1]]):
                intcode_aux[indexes[2]]=1
            else:
                intcode_aux[indexes[2]]=0
            pointer+=4

        # EQUAL-TO
        elif(opcode == 8):
            if(intcode_aux[indexes[0]] == intcode_aux[indexes[1]]):
                intcode_aux[indexes[2]]=1
            else:
                intcode_aux[indexes[2]]=0
            pointer+=4

    return intcode_aux[indexes[0]]


def amplify(intcode,conf):
    # Output of each amplifier is the input for next amplifier
    out_signal=0
    inputs=[]
    for phase in conf:
        # Add inputs (phase,previous_output)
        inputs.append(phase)
        inputs.append(out_signal)
        out_signal=intcode_program(intcode,inputs)

    return out_signal





# Examples
print("Result for examples:")
intcode=[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
phases=[4,3,2,1,0]
print(amplify(intcode,phases))

intcode=[3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
phases=[0,1,2,3,4]
print(amplify(intcode,phases))

intcode=[3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
phases=[1,0,4,3,2]
print(amplify(intcode,phases))



# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
intcode=[int(i) for i in file.readlines()[0][:-1].split(',')]

# Calculate the solution
phases=[0,1,2,3,4]
configs=list(itertools.permutations(phases))

solutions=[]
for conf in configs:
    solutions.append(amplify(intcode,conf))

solution=np.max(solutions)

# Print the solution
print(solution)

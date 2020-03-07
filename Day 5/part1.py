import numpy as np


def compute_gravity_assist_program(intcode,input):
    output=-1

    # Copy array
    intcode_aux=intcode[:]

    # Browse array by steps of 4
    pointer=0
    while(True):
        # Get opcode and mode of parameters
        opcode_instruction=str(intcode_aux[pointer])
        for i in range(len(opcode_instruction),5):
            opcode_instruction = '0'+opcode_instruction

        opcode=int(opcode_instruction[-2:])

        mode_params=[
            int(opcode_instruction[-3]),
            int(opcode_instruction[-4]),
            int(opcode_instruction[-5])
        ]

        # Get index of each parameter
        indexes=[
            intcode_aux[pointer+1] if mode_params[0] == 0 else pointer+1,
            intcode_aux[pointer+2] if mode_params[1] == 0 else pointer+2,
            intcode_aux[pointer+3] if mode_params[2] == 0 else pointer+3
        ]

        # Apply opcode operation
        # STOP
        if(opcode == 99):
            return intcode_aux[0]

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
            intcode_aux[indexes[0]]=input
            pointer+=2

        # OUTPUT
        elif(opcode == 4):
            print('Output: '+intcode_aux[indexes[0]].__str__())
            intcode_aux[0]=intcode_aux[indexes[0]]
            pointer+=2




# My puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
lines = file.readlines()[0][:-1].split(',')
intcode=[int(i) for i in lines]

# Calculate the solution
solution=compute_gravity_assist_program(intcode,1)

# Print the solution
print("Solution: "+solution.__str__())
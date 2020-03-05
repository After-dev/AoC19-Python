import numpy as np

def compute_gravity_assist_program(intcode):
    # Copy array
    intcode_aux=intcode[:]

    # Browse array by steps of 4
    for pointer in range(0, len(intcode_aux), 4):
        opcode=intcode_aux[pointer]

        # If sequence ends, break loop
        if(opcode == 99):
            break

        # Get 2 operators
        op1=intcode_aux[intcode_aux[pointer+1]]
        op2=intcode_aux[intcode_aux[pointer+2]]

        # Update destination pos
        if(opcode == 1):
            intcode_aux[intcode_aux[pointer+3]]=op1+op2
        elif(opcode == 2):
            intcode_aux[intcode_aux[pointer+3]]=op1*op2

    return intcode_aux[0]




# My puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
line = file.readlines()[0][:-1].split(',')
intcode=[int(i) for i in line]

# Calculate the solution
for noun in range(100):
    for verb in range(100):
        intcode[1]=noun
        intcode[2]=verb

        output=compute_gravity_assist_program(intcode)

        if(output == 19690720):
            solution=100*noun+verb

            # Print the solution
            print("-noun: "+noun.__str__())
            print("-verb: "+verb.__str__())
            print
            print("Solution: "+solution.__str__())
            break
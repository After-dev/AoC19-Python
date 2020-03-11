import numpy as np
import itertools


def compute_gravity_assist_program(intcode,pointer,input):
    out=[]
    # Copy array
    intcode_aux=intcode[:]

    # Browse array by steps of 4
    while pointer < len(intcode_aux):
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
            intcode_aux[indexes[0]]=input.pop()
            pointer+=2

        # OUTPUT
        elif(opcode == 4):
            out.append(intcode_aux[indexes[0]])
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

    return out,intcode_aux,pointer


def amplify(intcode,phases):
    out_signal=-999999

    # Output of each amplifier is the input for next amplifier
    output=0
    states=[]
    for i in range(len(phases)):
        states.append([intcode,0,[output,phases[i]]])
        [output_list,intcode_aux,pointer]=compute_gravity_assist_program(states[i][0],states[i][1],[output,phases[i]])
        states[i][0]=intcode_aux
        states[i][1]=pointer

        if(len(output_list) > 0):
            output=output_list[0]

    while(len(output_list) > 0):
        for i in range(len(phases)):
            [output_list,intcode_aux,pointer]=compute_gravity_assist_program(states[i][0],states[i][1],[output])
            states[i][0]=intcode_aux
            states[i][1]=pointer

            if(len(output_list) > 0):
                output=output_list[0]

    return output





# Examples
intcode=[3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
phases=[9,8,7,6,5]
print(amplify(intcode,phases))

intcode=[3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
phases=[9,7,8,5,6]
print(amplify(intcode,phases))



# My puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
lines = file.readlines()[0][:-1].split(',')
intcode=[int(i) for i in lines]

# Calculate the solution
phases=[5,6,7,8,9]
permutations=list(itertools.permutations(phases))

solutions=[]
for phase in permutations:
    solutions.append(amplify(intcode,phase))
#print(solutions)

# Print the solution
solution=np.max(solutions)
print("Solution: "+solution.__str__())
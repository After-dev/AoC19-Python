import numpy as np


def compute_gravity_assist_program(intcode):
    opcode_pos=0

    value1=intcode[opcode_pos]
    while((value1 == 1 or value1 == 2) and opcode_pos <= len(intcode)):
        value2=intcode[opcode_pos+1]
        value3=intcode[opcode_pos+2]
        value4=intcode[opcode_pos+3]

        op1=intcode[value2]
        op2=intcode[value3]

        if(value1 == 1):
            intcode[value4]=op1+op2
        else:
            intcode[value4]=op1*op2

        opcode_pos += 4
        value1=intcode[opcode_pos]

    return intcode[0]




# examples
print("Result for examples:")
intcode=[1,9,10,3,2,3,11,0,99,30,40,50]
print(intcode)
compute_gravity_assist_program(intcode)
print(intcode)

print("")

intcode=[1,0,0,0,99]
print(intcode)
compute_gravity_assist_program(intcode)
print(intcode)

print("")

intcode=[2,3,0,3,99]
print(intcode)
compute_gravity_assist_program(intcode)
print(intcode)

print("")

intcode=[2,4,4,5,99,0]
print(intcode)
compute_gravity_assist_program(intcode)
print(intcode)

print("")

intcode=[1,1,1,4,99,5,6,0,99]
print(intcode)
compute_gravity_assist_program(intcode)
print(intcode)



# my puzzle
print("Result for my puzzle:")
file = open('data/input.data', 'r')
lines = file.readlines()

cont=0
for line in lines:
    list=line.split(',')
    intcode=[int(i) for i in list]
    intcode[1]=12
    intcode[2]=2
    print(intcode)
    compute_gravity_assist_program(intcode)
    print(intcode)

    solution=intcode[0]
    print("Solution for line "+cont.__str__()+": "+solution.__str__())
    cont+=1
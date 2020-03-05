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




# my puzzle
print("Result for my puzzle:")
file = open('data/input.data', 'r')
lines = file.readlines()

cont=0
for line in lines:
    list=line.split(',')
    intcode=[int(i) for i in list]
    print(intcode)

    for noun in range(100):
        for verb in range(100):
            aux_intcode=intcode[:]
            aux_intcode[1]=noun
            aux_intcode[2]=verb

            output=compute_gravity_assist_program(aux_intcode)
            if(output == 19690720):
                solution=100*noun+verb
                print("Solution for line "+cont.__str__()+":")
                print("-noun: "+noun.__str__())
                print("-verb: "+verb.__str__())
                print
                print("100*noun + verb = "+solution.__str__())
                break

    cont+=1
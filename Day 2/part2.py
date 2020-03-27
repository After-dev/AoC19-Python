def intcode_program(intcode):
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
file = open('./input.data', 'r')
intcode=[int(i) for i in file.readlines()[0][:-1].split(',')]

# Calculate the solution
for noun in range(100):
    for verb in range(100):
        intcode[1]=noun
        intcode[2]=verb

        output=intcode_program(intcode)

        if(output == 19690720):
            solution=100*noun+verb

            # Print the solution
            print("-noun: "+str(noun))
            print("-verb: "+str(verb))
            print(solution)
            break

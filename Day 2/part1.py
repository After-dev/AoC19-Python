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




# Examples
print("Result for examples:")
intcode=[1,9,10,3,2,3,11,0,99,30,40,50]
print(intcode_program(intcode))

intcode=[1,0,0,0,99]
print(intcode_program(intcode))

intcode=[2,3,0,3,99]
print(intcode_program(intcode))

intcode=[2,4,4,5,99,0]
print(intcode_program(intcode))

intcode=[1,1,1,4,99,5,6,0,99]
print(intcode_program(intcode))



# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
line = file.readlines()[0][:-1].split(',')
intcode=[int(i) for i in line]

# Change initial values
intcode[1]=12
intcode[2]=2

# Calculate the solution
solution=intcode_program(intcode)

# Print the solution
print(solution)
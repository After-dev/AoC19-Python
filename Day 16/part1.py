import numpy as np


def FFT(input,phases):
    base_pattern=[0,1,0,-1]

    # Repeat several phases
    for phase in range(phases):
        # Gen new input
        input_copy=input[:]
        for d in range(len(input_copy)):
            # Calculate digit d
            sum=0
            for p in range(len(input_copy)):
                pos_base_pattern=int(np.floor((p+1)/(d+1))%len(base_pattern))
                sum += input_copy[p]*base_pattern[pos_base_pattern]
            input[d]=abs(sum)%10
        #print('After '+str(phase)+' phase: '+str(input))

    return input








# Examples
print("Result for examples:")
data='12345678'
input=[int(i) for i in data]
print(FFT(input,4))

data='80871224585914546619083218645595'
input=[int(i) for i in data]
print(FFT(input,100))

data='19617804207202209144916044189917'
input=[int(i) for i in data]
print(FFT(input,100))

data='69317163492948606335995924319873'
input=[int(i) for i in data]
print(FFT(input,100))





# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
lines = file.readlines()[0][:-1]
input=[int(i) for i in lines]

# Calculate the solution
solution=FFT(input,100)

# Print the solution
print(solution)
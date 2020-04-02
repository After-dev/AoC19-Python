def FFT(input, phases):
    # Use message from offset. This data is from the end, soo base_pattern is always 1
    offset = int(input[:7])
    input = [int(i) for i in input[offset:]]

    # Repeat several phases
    for phase in range(phases):
        # Calculate digit d
        for d in range(len(input)-2, -1, -1):
            input[d] = (input[d]+input[d+1])%10
        #print('After '+str(phase)+' phase: '+str(input))

    return "".join(map(str, input[:8]))








# Examples
print("Result for examples:")
data = '03036732577212944063491565474664'
input = data.strip()*10000
print(FFT(input, 100))

data = '02935109699940807407585447034323'
input = data.strip()*10000
print(FFT(input, 100))

data = '03081770884921959731165446850517'
input = data.strip()*10000
print(FFT(input, 100))



# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
input = file.readlines()[0][:-1].strip()*10000

# Calculate the solution
solution = FFT(input, 100)

# Print the solution
print(solution)

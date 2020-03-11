import numpy as np


def get_layers(image_data,image_dims):
    layers=[]

    # Calculate layer total size
    layer_size=image_dims[0]*image_dims[1]

    # Split each layer
    for x in range(0,len(image_data),layer_size):
        layer=[]

        # Get data for current layer
        data_layer=image_data[x:x+layer_size]

        # Compose the layer
        for y in range(image_dims[1]):
            layer.append(data_layer[y*image_dims[0]:(y+1)*image_dims[0]])

        layers.append(layer)

    return layers






# Examples
image_data='123456789012'
image_dims=[3,2]
print(get_layers(image_data,image_dims))



# My puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
image_data = file.readlines()[0][:-1]

# Calculate the solution
image_dims=[25,6]
layers=get_layers(image_data,image_dims)

fewest_zeros=image_dims[0]*image_dims[1]
fewest_layer=-1
for layer in layers:
    n_zeros=0

    for row in layer:
        n_zeros += row.count('0')

    if(n_zeros < fewest_zeros):
        fewest_zeros=n_zeros
        fewest_layer=layer

ones=twos=0
for row in fewest_layer:
    ones += row.count('1')
    twos += row.count('2')

# Print the solution
solution=ones*twos
print(fewest_layer)
print("Solution: "+solution.__str__())
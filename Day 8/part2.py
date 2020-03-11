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


def decode_image(layers,image_dims):
    image_decoded=[]

    # Search color for each pixel
    for row in range(image_dims[1]):
        row_total=''
        for col in range(image_dims[0]):
            # Compare same pixel of each layer, from first to last
            color=''
            for layer in layers:
                color=layer[row][col]

                # If current pixel's color is not transparent, break
                if(color != '2'):
                    break

            row_total += color

        image_decoded.append(row_total)

    return image_decoded





# Examples
image_data='0222112222120000'
image_dims=[2,2]
layers=get_layers(image_data,image_dims)
print(decode_image(layers,image_dims))



# My puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
image_data = file.readlines()[0][:-1]

# Calculate the solution
image_dims=[25,6]
layers=get_layers(image_data,image_dims)
image_decoded=decode_image(layers,image_dims)

# Print the solution
print("Solution:")
for row in image_decoded:
    print(row.replace('0',' ').replace('1','#'))
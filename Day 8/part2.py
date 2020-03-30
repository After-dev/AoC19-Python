def get_layers(image_data,image_dims,output_format='1d'):
    # Calculate layer total size
    layer_size=image_dims[0]*image_dims[1]

    # Split all data in different layers (1D)
    layers_1d=[image_data[i:i+layer_size] for i in range(0,len(image_data),layer_size)]
    if(output_format == '1d'):
        return layers_1d

    # Split each layer in rows (2D)
    layers_2d=[]
    row_size=layer_size/image_dims[1]
    for layer_1d in layers_1d:
        layer_2d=[layer_1d[i:i+row_size] for i in range(0,len(layer_1d),row_size)]
        layers_2d.append(layer_2d)

    return layers_2d


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
print("Result for examples:")
image_data='0222112222120000'
image_dims=[2,2]
layers=get_layers(image_data,image_dims,'2d')
print(decode_image(layers,image_dims))



# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
image_data = file.readlines()[0][:-1]
image_dims=[25,6]

# Calculate the solution
layers=get_layers(image_data,image_dims,'2d')
image_decoded=decode_image(layers,image_dims)

# Print the solution
for row in image_decoded:
    print(row.replace('0',' ').replace('1','#'))

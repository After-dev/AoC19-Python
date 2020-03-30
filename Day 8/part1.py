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






# Examples
print("Result for examples:")
image_data='123456789012'
image_dims=[3,2]
print(get_layers(image_data,image_dims,'2d'))



# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
image_data = file.readlines()[0][:-1]
image_dims=[25,6]

# Calculate the solution
layers=get_layers(image_data,image_dims)

fewest_zeros=image_dims[0]*image_dims[1]
fewest_layer=-1
for layer in layers:
    n_zeros=layer.count('0')
    if(n_zeros < fewest_zeros):
        fewest_zeros=n_zeros
        fewest_layer=layer

ones=fewest_layer.count('1')
twos=fewest_layer.count('2')
solution=ones*twos

# Print the solution
print(solution)

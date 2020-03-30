import numpy as np


def intcode_program(state, max_size, n_read):
    output=[]

    # Get state
    intcode_aux=state[0][:]
    inputs=state[1]
    pointer=state[2]
    relative_base=state[3]

    # Resize array (get more memory)
    intcode_aux=np.resize(intcode_aux,(max_size))

    # Browse array by steps
    while pointer < len(intcode):
        # Get opcode and mode of parameters
        opcode_instruction=str(intcode_aux[pointer])
        while(len(opcode_instruction) < 5):
            opcode_instruction = '0'+opcode_instruction

        opcode=int(opcode_instruction[-2:])
        mode_params=[
            int(opcode_instruction[-3]),
            int(opcode_instruction[-4]),
            int(opcode_instruction[-5])
        ]

        # Get index of each parameter
        indexes=[-1,-1,-1]
        for i in range(len(indexes)):
            pos=pointer+1+i
            if(pos < len(intcode_aux)):
                if(mode_params[i] == 0):
                    indexes[i]=intcode_aux[pos]
                elif(mode_params[i] == 1):
                    indexes[i]=pos
                elif(mode_params[i] == 2):
                    indexes[i]=relative_base+intcode_aux[pos]

        # Apply opcode operation
        # STOP
        if(opcode == 99):
            break

        # ADDITION
        elif(opcode == 1):
            op1=intcode_aux[indexes[0]]
            op2=intcode_aux[indexes[1]]
            intcode_aux[indexes[2]]=op1+op2
            pointer+=4

        # MULTIPLICATION
        elif(opcode == 2):
            op1=intcode_aux[indexes[0]]
            op2=intcode_aux[indexes[1]]
            intcode_aux[indexes[2]]=op1*op2
            pointer+=4

        # INPUT
        elif(opcode == 3):
            intcode_aux[indexes[0]]=inputs.pop(0)
            pointer+=2

        # OUTPUT
        elif(opcode == 4):
            #print('Output: '+intcode_aux[indexes[0]].__str__())
            output.append(intcode_aux[indexes[0]])
            pointer+=2
            if(len(output) == n_read):
                break

        # JUMP-IF-TRUE
        elif(opcode == 5):
            if(intcode_aux[indexes[0]] != 0):
                pointer=intcode_aux[indexes[1]]
            else:
                pointer+=3

        # JUMP-IF-FALSE
        elif(opcode == 6):
            if(intcode_aux[indexes[0]] == 0):
                pointer=intcode_aux[indexes[1]]
            else:
                pointer+=3

        # LESS-THAN
        elif(opcode == 7):
            if(intcode_aux[indexes[0]] < intcode_aux[indexes[1]]):
                intcode_aux[indexes[2]]=1
            else:
                intcode_aux[indexes[2]]=0
            pointer+=4

        # EQUAL-TO
        elif(opcode == 8):
            if(intcode_aux[indexes[0]] == intcode_aux[indexes[1]]):
                intcode_aux[indexes[2]]=1
            else:
                intcode_aux[indexes[2]]=0
            pointer+=4

        # ADJUST RELATIVE BASE
        elif(opcode == 9):
            relative_base += intcode_aux[indexes[0]]
            pointer+=2

    return output,intcode_aux,pointer,relative_base


def painting_robot(intcode):
    painted_panels={}
    pos=(0,0)
    dir=0
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    state=[intcode,[],0,0]

    # Movement until intcode ends
    while(True):
        # Get current panel color
        if(len(painted_panels) == 0):
            current_color=1
        else:
            current_color=painted_panels[pos] if pos in painted_panels else 0
        state[1].append(current_color)

        # Get color and direction
        [output,state[0],state[2],state[3]]=intcode_program(state, 2000, 2)
        if(len(output) != 2):
            break

        [color,direction]=output

        # Paint panel
        painted_panels[pos]=color

        # Move robot
        dir = (dir-1 if direction == 0 else dir+1)%len(directions)
        pos=(pos[0]+directions[dir][0],pos[1]+directions[dir][1])

    return painted_panels

def print_panel(panel):
    # Get bounds
    points=[i for i in panel]
    min_y=min([i[0] for i in points])
    min_x=min([i[1] for i in points])
    max_y=max([i[0] for i in points])
    max_x=max([i[1] for i in points])

    # Generate image
    fig=np.zeros([max_y-min_y+1,max_x-min_x+1], dtype=np.uint8)
    for point in panel:
        fig[max_y-point[0]][point[1]-min_x]=panel[point]

    # Show fig
    for row in fig:
        row_text=''
        for c in row:
            row_text += str(c)
        print(row_text.replace('0',' ').replace('1','#'))





# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
intcode=[int(i) for i in file.readlines()[0][:-1].split(',')]

# Calculate the solution
panel=painting_robot(intcode)

# Print the solution
print_panel(panel)

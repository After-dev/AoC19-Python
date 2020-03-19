import numpy as np


def get_entrance(map):
    pos_entrance=(-1,-1)
    for row in range(len(map)):
        for col in range(len(map[0])):
            if(map[row][col] == '@'):
                pos_entrance=(row,col)
                map[row]=map[row].replace('@','.')
                break
    return pos_entrance


def get_keys(map):
    keys={}
    for row in range(len(map)):
        for col in range(len(map[0])):
            if(map[row][col].islower()):
                keys.update({map[row][col]: (row,col)})
    return keys


def collect_keys(map,keys,pos,prev_pos,steps):
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    field_code=map[pos[0]][pos[1]]

    # Invalid position
    if(field_code == '#' or (field_code.isupper() and field_code.lower() in keys)):
        return float('inf')
    # All keys finded
    if(len(keys) == 0):
        return steps-1

    # If current field has a key
    key_finded=False
    if(field_code != '.' and field_code != '#' and field_code.islower() and field_code in keys):
        key_finded=True
        # Delete key and its door from map
        copy_keys=keys.copy()
        del copy_keys[field_code]
        keys=copy_keys

    # Move to posible fields
    min_steps=float('inf')
    for d in range(len(directions)):
        new_pos=(pos[0]+directions[d][0],pos[1]+directions[d][1])
        if(new_pos != prev_pos or key_finded):
            s=collect_keys(map,keys,new_pos,pos,steps+1)
            if(s < min_steps):
                min_steps=s

    return min_steps








# Examples
print("Result for examples:")
"""
map=[
    '#########',
    '#b.A.@.a#',
    '#########'
]
pos_entrance=get_entrance(map)
keys=get_num_keys(map)
print(collect_keys(map,keys,pos_entrance,pos_entrance,0))

map=[
    '########################',
    '#f.D.E.e.C.b.A.@.a.B.c.#',
    '######################.#',
    '#d.....................#',
    '########################'
]
pos_entrance=get_entrance(map)
keys=get_num_keys(map)
print(collect_keys(map,keys,pos_entrance,pos_entrance,0))

map=[
    '########################',
    '#...............b.C.D.f#',
    '#.######################',
    '#.....@.a.B.c.d.A.e.F.g#',
    '########################'
]
pos_entrance=get_entrance(map)
keys=get_keys(map)
print(collect_keys(map,keys,pos_entrance,pos_entrance,0))

map=[
    '#################',
    '#i.G..c...e..H.p#',
    '########.########',
    '#j.A..b...f..D.o#',
    '########@########',
    '#k.E..a...g..B.n#',
    '########.########',
    '#l.F..d...h..C.m#',
    '#################'
]
pos_entrance=get_entrance(map)
keys=get_keys(map)
print(collect_keys(map,keys,pos_entrance,pos_entrance,0))

map=[
    '########################',
    '#@..............ac.GI.b#',
    '###d#e#f################',
    '###A#B#C################',
    '###g#h#i################',
    '########################'
]
pos_entrance=get_entrance(map)
keys=get_num_keys(map)
print(collect_keys(map,keys,pos_entrance,pos_entrance,0))
"""




# My puzzle
"""
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
line = file.readlines()[0][:-1].split(',')
intcode=[int(i) for i in line]

# Calculate the solution
full_map=get_full_map(intcode)
mark_intersections(full_map)
print_map(full_map)
solution=sum_alignment_parameters(full_map)

# Print the solution
print(solution)
"""
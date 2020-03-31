import numpy as np


def minimum_ORE(reactions):
    ORE_units = 0
    unused_chemicals = {}
    generate_chemicals = [['FUEL', 1]]

    while len(generate_chemicals) > 0:
        # Get next chemical to generate
        [chemical, units_needed] = generate_chemicals.pop(0)

        # Try to reduce units_needed with unused chemicals
        if chemical in unused_chemicals:
            unused = unused_chemicals[chemical]
            if units_needed >= unused:
                units_needed -= unused
                del unused_chemicals[chemical]
            else:
                unused_chemicals[chemical] -= units_needed
                units_needed = 0

        if units_needed != 0:
            # Get reaction rule
            [reaction_output, reaction_inputs] = reactions[chemical]

            # Calculate how many times is it necessary to apply the rule
            p = int(np.ceil(float(units_needed)/float(reaction_output)))

            # Store unused chemicals
            unused_units = reaction_output*p-units_needed
            if unused_units > 0:
                unused_chemicals[chemical] = unused_units

            # For each input
            for input in reaction_inputs.split(','):
                # Get input
                [input_units, input_chemical] = input.split(' ')

                # Compute units to generate
                input_units_generated = p*int(input_units)

                # Add input chemical to generate list
                if input_chemical == 'ORE':
                    ORE_units += input_units_generated
                else:
                    generate_chemicals.append([input_chemical, input_units_generated])

    return ORE_units





# Examples
print("Result for examples:")
reactions = {
    'A':    [10, '10 ORE'],
    'B':    [1, '1 ORE'],
    'C':    [1, '7 A,1 B'],
    'D':    [1, '7 A,1 C'],
    'E':    [1, '7 A,1 D'],
    'FUEL': [1, '7 A,1 E']
}
print(minimum_ORE(reactions))

reactions = {
    'A':    [2, '9 ORE'],
    'B':    [3, '8 ORE'],
    'C':    [5, '7 ORE'],
    'AB':   [1, '3 A,4 B'],
    'BC':   [1, '5 B,7 C'],
    'CA':   [1, '4 C,1 A'],
    'FUEL': [1, '2 AB,3 BC,4 CA']
}
print(minimum_ORE(reactions))

reactions = {
    'NZVS':  [5, '157 ORE'],
    'DCFZ':  [6, '165 ORE'],
    'FUEL':  [1, '44 XJWVT,5 KHKGT,1 QDVJ,29 NZVS,9 GPVTF,48 HKGWZ'],
    'QDVJ':  [9, '12 HKGWZ,1 GPVTF,8 PSHF'],
    'PSHF':  [7, '179 ORE'],
    'HKGWZ': [5, '177 ORE'],
    'XJWVT': [2, '7 DCFZ,7 PSHF'],
    'GPVTF': [2, '165 ORE'],
    'KHKGT': [8, '3 DCFZ,7 NZVS,5 HKGWZ,10 PSHF']
}
print(minimum_ORE(reactions))

reactions = {
    'STKFG': [1, '2 VPVL,7 FWMGM,2 CXFTF,11 MNCFX'],
    'VPVL':  [8, '17 NVRVD,3 JNWZP'],
    'FUEL':  [1, '53 STKFG,6 MNCFX,46 VJHF,81 HVMC,68 CXFTF,25 GNMV'],
    'FWMGM': [5, '22 VJHF,37 MNCFX'],
    'NVRVD': [4, '139 ORE'],
    'JNWZP': [7, '144 ORE'],
    'HVMC':  [3, '5 MNCFX,7 RFSQX,2 FWMGM,2 VPVL,19 CXFTF'],
    'GNMV':  [6, '5 VJHF,7 MNCFX,9 VPVL,37 CXFTF'],
    'MNCFX': [6, '145 ORE'],
    'CXFTF': [8, '1 NVRVD'],
    'RFSQX': [4, '1 VJHF,6 MNCFX'],
    'VJHF':  [6, '176 ORE']
}
print(minimum_ORE(reactions))

reactions = {
    'CNZTR': [8, '171 ORE'],
    'PLWSL': [4, '7 ZLQW,3 BMBT,9 XCVML,26 XMNCP,1 WPTQ,2 MZWV,1 RJRHP'],
    'BHXH':  [4, '114 ORE'],
    'BMBT':  [6, '14 VRPVC'],
    'FUEL':  [1, '6 BHXH,18 KTJDG,12 WPTQ,7 PLWSL,31 FHTLT,37 ZDVW'],
    'FHTLT': [6, '6 WPTQ,2 BMBT,8 ZLQW,18 KTJDG,1 XMNCP,6 MZWV,1 RJRHP'],
    'ZLQW':  [6, '15 XDBXC,2 LTCX,1 VRPVC'],
    'ZDVW':  [1, '13 WPTQ,10 LTCX,3 RJRHP,14 XMNCP,2 MZWV,1 ZLQW'],
    'WPTQ':  [4, '5 BMBT'],
    'KTJDG': [9, '189 ORE'],
    'XMNCP': [2, '1 MZWV,17 XDBXC,3 XCVML'],
    'XDBXC': [2, '12 VRPVC,27 CNZTR'],
    'XCVML': [5, '15 KTJDG,12 BHXH'],
    'MZWV':  [7, '3 BHXH,2 VRPVC'],
    'VRPVC': [7, '121 ORE'],
    'RJRHP': [6, '7 XCVML'],
    'LTCX':  [5, '5 BHXH,4 VRPVC']
}
print(minimum_ORE(reactions))



# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
lines = [line[:-1].replace(', ', ',').split(' => ') for line in file.readlines()]
reactions = {}
for line in lines:
    [inputs, output] = line
    [output_units, output_chemical] = output.split(' ')
    reactions[output_chemical] = [int(output_units), inputs]

# Calculate the solution
solution=minimum_ORE(reactions)

# Print the solution
print(solution)

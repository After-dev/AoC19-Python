import numpy as np


def eval_password(password):
    # Conditions
    is_increasing=True
    has_two_eq_digits=False

    previous_digit=''
    for digit in str(password):
        if digit < previous_digit:
            is_increasing = False
            break
        if digit == previous_digit:
            has_two_eq_digits = True

        previous_digit = digit

    if is_increasing and has_two_eq_digits:
        return True

    return False

def gen_password_range(min,max):
    valid_passwords = []

    # Generate possible passwords
    for password in range(min, max + 1):
        # Eval password
        if(eval_password(password)):
            valid_passwords.append(password)

    return len(valid_passwords)




# My puzzle
print("Result for my puzzle:")
# Load data
file = open('data/input.data', 'r')
lines = file.readlines()[0].split('-')
min=int(lines[0])
max=int(lines[1])

# Calculate the solution
solution=gen_password_range(min,max)

# Print the solution
print("Solution is: "+solution.__str__())
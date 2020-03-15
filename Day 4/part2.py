def eval_password(password):
    # Conditions
    is_increasing=True
    duplicate_digits={}

    previous_digit=password[0]
    for digit in password[1:]:
        # Verify increasing condition
        if digit < previous_digit:
            is_increasing = False
            break
        elif digit == previous_digit:
            if digit in duplicate_digits:
                duplicate_digits[digit] += 1
            else:
                duplicate_digits.update({digit : 2})

        previous_digit = digit

    # If conditions are True
    return is_increasing and 2 in [duplicate_digits[i] for i in duplicate_digits]

def gen_password_range(min,max):
    valid_passwords = []

    # Generate possible passwords
    for password in range(min, max + 1):
        # Eval password
        if(eval_password(str(password))):
            valid_passwords.append(password)

    return len(valid_passwords)




# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
lines = file.readlines()[0].split('-')
min=int(lines[0])
max=int(lines[1])

# Calculate the solution
solution=gen_password_range(min,max)

# Print the solution
print(solution)
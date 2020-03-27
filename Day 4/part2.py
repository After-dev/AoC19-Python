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
            if digit not in duplicate_digits:
                duplicate_digits[digit] = 1
            duplicate_digits[digit] += 1

        previous_digit = digit

    # If conditions are True
    return is_increasing and 2 in [duplicate_digits[i] for i in duplicate_digits]


def gen_valid_password(min,max):
    valid_passwords = []

    # Generate possible passwords
    for password in range(min, max + 1):
        # Eval password
        if(eval_password(str(password))):
            valid_passwords.append(password)

    return valid_passwords




# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
bounds = file.readlines()[0].split('-')
min=int(bounds[0])
max=int(bounds[1])

# Calculate the solution
solution=len(gen_valid_password(min,max))

# Print the solution
print(solution)

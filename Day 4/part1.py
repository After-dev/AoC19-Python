def eval_password(password):
    # Conditions
    is_increasing = True
    has_duplicates = False

    previous_digit = password[0]
    for digit in password[1:]:
        # Verify increasing condition
        if digit < previous_digit:
            is_increasing = False
            break
        # Verify duplicate condition
        elif digit == previous_digit:
            has_duplicates = True

        previous_digit = digit

    # If conditions are True
    return is_increasing and has_duplicates


def gen_valid_password(min, max):
    valid_passwords = []

    # Generate possible passwords
    for password in range(min, max + 1):
        # Eval password
        if eval_password(str(password)):
            valid_passwords.append(password)

    return valid_passwords




# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
bounds = file.readlines()[0].split('-')
min = int(bounds[0])
max = int(bounds[1])

# Calculate the solution
solution = len(gen_valid_password(min, max))

# Print the solution
print(solution)

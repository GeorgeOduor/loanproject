import itertools

# Provided information
name = "George Oduor"
wife_name = "Mary Atieno"
kids = ["Kevin Otieno", "Rael Achieng"]
ages = [40, 30, 12, 9]
address = "Lucky Summer Estate"

# Function to generate all possible password combinations
def generate_password_combinations(include_special_chars=True):
    names = [name.lower(), wife_name.lower()] + [kid.lower().replace(" ", "") for kid in kids]
    ages_str = [str(age) for age in ages]

    all_characters = ''.join(names + ages_str + [address.lower()])
    if include_special_chars:
        all_characters += "!@#$%^&*()_+-=[]{}|;:,.<>?~"

    password_combinations = []

    # Generate permutations of different lengths (1 to total characters)
    for r in range(1, len(all_characters) + 1):
        permutations = itertools.permutations(all_characters, r)
        password_combinations.extend([''.join(perm) for perm in permutations])
    print(password_combinations)
    return password_combinations

# Generate password combinations including special characters
all_passwords_with_special_chars = generate_password_combinations(include_special_chars=True)

# Generate password combinations excluding special characters
all_passwords_without_special_chars = generate_password_combinations(include_special_chars=False)

# Print the results
print("All Password Combinations (Including Special Characters):")
print(all_passwords_with_special_chars)

print("\nAll Password Combinations (Excluding Special Characters):")
print(all_passwords_without_special_chars)

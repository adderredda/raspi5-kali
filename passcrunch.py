import itertools

# Get user input for characters to generate passwords from
characters = input("Enter the characters to generate passwords from: ")

# Generate all possible password combinations using the entered characters
passwords = []
for i in range(1, len(characters) + 1):
    passwords.extend([''.join(password) for password in itertools.product(characters, repeat=i)])

# Save all possible password combinations to a file named passwords.txt
with open("passwords.txt", "w") as file:
    for password in passwords:
        file.write(f"{password}\n")

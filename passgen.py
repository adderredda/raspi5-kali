import random
import string

def generate_password(length, characters):
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome! Let's generate passwords.")
    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            if password_length <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    characters1 = string.ascii_letters + string.digits + string.punctuation
    characters2 = string.ascii_letters + string.digits
    password1 = generate_password(password_length, characters1)
    password2 = generate_password(password_length, characters2)

    print("Special Characters:", password1)
    print("No Special Character:", password2)

if __name__ == "__main__":
    main()

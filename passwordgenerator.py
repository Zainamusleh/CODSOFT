import random
import string


def password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


while True:
    length = int(input("Enter the password length: "))
    if length > 0:
        break
    else:
        print("Please enter a positive number.")

password = password(length)
print("Generated Password:", password)

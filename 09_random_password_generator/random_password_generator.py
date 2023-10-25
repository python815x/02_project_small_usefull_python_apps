import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&'()*+,-./'")


def generate_password(length):
    password_length = length

    random.shuffle(characters)

    password = []

    for char in range(password_length):
        password.append(random.choice(characters))

    print(''.join(password))

    random.shuffle(password)

    print("".join(password))


length = int(input("How long do you want your password to be? :  "))
generate_password(length)


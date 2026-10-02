import random
import string

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits
    password_list = [random.choice(all_characters) for _ in range(length)]
    random.shuffle(password_list)
    return "".join(password_list)

new_password = generate_password(12)
print("Your random password is:", new_password)

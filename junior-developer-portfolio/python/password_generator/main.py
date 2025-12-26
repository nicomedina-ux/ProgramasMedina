# Password Generator
# Genera contraseñas aleatorias seguras

import random
import string

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Contraseña generada:", generate_password())

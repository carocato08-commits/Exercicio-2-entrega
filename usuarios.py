# Faker tiene que crear los datos ficticios de 15 usuarios y se deben almacenar en un diccionario
from faker import Faker
import random

faker = Faker("es_ES")
usuarios = {}

# Generamos los datos de 15 usuarios
for codigo in range(1, 16):
    usuarios[codigo] = {
        "nombre": faker.name(),
        "direccion": faker.address(),
        "email": faker.email(),
        "telefono": faker.phone_number(),
    }

print("Usuarios creados:")
for codigo, usuario in usuarios.items():
    print(codigo, usuario)

# Seleccionamos un usuario de forma aleatoria
codigo_aleatorio, datos_usuario = random.choice(list(usuarios.items()))
print(f"El usuario llamado {datos_usuario['nombre']} fue el afortunado.")

# URL do repositorio GitHub: https://github.com/carocato08-commits/Exercicio2_Usuarios_Faker
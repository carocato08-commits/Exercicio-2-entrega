#Faker tiene que crear los datos ficticcios de 15 usuarios y se deben almacenar en un diccionarios
from faker import Faker
import random
faker= Faker("es_ES")

usuarios={}
#Generamos los datos de 15 usuarios
for codigo in range(1,16):
    usuarios [codigo]= {"nombre":faker.name(),"direccion":faker.address(),"email":faker.email(), "telefono":faker.phone_number()
                       }
    print(usuarios) 

#2Seleccionamos un usuario de forma aleatoria 
usuario_afortunado= random.choice(list(usuarios.values()))
print(f"El usuario llamado{usuario_afortunado['nombre']} fue el afortunado")

# URL do repositorio GitHub: https://github.com/carocato08-commits/Exercicio2_Usuarios_Faker
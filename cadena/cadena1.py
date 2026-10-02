vector = ["j", "u", "a", "n"]
print(type(vector))

for letra in vector:
    print(letra)
nombre = "Juan"
print("*"*13)
for letra in nombre: 
    print(letra)

print(len(vector)) 
print(len(nombre)) 

def convertir_A_Mayuscula(texto):
    return f"{texto.upper()}"

def convertir_A_Minuscula(texto):
    return f"{texto.lower()}"

def capitalizar(texto):
    return f"{texto.capitalize()}"

def titulo(texto):
    return f"{texto.title()}"

def  generarEmail(texto):
    nombre = texto.split()
    email = ''.join(palabra[:3].lower() for palabra in nombre)
    return f"{email}@uamv.edu.ni"

print(convertir_A_Mayuscula(nombre))
#print(convertir_A_Mayuscula(vector))

for letra in vector:
    print(convertir_A_Mayuscula(letra), end="")

print()
print(convertir_A_Minuscula(nombre))
print(capitalizar(nombre))
print(titulo(nombre))
print(generarEmail("Horwin Josue Castillo Bolaños"))
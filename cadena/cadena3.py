#Leer una cadena de texto y buscar una palabra o texto
def buscar(valor):
    posicion = cadena.find(valor)
    if posicion >= 0:
        return "Se encontro el valor buscado"
    else:
        return "No se encuentra el valor que buscas"
def saberSiContiene(cadena, valor):
    return valor in cadena
   
cadena = input('Dime una frase: ')
valor = input('Dime la palabra que quieres buscar: ')

print(buscar(cadena, valor))
print(saberSiContiene(cadena, valor))
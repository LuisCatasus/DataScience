"""
Defina una función recursiva que reciba un número y devuelva el factorial de dicho número
Añada un programa que pida números positivos al usuario (en caso de no ser positivo volver a pedirlo
hasta que lo sea) y, haciendo uso de la función anterior, calcule y muestre el factorial de
dichos números. El programa termina cuando el usuario pulse el número 0.  
"""
import sys


# Pedimos al usuario que ingrese un entero positivo
def entero_positivo():
    while True:
        n = int(input("Ingresa un numero positivo, mayor de 0: "))
        if n == 0:
            sys.exit(0)  # si el numeroes 0 el programa se acaba
        if n > 0:
            break #si es un entero mayorr que cero, lo acepta como entrada
    return n # devuelve el entero positivo en una variable llamada n

n= entero_positivo()

def factorial(n):
    if n ==1:
        resultado = 1
    elif n > 1:
        resultado = n * factorial (n-1)
    return resultado

fact = factorial(n) 
print('El Factorial de ', n ,'es' , fact)

"""
def main():
    n = entero_positivo()
    fact = factorial(n) 
    print('El Factorial de ', n ,'es' , fact)

main()
"""

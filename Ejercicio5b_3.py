"""
Defina una función recursiva que reciba un número y devuelva el factorial de dicho número
Añada un programa que pida números positivos al usuario (en caso de no ser positivo volver a pedirlo
hasta que lo sea) y, haciendo uso de la función anterior, calcule y muestre el factorial de
dichos números. El programa termina cuando el usuario pulse el número 0.
Añada un programa que pida un número N y, haciendo uso de la función anterior, calcule y
muestre el factorial de cada número comprendido entre 1 y N.
"""
#While True:
n = int(input('Ingresa un número positivo mayor de cero:'))
if n> 1:
	n
elif n==0:
    exit
else:
    print('El numero debe ser mayor de 1. Ingrese nuevo número')

def factorial(i):
    for i in range (1, n + 1):
        if i ==1:
            resultado = 1
        elif i > 1:
            resultado = i * factorial (i-1)
        return resultado
for i in range (1, n + 1):
    fact = factorial(n) 
    print('El Factorial de ', i ,'es' , fact)       

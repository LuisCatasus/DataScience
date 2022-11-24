"""Defina una función recursiva que reciba un número y devuelva el número de
la serie de Fibonacci de dicho número.
Añada un programa que pida números positivos al usuario (en caso de no ser positivo
volver a pedirlo hasta que lo sea) y, haciendo uso de la función anterior, calcule
y muestre el Fibonacci de dichos números. El programa termina cuando el usuario pulse el número 0.  
"""
n = int(input('Ingresa un número positivo mayor de cero:'))
if n> 1:
	n
else:
    print('El numero debe ser mayor de 1. Ingrese nuevo número')
    exit

def fibonacci(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

fib = fibonacci(n)
print(fib)
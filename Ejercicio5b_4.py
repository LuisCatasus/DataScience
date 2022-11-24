"""Defina una función recursiva que reciba un número y devuelva el número de
la serie de Fibonacci de dicho número.
"""
def fibonacci(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

fib = fibonacci(10) # ejemplo para n=10
print(fib)
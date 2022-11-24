"""
Defina una función recursiva que reciba un número y devuelva el factorial de dicho número
"""
def factorial(n):
	if n==0 or n==1:
		resultado = 1
	elif n>1:
		resultado = n * factorial(n-1)
	return resultado

fact = factorial(5) # ejemplo para n=5
print(fact)


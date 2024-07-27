# Buscador de números primos en un rango:  
# Escribir un programa que pida al usuario dos números enteros y luego 
# muestre por pantalla todos los números primos que se encuentren en el 
# rango comprendido entre esos dos números.

print("----------------------------------------------------------------")
print("------------------------ Prime Number Finder -------------------")
print("----------------------------------------------------------------")

# Request the start and end of the range from the user
start = int(input("Please enter the start of the range: "))
end = int(input("Please enter the end of the range: "))

def is_prime(n): # verificar si es primo
    if n <= 1: # si es <= 1 no es primo
        return False
    for i in range(2, int(n**0.5) + 1): # verfica si es primo
        if n % i == 0:
            return False
    return True

primes = [] # alamcenar primos
for num in range(start, end + 1): # end + 1 para verificar hasta el ultimo numero
    if is_prime(num):
        primes.append(num) # agrega al array 

print("Prime numbers in the range", start, "to", end, ":", primes)
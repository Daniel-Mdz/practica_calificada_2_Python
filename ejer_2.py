# Calculadora de área y perímetro:  
# Escribir un programa que pregunte al usuario las dimensiones de un 
# rectángulo (largo y ancho) y calcule tanto el área como el perímetro del 
# rectángulo, mostrando ambos valores por pantalla.
print("----------------------------------------------------------------")
print("----------------------- Area and Perimeter ---------------------")
print("----------------------------------------------------------------")
large = int(input("Please enter a large of rectangle: "))
width = int(input("Please enter a width of rectangle: "))

area = large * width
perimeter = 2 * (large + width)

print("Area: ", area) # como para concatenar el print con un valor entero + se usa para string
print("Perimeter: ", perimeter)
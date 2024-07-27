# Conversor de unidades de temperatura:  
# Escribir un programa que pregunte al usuario por una temperatura en 
# grados Celsius y luego convierta esa temperatura a grados Fahrenheit y 
# Kelvin, mostrando los resultados por pantalla.

print("----------------------------------------------------------------")
print("-------------------- Temperature Converter ---------------------")
print("----------------------------------------------------------------")

# Request the user to enter a temperature in Celsius
celsius = float(input("Please enter a temperature in Celsius: "))

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Convert the entered temperature to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit: ", fahrenheit)
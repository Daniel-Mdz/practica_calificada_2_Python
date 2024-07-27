# 1. Programa de promedio de calificaciones:  
# Escribir un programa que pida al usuario que ingrese las calificaciones 
# de varios exámenes y luego calcule y muestre por pantalla el promedio 
# de esas calificaciones.

print("----------------------------------------------------------------")
print("----------------------- average qualifiers ---------------------")
print("----------------------------------------------------------------")

qualification_1 = input("Please enter your first qualifier: ")
while qualification_1.isdigit() == 0:
    print("\t [ERROR] - Please enter a number: ")
    qualification_1 = input("Please enter your first qualifier: ")

qualification_2 = input("Please enter your second qualifier: ")
while qualification_2.isdigit() == 0:
    print("\t [ERROR] - Please enter a number: ")
    qualification_2 = input("Please enter your second qualifier: ")
    
qualification_3 = input("Please enter your third qualifier: ")
while qualification_3.isdigit() == 0:
    print("\t [ERROR] - Please enter a number: ")
    qualification_3 = input("Please enter your third qualifier: ")
    
qualification_4 = input("Please enter your fourth qualifier: ")
while qualification_4.isdigit() == 0:
    print("\t [ERROR] - Please enter a number: ")
    qualification_4 = input("Please enter your fourth qualifier: ")

total_qualifications = int(qualification_1) + int(qualification_2) + int(qualification_3) + int(qualification_4)
prom_total = total_qualifications / 4;

print("\t\nYour average score is: ", prom_total)
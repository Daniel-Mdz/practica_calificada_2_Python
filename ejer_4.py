# Contador de palabras en un texto:    
# Escribir un programa que pida al usuario que ingrese un texto y luego 
# cuente y muestre por pantalla la cantidad de palabras que contiene ese 
# texto.

print("----------------------------------------------------------------")
print("------------------------ Word Counter --------------------------")
print("----------------------------------------------------------------")

# Request the user to enter a text
text = input("Please enter a text: ")

# Function to count the number of words in the text
# def count_words(text):
#     words = text.split()
#     return len(words)
def count_words(text):
    words = text.split() # numero de valores
    count = 0
    for word in words:
        count += 1
    return count

# Count the words in the entered text
word_count = count_words(text)

print("Number of words: ", word_count)
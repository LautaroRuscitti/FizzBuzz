# /*
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */


for index in range (1, 100):
        divisiblebythree = index % 3 == 0
        divisiblebyfive = index % 5 == 0
        if divisiblebythree & divisiblebyfive:
            print("Hire me")
        elif divisiblebythree:
            print("Hire")
        elif divisiblebyfive:
            print("Me")
        else:
            print(index)

        
    

from msvcrt import getch
import os
option = 0


print("-----> 1. Primer ajuste <-----")
print("       2. Mejor ajuste")
print("       3. Peor ajuste")
print("       4. Siguiente ajuste")
print("       Salir")
    
def Menu(count_option):
    if count_option == 0:
        print("-----> 1. Primer ajuste <-----")
        print("       2. Mejor ajuste")
        print("       3. Peor ajuste")
        print("       4. Siguiente ajuste")
        print("       Salir")

    elif count_option == 1:
        print("       1. Primer ajuste")
        print("-----> 2. Mejor ajuste <-----" )
        print("       3. Peor ajuste")
        print("       4. Siguiente ajuste")
        print("       Salir")
    
    elif count_option == 2:
        print("       1. Primer ajuste")
        print("       2. Mejor ajuste ")
        print("-----> 3. Peor ajuste <-----")
        print("       4. Siguiente ajuste")
        print("       Salir")
    
    elif count_option == 3:
        print("       1. Primer ajuste")
        print("       2. Mejor ajuste")
        print("       3. Peor ajuste")
        print("-----> 4. Siguiente ajuste <-----")
        print("       Salir")
    
    elif count_option == 4:
        print("       1. Primer ajuste")
        print("       2. Mejor ajuste")
        print("       3. Peor ajuste")
        print("       4. Siguiente ajuste")
        print("-----> Salir <-----")
    
    elif count_option >= 5:
        print("-----> 1. Primer ajuste <-----")
        print("       2. Mejor ajuste")
        print("       3. Peor ajuste")
        print("       4. Siguiente ajuste")
        print("       Salir")
        count_option = 0
    
    elif count_option < 0:
        print("       1. Primer ajuste")
        print("       2. Mejor ajuste")
        print("       3. Peor ajuste")
        print("       4. Siguiente ajuste")
        print("-----> Salir <-----")
        count_option = 4
    return count_option


while True:

    caracter = ord(getch())
    if caracter == 115:
        option += 1
    elif caracter == 119:
        option -= 1
    elif caracter == 13:
        print("Enter")
    os.system("cls")
    option = Menu(option)

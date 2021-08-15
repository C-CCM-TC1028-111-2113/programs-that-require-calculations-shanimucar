def main():
    #escribe tu código abajo de esta línea

    print('Dame un número')
number1 = int(input())
print('Dame un número')
number2 = int(input())

suma = number1 + number2
resta = number1 - number2
multi = number1 * number2

print('Suma: ' + str(suma)) #Show the addition
print('Resta: ' + str(resta)) #Show the substraction
print('Multiplicación: ' + str(multi)) #Show the multiplication
   

if __name__ == '__main__':
    main()

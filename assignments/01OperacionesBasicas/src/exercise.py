def main():
    #escribe tu código abajo de esta línea

print('Dame un número')
num1 = int(input()) #Read the first value
print('Dame otro número')
num2 = int(input()) #Read the second value

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2

print('Suma: ' + str(suma)) #Show the addition
print('Resta: ' + str(resta)) #Show the substraction
print('Multiplicación: ' + str(multi)) #Show the multiplication
   

if __name__ == '__main__':
    main()

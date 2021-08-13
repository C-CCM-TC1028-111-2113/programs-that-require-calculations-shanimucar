def main():
    #escribe tu código abajo de esta línea
    print('Enter a number')
number1 = int(input()) #Read the first value
print('Enter a second number')
number2 = int(input()) #Read the second value

suma=number1+number2
resta=number1-number2
multi=number1*number2

print('The addition of these numbers is: ' + str(suma)) #Show the addition
print('Your substraction of these numbers is: ' + str(resta)) #Show the substraction
print('Your multiplication of these numbers is: ' + str(multi)) #Show the multiplication

   

if __name__ == '__main__':
    main()

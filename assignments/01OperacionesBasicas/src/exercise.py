def main():
    #escribe tu código abajo de esta línea
    print('Enter a number')
    num1 = int(input()) #Read the first value
    print('Enter a second number')
    num2 = int(input()) #Read the second value

suma= num1+num2
resta= num1-num2
multi= num1*num2

print('The addition of these numbers is: ' + str(suma)) #Show the addition
print('Your substraction of these numbers is: ' + str(resta)) #Show the substraction
print('Your multiplication of these numbers is: ' + str(multi)) #Show the multiplication

   

if __name__ == '__main__':
    main()

def main():
    #escribe tu código abajo de esta línea
    edad = integer(input("Dame tu edad: "))
    anoActual = integer(input("Dame el año actual: "))
    anosFaltantes = 100 - edad
    tiempo = anoActual + anosFaltantes
    print("Cumplirás 100 años en el año: ",tiempo)



if __name__ == '__main__':
    main()

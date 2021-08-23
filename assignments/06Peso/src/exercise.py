def main():
    #escribe tu código abajo de esta línea
    
    p_inicial = float(input("Dame el peso inicial: "))
    p_final = float(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    kilos = (p_inicial-p_final)/meses
    print("Lo que debes bajar por mes es:",kilos)
    


if __name__ == '__main__':
    main()

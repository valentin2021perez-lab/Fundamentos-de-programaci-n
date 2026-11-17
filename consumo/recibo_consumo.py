
def calcular_consumo():
    anterior = float(input("Lectura anterior: "))
    while True:
        actual = float(input("Lectura actual: "))
        if actual >= anterior:
            break
        print("Lectura no válida, no puede ser menor que la anterior.")
    consumo = actual - anterior
    return anterior, actual, consumo

def calcular_importe(consumo):
    tarifa = 2.50
    cuota = 40
    return consumo * tarifa + cuota

def mostrar_recibo(anterior, actual, consumo, importe):
    print("Lectura anterior:", anterior)
    print("Lectura actual:", actual)
    print("Consumo:", consumo)
    if consumo <= 50:
        print("Nivel de consumo: bajo")
    elif consumo <= 100:
        print("Nivel de consumo: medio")
    else:
        print("Nivel de consumo: alto")
    print(f"Importe a pagar: ${importe:,.2f}")

anterior, actual, consumo = calcular_consumo()
importe = calcular_importe(consumo)
mostrar_recibo(anterior, actual, consumo, importe)







def calcular_consumo():
    """Recibe: nada (pide las lecturas al usuario).
    Devuelve: lectura anterior, lectura actual y consumo en kWh."""
    anterior = float(input("Lectura anterior: "))
    while True:
        actual = float(input("Lectura actual: "))
        if actual >= anterior:
            break
        print("Lectura no valida, no puede ser menor que la anterior.")
    consumo = actual - anterior
    return anterior, actual, consumo

def calcular_importe(consumo):
    """Recibe: consumo en kWh.
    Devuelve: importe a pagar (tarifa $2.50 por kWh + cuota fija $40)."""
    tarifa = 2.50
    cuota = 40
    return consumo * tarifa + cuota

def clasificar_consumo(consumo):
    """Recibe: consumo en kWh.
    Devuelve: 'bajo' (hasta 50), 'medio' (hasta 100) o 'alto' (mas de 100)."""
    if consumo <= 50:
        return "bajo"
    elif consumo <= 100:
        return "medio"
    else:
        return "alto"

def mostrar_recibo(anterior, actual, consumo, importe, nivel):
    """Recibe: lecturas, consumo, importe y nivel. Devuelve: nada (solo muestra)."""
    print("Lectura anterior:", anterior)
    print("Lectura actual:", actual)
    print("Consumo:", consumo, "kWh")
    print("Nivel de consumo:", nivel)
    print(f"Importe a pagar: ${importe:,.2f}")

anterior, actual, consumo = calcular_consumo()
importe = calcular_importe(consumo)
nivel = clasificar_consumo(consumo)
mostrar_recibo(anterior, actual, consumo, importe, nivel)
edad = int(input("ingresa la edad del visitante: "))
estudiante = input("es estudiante (si/no): ")

def precioinicial(edad):
    if edad < 12:
        return 40
    elif edad < 60:
        return 100
    else:
        return 60

preciofinal = precioinicial(edad)
print("el precio inicial segun su edad es:", preciofinal)

if estudiante == "si":
    descuento = preciofinal * 0.25
else:
    descuento = 0

total = preciofinal - descuento
print("el descuento es:", descuento)
print("el total con descuento es:", total)
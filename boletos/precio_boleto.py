edad = int(input("Ingresa la edad del visitante: "))
while edad < 0:
    print("Edad no valida, no se aceptan edades negativas.")
    edad = int(input("Ingresa la edad del visitante: "))

estudiante = input("Es estudiante (si/no): ").strip().lower()

if edad < 12:
    precio = 40
elif edad <= 59:
    precio = 100
else:
    precio = 60

descuento = 0
if estudiante in ("si", "sí") and 12 <= edad <= 59:
    descuento = precio * 0.25

total = precio - descuento
print(f"Precio inicial: ${precio:.2f}")
print(f"Descuento: ${descuento:.2f}")
print(f"Precio final: ${total:.2f}")
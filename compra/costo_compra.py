nombre1 = input("Nombre del primer producto: ")
precio1 = float(input("Precio del primer producto: "))
cantidad1 = int(input("Cantidad del primer producto: "))

nombre2 = input("Nombre del segundo producto: ")
precio2 = float(input("Precio del segundo producto: "))
cantidad2 = int(input("Cantidad del segundo producto: "))

nombre3 = input("Nombre del tercer producto: ")
precio3 = float(input("Precio del tercer producto: "))
cantidad3 = int(input("Cantidad del tercer producto: "))

subtotal1 = precio1 * cantidad1
subtotal2 = precio2 * cantidad2
subtotal3 = precio3 * cantidad3

subtotal = subtotal1 + subtotal2 + subtotal3
iva = subtotal * 0.16
total = subtotal + iva

print()
print(f"Subtotal de {nombre1}: ${subtotal1:.2f}")
print(f"Subtotal de {nombre2}: ${subtotal2:.2f}")
print(f"Subtotal de {nombre3}: ${subtotal3:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"IVA: ${iva:.2f}")
print(f"Total: ${total:.2f}")
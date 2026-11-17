def registrar_ventas():
  cantidad = 0
  total = 0
  venta_grande = False
  while True:
    importe = float(input("importe de la venta (0 para terminar):"))
    if importe == 0:
       break
    if importe < 0:
      print("importe no valido, no se aceptan negativos.")
      continue
    cantidad = cantidad + 1
    total = total + importe
    if importe >= 1000:
      venta_grande = True
  return cantidad,total,venta_grande
def mostrar_resumen(cantidad,total,venta_grande):
  if cantidad > 0:
    promedio = total / cantidad
  else:
      promedio = 0
  print("cantidad de ventas")
  print(cantidad)
  print("total vendido")
  print(f"${total:,.2f}")
  print("promedio por venta")
  print(f"${promedio:,.2f}")
  print("venta de $1000 o más")
  if venta_grande:
        print("Si")
  else:
        print("No")
cantidad, total, venta_grande = registrar_ventas()
mostrar_resumen(cantidad, total, venta_grande)


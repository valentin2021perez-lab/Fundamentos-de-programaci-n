import runpy

while True:
    print("\n=== MENU DE ACTIVIDADES ===")
    print("1. Calificacion")
    print("2. Temperatura")
    print("3. Factorial")
    print("4. Costo de una compra")
    print("5. Precio de boleto")
    print("6. Registro de ventas")
    print("7. Recibo de consumo")
    print("0. Salir")
    opcion = input("Selecciona el numero de la actividad: ")

    if opcion == "1":
        runpy.run_path("calificacion.py")
    elif opcion == "2":
        runpy.run_path("temperatura/temperatura.py")
    elif opcion == "3":
        runpy.run_path("factorial/factorial.py")
    elif opcion == "4":
        runpy.run_path("compra/costo_compra.py")
    elif opcion == "5":
        runpy.run_path("boletos/precio_boleto.py")
    elif opcion == "6":
        runpy.run_path("ventas/registro_ventas.py")
    elif opcion == "7":
        runpy.run_path("consumo/recibo_consumo.py")
    elif opcion == "0":
        print("Adios")
        break
    else:
        print("Opcion no valida, intenta de nuevo")
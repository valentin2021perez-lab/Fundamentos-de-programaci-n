p1 = float(input("ingresa la cantidad del primer producto:"))
p2 = float(input("ingresa la cantidad del segundo producto:"))
p3 = float(input("ingresa la cantidad del tercer producto:"))

def costodeunacompra(p1,p2,p3):
  return(p1*12.50)+(p2*35.00)+(p3*20.00)
subtotalfinal=costodeunacompra(p1,p2,p3)
print("el costo de la compra es :",subtotalfinal)
iva =subtotalfinal * 0.16
total =subtotalfinal + iva
print("el iva es :",iva)
print("el total con iva es :",total)

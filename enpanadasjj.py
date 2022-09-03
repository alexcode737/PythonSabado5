print("***Menu***")
print("1. Agregar 1 empanada")
print("2. Mostrar empanada")
print("3. Salir")

opcion = 0
empanadas = {}
#Datos empanada
#Sabor
#Ingredientes
#Precio fabricacion
#Precio venta

opcion = int(input("Digite una opcion: "))
while(opcion >= 1):
    if(opcion == 1):
        empanadas['sabor'] = input("Escriba el sabor de la empanada: ")
        empanadas['ingredientes'] = input("Escriba los ingredientes: ")
        empanadas['Precio fabricacion'] = input("Digite el valor de fabricacion: ")
        empanadas['Precio venta'] = input("Digite el valor de venta: ")
        break
    elif(opcion == 2):
        for llave,valor in empanadas.items():
            print(llave)
            print(valor)
    elif(opcion == 3):
        print("Adios")
    else:
        print("Digite una opcion valida")
        break
else:
    print("Fin")
#TASK 1 --> Diagrama de flujo 

#TASK 2 -->  Entrada de datos 
anchura = 47
print(f"\n{'=' * int(anchura /2)} INVENTARIO {'=' * int(anchura /2)}\n")

    #Declaracion variables 
nombre = input("Ingresa el nombre del producto: ").capitalize()
precio = float(input("Ingresa el precio del producto en USD: "))
cantidad = int(input("Ingresa la cantidad de productos: "))
contador = 1 #Controlar intentos de validacion

while True: #Validacion de precio y cantidad
    if precio > 0 and cantidad > 0:
        break
    if precio <= 0:
        precio = float(input("El precio del producto no puede ser igual o menor a cero >>> Ingresa el precio del producto correcto: "))
    if cantidad <= 0:
        cantidad = int(input("La cantidad de productos no puede ser igual o menor a cero >>> Ingresa la cantidad correcta: "))
    contador += 1
    if contador >= 3: #Limitar intentos de validacion
        print("Demasiados intentos. Saliendo...")
        exit()

#TASK 3 --> Operación matemática
costo_total = precio * cantidad

#TASK 4 --> Mostrar resultados 
print(f"\n{'=' * int(anchura /2)} FACTURA {'=' * int(anchura /2)}\n") 
print((anchura + 8) * '_')
print(f"| {'Producto':^25} | {'Detalles':^24} |".upper())
print((anchura + 8) * '_')


print(f"| {'Nombre':^25} | {nombre:^24} |\
      \n| {'Precio c/u':^25} | {precio:^24} |\
      \n| {'Cantidad':^25} | {cantidad:^24} |\
      \n| {'Precio total':^25} | {costo_total:^24.2f} |")
print((anchura + 8) * '_')



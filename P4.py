print("\nP4. REGISTRO DE ASISTENTES")

nombres = []
while True:
    nombre = input("Ingrese nombre (FIN para terminar): ").strip()
    if nombre == "FIN":
        break
    if nombre == "":
        print("Entrada vacía ignorada.")
        continue
    nombres.append(nombre)

print("Total ingresados:", len(nombres))

# detectar repetidos
repetidos = []
for n in nombres:
    if nombres.count(n) > 1 and n not in repetidos:
        repetidos.append(n)

if repetidos:
    print("Nombres repetidos:", repetidos)
else:
    print("No hay nombres repetidos.")

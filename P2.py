print("\nP2. PARTICIPANTE ELEGIBLE")

edad = int(input("Edad: "))
licencia = input("¿Tiene licencia? (si/no): ").lower()
vehiculo = input("¿Vehículo propio o préstamo autorizado? (si/no): ").lower()

if edad >= 18 and (licencia == "si") and (vehiculo == "si" or vehiculo == "prestamo"):
    print("Apto")
else:
    print("No apto")

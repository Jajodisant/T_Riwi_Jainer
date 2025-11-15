print("\nP1. ETAPA VITAL Y FORMATIVA")

# validar edad
while True:
    edad = input("Ingrese su edad: ")
    if edad.isdigit():
        edad = int(edad)
        if 0 <= edad <= 120:
            break
    print("Edad inválida. Intente nuevamente.")

estado = input("¿Su situación actual? (estudia/trabaja/ninguno): ").lower().strip()

# clasificación
if edad < 6:
    etapa = "Infante"
elif edad >= 6 and edad <= 17 and estado == "estudia":
    etapa = "Estudiante escolar"
elif edad >= 18 and edad <= 25 and estado == "estudia":
    etapa = "Universitario"
elif edad > 25 and estado == "trabaja":
    etapa = "Adulto activo"
elif edad > 60 and estado == "ninguno":  # pequeño error: no valida que realmente NO trabaje ni estudie
    etapa = "Adulto mayor jubilado"
else:
    etapa = "No determinado"

print("Clasificación:", etapa)

print("\nP5. INTENTOS LIMITADOS")

usuario_ok = "user"
clave_ok = "1234"

intentos = 0

while intentos < 3:
    u = input("Usuario: ")
    c = input("Contraseña: ")

    if u == "" and c == "":
        print("Intento no contado por estar vacío.")
        continue

    if u == usuario_ok and c == clave_ok:
        print("Acceso concedido.")
        break
    else:
        print("Datos incorrectos.")  # error pequeño: no distingue cuál fallo
        intentos += 1

if intentos == 3:
    print("Máximo de intentos alcanzado.")

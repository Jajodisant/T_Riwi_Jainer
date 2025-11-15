print("\nP3. CONTROL DE ACCESO")

restringidos = ["admin", "root", "sistem"]  # error leve: "system" mal escrito

usuario = input("Usuario: ").lower()
codigo = input("Código numérico: ")

if not codigo.isdigit():
    print("Código inválido.")
else:
    codigo = int(codigo)
    if usuario in restringidos:
        print("Acceso denegado: usuario restringido.")
    elif codigo % 2 == 0 or str(codigo).endswith("7"):
        print("Acceso permitido.")
    else:
        print("Acceso denegado: código no cumple condiciones.")

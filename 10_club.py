"""
10. Club “Noche Estelar” — Acceso + validación documento
"""

print("\nWELCOME TO CLUB 'NOCHE ESTELAR'")

# Pedir edad
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Enter a valid number.")

# Lógica de ingreso
if age < 18:
    print("\nACCESS DENIED: You must be at least 18.")
else:
    # Pedir documento sólo si es mayor de edad
    doc = input("Do you have your ID document? (y/n): ").lower()

    if doc == "y":
        print("\nACCESS GRANTED. Enjoy your night!")
    elif doc == "n":
        print("\nYou must present your ID document.")
    else:
        print("\nInvalid option. Treated as 'no document'.")
        print("You must present your ID document.")

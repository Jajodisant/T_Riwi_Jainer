"""
7. Restaurante “El Sabor Colombiano” — Menú + bebida + IVA
"""

print("\nWELCOME TO 'EL SABOR COLOMBIANO' RESTAURANT!")

menu_price = 12000
drink_price = 3000
iva = 0.08  # 8%

# Mostrar menú
print(f"\nMenu price: ${menu_price:,}")
print(f"Optional drink: ${drink_price:,} (y/n)\n")

# Preguntar por bebida
drink = input("Do you want a drink? (y/n): ").lower()

# Calcular subtotal
subtotal = menu_price

if drink == "y":
    subtotal += drink_price
elif drink != "n":
    print("Invalid option. Drink will not be added.")

# Aplicar IVA
total = subtotal + (subtotal * iva)

print(f"\nTotal to pay (IVA included): ${total:,.0f}")


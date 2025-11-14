"""
9. Supermercado “AhorroMax” — Descuentos y envío
"""

print("\nWELCOME TO AHORROMAX SUPERMARKET!")

unit_price = 2000
shipping_fee = 5000

# Pedir cantidad
while True:
    try:
        qty = int(input("Enter number of units: "))
        if qty < 0:
            print("Quantity cannot be negative. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Enter an integer number.")

# Subtotal sin descuento
subtotal = qty * unit_price

# Determinar descuento
if qty >= 30:
    discount = 0.15
elif qty >= 10:
    discount = 0.05
else:
    discount = 0

# Aplicar descuento
total_after_discount = subtotal - (subtotal * discount)

# Verificar envío
if total_after_discount < 50000:
    total_final = total_after_discount + shipping_fee
else:
    total_final = total_after_discount

# Resultados
print("\n--- TOTAL ---")
print(f"Subtotal: ${subtotal:,.0f}")
print(f"Discount applied: {discount*100:.0f}%")
print(f"After discount: ${total_after_discount:,.0f}")

if total_after_discount < 50000:
    print(f"Shipping fee added: ${shipping_fee:,.0f}")

print(f"\nFINAL TOTAL TO PAY: ${total_final:,.0f}")

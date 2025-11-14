"""
6. Parqueadero “RapidCar” — Tarifa escalonada
"""

print("\nWELCOME TO RAPIDCAR PARKING!")

rate_per_hour = 2000
extra_fee = 5000   # multa fija al pasar las 5 horas

# Validación de horas
while True:
    try:
        hours = float(input("Enter parking time in hours: "))
        if hours < 0:
            print("Hours cannot be negative. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Enter a number.")

# Cálculo del total
if hours <= 5:
    total = hours * rate_per_hour
else:
    total = (5 * rate_per_hour) + extra_fee

print(f"\nTotal to pay: ${total:,.0f}")

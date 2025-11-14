"""
5. "El Saber" Bookstore — Student discount + coupon
"""

print("\nWELCOME TO 'EL SABER' BOOKSTORE!")

book_price = 25000
student_discount = 0.15   # 15%
coupon_discount = 0.10    # 10%

print(f"\n{'-'*28}")
print(f"|{'CATEGORY':^15}| {'PRICE':^9}|")
print(f"{'-'*28}")
print(f"|{'Book':<15}| {'$25.000':<9}|")
print(f"{'-'*28}\n")

student = input("Are you a student? (y/n): ").lower()

# Si no es estudiante, no se debe pedir cupón
coupon = ""

if student == "y":
    coupon = input("Enter coupon code (if any): ").upper()

# Cálculo del precio final
total = book_price

if student == "y":
    total -= total * student_discount      # aplica 15%

    if coupon == "LIBRO10":               # aplica cupón correctamente
        total -= total * coupon_discount  # 10% adicional

elif student != "n":
    print("\nInvalid option for student (use 'y' or 'n').")

# Mostrar total formateado
print(f"\nTotal to pay: ${total:,.0f}")

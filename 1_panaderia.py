"""
1. Don Pacho Bakery - Discounts for bulk purchases
"""

print("Welcome to Don Pacho Bakery!".upper())
text = "Bakery Menu".upper()
print("\n", text.center(24))
print(f"\n|{'Cheese bread':15} | {'$300':^9}|\n")

Cheese_bread = 300  # Price per bread unit in COP

quantity = int(input("Enter the number of cheese breads you wish to purchase: ")) # Quantity of bread to purchase

total_price = quantity * Cheese_bread # Total price without discount
final_price = total_price  # Initialize final price
discount = 0  # Initialize discount


match quantity:
    case quantity if quantity < 1:
        print("Invalid quantity. Please enter a positive number.")
    case quantity if quantity > 50:
        discount = total_price * 0.20
        final_price -= discount
        print(f"You get a 20% discount! Your total is: ${int(final_price)} COP")
    case quantity if quantity > 20:
        discount = total_price * 0.10
        final_price -= discount
        print(f"You get a 10% discount! Your total is: ${int(final_price)} COP")
    case quantity if quantity < 21:
        print(f"Your total price without discount is: ${int(final_price)} COP")    
    case _:
        print("An unexpected error occurred.")

        
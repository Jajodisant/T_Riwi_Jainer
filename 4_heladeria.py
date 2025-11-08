"""
4. "Frosty"  Ice Cream Shop -- Flavor and topping
"""
print("Welcome to 'Frosty' Ice Cream Shop!".upper())

text = 'Frosty menu'.upper()
print("\n", text.center(28))
print(f"{'-'*28 }")
print(f"\n|{'FLAVORS':^15}| {'PRICES':^9}|")
print(f"{'-'*28 }")
print(f"|{'Vanilla':15}| {'$3,500':^9}|")
print(f"{'-'*28 }")
print(f"|{'Chocolate':15}| {'$4,000':^9}|")
print(f"{'-'*28 }")
print(f"|{'Topping':15}| {'$1,000':^9}|")
print(f"{'-'*28 }")

Vanilla = 3500  
Chocolate = 4000  
Topping = 1000  
price_total = 0



while True:
    flavor = input("\nPlease choose a flavor (Vanilla/Chocolate): ").strip().lower()    

    if flavor != "vanilla" and flavor != "chocolate":
         flavor = input("Please choose a correct flavor (Vanilla/Chocolate): ").strip().lower()   
           
    elif flavor == "vanilla":
        price_total += Vanilla

    elif flavor == "chocolate":
        price_total += Chocolate  
    break
     
    
    topping_choice = input("Would you like to add a topping for $1,000 COP? (yes/no): ").strip().lower()

    if topping_choice == "yes":
        price_total += Topping
    elif topping_choice == "no":
        price_total = price_total
    break
    
   
print(f"Your total price is: ${price_total} COP")

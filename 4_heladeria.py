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
total_price = 0



while True:
    choice_flavor = input("Select a flavor (chocolate/vanilla): ").strip().lower()

    if not choice_flavor in ["chocolate","vanilla"] or choice_flavor.isdigit():
        print("Select a available flavor")
        continue
   
    elif choice_flavor == "chocolate":
        while True:
            yes_topping = input("Would you like to add a topping? (yes/not): ")
            if not yes_topping in ["yes","not"] or choice_flavor.isdigit():
                print("You can only choice yes/not") 
                continue        
            else:
                if yes_topping == "yes":
                    total_price = Chocolate + Topping
                    break
                elif yes_topping == "not":
                    total_price = Chocolate 
                    break
        
    elif choice_flavor == "vanilla":
        while True:
            yes_topping = input("Would you like to add a topping? (yes/not): ")
            if not yes_topping in ["yes","not"] or choice_flavor.isdigit():
                print("You can only choice yes/not")  
                continue        
            else:
                if yes_topping == "yes":
                    total_price = Vanilla + Topping
                    break
                elif yes_topping == "not":
                    total_price = Vanilla
                    break
    break
    
   
print(f"Your total price is: ${total_price} COP")

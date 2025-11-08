"""
2. “La estrella” cinema -- Rates by age
"""

print("Welcome “La estrella” cinema!".upper())

age = int(input("Please enter your age: "))  # User's age input

match age:
    case age if age < 1:
        print("ERROR. Age must be a positive number.")
    case age if age < 5:
        print("Children under 5 enter for free!")
    case age if 5 < age <= 11:
        print("Children between 5 and 11 years old pay $5.000 COP.")
    case age if 12 < age <= 59:
        print("Childrens or Adults between 12 and 59 years old pay $8.000 COP.")   
    case age if age >= 60:
        print("People over 60 pay 4,000 COP thanks to the “senior citizen” discount.")
    case _:
        print("An unexpected error occurred.")
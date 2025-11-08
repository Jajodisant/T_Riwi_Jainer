"""
3. “Solo Leveling Fit” Gym -- Motivation + Bonus
"""

print("Welcome “Solo Leveling Fit” Gym!".upper())

days = int(input("Please enter the number of days you trained this week: "))  

match days:
    case days if days == 1:
        print("Don't give up, you can do better!")
    case days if 1 < days < 4:
        print("Good!, but you can do more.")
    case days if 4 <= days < 8:
        energy_point = 1
        print(f"Excellent work! You have earned {energy_point} energy point for your dedication!")
    case _:
        print("An unexpected error occurred.")
        
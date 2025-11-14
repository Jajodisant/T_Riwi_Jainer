"""
8. Empresa “TecnoPlus” — Evaluación compuesta
"""

print("\nEVALUACIÓN DE INGRESO — TECNOPLUS")

# Función para validar notas
def get_valid_score(name):
    while True:
        try:
            score = float(input(f"Enter score for {name} (0.0 - 5.0): "))
            if 0.0 <= score <= 5.0:
                return score
            else:
                print("Score must be between 0.0 and 5.0. Try again.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")

# Pedir notas
technical = get_valid_score("Technical Test")
logic = get_valid_score("Logic Test")

# Cálculo nota final
final_score = (technical * 0.7) + (logic * 0.3)

# Clasificación
if final_score >= 3:
    result = "APPROVED"
elif 2 <= final_score < 3:
    result = "REVIEW"
else:
    result = "FAILED"

# Mostrar resultados
print("\n--- RESULTS ---")
print(f"Final Score: {final_score:.2f}")
print(f"Status: {result}")

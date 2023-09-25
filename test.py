def NOT_gate(input_value):
    # Utilisez l'opérateur de complément binaire (~) pour inverser les bits
    result = ~input_value & 0xFFFF  # Assurez-vous que le résultat est sur 16 bits (0xFFFF)
    return result

# Exemple d'utilisation de la porte NOT
input_value = 12  # Par exemple, un nombre binaire représenté par 12 en décimal
output_value = NOT_gate(input_value)
print("Entrée:", input_value)
print("Sortie:", output_value)

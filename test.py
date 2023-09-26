def encoder_chaine(chaine):
    # Utilise replace() pour ajouter des caractères d'échappement aux guillemets doubles
    chaine_encodee = chaine.replace('"', '\\"')
    return chaine_encodee

# Exemple d'utilisation de la fonction
chaine_entree = '"'
chaine_encodee = encoder_chaine(chaine_entree)
print(chaine_encodee)  # Cela affichera '\"' en sortie

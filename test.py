import re

# Texte d'entrée avec les informations sur les armes, armures et anneaux
input_text = open('input.txt', 'r').readlines()
# Motifs regex pour extraire les informations
weapons_pattern = re.compile(r"(\w+)\s+(\d+)\s+(\d+)\s+(\d+)")
armors_pattern = re.compile(r"(\w+)\s+(\d+)\s+(\d+)\s+(\d+)")
rings_pattern = re.compile(r"(\w+\s*\+\d+)\s+(\d+)\s+(\d+)\s+(\d+)")

# Fonction pour extraire les informations sous forme de tuples
def extract_items(pattern, text):
    items = []
    matches = pattern.finditer(text)
    for match in matches:
        items.append((match.group(1), *map(int, match.groups()[1:])))
    return items

# Extraction des informations pour chaque catégorie
weapons = extract_items(weapons_pattern, input_text)
armors = extract_items(armors_pattern, input_text)
rings = extract_items(rings_pattern, input_text)

# Affichage des résultats
print("Weapons:", weapons)
print("Armors:", armors)
print("Rings:", rings)

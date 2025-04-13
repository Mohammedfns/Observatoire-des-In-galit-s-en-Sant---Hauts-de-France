import pandas as pd

# === 1. Charger le fichier CSV en sautant les 3 premières lignes (lignes inutiles) ===
df = pd.read_csv("data/Comparaisons_departementales.csv", skiprows=3)

# === 2. Renommer correctement les colonnes (8 colonnes visibles) ===
df.columns = [
    "code_dept", "nom_dept", 
    "effectif_total", 
    "densite_total", "densite_generalistes", "densite_specialistes", 
    "chirurgiens_dentistes", "pharmaciens"
]

# === 3. Supprimer les lignes vides ou mal formatées (ex : NaN ou "nan") ===
df = df.dropna(subset=["code_dept", "nom_dept"])

# === 4. Filtrer uniquement les départements des Hauts-de-France ===
hauts_de_france = ['02', '59', '60', '62', '80']
df = df[df["code_dept"].isin(hauts_de_france)]

# === 5. Convertir toutes les colonnes numériques (juste pour être sûr) ===
colonnes_num = df.columns[2:]  # toutes sauf code et nom
for col in colonnes_num:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# === 6. Exporter le fichier nettoyé dans outputs/ ===
df.to_csv("outputs/medecins_clean.csv", index=False)

# === 7. Afficher un aperçu ===
print("✅ Données filtrées (Hauts-de-France) :")
print(df)

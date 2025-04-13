import pandas as pd

# 1. Charger le CSV
df = pd.read_csv("data/Salaires_donnes.csv")

# 2. Renommer proprement
df = df.rename(columns={
    "en % de la moyenne nationale": "nom_dept",
    "Unnamed: 1": "ecart_moyenne_nationale"  # si nécessaire
})

# 3. Nettoyer les noms de département
df["nom_dept"] = df["nom_dept"].astype(str).str.strip().str.upper()

# 4. Filtrer uniquement les Hauts-de-France
hauts_de_france = ["AISNE", "NORD", "OISE", "PAS-DE-CALAIS", "SOMME"]
df = df[df["nom_dept"].isin(hauts_de_france)]

# 5. Sauvegarder le résultat final
df.to_csv("outputs/salaires_ecart_clean.csv", index=False)

# 6. Aperçu
print("✅ Données salaires Hauts-de-France nettoyées :")
print(df)





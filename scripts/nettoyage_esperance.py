import pandas as pd

# Charger le fichier CSV (sauter les lignes d'en-tête)
df = pd.read_csv("data/esperance_de_vie_departement.csv", sep=";", skiprows=2)

# Renommer les colonnes utiles
df = df.rename(columns={
    "Code": "code_dept",
    "Libellé": "nom_dept",
    "Espérance de vie des hommes à la naissance 2023": "esp_vie_h",
    "Espérance de vie des femmes à la naissance 2023": "esp_vie_f",
    "Taux de mortalité standardisé des 0 à 64 ans 2023": "mortalite_0_64"
})

# Ne garder que les colonnes utiles
df = df[["code_dept", "nom_dept", "esp_vie_h", "esp_vie_f", "mortalite_0_64"]]

# Filtrer uniquement les départements des Hauts-de-France
hauts_de_france = ['02', '59', '60', '62', '80']
df = df[df["code_dept"].isin(hauts_de_france)]

# Convertir les colonnes numériques (au cas où il y a des espaces ou des virgules)
df[["esp_vie_h", "esp_vie_f", "mortalite_0_64"]] = df[["esp_vie_h", "esp_vie_f", "mortalite_0_64"]].apply(
    lambda col: pd.to_numeric(col.astype(str).str.replace(",", ".").str.strip(), errors="coerce")
)

# Exporter le fichier nettoyé
df.to_csv("outputs/esp_vie_clean.csv", index=False)

# Affichage rapide
print("✅ Données espérance de vie / mortalité prématurée (Hauts-de-France) :")
print(df)

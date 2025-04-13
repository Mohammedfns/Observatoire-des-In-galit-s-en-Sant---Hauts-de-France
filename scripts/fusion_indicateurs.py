import pandas as pd

# === 1. Charger les fichiers nettoyés ===

medecins = pd.read_csv("outputs/medecins_clean.csv")
css = pd.read_csv("outputs/css_clean.csv")
esp_vie = pd.read_csv("outputs/esp_vie_clean.csv")
pauvrete = pd.read_csv("outputs/pauvrete_clean.csv")
salaires = pd.read_csv("outputs/salaires_ecart_clean.csv")

# === 2. Harmoniser les noms de département ===

# On nettoie les chaînes pour éviter les soucis d'espaces ou de casse
salaires["nom_dept"] = salaires["nom_dept"].str.upper().str.strip()
pauvrete["nom_dept"] = pauvrete["nom_dept"].str.upper().str.strip()

# === 3. Fusion progressive ===

# Fusion sur code_dept
fusion_1 = pd.merge(medecins, css, on="code_dept", how="left")
fusion_2 = pd.merge(fusion_1, esp_vie, on="code_dept", how="left")
fusion_3 = pd.merge(fusion_2, pauvrete, on="code_dept", how="left")
fusion_finale = pd.merge(fusion_3, salaires, on="nom_dept", how="left")

# === 4. Export final ===
fusion_finale.to_csv("outputs/indicateurs_fusionnes.csv", index=False)

df_simplifie = fusion_finale[[
    "code_dept",
    "nom_dept",
    "densite_generalistes",
    "css_moyenne_2023",
    "esp_vie_h",
    "esp_vie_f",
    "mortalite_0_64",
    "taux_pauvrete",
    "ecart_moyenne_nationale"
]]

# === 6. Renommer les colonnes avec des titres lisibles ===
df_simplifie = df_simplifie.rename(columns={
    "code_dept": "Code département",
    "nom_dept": "Département",
    "densite_generalistes": "Densité de médecins généralistes 100 000 habitants",
    "css_moyenne_2023": "Moyenne bénéficiaires CSS (2023)",
    "esp_vie_h": "Espérance de vie à la naissance (Hommes)(2023)",
    "esp_vie_f": "Espérance de vie à la naissance (Femmes)(2023)",
    "mortalite_0_64": "Taux de mortalité prématurée (2023)",
    "taux_pauvrete": "Taux de pauvreté(2023)",
    "ecart_moyenne_nationale": "Écart au salaire moyen national (%) (2023)"
})

# === 7. Export du fichier simplifié ===
df_simplifie.to_csv("outputs/indicateurs_simplifies.csv", index=False)

# === 8. Aperçu console ===
print("✅ Fusion complète dans : outputs/indicateurs_fusionnes.csv")
print("✅ Version simplifiée dans : outputs/indicateurs_simplifies.csv")
print(df_simplifie)

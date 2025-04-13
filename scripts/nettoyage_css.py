import pandas as pd

# === 1. Charger la feuille avec les données mensuelles par département ===
file_path = "data/Css.xlsx"
df = pd.read_excel(file_path, sheet_name="Bdd_Effectifs_C2S_Dpt_Mensuel")

# === 2. Créer une vraie date à partir des colonnes Mois + Année ===
df["DATE"] = pd.to_datetime(df["Mois"])

# === 3. Garder uniquement les départements des Hauts-de-France ===
hauts_de_france = ['02', '59', '60', '62', '80']
df = df[df["Num_Dpt"].astype(str).isin(hauts_de_france)]

# === 4. Filtrer entre janvier 2023 et décembre 2023 ===
df = df[(df["DATE"] >= "2023-01-01") & (df["DATE"] <= "2023-12-31")]

# === 5. Calculer la moyenne annuelle par département ===
df_moyenne = df.groupby("Num_Dpt")["Nombre_en_Milliers"].mean().reset_index()

# === 6. Renommer proprement les colonnes ===
df_moyenne.columns = ["code_dept", "css_moyenne_2023"]

# === 7. Exporter le fichier nettoyé ===
df_moyenne.to_csv("outputs/css_clean.csv", index=False)

# === 8. Aperçu ===
print("✅ Moyenne CSS 2023 (Hauts-de-France) :")
print(df_moyenne)

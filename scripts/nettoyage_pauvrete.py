import pandas as pd

# Charger la feuille Figure 2 avec les bonnes lignes
df = pd.read_excel("data/taux_pauvreté.xlsx", sheet_name="Figure 2", skiprows=2)

# Renommer les colonnes
df.columns = ["code_dept", "nom_dept", "taux_pauvrete"]

# Ne garder que les départements des Hauts-de-France
hauts_de_france = ['02', '59', '60', '62', '80']
df = df[df["code_dept"].astype(str).isin(hauts_de_france)]

# Convertir taux de pauvreté en float
df["taux_pauvrete"] = pd.to_numeric(df["taux_pauvrete"], errors='coerce')

# Sauvegarder les données nettoyées
df.to_csv("outputs/pauvrete_clean.csv", index=False)

# Aperçu
print("✅ Données taux de pauvreté Hauts-de-France :")
print(df)

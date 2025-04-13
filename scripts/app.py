
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import plotly.express as px

# Configuration de la page
st.set_page_config(page_title="Observatoire des Inégalités", layout="wide")

# Titre principal
st.title(" Observatoire des Inégalités en Santé - Hauts-de-France")

# Chargement des données
@st.cache_data
def charger_donnees():
    df = pd.read_csv("outputs/indicateurs_simplifies.csv")
    return df

df = charger_donnees()

# Affichage du tableau des données
st.subheader("🔍 Données disponibles")
st.dataframe(df)

# Sélecteur de variable pour le barplot
st.sidebar.title("🔧 Options")
colonne_a_afficher = st.sidebar.selectbox(
    "Choisissez l'indicateur à visualiser en barplot :",
    [
        "Taux de pauvreté(2023)",
        "Taux de mortalité prématurée (2023)",
        "Espérance de vie à la naissance (Hommes)(2023)",
        "Espérance de vie à la naissance (Femmes)(2023)",
        "Densité de médecins généralistes 100 000 habitants",
        "Moyenne bénéficiaires CSS (2023)",
        "Écart au salaire moyen national (%) (2023)"
    ]
)

# Barplot dynamique
st.subheader(f"📉 {colonne_a_afficher} par département")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df, x="Département", y=colonne_a_afficher, ax=ax, palette="viridis")
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("""
Cette étude menée sur les départements des **Hauts-de-France** met en évidence de fortes **inégalités territoriales en matière de santé**.  
Les données ont été collectées depuis le site de l’**INSEE** et d'autres sources publiques pour analyser des indicateurs clés :  
- taux de pauvreté  
- espérance de vie  
- mortalité prématurée  
- densité de médecins généralistes  
- bénéficiaires de la CSS  
- écarts de revenus

L’analyse statistique révèle des **corrélations fortes entre précarité et santé**.  
Un **modèle de régression linéaire multiple** permet de prédire efficacement le taux de mortalité prématurée.

Un **dashboard interactif** a été développé avec Streamlit pour faciliter la **visualisation des inégalités territoriales**, à destination des **acteurs publics et citoyens**.
""")

st.markdown("---")
st.subheader("📥 Télécharger les fichiers de données brutes")


# Densité de médecins généralistes 100 000 habitants
with open("data/Comparaisons_departementales.csv", "rb") as f:
    st.download_button(
        label="📄 Télécharger - Densité de médecins généralistes 100 000 habitants (CSV)",
        data=f,
        file_name="Comparaisons_departementales.csv"
    )

# CSS (Complémentaire santé solidaire)
with open("data/Css.xlsx", "rb") as f:
    st.download_button(
        label="📄 Télécharger - Données CSS (Complémentaire santé solidaire) (Excel)",
        data=f,
        file_name="Css.xlsx"
    )

# Espérance de vie
with open("data/esperance_de_vie_departement.csv", "rb") as f:
    st.download_button(
        label="📄 Télécharger - Espérance de vie (CSV)",
        data=f,
        file_name="Esperance_vie_departemental.csv",
        mime="text/csv"
    )

# Pauvreté
with open("data/taux_pauvreté.xlsx", "rb") as f:
    st.download_button(
        label="📄 Télécharger - Taux de pauvreté (Excel)",
        data=f,
        file_name="taux_pauvreté.xlsx"
    )

# Salaires
with open("data/Salaires_donnes.csv", "rb") as f:
    st.download_button(
        label="📄 Télécharger - Écart au salaire moyen (CSV)",
        data=f,
        file_name="Salaires_donnes.csv"
    )






import streamlit as st
import pandas as pd
#Titre principale
st.title("📂 Analyse des données")
#Bouton pour importer les données
fichier = st.file_uploader("Importer un fichier excel", type="XLSX")

if fichier is not None:
    #Lire les donnees
    df = pd.read_excel(fichier)

    st.write("Aperçu des données :")
    #Afficher les donnees
    st.dataframe(df)
    st.write("Colonnes :")
    #Afficher les colonnes
    st.write(df.columns)
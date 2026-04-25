import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#Titre principale
st.title("📊 Dashboard")
#Bouton pour importer les données
fichier = st.file_uploader("Importer un fichier excel", type="XLSX")

if fichier is not None:
    #Lire les donnees
    df = pd.read_excel(fichier)

    colonne_x = "Annees"

    # Multiselect
    colonnes_y = st.multiselect("Choisissez les indicateurs", df.columns)

    if len(colonnes_y) > 0:
        fig, ax = plt.subplots()

        for col in colonnes_y:
            if col != colonne_x:
                ax.plot(df[colonne_x], df[col], label=col)

        ax.set_xlabel("Années")
        ax.set_ylabel("Valeurs")
        ax.legend()

        st.pyplot(fig)
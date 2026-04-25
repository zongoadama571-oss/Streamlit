import streamlit as st
#Configuration de la pages 
st.set_page_config(page_title="App Data Analyst", layout="wide")

st.title("📊 Application Data Analyst")

st.write("Bienvenue dans votre application d'analyse de données")
st.write("Utilisez le menu à gauche pour naviguer entre les pages")

st.title("🏠 Accueil")
#Titre qui vas s'afficher sur l'ecran
st.write("""
Cette application permet :
- d'importer des données
- de les analyser
- de créer des graphiques interactifs
""")
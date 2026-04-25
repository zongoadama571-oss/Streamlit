import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
##################################### Mettre un titre principale
st.title("Ma premiere application streamlit")
##################################### Afficher du texte, nombre, tableau ou graphique
st.write("bonjour j'apprends streamlit !")

##################################### Pemettre a l'utilisateur d'interagire 
nom = st.text_input("Entrez votre nom")
age = st.number_input("Entrez votre age")
##################################### Bouton
if st.button("Valider"):
    st.write("Bonjour",nom,"Vous avez :",str(age) + "ans") 


##################################### Mettre un titre principale
st.title("Application interactive")
##################################### Menu deroulante
ville = st.selectbox("Choisissez une ville",["Ouagadougou","Bobo-dioulasso","Koudougou"])
##################################### Case a cocher
afficher = st.checkbox("Afficher un message")
##################################### Slider
age = st.slider("Choisissez votre age", 0, 100, 25)  #0=min 100=max et 25=valeur par defaut
#####################################Affichage
st.write("Ville choisie :", ville)
st.write("age :", age)
if afficher:
    st.write("Bienvenue dans l'application !")


##################################### Mettre un titre principale
st.title("Analyse de fichier CSV")
#####################################Cree un bouton pour importer un fichier
fichier = st.file_uploader("Choisissez un fichier CSV", type = "csv")
if fichier is not None:
    df = pd.read_csv(fichier, sep = ";") #Lecture du fichier
    st.write("Apercu des donnees :")
    st.dataframe(df) #Affichage des donnees
    #Infos sur les donnees
    st.write("Nombre de lignes :",df.shape[0])
    st.write("Nombre de colonnes :",df.shape[1])


###################################### Mettre un titre principale
st.title("Dashboard économique interactif")
# Charger fichier
fichier = st.file_uploader("Importer un fichier EXCEL", type="XLSX")
if fichier is not None:
    df = pd.read_excel(fichier)
    st.dataframe(df)
    
    colonne_x = "Annees"
    # FILTRE SUR LES ANNÉES
    min_annee = int(df[colonne_x].min())
    max_annee = int(df[colonne_x].max())

    annees = st.slider(
        "Sélectionnez la période",
        min_value=min_annee,
        max_value=max_annee,
        value=(min_annee, max_annee)
    )
    
    # Choix des variables
    colonnes_y = st.multiselect(
        "Choisissez les indicateurs",
        df.columns
    )


    type_graphique = st.selectbox(
    "Choisissez le type de graphique",
    ["Courbe", "Histogramme", "Barres", "Camembert", "Boxplot", "Scatter"]
)
#Adapter le choix des graphiques 
if type_graphique in ["Courbe", "Barres"]: #Graphique a plusieurs variables
    colonnes_y = st.multiselect("Choisissez les variables", df.columns)
elif type_graphique == "Scatter": #Graphique a deux variables
    col_x = st.selectbox("Variable X", df.columns)
    col_y = st.selectbox("Variable Y", df.columns)
elif type_graphique in ["Histogramme", "Boxplot", "Camembert"]: #Graphique a un variables
    colonne = st.selectbox("Choisissez une seule variable", df.columns)

    # GRAPHIQUE
    if len(colonnes_y) > 0:
        fig, ax = plt.subplots() #Initialiser un espace de dessin

        for col in colonnes_y:
            if col != colonne_x:
                ax.plot(df[colonne_x], df[col], label=col) # df[colonne_x] :Axe x   df[col] :Axe y
                if type_graphique == "Histogramme":
                    ax.hist(df[colonne_x], df[col], label=col)

                elif type_graphique == "Barres":
                    ax.bar(df[colonne_x], df[col], label=col)

                elif type_graphique == "Camembert":
                    ax.pie(df[col], labels=df[col], autopct="%1.1f%%")

                elif type_graphique == "Boxplot":
                    ax.boxplot(df[col])

                elif type_graphique == "Scatter":
                    ax.scatter(df[colonne_x], df[col], label=col)



        ax.set_xlabel("Années")
        ax.set_ylabel("Valeurs")
        ax.set_title("Évolution des indicateurs")

        ax.legend()

        st.pyplot(fig)






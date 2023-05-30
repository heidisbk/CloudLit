import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from run import page_1, page_2


df = pd.read_csv('data.csv').dropna()

### Config
st.set_page_config(
    page_title="Dashboard Marketing",
    page_icon="🚀",
    layout="wide"
)

def home_page():
    st.title("Votre Dashboard interactif avec Streamlit 🎨")

    st.markdown("""
    
    Bienvenue sur notre plateforme interactive qui vous permettra d'explorer et d'analyser des données de manière intuitive. Ce Dashboard a été spécialement conçu pour vous aider à mieux comprendre les concepts clés de la data science et à acquérir une expérience pratique en utilisant Streamlit.

    ### Comment utiliser `Streamlit` ?

    Voici les quelques commandes de base pour utiliser `Streamlit` :

    ### Titre et texte
    - `st.title('Title')` : pour afficher un titre
    - `st.markdown('Some text')` : pour afficher du texte
    - `st.write(data)` ou `st.dataframe(df)` : pour afficher des données

    ### Widgets
    - `st.checkbox('Show raw data')` : pour afficher des données brutes
    - `st.selectbox('Choose a city',('London','New York','San Francisco'))` : pour afficher une liste déroulante
    - `st.button('Submit')` : pour afficher un bouton de soumission

    ### Afficher des graphiques
    - `st.line_chart(data)` : pour afficher un graphique linéaire
    - `st.bar_chart(data)` : pour afficher un graphique à barres
    - `st.pyplot(fig)` : pour afficher un graphique matplotlib
    - `st.map(data)` : pour afficher une carte

    """)



    ## Affichage des données brutes à l'aide d'une checkbox
    st.subheader("Affichage des données brutes")

    #1. Afficher les données brutes avec : st.write
    if st.checkbox('Afficher les données brutes'):
        st.subheader('Données brutes')
        st.write(df)

    st.subheader("Affichage des graphiques")

    #2. Afficher le graphique contenu dans la variable fig avec : st.plotly_chart
    fig = px.histogram(df.sort_values("Profession"), x="Profession", barmode="group")
    st.plotly_chart(fig, use_container_width=True)


    #3. Afficher le graphique contenu dans la variable fig avec : st.bar_chart
    Family_Size_per_Work_Experience = df.set_index("Work_Experience")['Family_Size']
    st.bar_chart(Family_Size_per_Work_Experience)




    st.subheader("Affichage dynamique des données")

    #### Create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**1️⃣ Example de widget**")

        #4. Créer une liste déroulante pour la variable 'Profession' avec : st.selectbox
        Profession_ = st.selectbox("Choisissez la profession :", df.Profession.unique())

        #5. Créer une liste déroulante avec : st.selectbox contenanant la liste : ['Age', 'Work_Experience', 'Family_Size'] 
        Critère_ = st.selectbox("Choisissez le critère :", ['Age', 'Work_Experience', 'Family_Size'])

        # Sélectionner les données correspondantes à la profession choisie
        data = df[df['Profession'] == Profession_].groupby('Gender').mean()[Critère_]

        # Création de la figure
        fig = go.Figure(data=[go.Bar(x=data.index, y=data.values)])

        # Mise en forme du graphique
        fig.update_layout(title=f'Répartition hommes-femmes en fonction de la profession : {Profession_}',
                        xaxis_title='Genre',
                        yaxis_title='Moyenne d\'âge')

        fig.update_layout(bargap=0.2)
        st.plotly_chart(fig, use_container_width=True)


    with col2:
        st.markdown("**2️⃣ Example de widget form**")

        with st.form("average_sales_per_country"):

            #6. Créez une liste déroulante avec : st.selectbox contenanant la liste : ['Ever_Married', 'Graduated']
            #   Créez une liste déroulante avec : st.selectbox contenanant la liste : ['Yes', 'No']
            #   Créez une liste déroulante avec : st.selectbox contenanant la liste : range(18, 100, 5) et range(0, 15)

            Critère = st.selectbox("Sélectionnez un critère :", ['Ever_Married', 'Graduated'])
            
            Boolean = st.selectbox("Sélectionnez une valeur :", ['Yes', 'No'])

            age = st.selectbox("Sélectionnez un age minimum :", range(18, 100, 5))
            family = st.selectbox("Sélectionnez la taille minimum du foyer :", range(0, 15))
            

            #7. Créez un bouton pour soumettre le formulaire avec : st.form_submit_button
            submit = st.form_submit_button(label="Soumettre")


            if submit:
                data_ = df[df[Critère]==Boolean]
                data_ = data_[(data_['Age']>=age) & (data_['Family_Size']>=family)]

                #8. Affichez la moyenne de la variable 'Work_Experience' avec la commande : st.metric
                st.metric("Nombre d'année d'expérience moyen :", value=df.Work_Experience.mean())




#9. Créez une colonne latérale avec : st.sidebar.header
st.sidebar.header("Build dashboards with Streamlit")

### Pages dictionnaire
page = st.sidebar.selectbox("Choisissez une page :", ["Page d'accueil", "Tutorial", "Video"])

dict_page = {"Page d'accueil": home_page, "Tutorial": page_1, "Video": page_2}

dict_page[page]()

st.sidebar.markdown("""* [Bienvenue sur votre Dashboard](#votre-dashboard-interactif-avec-streamlit)""")
st.sidebar.markdown("""* [Affichage des données brutes](#affichage-des-donn-es-brutes)""")
st.sidebar.markdown("""* [Affichage des graphiques](#affichage-des-graphiques)""")
st.sidebar.markdown("""* [Affichage dynamique des données](#affichage-dynamique-des-donn-es)""")


#10. Créez un footer avec : st.columns([1, 1])
# footer, empty_space = #** à compléter avec la fonction footer, __ = st.columns([1, 1]) **#

# with footer:
    # Ajouter du texte avec : st.markdown

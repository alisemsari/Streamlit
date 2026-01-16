import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate
import pandas as pd
df = pd.read_csv("exo.csv")
lesDonneesDesComptes = {'usernames': {}}

for index, row in df.iterrows():
    lesDonneesDesComptes['usernames'][row['username']] = {
        'name': row['name'],
        'password': row['password'],
        'email': row['email'],
        'failed_login_attemps': row['failed_login_attemps'],
        'logged_in': row['logged_in'],
        'role': row['role']
    }


authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie name",
    "cookie key",
    30
)

authenticator.login()
def accueil(): 
  with st.sidebar:
       nom_utilisateur = st.session_state["name"]
       se = option_menu(f"Bienvenue {nom_utilisateur}", ["Accueil", "Les photos de mon chat"])
       st.markdown(
         """
         <style>
          img{
             height: 300px !important;
             width: 600px !important;
             object-fit: cover;
            }
    
         </style>
         """,
         unsafe_allow_html=True)
       
  if se=="Accueil":
         st.title("Bienvenue sur ma Page")

         st.image("https://static.streamlit.io/examples/dog.jpg",caption="The dog")
  else:
         st.title("Bienvenue dans l'album de mon chat")
         col1,col2,col3=st.columns([1,2,1])
         with col1:
             st.image("https://static.streamlit.io/examples/dog.jpg",caption="The dog")
         with col2:
             st.image("https://static.streamlit.io/examples/cat.jpg",caption="The dog")
         with col3:
             st.image("https://static.streamlit.io/examples/owl.jpg",caption="The dog")

if st.session_state["authentication_status"]:
   accueil()
   authenticator.logout("Déconnexion","sidebar")
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
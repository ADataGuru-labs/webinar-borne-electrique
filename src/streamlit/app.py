import streamlit as st

from src.streamlit.helper import (
    get_les_donnees_depuis,
    gestion_et_affichage_les_donnees_brutes,
    afficher_les_bornes_sur_une_carte,
    afficher_en_camembert_la_repartition_des_bornes_par_statut,
    afficher_en_bar_chart_la_repartition_des_bornes_par_statut_et_arrondissment,
)
import cufflinks as cf

chemin = "/Users/loic.caminale/Workspace/formation/dataguru/webinar-python-borne-electrique/src/streamlit/data.parquet"

st.title("Points de recharge pour véhicules électriques dans Paris")

data_load_state = st.text("Chargement des données...")
df_bornes_elec = get_les_donnees_depuis(chemin)
data_load_state.text("Les données sont chargées !")
gestion_et_affichage_les_donnees_brutes(df_bornes_elec)

st.subheader("Géolocalisation des Points de recharge Disponible")
afficher_les_bornes_sur_une_carte(df_bornes_elec)

st.subheader("Répartition des Points de recharge du nouveau réseau Belib par statut")

afficher_en_camembert_la_repartition_des_bornes_par_statut(df_bornes_elec)

st.subheader("Répartition des Points de recharge du nouveau réseau Belib' par statut et par arrondissement")

afficher_en_bar_chart_la_repartition_des_bornes_par_statut_et_arrondissment(df_bornes_elec)

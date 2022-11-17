import pandas as pd
import streamlit as st
import cufflinks as cf

cf

@st.cache
def get_les_donnees_depuis(chemin: str):
    return pd.read_parquet(chemin)


def gestion_et_affichage_les_donnees_brutes(donnee: pd.DataFrame):
    if st.checkbox("Affichage des données brutes"):
        st.subheader("Données brutes")
        st.write(donnee)


def afficher_les_bornes_sur_une_carte(donnee: pd.DataFrame):
    status_uniques = donnee["statut"].unique()
    statut_selectionne = st.selectbox(
        "Veuillez sélectionner le statut pour filtrer les bornes de recharges", status_uniques
    )
    st.write("Vous avez séléctionné", statut_selectionne)
    st.map(donnee[donnee["statut"] == statut_selectionne])


def afficher_en_camembert_la_repartition_des_bornes_par_statut(donnee: pd.DataFrame):
    statut_col = "statut"
    recharge_count = donnee.groupby(by=statut_col).count()[["id"]].rename(columns={"id": "count"}).reset_index()
    camembert_fig = recharge_count.iplot(
        kind="pie",
        labels=statut_col,
        values="count",
        title="Répartition des Points de recharge du nouveau réseau Belib par statut",
        asFigure=True,
        hole=0.4,
    )
    st.write(camembert_fig)


def afficher_en_bar_chart_la_repartition_des_bornes_par_statut_et_arrondissment(donnee: pd.DataFrame):
    nbr_de_bornes_par_arrondissement_et_statut = (
        donnee.groupby(by=["arrondissement", "statut"]).count()[["id"]].reset_index()
    )
    df_pivoted = nbr_de_bornes_par_arrondissement_et_statut.pivot_table(
        index="arrondissement", columns=["statut"], values="id", fill_value=0
    ).reset_index()
    df_pivoted.set_index("arrondissement", inplace=True)
    st.bar_chart(data=df_pivoted[["Disponible", "Occupé"]])

chemin = "s3://bornes-electriques-webinar/dev/bornes_electriques.parquet"

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

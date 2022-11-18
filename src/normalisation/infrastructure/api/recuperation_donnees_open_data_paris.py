from datetime import datetime
from typing import Dict, List
import requests

from src.normalisation.objet_metier.borne_electrique import BorneElectrique
from src.normalisation.contrat_interface.recuperation_donnees_bornes_elec import (
    RecuperationDesDonneesBornesElectriques,
)
from src.normalisation.resources.configs import configs

open_data_url = (
    "https://%s?dataset=%s=&rows=%s&sort=code_insee_commune&facet=statut_pdc&facet=last_updated&facet=arrondissement"
    % (
        configs["open_data_api"].get("base_name"),
        configs["open_data_api"].get("dataset_name"),
        configs["open_data_api"].get("nbr_rows"),
    )
)


class RecuperationDesDonneesBornesElectriquesSurOpenDataParis(
    RecuperationDesDonneesBornesElectriques
):
    def recuperation_des_donnees_bornes_electriques(self) -> List[BorneElectrique]:
        donnees_non_normalisees = self.appeler_lapi(open_data_url)
        return [
            BorneElectrique(
                el["fields"].get("id_pdc"),
                datetime.strptime(
                    el["fields"].get("last_updated"), "%Y-%m-%dT%H:%M:%S%z"
                ),
                el["fields"].get("coordonneesxy")[0],
                el["fields"].get("coordonneesxy")[1],
                el["fields"].get("adresse_station"),
                el["fields"].get("statut_pdc"),
                el["fields"].get("arrondissement"),
            )
            for el in donnees_non_normalisees["records"]
        ]

    def appeler_lapi(self, url: str) -> Dict:
        r = requests.get(url)
        return r.json()

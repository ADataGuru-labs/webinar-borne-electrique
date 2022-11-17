from datetime import datetime
from typing import Dict, List
import requests

from src.normalisation.bornes_electriques import BornesElectriques
from src.normalisation.recuperation_donnees_bornes_elec import RecuperationDesDonneesBornesElectriques


class SchemaErrorOpenDataParis(Exception):
    pass


schema_dentree = {
    "type": "object",
    "properties": {
        "id_pdc": {"type": "string"},
        "last_updated": {"type": "string"},
        "coordonneesxy": {"type": "array"},
        "adresse_station": {"type": "string"},
        "statut_pdc": {"type": "string"},
        "arrondissement": {"type": "string"},
    },
    "required": ["id_pdc", "last_updated", "coordonneesxy", "adresse_station", "statut_pdc", "arrondissement"],
}

nbr_rows = "100"
base_name = "opendata.paris.fr/api/records/1.0/search/"
dataset_name = "belib-points-de-recharge-pour-vehicules-electriques-disponibilite-temps-reel&q"
url = (
    "https://%s?dataset=%s=&rows=%s&sort=code_insee_commune&facet=statut_pdc&facet=last_updated&facet=arrondissement"
    % (base_name, dataset_name, nbr_rows)
)


class RecuperationDesDonneesBornesElectriquesSurOpenDataParis(RecuperationDesDonneesBornesElectriques):
    def recuperation_des_donnees_bornes_electriques(self) -> List[BornesElectriques]:
        resultat = self.appeler_lapi(url)
        print("hello")
        return [
            BornesElectriques(
                el["fields"].get("id_pdc"),
                datetime.strptime(el["fields"].get("last_updated"), "%Y-%m-%dT%H:%M:%S%z"),
                el["fields"].get("coordonneesxy")[0],
                el["fields"].get("coordonneesxy")[1],
                el["fields"].get("adresse_station"),
                el["fields"].get("statut_pdc"),
                el["fields"].get("arrondissement"),
            )
            for el in resultat["records"]
        ]

    def appeler_lapi(self, url: str) -> Dict:
        r = requests.get(url)
        return r.json()

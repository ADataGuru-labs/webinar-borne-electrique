import unittest
from datetime import datetime
from typing import List
from unittest.mock import MagicMock

from src.normalisation.bornes_electriques import BornesElectriques
from src.normalisation.recuperation_donnees_open_data_paris import (
    RecuperationDesDonneesBornesElectriquesSurOpenDataParis,
)


class TestRecuperationOpenDataParis(unittest.TestCase):
    def test_recuperations_doit_retourner_des_donnees_de_bornes_electriques(self):
        # Given
        service_recuperation = RecuperationDesDonneesBornesElectriquesSurOpenDataParis()
        retour_api = {
            "records": [
                {
                    "datasetid": "belib-points-de-recharge-pour-vehicules-electriques-disponibilite-temps-reel",
                    "recordid": "3e523ec89bb63d4cec14f5e4f96f6c4ab6779acc",
                    "fields": {
                        "adresse_station": "1-3 Av. du Général Sarrail 75016 Paris",
                        "arrondissement": "16e Arrondissement",
                        "statut_pdc": "Disponible",
                        "code_insee_commune": "16116",
                        "last_updated": "2022-11-17T03:30:03+00:00",
                        "id_pdc": "FR*V75*EHBSAE*PDA*04*2",
                        "coordonneesxy": [48.846973, 2.2558389],
                    },
                    "geometry": {"type": "Point", "coordinates": [2.2558389, 48.846973]},
                    "record_timestamp": "2022-11-17T03:30:04.489Z",
                }
            ],
        }
        service_recuperation.appeler_lapi = MagicMock(return_value=retour_api)
        # When
        # Then
        donnees_bornes_electriques: List[
            BornesElectriques
        ] = service_recuperation.recuperation_des_donnees_bornes_electriques()
        assert donnees_bornes_electriques == [
            BornesElectriques(
                "FR*V75*EHBSAE*PDA*04*2",
                datetime.strptime("2022-11-17T03:30:03+00:00", "%Y-%m-%dT%H:%M:%S%z"),
                48.846973,
                2.2558389,
                "1-3 Av. du Général Sarrail 75016 Paris",
                "Disponible",
                "16e Arrondissement",
            )
        ]

import unittest

from src.normalisation.infra.api.recuperation_donnees_open_data_paris import (
    RecuperationDesDonneesBornesElectriquesSurOpenDataParis,
)


class TestRecuperationOpenDataParis(unittest.TestCase):
    def test_appeler_lapi_doit_retourner_un_resultat_sous_format_json_valide(self):
        # Given
        service_recuperation = RecuperationDesDonneesBornesElectriquesSurOpenDataParis()
        nbr_rows = "1"
        base_name = "opendata.paris.fr/api/records/1.0/search/"
        dataset_name = "belib-points-de-recharge-pour-vehicules-electriques-disponibilite-temps-reel&q"
        # When
        resultat = service_recuperation.appeler_lapi(
            url=(
                "https://%s?dataset=%s=&rows=%s&sort=code_insee_commune&facet=statut_pdc&facet=last_updated&facet=arrondissement"
                % (base_name, dataset_name, nbr_rows)
            )
        )
        # Then
        assert type(resultat) is dict

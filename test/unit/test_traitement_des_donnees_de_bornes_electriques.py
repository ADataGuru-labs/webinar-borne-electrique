from unittest.mock import MagicMock, Mock

import pandas as pd

from src.normalisation.traitement_des_donnees_de_bornes_electriques import (
    TraitementDesDonneesDeBornesElectriques,
)
from src.normalisation.stockage_objet import EnregistrementStockageObjet
from src.normalisation.recuperation_donnees_open_data_paris import (
    RecuperationDesDonneesBornesElectriquesSurOpenDataParis,
)


class TestTraitementDesDonneesDeBornesElectriques:
    def test_doit_appeler_le_service_de_recuperation_des_donnees(self):
        # Given
        service_recuperation_donnees = RecuperationDesDonneesBornesElectriquesSurOpenDataParis()
        service_recuperation_donnees.recuperation_des_donnees_bornes_electriques = MagicMock()

        uc = TraitementDesDonneesDeBornesElectriques(service_recuperation_donnees, Mock())

        # When
        uc.appliquer()

        # Then
        service_recuperation_donnees.recuperation_des_donnees_bornes_electriques.assert_called_once()

    def test_doit_appeler_la_sauvegarde(self):
        df = pd.DataFrame({"id": ["1", "2"]})
        service_recuperation_donnees = RecuperationDesDonneesBornesElectriquesSurOpenDataParis()
        service_recuperation_donnees.recuperation_des_donnees_bornes_electriques = MagicMock(return_value=df)

        service_enregistrement_donnees = EnregistrementStockageObjet()
        service_enregistrement_donnees.enregistrement = MagicMock()

        uc = TraitementDesDonneesDeBornesElectriques(service_recuperation_donnees, service_enregistrement_donnees)

        # When
        uc.appliquer()

        # Then
        service_enregistrement_donnees.enregistrement.assert_called_once_with(df)

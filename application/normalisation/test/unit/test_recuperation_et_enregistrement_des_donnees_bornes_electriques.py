from unittest.mock import MagicMock, Mock

import pandas as pd

from application.normalisation.src.infrastructure.stockage_objet.aws_s3 import EnregistrementStockageObjet
from application.normalisation.src.usecase.recuperation_et_enregistrement_des_donnees_de_bornes_electriques import (
    RecuperationEtEnregistrementDesDonneesBornesElectriques,
)
from application.normalisation.src.infrastructure.api.recuperation_donnees_open_data_paris import (
    RecuperationDesDonneesBornesElectriquesSurOpenDataParis,
)


class TestTraitementDesDonneesDeBornesElectriques:
    def test_doit_appeler_le_service_de_recuperation_des_donnees(self):
        # Given
        service_recuperation_donnees = (
            RecuperationDesDonneesBornesElectriquesSurOpenDataParis()
        )
        service_recuperation_donnees.recuperation_des_donnees_bornes_electriques = (
            MagicMock()
        )

        uc = RecuperationEtEnregistrementDesDonneesBornesElectriques(
            service_recuperation_donnees, Mock()
        )

        # When
        uc.appliquer()

        # Then
        service_recuperation_donnees.recuperation_des_donnees_bornes_electriques.assert_called_once()

    def test_doit_appeler_la_sauvegarde(self):
        df = pd.DataFrame({"id": ["1", "2"]})
        service_recuperation_donnees = (
            RecuperationDesDonneesBornesElectriquesSurOpenDataParis()
        )
        service_recuperation_donnees.recuperation_des_donnees_bornes_electriques = (
            MagicMock(return_value=df)
        )

        service_enregistrement_donnees = EnregistrementStockageObjet()
        service_enregistrement_donnees.enregistrement = MagicMock()

        uc = RecuperationEtEnregistrementDesDonneesBornesElectriques(
            service_recuperation_donnees, service_enregistrement_donnees
        )

        # When
        uc.appliquer()

        # Then
        service_enregistrement_donnees.enregistrement.assert_called_once_with(df)

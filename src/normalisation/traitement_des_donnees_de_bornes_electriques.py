from typing import List

from src.normalisation.bornes_electriques import BornesElectriques
from src.normalisation.enregistrement_bornes_elec import EnregistrementDesDonneesBornesElectriques
from src.normalisation.recuperation_donnees_bornes_elec import RecuperationDesDonneesBornesElectriques
from src.normalisation.infra.api.recuperation_donnees_open_data_paris import (
    RecuperationDesDonneesBornesElectriquesSurOpenDataParis,
)
from src.normalisation.infra.stockage_objet.stockage_objet import EnregistrementStockageObjet


class RecuperationEtEnregistrementDesDonneesDeBornesElectriques:
    def __init__(
        self,
        service_recuperation: RecuperationDesDonneesBornesElectriques,
        service_enregistrement: EnregistrementDesDonneesBornesElectriques,
    ):
        self.service_enregistrement = service_enregistrement
        self.service_recuperation_de_donnees = service_recuperation

    def appliquer(self):
        donnees_bornes_electriques: List[
            BornesElectriques
        ] = self.service_recuperation_de_donnees.recuperation_des_donnees_bornes_electriques()
        self.service_enregistrement.enregistrement(donnees_bornes_electriques)


if __name__ == "__main__":
    RecuperationEtEnregistrementDesDonneesDeBornesElectriques(
        RecuperationDesDonneesBornesElectriquesSurOpenDataParis(), EnregistrementStockageObjet()
    ).appliquer()

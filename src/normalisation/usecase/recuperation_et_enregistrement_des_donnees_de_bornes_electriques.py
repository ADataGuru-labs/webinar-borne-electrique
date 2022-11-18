from typing import List

from src.normalisation.objet_metier.borne_electrique import BorneElectrique
from src.normalisation.contrat_interface.enregistrement_bornes_elec import EnregistrementDesDonneesBornesElectriques
from src.normalisation.contrat_interface.recuperation_donnees_bornes_elec import RecuperationDesDonneesBornesElectriques
from src.normalisation.infrastructure.api.recuperation_donnees_open_data_paris import (
    RecuperationDesDonneesBornesElectriquesSurOpenDataParis,
)
from src.normalisation.infrastructure.stockage_objet.aws_s3 import EnregistrementStockageObjet


class RecuperationEtEnregistrementDesDonneesBornesElectriques:
    def __init__(
        self,
        service_recuperation: RecuperationDesDonneesBornesElectriques,
        service_enregistrement: EnregistrementDesDonneesBornesElectriques,
    ):
        self.service_enregistrement = service_enregistrement
        self.service_recuperation_de_donnees = service_recuperation

    def appliquer(self):
        donnees_bornes_electriques: List[
            BorneElectrique
        ] = self.service_recuperation_de_donnees.recuperation_des_donnees_bornes_electriques()
        self.service_enregistrement.enregistrement(donnees_bornes_electriques)

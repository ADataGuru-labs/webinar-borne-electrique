from abc import ABC, abstractmethod

import pandas as pd


class RecuperationDesDonneesBornesElectriques(ABC):
    @abstractmethod
    def recuperation_des_donnees_bornes_electriques(self) -> pd.DataFrame:
        pass


class EnregistrementDesDonneesBornesElectriques:
    def enregistrement(self, df: pd.DataFrame):
        pass


class TraitementDesDonneesDeBornesElectriques:
    def __init__(
        self,
        service_recuperation: RecuperationDesDonneesBornesElectriques,
        service_enregistrement: EnregistrementDesDonneesBornesElectriques,
    ):
        self.service_enregistrement = service_enregistrement
        self.service_recuperation_de_donnees = service_recuperation

    def appliquer(self):
        df = self.service_recuperation_de_donnees.recuperation_des_donnees_bornes_electriques()
        self.service_enregistrement.enregistrement(df)

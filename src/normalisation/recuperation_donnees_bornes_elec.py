from abc import ABC, abstractmethod
from typing import List

from src.normalisation.bornes_electriques import BornesElectriques


class RecuperationDesDonneesBornesElectriques(ABC):
    @abstractmethod
    def recuperation_des_donnees_bornes_electriques(self) -> List[BornesElectriques]:
        pass

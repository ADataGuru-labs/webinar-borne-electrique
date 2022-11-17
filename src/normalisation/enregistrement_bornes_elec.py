from abc import ABC, abstractmethod
from typing import List

from src.normalisation.bornes_electriques import BornesElectriques


class EnregistrementDesDonneesBornesElectriques(ABC):
    @abstractmethod
    def enregistrement(self, donnees_bornes_electriques: List[BornesElectriques]) -> None:
        pass

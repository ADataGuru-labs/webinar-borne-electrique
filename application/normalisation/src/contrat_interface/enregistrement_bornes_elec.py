from abc import ABC, abstractmethod
from typing import List

from application.normalisation.src.objet_metier.borne_electrique import BorneElectrique


class EnregistrementDesDonneesBornesElectriques(ABC):
    @abstractmethod
    def enregistrement(self, donnees_bornes_electriques: List[BorneElectrique]) -> None:
        pass

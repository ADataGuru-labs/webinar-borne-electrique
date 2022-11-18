from abc import ABC, abstractmethod
from typing import List

from src.normalisation.objet_metier.borne_electrique import BorneElectrique


class RecuperationDesDonneesBornesElectriques(ABC):
    @abstractmethod
    def recuperation_des_donnees_bornes_electriques(self) -> List[BorneElectrique]:
        pass

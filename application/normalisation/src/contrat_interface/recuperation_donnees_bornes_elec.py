from abc import ABC, abstractmethod
from typing import List

from application.normalisation.src.objet_metier.borne_electrique import BorneElectrique


class RecuperationDesDonneesBornesElectriques(ABC):
    @abstractmethod
    def recuperation_des_donnees_bornes_electriques(self) -> List[BorneElectrique]:
        pass

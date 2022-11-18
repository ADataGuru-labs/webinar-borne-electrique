from typing import List

import pandas as pd

from src.normalisation.objet_metier.borne_electrique import BorneElectrique
from src.normalisation.contrat_interface.enregistrement_bornes_elec import EnregistrementDesDonneesBornesElectriques
from src.normalisation.resources.configs import configs


class EnregistrementStockageObjet(EnregistrementDesDonneesBornesElectriques):
    def enregistrement(self, donnees_bornes_electriques: List[BorneElectrique]):
        pd.DataFrame(donnees_bornes_electriques).to_parquet(configs.get("s3_path"))

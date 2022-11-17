from typing import List

import pandas as pd

from src.normalisation.bornes_electriques import BornesElectriques
from src.normalisation.enregistrement_bornes_elec import EnregistrementDesDonneesBornesElectriques
from src.normalisation.resources.configs import configs


class EnregistrementStockageObjet(EnregistrementDesDonneesBornesElectriques):
    def enregistrement(self, donnees_bornes_electriques: List[BornesElectriques]):
        pd.DataFrame(donnees_bornes_electriques).to_parquet(configs.get("s3_path"))

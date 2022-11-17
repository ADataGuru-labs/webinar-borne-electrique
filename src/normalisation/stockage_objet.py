from typing import List

import pandas as pd

from src.normalisation.bornes_electriques import BornesElectriques
from src.normalisation.enregistrement_bornes_elec import EnregistrementDesDonneesBornesElectriques

s3_path = "s3://bornes-electriques-webinar/test/bornes_electriques.parquet"


class EnregistrementStockageObjet(EnregistrementDesDonneesBornesElectriques):
    def enregistrement(self, donnees_bornes_electriques: List[BornesElectriques]):
        pd.DataFrame(donnees_bornes_electriques).to_parquet(s3_path)

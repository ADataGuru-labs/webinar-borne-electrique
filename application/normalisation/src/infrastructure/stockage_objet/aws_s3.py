from typing import List

import pandas as pd

from application.normalisation.src.objet_metier.borne_electrique import BorneElectrique
from application.normalisation.src.contrat_interface.enregistrement_bornes_elec import (
    EnregistrementDesDonneesBornesElectriques,
)
from application.normalisation.src.resources.configs import configs


class EnregistrementStockageObjet(EnregistrementDesDonneesBornesElectriques):
    def enregistrement(self, donnees_bornes_electriques: List[BorneElectrique]):
        pd.DataFrame(donnees_bornes_electriques).to_parquet(configs.get("s3_path"))

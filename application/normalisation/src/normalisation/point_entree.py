from application.normalisation.src.normalisation.infrastructure.api.recuperation_donnees_open_data_paris import (
    RecuperationDesDonneesBornesElectriquesSurOpenDataParis,
)
from application.normalisation.src.normalisation.infrastructure.stockage_objet.aws_s3 import (
    EnregistrementStockageObjet,
)
from application.normalisation.src.normalisation.usecase.recuperation_et_enregistrement_des_donnees_de_bornes_electriques import (
    RecuperationEtEnregistrementDesDonneesBornesElectriques,
)

if __name__ == "__main__":
    RecuperationEtEnregistrementDesDonneesBornesElectriques(
        RecuperationDesDonneesBornesElectriquesSurOpenDataParis(),
        EnregistrementStockageObjet(),
    ).appliquer()

from flask import Flask

app = Flask(__name__)


from application.normalisation.src.infrastructure.api.recuperation_donnees_open_data_paris import (
    RecuperationDesDonneesBornesElectriquesSurOpenDataParis,
)
from application.normalisation.src.infrastructure.stockage_objet.aws_s3 import (
    EnregistrementStockageObjet,
)
from application.normalisation.src.usecase.recuperation_et_enregistrement_des_donnees_de_bornes_electriques import (
    RecuperationEtEnregistrementDesDonneesBornesElectriques,
)

@app.route("/")
def recuperation_et_enregistrement():
    RecuperationEtEnregistrementDesDonneesBornesElectriques(
        RecuperationDesDonneesBornesElectriquesSurOpenDataParis(),
        EnregistrementStockageObjet(),
    ).appliquer()
    return "RecuperationEtEnregistrementDesDonneesBornesElectriques appliqué !"


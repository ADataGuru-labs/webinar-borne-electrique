import os

env = os.environ.get("ENVIRONMENT", "test")
configs = {
    "s3_path": ("s3://bornes-electriques-webinar/%s/bornes_electriques.parquet" % env),
    "open_data_api": {
        "nbr_rows": 1000,
        "base_name": "opendata.paris.fr/api/records/1.0/search/",
        "dataset_name": "belib-points-de-recharge-pour-vehicules-electriques-disponibilite-temps-reel&q",
    },
}

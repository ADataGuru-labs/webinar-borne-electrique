from dataclasses import dataclass
from datetime import datetime


@dataclass
class BorneElectrique:
    id: str
    timestamp: datetime
    latitude: float
    longitude: float
    adresse_station: str
    statut: str
    arrondissement: str

# Webinar Python borne Electrique


Dans ce dépôt nous pouvons retrouver le code permettant de récupérer les données sur l'api Belib' (stations de bornes
électriques pour voiture).


## Vue globale de l'architecture réalisée

![vue_globale.png](static/archi_vue_globale.png)

+ Des tableaux de bord, pour afficher des Kpis sur les données de bornes électriques, vous pouvez retrouver le code dans 
[app.py](exposition/streamlit/app.py) 
+ Un traitement de récupération des données Bélib' et enregistrement sur un bucket s3


## Todo qui a servi pour développer 

- [ ]  Créer un usecase : RecuperationEtEnregistrementDonneesBorneElec
    - Doit appeler Le service de récupération : RecuperationDonneesBorneElec
    - Doit appeler Le service d'enregistrement : EnregistrementDonneesBorneElec
![img_3.png](static/implementation_usecase.png)
- [ ]  Implémenter un service de récupération : RecuperationDonneesBelib
![img_4.png](static/implementation_service_recuperation.png)
- [ ]  Implémenter un service d'enregistrement : EnregistrementSurS3
![img_5.png](static/implementation_service_enregistrement.png)

---
title: "Vers un cloud "carbon-aware""
date: 2023-07-04T10:48:50Z
github_username: obierlaire
twitter_username: obierlaire
---
### Author's Name

Olivier Bierlaire

### Author's Bio

Basé à Nantes, je m'intéresse au cloud durable et responsable.
Ex-équipe fondatrice de Canva, j'ai travaillé chez Elastic et maintenant sur Carbonifer.io

### Expected time

Standard talk (~40 min)

### Language

- [X] French
- [ ] English

### Abstract

# "J'ai toute mon infrastructure dans le cloud, je n'émet pas de CO2"

Le Cloud cache un vilain secret : il génère autant de gaz à effet de serre que des pays entiers comme la France ou le Royaume-Uni ([IEA, 2021](https://www.iea.org/reports/data-centres-and-data-transmission-networks)). Et ça ne fait qu'empirer ! Imaginez, ces émissions équivalent à celles du secteur aérien !

Les équipes Infra & Cloud ont l’opportunité d’atténuer ce problème. Tout commence par une simple décision : choisir la bonne région sur GCP, Azure ou AWS. Et devinez quoi ? Ce choix peut diviser vos émissions par 10, voire 20 ! Selon la météo, un pays comme l’Irlande a une intensité carbone de 400 gCO2eq/kWh quand le réseau français peut descendre à 20 g. Je vais donc montrer comment on peut mesurer et réduire drastiquement ces émissions : rendre son cloud “carbon-aware”.

# Structure du talk

Dans cette présentation, je vais :

- Parler du problème des émissions de CO2 du cloud.
- Présenter le contexte réglementaire et financier
- Présenter comment mesurer et estimer les émissions.
- Présenter comment réduire les émissions de son infrastructure.
- Expliquer le concept de "carbon-awareness" (auto-ajustement de l'infrastructure selon les émissions).
- Faire une Démo d'une infrastructure carbon-aware.

# Qui suis-je
Ex premier dévelopeur sur Canva à Sydney, j'ai ensuite rejoint Elastic pendant quelques années. Aujourd'hui j'ai lancé [Carbonifer](carbonifer.io) un projet qui ambitionne de rendre les infras cloud "carbon aware"
Le reste du talk ne présentera pas nécessairement le projet Carbonifer en particulier (pas de pub), mais l'ensemble des outils.

# Détails

## Pourquoi vous embêter avec tout cela ?

Parce que le monde change, et les réglementations et les investisseurs vous poussent à agir. Les réglementations nationales et européennes sont mises en place pour forcer les entreprises à mesurer leur empreinte carbone. Les entreprises devront montrer des efforts mesurables. Les fonds ESG cherchent également à investir dans des entreprises vertueuses. Et enfin, c'est un outil efficace pour attirer des talents et fidéliser des clients.

## Mesurer

"You can't improve what you don't measure." - Peter Drucker

Je vais montrer l'utilisation des outils d'observabilité pour estimer les émissions de son infrastructure cloud.

L'intensité carbone du réseau électrique alimentant les datacenters est une donnée publique, donc on peut estimer en direct les émissions de son cloud.

## Réduire

Une fois que nous savons mesurer, la prochaine étape est l'action. Je présenterai des méthodes concrètes pour réduire l'empreinte carbone de votre infrastructure cloud. Nous allons au-delà de la simple mise en pause des machines sous-utilisées, on peut envisager de choisir une région moins émettrice. Enfin, les auto-scaling groups et les services serverless permettent d'émettre le strict minimum.

## *Carbon-Awareness*

On peut aussi imaginer une infrastructure qui s'adapte en fonction de ses émissions. Lorsque l'électricité alimentant la région devient trop carbonée, on peut automatiquement réduire le nombre de machines de son cluster ou le déplacer temporairement dans une région moins carbonée.

Pour illustrer ces concepts, je ferai une démo d'une infrastructure qui peut "déplacer" un cluster d'instances d'une région à une autre en fonction de l'intensité carbone du réseau électrique, sans aucun temps d'arrêt ni compromis sur la qualité du service.

De plus, nous explorerons comment planifier intelligemment des tâches lourdes et asynchrones, comme l'entraînement de modèles IA et le traitement vidéo. En les exécutant dans une région à faible intensité carbone et/ou lorsque les conditions météorologiques seront favorables, on peut diminuer drastiquement son empreinte.

Tout cela pour montrer qu'on peut rendre son infrastructure auto-ajustable en fonction de ses émissions et la rendre "carbon-aware" !


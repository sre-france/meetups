---
title: "Kubernetes Gateway API : Pourquoi remplacer les Ingress ?"
date: 2022-10-24T15:28:47Z
github_username: pyaillet
twitter_username: pyaillet
---
__author name__:
Pierre-Yves Aillet @pyaillet

__author bio__:
Passionné d'informatique, Pierre-Yves travaille depuis 15 ans sur des technologies variées allant de PHP à Java en passant par Javascript. Son IHM de prédilection est la ligne de commande. Il est consultant chez Zenika Nantes et intervient sur des missions d’audit, d’accompagnement à la mise en place d'outils liés la conteneurisation, Kubernetes et au Cloud.

__expected time__ :

- [ ] short talk (~ 5 min)
- [x] 15 min

__language__:

- [x] :fr:
- [x] :uk:

**this talk can be done**:
- [x] remotely
- [x] physically Nantes

__abstract__:
L'objectif de cette présentation est de faire un rapide tour d'horizon de ce qui nous attend sur Kubernetes avec la nouvelle Kubernetes Gateway API.

En tant qu'utilisateur des offres de Kubernetes managées, nous sommes souvent amenés à manipuler les services de type Load Balancers proposés avec une intégration par les Cloud Providers. Malheureusement, ces offres sont limitées : pas de réutilisation d'un Load Balancer entre plusieurs services, pas de routing L7, etc
Un complément usuel est la mise en place d'un Ingress Controller et des ressources de type Ingress, mais l'intégration n'est pas toujours satisfaisante et nous éloigne du service géré pour nous.

Après un tour d'horizon de ce qui existe aujourd'hui, l'objectif sera de présenter ce qui nous attend avec la nouvelle Kubernetes Gateway API et en quoi elle répond aux problèmes précédemment évoqués.




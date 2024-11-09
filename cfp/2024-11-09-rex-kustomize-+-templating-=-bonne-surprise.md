---
title: "REX : Kustomize + templating = bonne surprise"
date: 2024-11-09T22:45:47Z
github_username: busser
twitter_username: ArthurBusser
---
### Author's Name

Arthur Busser

### Author's Bio

Arthur est un SRE parisien. I travaille sur Pigment, une application cloud native, axée sur les données et à l'échelle mondiale. Il aime fabriquer des outils qui rendent les ingénieur·e·s plus productif·ve·s et estime que la simplicité est essentielle.

### Expected time

Standard talk (~15 min)

### Language

- [X] French
- [ ] English

### Abstract

Chez Pigment, nous avons choisi Kustomize pour déployer nos services in-house, en laissant Helm aux logiciels tiers. Pourquoi ? Kustomize, avec sa capacité de patching, rend la configuration à la fois lisible et modulaire, même pour les non-SRE, tout en restant fidèle aux spécifications Kubernetes. Cependant, Kustomize atteint parfois ses limites, en particulier lorsque le patching devient inutilement complexe.

Pour contourner cette complexité, nous avons introduit du templating en petite dose via un outil custom, Toner. Cette approche permet de combler les lacunes du patching tout en conservant flexibilité et simplicité. Je partagerai des exemples concrets illustrant les défis rencontrés avec Kustomize et les solutions élégantes apportées par Toner.

Ce retour d'expérience se clôturera sur une réflexion : sous quelle forme rendre open-source la logique de Toner, pour combiner le meilleur de Kustomize et du templating ?


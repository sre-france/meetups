---
title: "Maîtrisez votre code Terraform: bonnes pratiques de refactoring et introduction à tfautomv"
date: 2023-06-19T11:47:37Z
github_username: busser
twitter_username: ArthurBusser
---
### Author's Name

Arthur Busser @ArthurBusser

### Author's Bio

Arthur est un SRE parisien. I travaille sur Pigment, une application cloud native, axée sur les données et à l'échelle mondiale. Il aime fabriquer des outils qui rendent les ingénieur·e·s plus productif·ve·s et estime que la simplicité est essentielle.

### Expected time

Standard talk (~40 min)

### Language

- [X] French
- [ ] English

### Abstract

En matière d'infrastructure as code, Terraform est un outil puissant mais complexe. Dans cette présentation, nous explorerons des stratégies pour contrôler cette complexité et concevoir un code Terraform maintenable et malléable.

Nous aborderons comment découper votre code Terraform en adéquation avec le cycle de vie de l'infrastructure et l'importance d'utiliser des modules en tant qu'abstractions pour maîtriser la complexité. Nous dévoilerons également des patterns spécifiques pour gérer efficacement l'explosion de la complexité dans les infrastructures web modernes avec une multitude d'environnements et de services.

L'un des points phares de notre présentation sera [tfautomv](https://github.com/busser/tfautomv), un outil conçu pour alléger le processus de refactoring du code Terraform. Cet outil, en analysant le plan de Terraform, génère automatiquement les commandes ou blocs nécessaires pour redéfinir l'adresse des ressources déplacées, minimisant les erreurs et facilitant la maintenance.

Ce talk s'adresse principalement aux SRE ayant une expérience avancée avec Terraform. Notre objectif est de vous aider à saisir l'importance de la maîtrise de la complexité du code Terraform, de vous présenter des patterns utiles pour articuler votre vision de l'infrastructure dans votre code et de vous initier à l'utilisation de [tfautomv](https://github.com/busser/tfautomv) pour un refactoring plus fluide.


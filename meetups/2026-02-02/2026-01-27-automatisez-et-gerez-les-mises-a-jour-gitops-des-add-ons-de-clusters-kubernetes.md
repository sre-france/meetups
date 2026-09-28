---
title: "Automatisez et gerez les mises à jour GitOps des « add-ons » de clusters Kubernetes"
date: 2026-01-27T20:13:54Z
github_username: xakraz
---
### Author's Name

Xavier Krantz

### Author's Bio

_No response_

### Expected time

Standard talk (~15 min)

### Language

- [x] French
- [ ] English

### Abstract

Contexte: 
* Vous utilisez **Kubernetes** 👍️ 
* Vous avez une pratique **GitOps** pour le deploiement 👍️
* Vous déployez des **« add-ons »**, comme les CNI, Ingress-controllers, Operators, gestion des certificats, etc. 🧱 
* Vous administrez **plusieurs clusters** 🪢 



❓️Comment gérez-vous les **mises à jour** de ces « composants » à travers votre flotte de clusters ?
- Comment suivez-vous les montées de version et les dernières releases ?
- Comment être sûr d'avoir déployé le dernier fix de sécurité ?
- Comment déployer de manière sûre et efficace à travers les « environnements » et contrôler le blast-radius ?


💡Et si nous utilisions des outils de gestion de versions comme **Dépendabot/Renovate** ?
 

🎯 Durant cette présentation, nous allons explorer une solution utilisant le concept de **« promotion »,** aka des pipelines, et une approche _[« issueOps »](https://issue-ops.github.io/docs/)_ afin d'éviter la PR-fatigue et les revues aveugles.

Nous expliquerons comment l’usage combiné de branches git DRY/WET, de Kustomize/Helm, et d’outils tels que ArgoCD et Kargo.io permet de faciliter le processus de CI/CD de « composants » nécessaires pour une « plateforme » Kubernetes-based.

Nous montrerons :
- Comment fiabiliser et accélérer les déploiements multi-environnements
- Comment concilier simplicité pour l'operateur et contrôle pour la production
- Les gains en traçabilité et en auditabilité, mais aussi les limites et écueils rencontrés


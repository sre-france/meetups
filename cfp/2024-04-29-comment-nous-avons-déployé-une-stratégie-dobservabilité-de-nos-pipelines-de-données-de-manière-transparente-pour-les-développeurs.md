---
title: "Comment nous avons déployé une stratégie d'observabilité de nos pipelines de données de manière transparente pour les développeurs"
date: 2024-04-29T08:34:12Z
github_username: benoitgoujon
---
### Author's Name

Emma Galliere et Benoît Goujon

### Author's Bio

Emma et Benoît sont software engineers chez Artefact. Ils travaillent aujourd'hui ensemble au sein d'une équipe en charge de mettre à disposition des outils pour faciliter les opérations sur les cas d'usage data d'un grand groupe du luxe.

### Expected time

Standard talk (~15 min)

### Language

- [X] French
- [ ] English

### Abstract

Environ 600 flux de données sont aujourd'hui déployés en production chez ce grand groupe du luxe français. Les observer est un enjeu crucial. Les observer signifie dans notre cas plusieurs choses. Ce n'est pas seulement connaître leur statut. C'est aussi mesurer les coûts (enjeu majeur quand on manipule beaucoup de données), connaître les versions des logiciels utilisés, connaître les temps d'exécution et repérer d'éventuelles anomalies, etc.

Nous avons mis cela en place en respectant également une contrainte forte : l'observabilité ne doit nécessiter aucune action de la part des squads en charge du développement des cas d'usage. Le process doit être transparent.

Nous verrons de ce talk comment nous avons résolu cette problématique en utilisant notamment les sidecars de Kubernetes.


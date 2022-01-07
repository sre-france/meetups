---
title: "Ne laissez pas vos mauvaises habitudes k8s devenir le cauchemar de vos administrateurs k8s"
date: 2022-01-07T17:49:58Z
github_username: henrikrexed
twitter_username: hrexed
---
__author name__:
Henrik Rexed

__author bio__:
Henrik est Cloud Native Advocate chez Dynatrace, la plateforme leader de l’Observabilité.
Avant Dynatrace, Henrik a travaillé en tant que Partner Solution Evangelists, animant de nombreux webinars et conférences, construisant des prototypes pour améliorer le capacités et les intégrations de NeoLoad.
Henrik Rexed est également l’un des fondateurs de la conférence Performance Advisory Council et anime la chaîne Youtube IsitObservable


__expected time__ :

- [ ] lightning talk (~ 5 min)
- [ X] 15 min

__language__:

- [X ] :fr:
- [ ] :uk:

**this talk will be done**:
- [ X] remotely
- [X ] physically

__abstract__:
Comme toute transformation technologique, l'adoption de k8s commence généralement par de petits "projets domestiques". Un cluster k8s ici, un autre là. Si vous ne regardez pas de près, vous finissez comme de nombreuses organisations de nos jours. Quelque chose qui se répand comme une traînée de poudre : des centaines ou des milliers de clusters k8s, appartenant à des équipes différentes, répartis sur site et dans le cloud. Certains sont partagés. D'autres sont très isolés.

Lorsque nous commençons à créer des applications pour k8s, nous ne nous concentrons pas sur les limites de ressources correctement définies ou nous ignorons complètement les contraintes liées aux nœuds et aux clusters, comme le nombre d'adresses IP disponibles. Ce sont de mauvaises habitudes qui entraînent des travaux non planifiés et empêchent vos applications d'évoluer et de fonctionner comme vous le souhaitez. Au cours des dernières années, la communauté k8s a appris de bonnes habitudes que nous pouvons traduire en validations d'architecture et de performance.
Pour simplifier la gestion de notre cluster et réduire les tâches "non planifiées" pour réduire le coût et augmenter la fiabilité de nos applications, nous devons utiliser les bonnes règles de validation dans le cycle de vie de votre projet...
Au cours de cette présentation, nous utiliserons des histoires réelles de production, sur la façon dont la vie des administrateurs de k8S est devenue un cauchemar en raison de l'absence de validation dans nos processus CICD.
Nous présenterons les différents kpi utilisés par nos opérateurs K8s et comprendrons :
- comment tirer parti de ces mesures au cours de vos premières activités d'ingénierie de la performance.
- Le type d'outils que nous devons mettre en place pour avoir le bon niveau d'observabilité.
- Les processus automatisés qui réduiront les tâches de maintenance 




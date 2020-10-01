Bonjour à tous et à toutes,

Nous sommes ravis de vous inviter au 7ème meetup SRE Paris !!

Cet édition de septembre sera complément en ligne et on a choisi un format plus court et dynamique car la plupart d'entre passe déjà pas mal de temps en vidéoconférence ;) donc ça sera l’occasion de partager des nouveautés et des projets du groupe, ainsi que d'en parler sur Infrastructure as code.

Voici le programme de la soirée :

* 19h00-19h10 : Présentation du programme et des news du groupe
* 19h10-19h25 : Datacenter Unplugged par Mathieu Tortuyaux (@tormath1)
* 19h25-19h40 : Reliability Report par Pablo Seminario
* 19h40-19h45 : Announcement : call for participation to a study on infrastructure drift par Gerald Crescione
* 19h45-20h00 : Questions et feedback pour le prochain meetup

Comme d'habitude, s'il y a des gens motivés pour un lightning talk (~5/10 minutes) ou pour des autres annonces rapides n'hésitez pas à les proposer, les talks sont ouverts à tout type de niveaux et de thématiques SRE: principes, on-call, monitoring, best practices, incident management, post-mortem, outils, retours d'expérience, etc.

A mercredi !

---

# Détail des présentations

## Datacenter Unplugged

* Speaker Name: Mathieu Tortuyaux (@tormath1)
* Speaker bio: Open-Source maintainer, Gentoo lover and remote devops engineer @ cycloid
* Talk Abstract: What if I pull the plug of the datacenter ? What if someone ran a script deleting all my cloud resources ? What if my AWS organization is deleted by "mistake" ? This scenarios can be horrific or fearless, depending on the answer of this question: is my infra as code ?

In this session, we will talk about IaC and more specifically the transition from IaDN (Infra as /dev/null) to IaC. How can you adapt your workflow and your legacy infra without impacting your running resources. We will go through an actual example: starting from a legacy infra, how can we generate and manipulate IaC to make the infra persistent.

## Reliability Report

* Speaker Name: Pablo Seminario (@pabluk)
* Speaker bio: SRE @PeopleDoc
* Talk Abstract: A lightning talk about a project to create a collaborative site/newsletter about Reliability Engineering using an event-driven architecture.

## Announcement : call for participation to a study on infrastructure drift

* Speaker Name: Gerald Crescione
* Speaker bio: CMO at Cloudskiff, a platform that helps DevOps better collaborate over Infrastructure as Code. Currently working on ‘driftctl’, an OSS CLI that tracks, analyzes, prioritizes, and warns users of infrastructure drift (launching soon)
* Talk Abstract: as part of our work on ‘driftctl’ we are writing a report on how infrastructure drift can be a challenge for DevOps teams, and how they address it. The goal is to share with the community core problems and best practices.

What we call infrastructure drift is when the actual state of infrastructure diverges from the IaC codebase. It can be driven by human input, poor configuration, applications making unwanted changes, etc. We think it's an important, emerging topic and there is an opportunity for practitioners to come up and share their stories and tips with others.

So for those interested, all you have to do is chat with us for 30 minutes and share your side of things.

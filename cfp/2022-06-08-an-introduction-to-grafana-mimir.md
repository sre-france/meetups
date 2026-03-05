---
title: "An introduction to Grafana Mimir"
date: 2022-06-08T21:21:57Z
github_username: ahadjidj
---
__author name__:
Abdelkrim Hadjidj

__author bio__:
Abdelkrim Hadjidj is a Solutions Engineering Manager at Grafana Labs with over a decade of experience on distributed and data intensive systems. His team helps customers in EMEA define their observability strategy with Grafana Labs products. He is an Open Source advocate and works with OSS technologies such as Grafana, Prometheus, Loki and Tempo. He loves sharing best practices with the community at meetups or tech conferences such as GrafanaCon, ApacheCon, Strata, and Flink Forward.

__expected time__ :

- [ ] lightning talk (~ 5 min)
- [x] 30 min

__language__:

- [x] :fr:
- [x] :uk:

**this talk will be done**:
- [ ] remotely
- [x] physically

__abstract__:
Prometheus and Grafana are the de facto standards for monitoring modern cloud native applications and infrastructures.

For organizations needing massive scale, Grafana Labs has launched Grafana Mimir as a solution for extending Prometheus, with high availability, horizontal scalability, multi-tenancy, durable storage, and blazing fast query performance over long periods of time. Grafana Mimir is suitable for running at any scale. We’ve successfully run it on a laptop without WiFi, as well as in production with more than 1 billion active time series.

In this talk, we’ll go over:
- What is Grafana Mimir
- The Mimir architecture, requirements and configuration
- A look at some of the features of Grafana Mimir, like query sharding and the two-stage compactor
- The upcoming features and what you could expect from Mimir in the near future


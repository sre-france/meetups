---
title: "An introduction to Grafana Loki"
date: 2022-06-08T21:37:40Z
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
Grafana’s Loki open source project for logging aggregation has seen a great uptick in adoption by users benefiting from its small index, ease of use, and cost effectiveness. Enterprises like Grofers and [Paytm Insider](https://grafana.com/blog/2019/11/19/how-loki-helped-paytm-insider-save-75-of-logging-and-monitoring-costs/) are using Loki in both Grafana Labs’ hosted offering and on premise. And with the April 2022 [Loki 2.5](https://grafana.com/blog/2022/04/11/new-in-grafana-loki-2.5-faster-queries-more-log-sources-so-long-s3-rate-limits-and-more/?pg=webinar-getting-started-with-logging-and-grafana-loki&plcmt=body-txt) release, we’ve made big gains for improving performance through regular expressions, binary operations, and hedging requests.

In this talk, we’ll go over:
- What is Grafana Loki, how it works, what makes it different, what it’s good at
- The Loki architecture, requirements and configuration
- A look at some of the features of Grafana Loki, such as LogQL, metrics extraction, alerting with powerful Prometheus-style alerting rules
- How to correlate your Prometheus metrics and Loki logs thanks to service discovery and labels


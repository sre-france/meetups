---
title: "Secrets, race conditions, and statelessness"
date: 2022-08-05T14:02:35Z
github_username: busser
twitter_username: ArthurBusser
---
### Author's Name

Arthur Busser (@ArthurBusser)

### Author's Bio

Arthur is an SRE @ Padok where he builds cloud infrastructure. He maintains a couple open source projects and believes in keeping things simple.

### Expected time

Lightning talk (~15 min)

### Language

- [X] French
- [ ] English

### Abstract

Race conditions during service upgrades are the worst. Particularly when a service and its configuration are both updated at the same time, asynchronously, and something goes subtly wrong. In some cases, we end up with inconsistency between multiples instances of the same stateless service.

But wait, isn't the whole point of a stateless service that all instances are identical in every way? Well, yes. But it's easy to make your services a tiny bit stateful without realising it, and a lot of us have been doing just that.

Let me share my experience with these situations, where a stateless service suddenly becomes slightly stateful and our assumptions about our infrastructure are suddenly false. I will look specifically at the common practice of storing secrets in an external secret manager and synchronising them with Kubernetes secrets. While very common, this practice has lead to strange bugs that challenge our understanding of statelessness.

I will also present an alternative model for fetching secrets from external sources, which does not suffer from the same issue and is already used by a few open source projects, with the goal of making our infrastructure more predictable and reliable.


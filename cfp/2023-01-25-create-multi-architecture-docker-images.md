---
title: "Create multi-architecture docker images"
date: 2023-01-25T09:59:41Z
github_username: hhassen
---
__author name__:
Hassen Harzallah

__author bio__:
SRE at Aircall

__expected time__ :

- [ ] short talk (~ 5 min)
- [x] 15 min

__language__:

- [x] :fr:
- [x] :uk:

**this talk can be done**:
- [x] remotely
- [x] physically : Paris

__abstract__:
In Aircall we wanted to switch our Lambda functions in AWS to the less expensive ARM64 architecture runtime. In that context, we decided to migrate to multi-container docker images to make the Lambda migration much easier.
In this short talk, I'll explain why and how we started using multi-architecture docker images at Aircall. These docker images are conceived to run in different architectures and OS (AMD64, ARM64v8 ...).



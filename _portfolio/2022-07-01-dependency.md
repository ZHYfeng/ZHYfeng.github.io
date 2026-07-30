---
title: "Dependency"
excerpt: "A systematic study of dependency challenges in kernel fuzzing, including tools for measurement and mitigation."
collection: portfolio
permalink: /portfolio/dependency
date: 2022-07-01
---

**Demystifying the Dependency Challenge in Kernel Fuzzing**

## Overview

This project systematically studies the dependency challenge in kernel fuzzing — where kernel code is
locked behind specific kernel states that fuzzers struggle to reach. It provides measurement tools and
analysis framework to quantify how dependencies hinder coverage, along with techniques to improve
fuzzer effectiveness through better state exploration.

## Key Features


- **Comprehensive measurement study of kernel dependency coverage gaps**

- **Static analysis for unresolved dependency identification**

- **State-aware fuzzing techniques for improved coverage**

- **Evaluation framework for assessing fuzzer effectiveness under dependencies**


## Technologies


- Go / C++ / C / Python

- LLVM

- Syzkaller

- Protobuf / gRPC



**🏆 Google Research Paper Rewards**


[📄 Paper](http://zhyfeng.github.io/files/icse22_dependency_measurement.pdf) | [🐙 GitHub](https://github.com/seclab-ucr/Dependency)
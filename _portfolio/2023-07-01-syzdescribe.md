---
title: "SyzDescribe"
excerpt: "Statically generates complete syscall descriptions for Linux kernel drivers to enable driver-specific fuzzing."
collection: portfolio
permalink: /portfolio/syzdescribe
date: 2023-07-01
---

**Principled, Automated, Static Generation of Syscall Descriptions for Kernel Drivers**

## Overview

SyzDescribe pioneers a principled static analysis approach to automatically generate system call descriptions
for Linux kernel drivers. By analyzing kernel driver source code and leveraging device model semantics,
SyzDescribe produces high-quality syzkaller descriptions that enable targeted driver fuzzing. It has generated
descriptions for over 900 drivers, uncovering 40+ unique kernel bugs.

## Key Features


- **Static analysis of kernel driver source code**

- **Automated ioctl command extraction and argument type inference**

- **Device file path and permission analysis**

- **Semantic type inference for complex driver arguments**


## Technologies


- Static Program Analysis

- LLVM

- Syzkaller Integration

- Python / C++




[📄 Paper](http://zhyfeng.github.io/files/oakland23_syzdescribe.pdf) | [🐙 GitHub](https://github.com/seclab-ucr/SyzDescribe)
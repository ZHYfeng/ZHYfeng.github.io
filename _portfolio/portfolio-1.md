---
title: "Dependency: Demystifying the Dependency Challenge in Kernel Fuzzing"
excerpt: "A tool for understanding and addressing dependency challenges in kernel fuzzing, associated with ICSE 2022 paper."
collection: portfolio
---

## Overview

This project addresses the dependency challenge in kernel fuzzing, where much of the kernel code is locked under specific kernel states that current fuzzers struggle to explore. The artifact provides tools to systematically study dependencies in kernel fuzzing, including measurement studies and techniques to improve fuzzer effectiveness.

## Key Features

- **Dependency Analysis**: Identifies and categorizes dependencies in kernel code that hinder fuzzing.
- **Integration with Syzkaller**: Modified syzkaller for enhanced coverage collection and dependency tracking.
- **Static Analysis**: Components for analyzing kernel bitcode and assembly to detect unresolved conditions.
- **Reproducibility**: Complete setup for reproducing paper results, including virtual machine and evaluation data.

## Technologies Used

- **Languages**: Go (94.9%), C++, C, Python
- **Tools**: LLVM, Syzkaller, Protobuf, gRPC

## Links

- [GitHub Repository](https://github.com/ZHYfeng/Dependency)
- [Paper (ICSE 2022)](https://ieeexplore.ieee.org/document/9793967)
- [Artifact Evaluation](https://doi.org/10.5281/zenodo.6029158)

## Awards

- Google Research Paper Rewards

This project has garnered 24 stars on GitHub and contributes to advancing the field of operating system security through improved fuzzing techniques. 

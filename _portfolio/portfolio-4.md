---
title: "SyzSpec: Specification Generation for Linux Kernel Fuzzing via Under-Constrained Symbolic Execution"
excerpt: "A tool that uses under-constrained symbolic execution to automatically generate syscall specifications for improved Linux kernel fuzzing."
collection: portfolio
---

## Overview

SyzSpec leverages under-constrained symbolic execution to automatically generate precise syscall specifications for Linux kernel fuzzing. This addresses the limitations of manual specification writing, enabling more effective and comprehensive fuzzing of kernel interfaces.

## Key Features

- **Under-Constrained Symbolic Execution**: Uses symbolic execution with relaxed constraints to explore syscall behaviors.
- **Automatic Specification Generation**: Produces syzkaller-compatible syscall descriptions without manual effort.
- **Based on KLEE**: Extends the KLEE symbolic execution engine for kernel-specific analysis.
- **Kernel Fuzzing Enhancement**: Improves fuzzing coverage and effectiveness for Linux kernel drivers.

## Technologies Used

- **Languages**: C++ (77.4%), C (12.6%), Python, CMake, LLVM
- **Framework**: KLEE symbolic execution engine

## Links

- [GitHub Repository](https://github.com/seclab-ucr/SyzSpec)
- [Paper (CCS 2025)](https://www.cs.ucr.edu/~zhiyunq/pub/oakland23_syzdescribe.pdf) (Note: Link may need updating)
- [Slides](https://github.com/seclab-ucr/SyzSpec/blob/main/CCS25.pdf)

## Awards

- **Distinguished Paper Award** at ACM SIGSAC Conference on Computer and Communications Security (CCS) 2025

This project has garnered 11 stars on GitHub and represents cutting-edge work in automated specification generation for kernel security testing.
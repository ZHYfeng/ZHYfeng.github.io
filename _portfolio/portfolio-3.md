---
title: "SyzDescribe: Principled, Automated, Static Generation of Syscall Descriptions for Kernel Drivers"
excerpt: "A static analysis tool for automatically generating syscall descriptions for Linux kernel drivers, enabling better fuzzing coverage."
collection: portfolio
---

## Overview

SyzDescribe is a principled, automated tool that uses static analysis to generate syscall descriptions for Linux kernel drivers. This addresses the challenge of manually writing syscall descriptions for syzkaller, improving kernel fuzzing effectiveness by providing accurate and comprehensive descriptions.

## Key Features

- **Static Analysis**: Leverages LLVM bitcode and debug information to analyze kernel driver code.
- **Syscall Description Generation**: Automatically produces syzkaller-compatible syscall descriptions.
- **Kernel Support**: Supports multiple Linux kernel versions (v5.12, v6.1, v6.2).
- **Integration with Syzkaller**: Generated descriptions can be directly used in syzkaller for fuzzing.

## Technologies Used

- **Languages**: C++ (99.3%)
- **Tools**: LLVM/Clang 14, CMake

## Links

- [GitHub Repository](https://github.com/seclab-ucr/SyzDescribe)
- [Paper (S&P 2023)](https://www.computer.org/csdl/proceedings-article/sp/2023/933600d262/1Nrc0F2nDO0)
- [Generated Syscall Descriptions](https://github.com/ZHYfeng/SyzDescribe_Syscall_Description)

## Presentations

- Linux Security Summit North America 2023
- Qualcomm Product Security Summit 2023
- Symposium on the Science of Security (HoTSoS) 2024

This project has garnered 59 stars on GitHub and is actively used in kernel security research.
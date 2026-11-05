---
layout: home
permalink: /
author_profile: false
title: ""
redirect_from:
  - /about/
  - /about.html
name_en: Yu Hao
name_zh: 郝宇
kicker: Security researcher, HarmonyOS System Security Team, Huawei
lead: >-
  I work on operating-system security and program analysis for C/C++ systems,
  combining fuzzing, static analysis, symbolic execution and LLM-based reasoning
  to find and fix memory-safety bugs in real kernels: Linux, Android and HarmonyOS.
education: Ph.D., UC Riverside, 2024
toc:
  - { text: research, url: "#research" }
  - { text: publications, url: "#publications" }
  - { text: news, url: "#news" }
  - { text: cv.pdf, url: /files/cv.pdf }
# Venues shown on the homepage, in this order; conferences not listed are omitted.
venues: [S&P, CCS, USENIX Security, NDSS, ICSE, FSE, OOPSLA]
note: >-
  I am open to collaboration with researchers and industry partners in operating
  system security, and I am hiring interns and full-time researchers.
research:
  - title: Kernel fuzzing
    text: >-
      Specification generation for Linux kernel drivers, so fuzzers reach code that
      hand-written syscall descriptions never cover.
    more: SyzDescribe (S&P 23), SyzSpec (CCS 25)
    publication: syzspec-2025
  - title: LLMs for security
    text: >-
      E&V prompts an LLM to execute pseudo-code and verify its own result, locating
      the function to patch with over 80% accuracy on 170 Linux kernel crashes.
    more: E&V, LLift (OOPSLA 24)
    publication: ev-2023
  - title: Static analysis
    text: >-
      Precise and scalable detection of use-before-initialization bugs in the Linux
      kernel, with an LLM in the loop to cut false positives.
    more: UBITect (FSE 20), NDSS 22
    publication: llift-2024
  - title: Symbolic execution
    text: >-
      Under-constrained symbolic execution behind the kernel projects above, and
      accurate bisection of fuzzer-exposed vulnerabilities.
    more: SymBisect (USENIX Security 24)
    publication: symbisect-2024
selected:
  - syzspec-2025
  - symbisect-2024
  - llift-2024
  - ev-2023
  - syzdescribe-2023
  - dependency-2022
---

- **2025** Received the Distinguished Paper Award at CCS 2025 for "SyzSpec: Specification Generation for Linux Kernel Fuzzing via Under-Constrained Symbolic Execution".
- **2025** "SyzSpec" was accepted by CCS 2025.
- **2024** Received the Laxmi Bhuyan Fellowship Award from University of California, Riverside.

---
layout: archive
permalink: /publications/
author_profile: true
title: "Publications"
redirect_from:
  - /publications.html
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

<div class="pub-card" markdown="1">
[**NeuroMerge: ML-Guided State Merging for Efficient Symbolic Execution**](/publication/neuromerge-ml-guided-state-merging-for-efficient-symbolic-execution/)  
Shenghan Zhng, Shitong Zhu, **Yu Hao**, Xingyu Li, Keyu Man, Zhang Zheng, Qing Deng, Zhiyun Qian, Srikanth Krishnamurthy
*IEEE International Symposium on Software Reliability Engineering, ISSRE 26*


</div>

<div class="pub-card" markdown="1">
[**SyzSpec: Specification Generation for Linux Kernel Fuzzing via Under-Constrained Symbolic Execution**](/publication/syzspec-specification-generation-for-linux-kernel-fuzzing-via-under-constrained-/)  
**Yu Hao**, Juefei Pu, Xingyu Li, Zhiyun Qian, Ardalan Amiri Sani
*ACM SIGSAC Conference on Computer and Communications Security, CCS 25*
[PDF](http://zhyfeng.github.io/files/ccs25_syzspec.pdf) [Tool](https://github.com/seclab-ucr/SyzSpec)
**Distinguished Paper Award**

</div>

<div class="pub-card" markdown="1">
[**SCAD: Towards a Universal and Automated Network Side-Channel Vulnerability Detection**](/publication/scad-towards-a-universal-and-automated-network-side-channel-vulnerability-detect/)  
Keyu Man, Zhongjie Wang, **Yu Hao**, Shenghan Zheng, Xin'an Zhou, Yue Cao, Zhiyun Qian
*IEEE Symposium on Security and Privacy, S&P 25*
[PDF](http://zhyfeng.github.io/files/oakland25_side_channel_discovery.pdf) [Tool](https://github.com/seclab-ucr/SCAD)

</div>

<div class="pub-card" markdown="1">
[**SymBisect: Accurate Bisection for Fuzzer-Exposed Vulnerabilities**](/publication/symbisect-accurate-bisection-for-fuzzer-exposed-vulnerabilities/)  
Zheng Zhang, **Yu Hao**, Weiteng Chen, Xiaochen Zou, Xingyu Li, Haonan Li, Yizhuo Zhai, Zhiyun Qian, Billy Lau
*USENIX Security Symposium 2024*
[PDF](http://zhyfeng.github.io/files/sec24_symbisect.pdf) [Paper](https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-zheng) [Tool](https://github.com/seclab-ucr/SyzBridge)
**Linux Security Summit 25**

</div>

<div class="pub-card" markdown="1">
[**Enhancing Static Analysis for Practical Bug Detection: An LLM-Integrated Approach**](/publication/enhancing-static-analysis-for-practical-bug-detection-an-llm-integrated-approach/)  
Haonan Li, **Yu Hao**, Yizhuo Zhai, Zhiyun Qian
*ACM SIGPLAN International Conference on Object-Oriented Programming Systems, Languages, and Applications, OOPSLA 24*
[PDF](http://zhyfeng.github.io/files/oopsla24_llift.pdf) [Paper](https://dl.acm.org/doi/10.1145/3649828) [Tool](https://github.com/seclab-ucr/LLift)

</div>

<div class="pub-card" markdown="1">
[**SyzGen++: Dependency Inference for Augmenting Kernel Driver Fuzzing**](/publication/syzgen-dependency-inference-for-augmenting-kernel-driver-fuzzing/)  
Weiteng Chen, **Yu Hao**, Zheng Zhang, Xiaochen Zou, Dhilung Kirat, Shachee Mishra, Douglas Schales, Jiyong Jang, Zhiyun Qian
*IEEE Symposium on Security and Privacy, S&P 24*
[PDF](http://zhyfeng.github.io/files/oakland24_syzgenplusplus.pdf) [Paper](https://www.computer.org/csdl/proceedings-article/sp/2024/313000e661/1ZZvBxFudzi) [Tool](https://github.com/seclab-ucr/SyzGenPlusPlus)

</div>

<div class="pub-card" markdown="1">
[**SyzBridge: Bridging the Gap in Exploitability Assessment of Linux Kernel Bugs in the Linux Ecosystem**](/publication/syzbridge-bridging-the-gap-in-exploitability-assessment-of-linux-kernel-bugs-in-/)  
Xiaochen Zou, **Yu Hao**, Zheng Zhang, Juefei Pu, Weiteng Chen, Zhiyun Qian
*Network and Distributed System Security Symposium, NDSS 24*
[PDF](http://zhyfeng.github.io/files/ndss24_syzbridge.pdf) [Paper](https://www.ndss-symposium.org/ndss-paper/syzbridge-bridging-the-gap-in-exploitability-assessment-of-linux-kernel-bugs-in-the-linux-ecosystem/) [Tool](https://github.com/seclab-ucr/SyzBridge)

</div>

<div class="pub-card" markdown="1">
[**E&V: Prompting Large Language Models to Perform Static Analysis by Pseudo-code Execution and Verification**](/publication/ev-prompting-large-language-models-to-perform-static-analysis-by-pseudo-code-exe/)  
**Yu Hao**, Weiteng Chen, Ziqiao Zhou, Weidong Cui
[PDF](https://arxiv.org/abs/2312.08477)

</div>

<div class="pub-card" markdown="1">
[**Assisting Static Analysis with Large Language Models: A ChatGPT Experiment**](/publication/assisting-static-analysis-with-large-language-models-a-chatgpt-experiment/)  
Haonan Li, **Yu Hao**, Yizhuo Zhai, Zhiyun Qian
*The ACM International Conference on the Foundations of Software Engineering, Ideas, Visions and Reflections, FSE 23 IVR*
[PDF](https://arxiv.org/abs/2308.00245) [Paper](https://dl.acm.org/doi/10.1145/3611643.3613078) [Paper](https://dl.acm.org/doi/10.1145/3611643.3613078) [Tool](https://github.com/seclab-ucr/GPT-Expr)

</div>

<div class="pub-card" markdown="1">
[**SyzDescribe: Principled, Automated, Static Generation of Syscall Descriptions for Kernel Drivers**](/publication/syzdescribe-principled-automated-static-generation-of-syscall-descriptions-for-k/)  
**Yu Hao**, Guoren Li, Xiaochen Zou, Weiteng Chen, Shitong Zhu, Zhiyun Qian, Ardalan Amiri Sani
*IEEE Symposium on Security and Privacy, S&P 23*
[PDF](http://zhyfeng.github.io/files/oakland23_syzdescribe.pdf) [Paper](https://www.computer.org/csdl/proceedings-article/sp/2023/933600d262/1Nrc0F2nDO0) [Tool](https://github.com/seclab-ucr/SyzDescribe) [Result](https://github.com/ZHYfeng/SyzDescribe_Syscall_Description)

</div>

<div class="pub-card" markdown="1">
[**Demystifying the Dependency Challenge in Kernel Fuzzing**](/publication/demystifying-the-dependency-challenge-in-kernel-fuzzing/)  
**Yu Hao**, Hang Zhang, Guoren Li, Xingyun Du, Zhiyun Qian, Ardalan Amiri Sani
*IEEE/ACM International Conference on Software Engineering, ICSE 22*
[PDF](http://zhyfeng.github.io/files/icse22_dependency_measurement.pdf) [Paper](https://ieeexplore.ieee.org/document/9793967) [Paper](https://dl.acm.org/doi/abs/10.1145/3510003.3510126) [Tool](https://github.com/seclab-ucr/Dependency)
**Google Research Paper Rewards**

</div>

<div class="pub-card" markdown="1">
[**Progressive Scrutiny: Incremental Detection of UBI bugs in the Linux Kernel**](/publication/progressive-scrutiny-incremental-detection-of-ubi-bugs-in-the-linux-kernel/)  
Yizhuo Zhai, **Yu Hao**, Zheng Zhang, Weiteng Chen, Guoren Li, Zhiyun Qian, Chengyu Song, Manu Sridharan, Srikanth V. Krishnamurthy, Trent Jaeger, Paul Yu
*Network and Distributed System Security Symposium, NDSS 22*
[PDF](http://zhyfeng.github.io/files/ndss22_incremental_analysis.pdf) [Paper](https://www.ndss-symposium.org/ndss-paper/auto-draft-249/) [Tool](https://github.com/seclab-ucr/IncreLux)
**2023 Cyber Security CRA Capstone Poster**

</div>

<div class="pub-card" markdown="1">
[**Eluding ML-based Adblockers With Actionable Adversarial Examples**](/publication/eluding-ml-based-adblockers-with-actionable-adversarial-examples/)  
Shitong Zhu, Zhongjie Wang, Xun Chen, Shasha Li, Keyu Man, Umar Iqbal, Zhiyun Qian, Kevin S Chan, Srikanth V Krishnamurthy, Zubair Shafiq, **Yu Hao**, Guoren Li, Zheng Zhang, Xiaochen Zou
*Annual Computer Security Applications Conference, ACSAC 21*
[PDF](http://zhyfeng.github.io/files/acsac21_adblock_AML.pdf) [Paper](https://dl.acm.org/doi/10.1145/3485832.3488008) [Tool](https://github.com/seclab-ucr/A4)

</div>

<div class="pub-card" markdown="1">
[**Themis: Ambiguity-Aware Network Intrusion Detection based on Symbolic Model Comparison**](/publication/themis-ambiguity-aware-network-intrusion-detection-based-on-symbolic-model-compa/)  
Zhongjie Wang, Shitong Zhu, Keyu Man, Pengxiong Zhu, **Yu Hao**, Zhiyun Qian, Srikanth V. Krishnamurthy, Tom La Porta, Michael J. De Lucia
*ACM SIGSAC Conference on Computer and Communications Security, CCS 21*
[PDF](http://zhyfeng.github.io/files/ccs21_themis.pdf) [Paper](https://dl.acm.org/doi/10.1145/3460120.3484762) [Tool](https://github.com/seclab-ucr/Themis)

</div>

<div class="pub-card" markdown="1">
[**Statically Discovering High-Order Taint Style Vulnerabilities in OS Kernels**](/publication/statically-discovering-high-order-taint-style-vulnerabilities-in-os-kernels/)  
Hang Zhang, Weiteng Chen, **Yu Hao**, Guoren Li, Yizhuo Zhai, Xiaochen Zou, Zhiyun Qian
*ACM SIGSAC Conference on Computer and Communications Security, CCS 21*
[PDF](http://zhyfeng.github.io/files/ccs21_static_high_order.pdf) [Paper](https://dl.acm.org/doi/abs/10.1145/3460120.3484798) [Tool](https://github.com/seclab-ucr/SUTURE)

</div>

<div class="pub-card" markdown="1">
[**UBITect: A Precise and Scalable Method to Detect Use-before-Initialization Bugs in Linux Kernel**](/publication/ubitect-a-precise-and-scalable-method-to-detect-use-before-initialization-bugs-i/)  
Yizhuo Zhai, **Yu Hao**, Hang Zhang, Daimeng Wang, Chengyu Song, Zhiyun Qian, Mohsen Lesani, Srikanth V. Krishnamurthy, Paul Yu
*ACM SIGSOFT International Symposium on Foundations of Software Engineering, FSE 20*
[PDF](http://zhyfeng.github.io/files/fse20_UBITect.pdf) [Paper](https://dl.acm.org/doi/10.1145/3368089.3409686) [Tool](https://github.com/seclab-ucr/UBITect)
**2023 Cyber Security CRA Capstone Poster**

</div>

<div class="pub-card" markdown="1">
[**ConcSpectre: Be Aware of Forthcoming Malware Hidden in Concurrent Programs**](/publication/concspectre-be-aware-of-forthcoming-malware-hidden-in-concurrent-programs/)  
Yang Liu, Ming Fan, Ting Liu, **Yu Hao**, Zisen Xu, Kai Chen, Hao Chen, and Yan Cai
*IEEE Transactions on Reliability*
 [Paper](https://ieeexplore.ieee.org/document/9761977) [Code](https://github.com/ZHYfeng/Malicious_Code_Conceal) [Result](https://github.com/XJTU-ConcSpectre/CLB)

</div>

<div class="pub-card" markdown="1">
[**ConcSpectre: Be Aware of Forthcoming Malware Hidden in Concurrent Programs**](/publication/concspectre-be-aware-of-forthcoming-malware-hidden-in-concurrent-programs/)  
Yang Liu, Ming Fan, Ting Liu, **Yu Hao**, Zisen Xu, Kai Chen, Hao Chen, and Yan Cai
*IEEE International Conference on Software Quality, Reliability, and Security, QRS 21*
 [Code](https://github.com/ZHYfeng/Malicious_Code_Conceal) [Result](https://github.com/XJTU-ConcSpectre/CLB)
**Best Paper Award**

</div>

<div class="pub-card" markdown="1">
[**Tell You a Definite Answer: Whether Your Data is Tainted During Thread Scheduling**](/publication/tell-you-a-definite-answer-whether-your-data-is-tainted-during-thread-scheduling/)  
Xiaodong Zhang, Zijiang Yang, Qinghua Zheng, **Yu Hao**, Pei Liu, Ting Liu
*IEEE Transactions on Software Engineering, TSE*
 [Paper](https://ieeexplore.ieee.org/document/8472790) [Tool](https://github.com/ZHYfeng/Cap_Taint_Analysis) [Benchmarks](https://github.com/ZHYfeng/Cap_Benchmarks) [Result](https://github.com/ZHYfeng/Cap_Taint_Analysis_Results)

</div>

<div class="pub-card" markdown="1">
[**Debugging Multithreaded Programs as if They Were Sequential**](/publication/debugging-multithreaded-programs-as-if-they-were-sequential/)  
Xiaodong Zhang, Zijiang Yang, Qinghua Zheng, **Yu Hao**, Pei Liu, Lechen Yu, Ting Liu
*IEEE Access*
 [Paper](https://ieeexplore.ieee.org/document/8357815) [Tool](https://github.com/ZHYfeng/Cap_6)

</div>

<div class="pub-card" markdown="1">
[**Automated Testing of Definition-Use Data Flow for Multithreaded Programs**](/publication/automated-testing-of-definition-use-data-flow-for-multithreaded-programs/)  
Xiaodong Zhang, Zijiang Yang, Qinghua Zheng, Pei Liu, Jialiang Chang, **Yu Hao**, Ting Liu
*IEEE International Conference on Software Testing, Verification and Validation, ICST 17*
 [Paper](https://ieeexplore.ieee.org/document/7927973) [Tool](https://github.com/xjtuSoftware/datarace)

</div>

<div class="pub-card" markdown="1">
[**Debugging Multithreaded Programs as if They Were Sequential**](/publication/debugging-multithreaded-programs-as-if-they-were-sequential/)  
Xiaodong Zhang, Zijiang Yang, Qinghua Zheng, **Yu Hao**, Pei Liu, Lechen Yu, Ming Fan, Ting Liu
*IEEE International Conference on Software Analysis, Testing and Evolution, SATE 16*
 [Paper](https://ieeexplore.ieee.org/document/7780198) [Tool](https://github.com/ZHYfeng/Cap_3)

</div>

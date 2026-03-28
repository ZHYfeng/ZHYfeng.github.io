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

**SyzSpec: Specification Generation for Linux Kernel Fuzzing via Under-Constrained Symbolic Execution**  
**Yu Hao**, Juefei Pu, Xingyu Li, Zhiyun Qian, Ardalan Amiri Sani  
*ACM SIGSAC Conference on Computer and Communications Security, CCS 25.*  
**[Distinguished Paper Award]**  

**SCAD: Towards a Universal and Automated Network Side-Channel Vulnerability Detection**  
Keyu Man, Zhongjie Wang, **Yu Hao**, Shenghan Zheng, Xin'an Zhou, Yue Cao, Zhiyun Qian  
*IEEE Symposium on Security and Privacy, S&P 25.*  

**SymBisect: Accurate Bisection for Fuzzer-Exposed Vulnerabilities**  
Zheng Zhang, **Yu Hao**, Weiteng Chen, Xiaochen Zou, Xingyu Li, Haonan Li, Yizhuo Zhai, Zhiyun Qian, Billy Lau  
*USENIX Security Symposium 2024.*  
[Paper](https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-zheng)  

**Enhancing Static Analysis for Practical Bug Detection: An LLM-Integrated Approach**  
Haonan Li, **Yu Hao**, Yizhuo Zhai, Zhiyun Qian  
*ACM SIGPLAN International Conference on Object-Oriented Programming Systems, Languages, and Applications, OOPSLA 24.*  
[PDF](http://zhyfeng.github.io/files/2024-OOPSLA.pdf) [Paper](https://dl.acm.org/doi/10.1145/3649828) [Tool](https://github.com/seclab-ucr/LLift)  

**SyzGen++: Dependency Inference for Augmenting Kernel Driver Fuzzing**  
Weiteng Chen, **Yu Hao**, Zheng Zhang, Xiaochen Zou, Dhilung Kirat, Shachee Mishra, Douglas Schales, Jiyong Jang, Zhiyun Qian  
*IEEE Symposium on Security and Privacy, S&P 24.*  
[PDF](http://zhyfeng.github.io/files/2024-IEEE-SP-SyzGen++.pdf) [Paper](https://www.computer.org/csdl/proceedings-article/sp/2024/313000e661/1ZZvBxFudzi) [Tool](https://github.com/seclab-ucr/SyzGenPlusPlus)  

**SyzBridge: Bridging the Gap in Exploitability Assessment of Linux Kernel Bugs in the Linux Ecosystem**  
Xiaochen Zou, **Yu Hao**, Zheng Zhang, Juefei Pu, Weiteng Chen, Zhiyun Qian  
*Network and Distributed System Security Symposium, NDSS 24.*  
[PDF](http://zhyfeng.github.io/files/2024-NDSS-SyzBridge.pdf) [Paper](https://www.ndss-symposium.org/ndss-paper/syzbridge-bridging-the-gap-in-exploitability-assessment-of-linux-kernel-bugs-in-the-linux-ecosystem/) [Tool](https://github.com/seclab-ucr/SyzBridge)  

**E&V: Prompting Large Language Models to Perform Static Analysis by Pseudo-code Execution and Verification**  
**Yu Hao**, Weiteng Chen, Ziqiao Zhou, Weidong Cui  
[arXiv](https://arxiv.org/abs/2312.08477)  
**[AGI Leap Summit 2024]** **[Symposium on the Science of Security 24]**  

**Assisting Static Analysis with Large Language Models: A ChatGPT Experiment**  
Haonan Li, **Yu Hao**, Yizhuo Zhai, Zhiyun Qian  
*The ACM International Conference on the Foundations of Software Engineering, Ideas, Visions and Reflections, FSE 23 IVR*  
[PDF](http://zhyfeng.github.io/files/2023-FSE-IVR.pdf) [Paper](https://dl.acm.org/doi/10.1145/3611643.3613078) [Tool](https://github.com/seclab-ucr/GPT-Expr) [arXiv](https://arxiv.org/abs/2308.00245)  

**SyzDescribe: Principled, Automated, Static Generation of Syscall Descriptions for Kernel Drivers**  
**Yu Hao**, Guoren Li, Xiaochen Zou, Weiteng Chen, Shitong Zhu, Zhiyun Qian, Ardalan Amiri Sani  
*IEEE Symposium on Security and Privacy, S&P 23.*  
[PDF](http://zhyfeng.github.io/files/2023-IEEE-SP.pdf) [Paper](https://www.computer.org/csdl/proceedings-article/sp/2023/933600d262/1Nrc0F2nDO0) [Tool](https://github.com/seclab-ucr/SyzDescribe) [Result](https://github.com/ZHYfeng/SyzDescribe_Syscall_Description)  
**[Linux Security Summit 23]** **[Qualcomm Product Security Summit 23]** **[Symposium on the Science of Security 24]**  

**Demystifying the Dependency Challenge in Kernel Fuzzing**  
**Yu Hao**, Hang Zhang, Guoren Li, Xingyun Du, Zhiyun Qian, Ardalan Amiri Sani  
*IEEE/ACM International Conference on Software Engineering, ICSE 22.*  
[PDF](http://zhyfeng.github.io/files/2022-ICSE.pdf) [Paper](https://ieeexplore.ieee.org/document/9793967) [Paper](https://dl.acm.org/doi/abs/10.1145/3510003.3510126) [Tool](https://github.com/seclab-ucr/Dependency) [Result](https://www.doi.org/10.5281/zenodo.5441138)  
**[Google Research Paper Rewards]**  

**Progressive Scrutiny: Incremental Detection of UBI bugs in the Linux Kernel**  
Yizhuo Zhai, **Yu Hao**, Zheng Zhang, Weiteng Chen, Guoren Li, Zhiyun Qian, Chengyu Song, Manu Sridharan, Srikanth V. Krishnamurthy, Trent Jaeger, Paul Yu  
*Network and Distributed System Security Symposium, NDSS 22.*  
[PDF](http://zhyfeng.github.io/files/2022-NDSS.pdf) [Paper](https://www.ndss-symposium.org/ndss-paper/auto-draft-249/) [Tool](https://github.com/seclab-ucr/IncreLux)  
[2023 Cyber Security CRA Capstone Poster]  

**Eluding ML-based Adblockers With Actionable Adversarial Examples**  
Shitong Zhu, Zhongjie Wang, Xun Chen, Shasha Li, Keyu Man, Umar Iqbal, Zhiyun Qian, Kevin S Chan, Srikanth V Krishnamurthy, Zubair Shafiq, **Yu Hao**, Guoren Li, Zheng Zhang, Xiaochen Zou  
*Annual Computer Security Applications Conference, ACSAC 21.*  
[PDF](http://zhyfeng.github.io/files/2022-ACSCA.pdf) [Paper](https://dl.acm.org/doi/10.1145/3485832.3488008) [Tool](https://github.com/seclab-ucr/A4)  

**Themis: Ambiguity-Aware Network Intrusion Detection based on Symbolic Model Comparison**  
Zhongjie Wang, Shitong Zhu, Keyu Man, Pengxiong Zhu, **Yu Hao**, Zhiyun Qian, Srikanth V. Krishnamurthy, Tom La Porta, Michael J. De Lucia  
*ACM SIGSAC Conference on Computer and Communications Security, CCS 21.*  
[PDF](http://zhyfeng.github.io/files/2021-CCS-Themis.pdf) [Paper](https://dl.acm.org/doi/10.1145/3460120.3484762) [Tool](https://github.com/seclab-ucr/Themis)  

**Statically Discovering High-Order Taint Style Vulnerabilities in OS Kernels**  
Hang Zhang, Weiteng Chen, **Yu Hao**, Guoren Li, Yizhuo Zhai, Xiaochen Zou, Zhiyun Qian  
*ACM SIGSAC Conference on Computer and Communications Security, CCS 21.*  
[PDF](http://zhyfeng.github.io/files/2021-CCS-Statically.pdf) [Paper](https://dl.acm.org/doi/abs/10.1145/3460120.3484798) [Tool](https://github.com/seclab-ucr/SUTURE)  

**UBITect: A Precise and Scalable Method to Detect Use-before-Initialization Bugs in Linux Kernel**  
Yizhuo Zhai, **Yu Hao**, Hang Zhang, Daimeng Wang, Chengyu Song, Zhiyun Qian, Mohsen Lesani, Srikanth V. Krishnamurthy, Paul Yu  
*ACM SIGSOFT International Symposium on Foundations of Software Engineering, FSE 20.*  
[PDF](http://zhyfeng.github.io/files/2020-FSE.pdf) [Paper](https://dl.acm.org/doi/10.1145/3368089.3409686) [Tool](https://github.com/seclab-ucr/UBITect)  
[2023 Cyber Security CRA Capstone Poster]  

**ConcSpectre: Be Aware of Forthcoming Malware Hidden in Concurrent Programs**  
Yang Liu, Ming Fan, Ting Liu, **Yu Hao**, Zisen Xu, Kai Chen, Hao Chen, and Yan Cai  
*IEEE Transactions on Reliability*  
[Paper](https://ieeexplore.ieee.org/document/9761977) [Code](https://github.com/ZHYfeng/Malicious_Code_Conceal) [Result](https://github.com/XJTU-ConcSpectre/CLB)  

**ConcSpectre: Be Aware of Forthcoming Malware Hidden in Concurrent Programs**  
Yang Liu, Ming Fan, Ting Liu, **Yu Hao**, Zisen Xu, Kai Chen, Hao Chen, and Yan Cai  
*IEEE International Conference on Software Quality, Reliability, and Security, QRS 21.*  
[PDF](http://zhyfeng.github.io/files/2021-QRS.pdf) [Code](https://github.com/ZHYfeng/Malicious_Code_Conceal) [Result](https://github.com/XJTU-ConcSpectre/CLB)  
**[Best Paper Award]**  

**Tell You a Definite Answer: Whether Your Data is Tainted During Thread Scheduling**  
Xiaodong Zhang, Zijiang Yang, Qinghua Zheng, **Yu Hao**, Pei Liu, Ting Liu  
*IEEE Transactions on Software Engineering, **TSE***  
[Paper](https://ieeexplore.ieee.org/document/8472790) [Tool](https://github.com/ZHYfeng/Cap_Taint_Analysis) [Benchmarks](https://github.com/ZHYfeng/Cap_Benchmarks) [Result](https://github.com/ZHYfeng/Cap_Taint_Analysis_Results)  
[S&P 17 Poster](https://www.ieee-security.org/TC/SP2017/poster-abstracts/IEEE-SP17_Posters_paper_8.pdf)  
Patent: [PCT](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2017181628) [CN](https://patentscope.wipo.int/search/en/detail.jsf?docId=CN178124948)  

**Debugging Multithreaded Programs as if They Were Sequential**  
Xiaodong Zhang, Zijiang Yang, Qinghua Zheng, **Yu Hao**, Pei Liu, Lechen Yu, Ting Liu  
*IEEE Access*  
[Paper](https://ieeexplore.ieee.org/document/8357815) [Tool](https://github.com/ZHYfeng/Cap_6)  

**Automated Testing of Definition-Use Data Flow for Multithreaded Programs**  
Xiaodong Zhang, Zijiang Yang, Qinghua Zheng, Pei Liu, Jialiang Chang, **Yu Hao**, Ting Liu  
*IEEE International Conference on Software Testing, Verification and Validation, ICST 17.*  
[PDF](http://zhyfeng.github.io/files/2017-ICST.pdf) [Paper](https://ieeexplore.ieee.org/document/7927973) [Tool](https://github.com/xjtuSoftware/datarace)  

**Debugging Multithreaded Programs as if They Were Sequential**  
Xiaodong Zhang, Zijiang Yang, Qinghua Zheng, **Yu Hao**, Pei Liu, Lechen Yu, Ming Fan, Ting Liu  
*IEEE International Conference on Software Analysis, Testing and Evolution, SATE 16.*  
[Paper](https://ieeexplore.ieee.org/document/7780198) [Tool](https://github.com/ZHYfeng/Cap_3)  

<!-- New style rendering if publication categories are defined -->
<!-- {% if site.publication_category %}
  {% for category in site.publication_category  %}
    {% assign title_shown = false %}
    {% for post in site.publications reversed %}
      {% if post.category != category[0] %}
        {% continue %}
      {% endif %}
      {% unless title_shown %}
        <h2>{{ category[1].title }}</h2><hr />
        {% assign title_shown = true %}
      {% endunless %}
      {% include archive-single.html %}
    {% endfor %}
  {% endfor %}
{% else %}
  {% for post in site.publications reversed %}
    {% include archive-single.html %}
  {% endfor %}
{% endif %} -->




---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}



<!-- ## Summary

| International Journal | International Conference | Domain Journal | Domain Conference |
|:---------------------:|:------------------------:|:--------------:|:-----------------:|
|           4           |             3            |        1       |         9         | -->


<!-- ## International Journals
---
* [**Youngwoo Oh**](#) and Wooyeol Choi, “Federated Multi-Agent Reinforcement Learning-based Joint Antenna Selection and Power Allocation for Cell-free Massive MIMO",.

* [**Youngwoo Oh**](#), Islam Helmy, and Wooyeol Choi, “Joint Channel Estimation and Automatic Modulation Classification for Massive MIMO via Deep Learning",.

* [**Youngwoo Oh**](#) and Wooyeol Choi, “Multi-Objective Deep Reinforcement Learning-based Power Allocation Method for Tradeoff Optimization in Massive MIMO Systems",.

* Yonggang Kim, Gyungmin Kim, [**Youngwoo Oh**](#), and Wooyeol Choi, "Transmission Delay-Based Uplink Multi-User Scheduling in IEEE 802.11ax Networks", *Applied Sciences*, vol. 11, no. 19, article no. 9196, October. 2021. (IF: 2.679 / JCR 2020)


## International Conferences
---
* [**Youngwoo Oh**](#), Islam Helmy, and Wooyeol Choi, “Capsule Neural Network-based Joint Channel Estimation and Automatic Modulation Classification for Massive MIMO Systems”, *2023 IEEE International Conference on Computer Communications*, Newyork, USA, Mar. 17-20, 2023.

* [**Youngwoo Oh**](#) and Wooyeol Choi, “Real Time Localization System based on Deep Reinforcement Learning for Livestock Tracking”, *2023 IEEE International Conference on Computer Communications*, Newyork, USA, Mar. 17-20, 2023.

* [**Youngwoo Oh**](#) and Wooyeol Choi, "Deep Reinforcement Learning-Based Power Allocation in Multi-Cell Massive MIMO",  *International Conference on Maritime IT Convergence*, Jeju, Republic of Korea, Sep. 22-23, 2022.


## Domain Journals
---
* **오영우**, 최우열, "심볼 간 간섭 보상을 위한 적응형 등화기 및 TDMA 기반 다중 홉 릴레이 네트워크 설계 및 구현", *한국통신학회지*, vol. 46, no. 6, 2021.06.06.



## Domain Conferences
---
* **오영우**, 김범수, 최우열, “의료-ICT 융합 헬스케어 기반 모바일 애플리케이션 설계 및 구현”,.


* **오영우**, 한혜주, 박민수, 전광명, 임채준, 최우열, “Internet of Things(IoT) 기반 실시간 실내 위치 추정 시스템 설계 및 구현”,.


* **오영우**, 최우열, "MIMO 시스템을 위한 Actor-Critic 심층강화학습 기반 안테나 선택 기법", *한국통신학회 하계종합학술대회*, 2022.06.22 - 24.


* **오영우**, 최우열, "합성곱 신경망을 이용한 자동 변조 분류 기법 설계와 성능 분석", *한국통신학회 인공지능학술대회*, 2021.09.29 - 10.01.


* 전광명, 류인철, 김누리, 임채준, **오영우**, 전찬준, 최우열, "스마트글라스 및 경량 OCR 기반 축산동물 귀표 식별 시스템", *한국통신학회 인공지능학술대회*, 2021.09.29 - 10.01.


* **오영우**, 김동민, 최우열, "Rayleigh Fading 환경에서 LMS 기반 적응형 등화를 이용한 M-QAM/OFDM 시스템의 성능 분석", *한국전자파학회 하계종합학술대회*, 2021.08.18 - 21.


* **오영우**, 최우열, "시분할 다중접속 기반 다중 홉 릴레이 네트워크 구현 및 성능 분석 ", *한국통신학회 추계학술대회*, 2020.11.13. (최우수 논문)​​


* **오영우**, 김준수, 박시웅, 최우열, "소프트웨어 정의 라디오 테스트베드 기반 다중 홉 릴레이 네트워크 설계", *대한전자공학회 하계학술대회*, 2020.08.19 - 21.​


* **오영우**, 최우열, "소프트웨어 정의 라디오 테스트베드 기반 노이즈 필터 성능 분석", *한국스마트미디어학회 춘계학술대회*, 2020.05.22 - 23. -->
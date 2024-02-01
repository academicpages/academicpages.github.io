---
title: "Cryptography on Hardware-based Platforms"
collection: courses
type: "Undergraduate / Graduate Course"
permalink: /courses/cryptography-hardware
venue: "Ruhr University Bochum"
date: 2022-10-01
location: "Bochum, Germany"
---

* Lecturer: Prof. Dr. Güneysu
* Language: German
* Credits: 5 CP
* Programs: B.Sc. IT-Security, M.Sc. Computer Science
* Examination: 100 % Written Exam (120 Minutes) + 10 % Homework

Learning Outcomes
=====

Students are familiar with the concepts of practical hardware development with abstract hardware description languages (VHDL) and the simulation of hardware circuits on FPGAs. They master standard techniques of hardware-related processor development and are familiar with the implementation of symmetric and asymmetric cryptosystems on modern FPGA systems.

Course Description
======

Due to their complexity, cryptographic systems place high demands on small processors and embedded systems in particular.
In combination with the demand for high data throughput at the lowest hardware costs, fundamental problems arise here for the developer, which are to be illuminated in this lecture.
The lecture deals with the most interesting aspects of how to implement current cryptographic methods on practical hardware systems.
Cryptosystems such as the block cipher AES, the hash functions SHA-1 as well as asymmetric systems RSA and ECC are dealt with.
Furthermore, special hardware requirements such as the generation of true randomness (TRNG) and the use of Physically Unclonable Functions (PUF) are discussed.
The efficient implementation of these cryptosystems, especially with regard to optimization for high speed, is discussed on modern FPGAs and implemented in practical exercises using the hardware description language VHDL.


Contents
======

1. Introduction
2. Logical Functions and Introduction to HDL
3. Register Transfer Level & VHDL
4. Finite State Machines & Circuit Synthesis
5. Programmable Logic Devices
6. Cryptographic Hardware Implementations
7. AES Implementation
8. Side-Channel Analysis and Protections
9. Hash Function Implementation
10. Modular Arithmetic Implementation
11. Modular Arithmetic & RSA/ECC Implementation
12. Post-Quantum Cryptography
13. Physical Unclonable Functions
14. True Random Number Generation

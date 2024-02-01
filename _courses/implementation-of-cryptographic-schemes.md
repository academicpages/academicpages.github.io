---
title: "Implementation of Cryptographic Schemes"
collection: courses
type: "Undergraduate Course"
permalink: /courses/implementation-of-cryptographic-schemes
venue: "Ruhr University Bochum"
date: 2020-10-01
location: "Bochum, Germany"
---

* Lecturer: Dr.-Ing. Schellenberg
* Language: German
* Credits: 5 CP
* Programs: B.Sc. IT-Security, M.Sc. IT-Security / Networks and Systems
* Examination: 70 % Written Exam (120 Minutes) + 30 % Programming Projects

Prior Knowledge
=====

* Basic Knowledge of Programming Languages C or C++
* Introduction to Cryptography

Learning Outcomes
=====

Students learn the basic algorithms for the efficient implementation of computationally intensive crypto procedures. 
In particular, they will have understood the handling of algorithms with very long operands after the module, as well as the interplay between implementation methods and cryptographic security.

Course Description
======

This lecture gives an introduction to methods for fast and secure implementation of cryptographic algorithms.
In the first part, methods for efficient exponentiation are discussed in detail, since these are of great importance for all widespread asymmetric methods.
Special acceleration methods are also presented for the widely used RSA algorithm.

In the second part, algorithms for efficient long-number arithmetic are developed.
First, basic methods for representing long numbers in computers and procedures for addition are presented.
The focus of this part is on algorithms for efficient modular multiplication.
In addition to the Karatsuba algorithm, Montgomery multiplication is discussed.

In the third part, secure implementation is discussed.
There is an introduction to active and passive side-channel attacks.
Active attacks against block ciphers and RSA are presented.
As important representatives of passive attacks, the basics of SPA (simple power analysis) and DPA (differential power analysis) are introduced.

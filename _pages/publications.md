---
layout: archive-search
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<html>
<head>
<script>
   const url="http://api.weatherapi.com/v1/current.json?key=47a53ef1aeff4b29ba811204220210%q=London&aqui=no"
 async function makeAPICALL(){
  const result = await fetch(url)
  result.json().then(data=>{
    console.log(data)
  })
 }
 makeAPICALL()
</script>
<h1>HEY</h1>
</head>
<body>
<div id="result">HELLO TEST</div>
<ol reversed="">
<li>Rudi Eigenmann and Barry Schneider, “The National Strategic Computing
  Initiative - Guest Editor's Introduction,” <em>Computing in Science &amp;
    Engineering,</em> vol:20, no:5, Sep/Oct 2018, pages 5-7.

<p>
</p></li>
<li>Aurangzeb and Rudolf Eigenmann, “AutoHiPA: An Automated System for Function
Approximation,” <em>WAPCO: 4th Workshop on Approximate Computing</em>, January
2018.

<p>
</p></li>
<li>Putt Sakdhnagool, Amit Sabne and Rudolf Eigenmann, “Comparative analysis
  of coprocessors,” <em>Concurrency Computation; Practice and Experience</em>,
  September 2018; e4756. https://doi.org/10.1002/cpe.4756

<p>
</p></li>
<li>Tsung Tai Yeh, Amit Sabne, Putt Sakdhnagool, Rudolf Eigenmann, and Timothy
  G. Rogers. 2018. “Pagoda: A GPU Runtime System For Narrow Tasks,” <em>ACM
    Transactions on Parallel Computing</em> 9, 4, Article 39, December 2018, 22
  pages.

<p>
</p></li>
<li>Tsung Tai Yeh and Amit Sabne and Putt Sakdhnagool and Rudolf Eigenmann and
Timothy G. Rogers, “Pagoda: Fine-Grained GPU Resource Virtualization for
Narrow Tasks”, <em>PPoPP '17: Proceedings of the ACM SIGPLAN symposium on
  Principles and practice of parallel programming</em>, nominated for best paper,
2017.

<p>
</p></li>
<li>Aurangzeb and Rudolf Eigenmann, “PROCsimate: A Scheme for Approximating
Procedures with Dynamic Quality Monitoring and Result Guarantees,” 3rd
Workshop On Approximate Computing (WAPCO 2017), Stockholm, Sweden, 2017.

<p>
</p></li>
<li>Aurangzeb and Rudolf Eigenmann, “History-based Piecewise Approximation Scheme
for Procedures”, <em>2nd Workshop on Approximate Computing,</em> Prague, Czech
Republic, 2016.

<p>
</p></li>
<li>Tsung Tai Yeh and Amit Sabne and Putt Sakdhnagool and Rudolf Eigenmann and
Timothy G Rogers, “A Runtime System to Maximize GPU Utilization in Data
Parallel Tasks with Limited Parallelism”, <em>Proceedings of the 2016
  International Conference on Parallel Architectures and Compilation</em>, Poster,
pages 449-450, 2016.

<p>
</p></li>
<li>Aurangzeb and Rudolf Eigenmann, “DOT APPROX: Making a Case for Dynamic Online
Training for Function Approximation Techniques”, <em>Workshop on Approximate
  Computing Across the Stack (WAX),</em> Atlanta, GA, USA, 2016.

<p>
</p></li>
<li>Aurangzeb and Rudolf Eigenmann, “Harnessing Parallelism in Multicore Systems
to Expedite and Improve Function Approximation,” <em>29th International
  Workshop on Languages and Compilers for Parallel Computing (LCPC)</em>,
Rochester, NY, USA, 2016.

<p>
</p></li>
<li>Amit Sabne and Putt Sakdhnagool and Rudolf Eigenmann, “Formalizing Structured
Control Flow Graphs,” <em>29th International Workshop on Languages and
  Compilers for Parallel Computing (LCPC)</em>, Rochester, NY, USA, 2016.

<p>
</p></li>
<li>Dheya Mustafa and Rudolf Eigenmann, “PETRA: Performance Evaluation Tool for
Modern Parallelizing Compilers,” <em>International Journal of Parallel
  Programming</em>, 43, no. 4 (2015): 549-571.

<p>
</p></li>
<li>Amit Sabne, Putt Sakdhnagool and Rudolf Eigenmann,
“HeteroDoop : A MapReduce Programming System for Accelerator Clusters,”
<em>International ACM Symposium on High-Performance and Distributed
  Computing</em>, June 2015, pages 235-246.

<p>
</p></li>
<li>Putt Sakdhnagool, Amit Sabne and Rudolf Eigenmann,
“HYDRA : Extending Shared Address Programming For Accelerator Clusters,”
 <em>LCPC '15: Proceedings of the International Workshop on Languages
    and Compilers for Parallel Computing</em>, 2015.

<p>
</p></li>
<li>Tanzima Zerin Islam, Saurabh Bagchi and Rudolf Eigenmann, “Reliable and
Efficient Distributed Checkpointing System for Grid Environments,” <em>  Journal of Grid Computing</em>, 12.4 (2014): 593-613.

<p>
</p></li>
<li>Fahed Jubair, Okwan Kwon, Rudolf Eigenmann, and Samuel Midkiff, “PI
Abstraction: Parallelism-Aware Array Data Flow Analysis for OpenMP,” In <em>  Languages and Compilers for Parallel Computing</em>, pages 253-267, Springer
International Publishing, 2014.

<p>
</p></li>
<li>Amit Sabne, Putt Sakdhnagool and Rudolf Eigenmann,
  “Scaling large-data computations on multi-GPU accelerators,”
  <em>Proceedings of the 27th international ACM conference on International
    conference on supercomputing</em>, ACM, 2013,  pages 443-454.

<p>
</p></li>
<li>Hao Lin, Hansang Bae, Samuel P. Midkiff, Rudolf Eigenmann, and Soohong P. Kim,
“A Study of the Usefulness of Producer/Consumer Synchronization,” In <em>  Languages and Compilers for Parallel Computing</em>, pages 141-155, Springer
Berlin Heidelberg, 2013.

<p>
</p></li>
<li>JoAnn Browning, Santiago Pujol, Rudolf Eigenmann, and Julio A. Ramirez,
  “NEEShub Databases - Quick access to concrete data”, CI - Concrete
  International, April 2013, page 55.

<p>
</p></li>
<li>Seyong Lee and Rudolf Eigenmann, “OpenMPC: Extended OpenMP for Efficient
  Programming and Tuning on GPUs,” <em>International Journal of
  Computational Science and Engineering</em>, 2012.

<p>
</p></li>
<li>Hansang Bae, Dheya Mustafa, Jae-Woo Lee, Aurangzeb, Hao Lin, Chirag Dave,
  Rudolf Eigenmann and Samuel P. Midkiff, “The Cetus Source-to-Source Compiler
  Infrastructure: Overview and Evaluation”, <em>International Journal of
    Parallel Programming</em>, 2012.

<p>
</p></li>
<li>Thomas Hacker, Rudolf Eigenmann, and Ellen Rathje, “Advancing Earthquake
  Engineering Research Through Cyberinfrastructure,” Journal of Structural
  Engineering, December 2012.

<p>
</p></li>
<li>Okwan Kwon, Fahed Jubair, Rudolf Eigenmann and Samuel Midkiff, “A Hybrid
  Approach of OpenMP for Clusters”, <em>Proceedings of the 17th ACM symposium
    on Principles and practice of parallel programming</em>, 2012.

<p>
</p></li>
<li>Amit Sabne, Putt Sakdhnagool, and Rudolf Eigenmann, “Effects of Compiler
  Optimizations in OpenMP to CUDA Translation,” <em>Proc. of the
    International Workshop on OpenMP, IWOMP</em>, 2012.

<p>
</p></li>
<li>Dheya Mustafa and Rudolf Eigenmann, “Portable Section-level Tuning of
  Compiler Parallelized Applications,” <em>SC'12: Proceedings of the 2010
    ACM/IEEE conference on Supercomputing</em>, IEEE press, 2012.

<p>
</p></li>
<li>Tanzima Zerin Islam, Kathryn Mohrory, Saurabh Bagchi, Adam Moodyy, Bronis
  R. de Supinskiy and Rudolf Eigenmann, “mcrEngine: A Scalable Checkpointing
  System Using Data-Aware Aggregation and Compression”, <em>SC'12:
    Proceedings of the 2010 ACM/IEEE conference on Supercomputing</em>, nominated
  for best student paper, IEEE press, 2012.

<p>
</p></li>
<li>Ayguade, Eduard, Dionisios Pnevmatikatos, Rudolf Eigenmann, Mikel LujÃ¡n, and
Sabri Pllana. “Topic 11: Multicore and Manycore Programming,” In <em>  Euro-Par 2012 Parallel Processing</em>, pages 587-588, Springer Berlin
Heidelberg, 2012.

<p>
</p></li>
<li>Rudolf Eigenmann and Samuel Midkiff, “Compiler Infrastructure - Guest
  Editor's Introduction,” International Journal of Parallel Programming, 2012.

<p>
</p></li>
<li>Hacker, T.J., Eigenmann, R., Bagchi, S., Irfanoglu, A., Pujol, S.,
  Catlin, A. and Rathje, E., “The NEEShub Cyberinfrastructure for Earthquake
  Engineering,” Computing in Science &amp; Engineering, vol:13, no:4, pages
67-78, 2011.

<p>
</p></li>
<li>Dheya Mustafa, Aurangzeb and Rudolf Eigenmann, “Performance Analysis and
  Tuning of Automatically Parallelized OpenMP Applications,” <em>Proc. of the
    International Workshop on OpenMP, IWOMP</em>, Springer Verlag, 6665, 2011,
  pages 150-164.

<p>
</p></li>
<li>Okwan Kwon, Fahed Jubair, Seung-Jai Min, Hansang Bae, Rudolf Eigenmann
  and Samuel Midkiff, “Automatic Scaling of OpenMP Beyond Shared Memory,”
  <em>LCPC '11: Proceedings of the 24th International Workshop on Languages
    and Compilers for Parallel Computing</em>, 2011.

<p>
</p></li>
<li>Eigenmann, R. and Irfanoglu, A., “Computational Earthquake and Tsunami
  Research - Guest Editor's Introduction,” Computing in Science &amp; Engineering, vol:13, no:4, pages 11-13,
  2011.

<p>
</p></li>
<li>R. Eigenmann, T. Hacker and E. Rathje, “NEES Cyberinfrastructure: A
  Foundation for Innovative Research and Education,” 2010 US-CANADA joint
  conference on Earthquake Engineering, Toronto, Canada, July 2010.

<p>
</p></li>
<li>Julio Ramirez, Thalia Anagnos, Rudolf Eigenmann, “The George E. Brown,
  Jr. Network for Earthquake Engineering Simulation (NEES): A Resource for
  Structural Engineers,” Proc. of the 2010 Structural Engineers Association of
  California Convention (SEAOC), September 2010.

<p>
</p></li>
<li>Seyong Lee and Rudolf Eigenmann, “OpenMPC: Extended OpenMP Programming and
  Tuning System for GPUs,” in <em>Proc. of the ACM International Conference
    on High Performance Computing Networking, Storage and Analysis, SC'10</em>,
  (Best Student Paper), November 2010.

<p>
</p></li>
<li>Chirag Dave, Hansang Bae, Seung-Jai Min, Seyong Lee, Rudolf Eigenmann and
  Samuel Midkiff, “Cetus: A Source-to-Source Compiler Infrastructure for
  Multicores,” <em>IEEE Computer</em>, vol. 42, 2009, pages 36-42.

<p>
</p></li>
<li>Seyong Lee, Seung-Jai Min and Rudolf Eigenmann, “OpenMP to GPGPU: A
  Compiler Framework for Automatic Translation and Optimization,” in <em>    PPoPP '09: Proceedings of the 14th ACM SIGPLAN symposium on Principles and
    practice of parallel programming</em>, 2009, pages 101-110.

<p>
</p></li>
<li>Hansang Bae, Leonardo Bachega, Chirag Dave, Sang-Ik Lee, Seyong Lee,
  Seung-Jai Min, Rudolf Eigenmann and Samuel Midkiff, “Cetus: A
  Source-to-Source Compiler Infrastructure for Multicores,” in <em>Proc. of
    the 14th Int'l Workshop on Compilers for Parallel Computing (CPC'09)</em>,
  2009, 14 pages.

<p>
</p></li>
<li>Chirag Dave and Rudolf Eigenmann, “Automatically tuning parallel and
  parallelized programs,” <em>Proc. of the Workshop on Languages and
    Compilers for Parallel Computing (LCPC'09)</em>, 14 pages, 2009.

<p>
</p></li>
<li>Tanzima Zerin Islam, Saurabh Bagchi and Rudolf Eigenmann, “FALCON - A
  System for Reliable Checkpoint Recovery in Shared Grid Environments,” in
  <em>Proc. of the ACM International Conference on Supercomputing, SC'09</em>,
  (nominated for best paper), 12 pages, November 2009.

<p>
</p></li>
<li>Rudolf Eigenmann and Eduard Ayguade, “Special Issue on OpenMP - Guest
 Editor's Introduction”, International Journal of Parallel, Vol 37, No 3, June
 2009.

<p>
</p></li>
<li>Jong-Kook Kim, Howard&nbsp;Jay Siegel, Anthony&nbsp;A. Maciejewski, and Rudolf
  Eigenmann, “Dynamic resource management in energy constrained heterogeneous
  computing systems using voltage scaling,” <em>IEEE Trans. Parallel
    Distributed Syst."</em>  2008.

<p>
</p></li>
<li>Mohamed Sayeed, Hansang Bae, Yili Zheng, Brian Armstrong, Rudolf Eigenmann,
  and Faisal Saied, “Measuring high-performance computing with real
  applications,” <em>IEEE Computation in Science and Engineering</em>, vol. 10,
  no. 4, pp. 60-69, 2008.

<p>
</p></li>
<li>Zhelong Pan and Rudolf Eigenmann, “PEAK--a fast and effective performance
  tuning system via compiler optimization orchestration,” <em>ACM
    Trans. Program. Lang. Syst.</em>, vol. 30, no. 3, pp. 1-43, 2008.

<p>
</p></li>
<li>Brian Armstrong and Rudolf Eigenmann,
<br>“Application of automatic parallelization to modern challenges of
  scientific computing industries,”
<br>
in <em>Proc. of the International Conference on Parallel
  Processing</em>. IEEE Computer Society, 2008.

<p>
</p></li>
<li>Ayon Basumallik and Rudolf Eigenmann,
<br>“Incorporation of OpenMP memory consistency into conventional
  dataflow analysis,”
<br>
in <em>Proc. of the International Workshop on OpenMP, IWOMP</em>. 2008,
  vol. 5004 of <em>LNCS</em>, Springer Verlag.

<p>
</p></li>
<li>Seyong Lee, Xiaojuan Ren, and Rudolf Eigenmann,
<br>“Efficient content1 search in iShare, a P2P-based
  internet-sharing system,”
<br>
in <em>Proc. of the 2nd Workshop on Large-scale, Volatile Desktop
  Grids</em>, April 2008.

<p>
</p></li>
<li>Seyong Lee and Rudolf Eigenmann,
<br>“Adaptive runtime tuning of parallel sparse matrix-vector
  multiplication on distributed memory systems,”
<br>
in <em>Proc. of the ACM International Conference on Supercomputing
  (ICS08)</em>, June 2008.

<p>
</p></li>
<li>Seung-Jai Min and Rudolf Eigenmann,
<br>“Optimizing Irregular Shared-Memory Applications for Clusters,”
<br>
in <em>Proc. of the ACM International Conference on Supercomputing</em>,
  New York, NY, USA, 2008, pp. 256-265, ACM.

<p>
</p></li>
<li>Seyong Lee and Rudolf Eigenmann,
<br>“Adaptive tuning in a dynamically changing resource environment,”
<br>
in <em>Workshop on Next-Generation Software Systems, Int'l Parallel
  and Distributed Processing Symposium</em>, 2008.

<p>
</p></li>
<li>Xiaojuan Ren, Seyong Lee, Rudolf Eigenmann and Saurabh Bagchi, “Prediction
  of Resource Availability in Fine-Grained Cycle Sharing Systems and Empirical
  Evaluation,” <em>Journal of Grid Computing</em>, vol. 5, pages 173-195, 2007.

<p>
</p></li>
<li>Troy A. Johnson, T. N. Vijaykumar and Rudolf Eigenmann, “Speculative Thread
  Decomposition Through Empirical Optimization”, <em>Proceedings of the ACM
    Symposium on the Principles and Practice of Parallel Programming</em>, March
  2007.

<p>
</p></li>
<li>Xiaojuan Ren, Rudolf Eigenmann and Saurabh Bagchi, “Failure-Aware
  Checkpointing in Fine-Grained Cycle Sharing Systems,” <em>IEEE
    International Symposium on High Performance Distributed Computing,</em>
  nominated for best paper award, pages 33-42, 2007.

<p>
</p></li>
<li>Ayon Basumallik, Seung-Jai Min, Rudolf Eigenmann, “Programming Distributed
  Memory Systems Using OpenMP,” <em>Proc. HIPSâ€™07 Workshop of the IPDPS'07:
    Proceedings of the 17th International Symposium on Parallel and Distributed
    Processing</em>, 2007, 8 pages.

<p>
</p></li>
<li>X. Ren and A. Basumallik and Z. Pan and R. Eigenmann, “Open Internet-based
  Sharing for Desktop Grids in iShare,” <em>Proc. of the 1st Workshop on
    Large-scale, Volatile Desktop Grids: Proceedings of the 17th International
    Symposium on Parallel and Distributed Processing,</em> 2007, 8 pages.

<p>
</p></li>
<li>Seon Wook Kim and Chong-Liang Ooi and Rudolf Eigenmann and Babak Falsafi and
  T. N. Vijaykumar, “Reference Idempotency to Reduce Speculative Storage
  Overflow,” <em>ACM Transactions on Programming Languages and Systems</em>,
  Vol. 28. No. 5, pages 942-965, 2006.

<p>
</p></li>
<li>Brian Armstrong, Hansang Bae, Rudolf Eigenmann, Faisal Saied, Mohamed
  Sayeed and Yili Zheng, “HPC Benchmarking and Performance Evaluation With Realistic
 Applications,” Proceedings of Benchmarking Workshop 2006, Austin, Texas,
 January 2006.

<p>
</p></li>
<li>Zhelong Pan, Xiaojuan Ren, Rudolf Eigenmann and Dongyan Xu, “Executing
  MPI Programs on Virtual Machines in an Internet Sharing System,” <em>IEEE
    International Parallel &amp; Distributed Processing Symposium (IPDPS)</em>,” 10
  pages, April 2006.

<p>
</p></li>
<li>Zhelong Pan and Rudolf Eigenmann, “Fast and Effective Orchestration of
  Compiler Optimizations for Automatic Performance Tuning,” <em>The 4th
    Annual International Symposium on Code Generation and Optimization (CGO)</em>,
  12 pages, March, 2006.

<p>
</p></li>
<li>Ayon Basumallik and Rudolf Eigenmann, “Optimizing Irregular
  Shared-Memory Applications for Distributed-Memory Systems,”
  <em>Proc. of the ACM Symposium on Principles and Practice of
  Parallel Programming (PPOPP'06)</em>, ACM Press, 10 pages, 2006.

<p>
</p></li>
<li>Troy Johnson and Rudolf Eigenman, “Context-Sensitive Domain-Independent
  Algorithm Composition and Selection”, <em>Proceedings of the ACM SIGPLAN
    Conference on Programming Language Design and Implementation</em>, 10 pages,
  2006.

<p>
</p></li>
<li>Xiaojuan Ren, Seyong Lee, Rudolf Eigenmann and Saurabh Bagchi, “Resource
  Availability Prediction in Fine-Grained Cycle Sharing Systems,” <em>    Proceedings of the 15th IEEE International Symposium on High Performance
    Distributed Computing</em>, runner-up for best paper award, pages 93-104,
  2006.

<p>
</p></li>
<li>Xiaojuan Ren and Rudolf Eigenmann,
“Empirical Studies on the Behavior of Resource Availability in
 Fine-Grained Cycle Sharing Systems,”
<em>International Conference on Parallel Processing,</em>
pages 3-11,
2006.

<p>
</p></li>
<li>Zhelong Pan and Rudolf Eigenmann,
“Fast, Automatic, Procedure-Level Performance Tuning,”
<em>Proc. of Parallel architectures and Compilation Techniques,</em>
pages 173-181,
2006.

<p>
</p></li>
<li>Matthijs van Waveren, Kumaran Kalyanasundaram, Greg Gaertner, Wesley
  Jones, Rudolf Eigenmann, Ron Lieberman, Matthias S. Müller, Brian Whitney
  and Hideki Saito, “SPEC HPG Benchmarks for HPC Systems,” <em>    Proc. Benchmarking Workshop 2006,</em> (8 pages, on CDROM) 2006.

<p>
</p></li>
<li>Troy A. Johnson, Sang-Ik Lee, Seung-Jai Min and Rudolf Eigenmann, “Can
  Transactions Enhance Parallel Programs?,” <em>Proceedings of the Workshop
    on Languages and Compilers for Parallel Computing</em>, November 2006.

<p>
</p></li>
<li>Ayon Basumallik and Xiaojuan Ren and Rudolf Eigenman and Sebastien Goasguen,
  “iShare - Bringing the TeraGrid to the User's Desktop,” <em>TeraGrid'06
    Conference</em>, Indianapolis, Indiana, June 2006.

<p>
</p></li>
<li>Xiaojuan Ren, Seyong Lee, Saurabh Bagchi, and Rudolf Eigenmann, “Resource
  Fault Prediction for Fine-Grained Cycle Sharing,” <em>IEEE International
    Conference on Dependable Systems and Networks (DSN)</em>, (Fast Abstract,) June
  2005, Yokohama, Japan.

<p>
</p></li>
<li>Hansang Bae and Rudolf Eigenmann, “Interprocedural Symbolic Range
  Propagation for Optimizing Compilers,” <em>Proc. of the Workshop on
    Languages and Compilers for Parallel Computing(LCPC'05)</em>, 13 pages,
  October, 2005.

<p>
</p></li>
<li>Zhelong Pan, Brian Armstrong, Hansang Bae and Rudolf Eigenmann, “On the
  Interaction of Tiling and Automatic Parallelization,” <em>First
    International Workshop on OpenMP</em>, (12 pages), June, 2005.

<p>
</p></li>
<li>Jong-Kook Kim, Howard Jay Siegel, Anthony A. Maciejewski, and
Rudolf Eigenmann, “Dynamic mapping in Energy Constrained Heterogeneous
Computing Systems,” <em>19th International Parallel and Distributed
Processing Symposium (IPDPS 2005)</em>, IEEE Computer Society,
Denver, Colorado, Apr. 2005.

<p>
</p></li>
<li>Xiaojuan Ren and Rudolf Eigenmann, “iShare - Open Internet Sharing Built
  on Peer-to-Peer and Web,” <em>European Grid Conference</em>, pages 1117-1127,
  February, 2005.

<p>
</p></li>
<li>Ayon Basumallik and Rudolf Eigenmann, “Towards Automatic Translation of
  OpenMP to MPI,” <em>Proc. of the International Conference on
    Supercomputing, ICS'05</em>, pages 189-198, 2005.

<p>
</p></li>
<li>Matthias S. Müller, Kumaran Kalyanasundaram, Greg Gaertner, Wesley Jones,
  Rudolf Eigenmann, Ron Lieberman, Matthijs van Waveren and Brian Whitney,
  “SPEC HPG Benchmarks for High Performance Systems,” <em>International
    Journal of High-Performance Computing and Networking</em>, vol. 1, no. 4, pages
  162-170, 2004.

<p>
</p></li>
<li>Zhelong Pan and Rudolf Eigenmann, “Rating Compiler Optimizations for Automatic
Performance Tuning,” <em>SC2004: High Performance Computing, Networking and
Storage Conference</em>, on CDROM (10 pages), November, 2004.

<p>
</p></li>
<li>Seung-Jai Min and Rudolf Eigenmann, “Combined Compile-time and Runtime-driven,
Pro-active Data Movement in Software DSM Systems,” <em>Proc. of Seventh
Workshop on Languages, Compilers, and Run-Time Systems for Scalable Computers
(LCR2004)</em>, October, 2004.

<p>
</p></li>
<li>Wessam Hassanein, Jose Fortes and Rudolf Eigenmann, “Forwarding Through
In-Memory Precomputation Threads,” <em>Proceedings of the ACM International
Conference on Supercomputing</em>, 2004.

<p>
</p></li>
<li>Xuxian Jiang, Dongyan Xu and Rudolf Eigenmann, “Protection Mechanisms for
Application Service Hosting Platforms,” <em>Proceedings of IEEE International
Symposium on Cluster Computing and the Grid (CCGrid)</em>, pages 656-663, 2004.

<p>
</p></li>
<li>Troy A. Johnson, Sang-Ik Lee, Long Fei, Ayon Basumallik, Gautam
  Upadhyaya, Rudolf Eigenmann and Samuel P. Midkiff, “Experiences in Using
  Cetus for Source-to-Source Transformations,” <em>Proc. of the Workshop on
    Languages and Compilers for Parallel Computing (LCPC'04)</em>, Springer Verlag,
  Lecture Notes in Computer Science, pages 1-14, 2004.

<p>
</p></li>
<li>Xiaojuan Ren, Zhelong Pan, Rudolf Eigenmann and Y. Charlie Hu,
  “Decentralized and Hierarchical Discovery of Software Applications in the
  iShare Internet Sharing System,” <em>Proceedings of International
    Conference on Parallel and Distributed Computing Systems</em>, pages 124-130,
  September 2004.

<p>
</p></li>
<li>Troy A. Johnson, Rudolf Eigenmann and T. N. Vijaykumar,
“Min-Cut Program Decomposition for Thread-Level Speculation,”
<em>Proceedings of the ACM SIGPLAN 2003 Conference on Programming
 Language Design and Implementation</em>, pages 59-70, 2004.

<p>
</p></li>
<li>Vishal Aslot and Rudolf Eigenmann, “Quantitative Performance Analysis of the
SPEC OMP2001 Benchmarks,” <em>Scientific Programming</em>, volume 11, number 2,
2003, pages 105-124.

<p>
</p></li>
<li>Seung-Jai Min, Ayon Basumallik and Rudolf Eigenmann, “Optimizing OpenMP
Programs on Software Distributed Shared Memory Systems,” in <em>International
Journal of Parallel Programming</em>, Vol 31, No 3, pages 225-249, 2003.

<p>
</p></li>
<li>Hideki Saito, Greg Gaertner, Wesley Jones, Rudolf Eigenmann, Hidetoshi
Iwashita, Ron Lieberman and Matthijs van Waveren, “Large System Performance of
SPEC OMP Benchmark Suites,” in <em>International Journal of Parallel
Programming</em>, Vol 31, No 3, pages 197-209, 2003.

<p>
</p></li>
<li>Seung-Jai Min, Ayon Basumallik and Rudolf Eigenmann, “Supporting Realistic
OpenMP Applications on a Commodity Cluster of Workstations,” in <em>OpenMP
Shared Memory Parallel Programming: International Workshop on OpenMP
Applications and Tools, WOMPAT 2003</em>, Toronto, Canada, June 26-27,
pp. 170-179, 2003.

<p>
</p></li>
<li>Sang-Ik Lee, Troy A. Johnson and Rudolf Eigenmann, “Cetus - An Extensible
Compiler Infrastructure for Source-to-Source Transformation,”in <em>Proc. of
the Workshop on Languages and Compilers for Parallel Computing(LCPC'03)</em>,
Lecture Notes in Computer Science #2958, pages 539-553,
October 2003.

<p>
</p></li>
<li>Wessam Hassanein, Greg Astfalk and Rudolf Eigenmann, “Performance Analysis and
Tracing of Technical and Java Applications On the Itanium 2 Processor,” in
<em>Proceedings of the IEEE International Symposium on Performance Analysis of
Systems and Software</em>, pages 91-100, 2003.

<p>
</p></li>
<li>Rudolf Eigenmann, Jay Hoeflinger, Robert H. Kuhn, David Padua, Ayon Basumallik,
Seung-Jai Min, and Jiajing Zhu, “Is OpenMP for Grids ?” Workshop on
Next-Generation Software, International Parallel and Distributed Processing
Symposium, Ft. Lauderdale, April 2002, 8 pages (on CDROM).

<p>
</p></li>
<li>Rudolf Eigenmann, Greg Gaertner, and Wesley Jones, “SPEC HPC2002: The Next
High-Performance Computer Benchmark,” <em>Lecture Notes in Computer Science,
#2327</em>, Springer Verlag, pages 7-10, Invited Talk at the International
Symposium on High-Performance Computing, Nara, Japan, 2002, pages 7-10.

<p>
</p></li>
<li>Hideki Saito, Greg Gaertner, Wesley Jones, Rudolf Eigenmann, Hidetoshi
Iwashita, Ron Lieberman, and Matthijs van Waveren, “Large System Performance
of SPEC OMP2001 Benchmarks,” <em>Lecture Notes in Computer Science, #2327</em>,
Springer Verlag, Invited paper at the International Workshop on
OpenMP: Experiences and Implementation, Nara, Japan, 2002, pages 370-379.

<p>
</p></li>
<li>Ayon Basumallik, Seung-Jai Min, and Rudolf Eigenmann, “Towards OpenMP
Execution on Software Distributed Shared Memory Systems,” <em>Lecture Notes
in Computer Science, #2327</em>, pages 457-468, Springer Verlag, International
Workshop on OpenMP: Experiences and Implementation, Nara, Japan, 2002, pages
457-468.

<p>
</p></li>
<li>Wessam Hassanein, José Fortes, and Rudolf Eigenmann, “Towards Guided Data
Forwarding using Intelligent Memory,” Proceedings of the 2nd Workshop on
Memory Performance Issues, held in conjunction with the 29th International
Symposium in Computer Architecture, May 2002, 10 pages.

<p>
</p></li>
<li>Hansang Bae and Rudolf Eigenmann, “Performance Analysis of Symbolic Analysis
Techniques for Parallelizing Compilers,” in <em>Workshop on Languages and
Compilers for Parallel Computing</em>, August, 2002, (on CD ROM, 10 pages).

<p>
</p></li>
<li>Brian Armstrong and Rudolf Eigenmann, “Challenges in the automatic
parallelization of large-scale computational applications,” in <em>Commercial
Applications for High-Performance Computing</em>.  International Society for
Optical Engineers, Aug. 2001, volume 4528 of <em>Proceedings of SPIE</em>, pages
50-60.

<p>
</p></li>
<li>Jose A. B. Fortes, Nirav H. Kapadia, Rudolf Eigenmann, Renato J. Figueiredo,
Valerie Taylor, Alok Choudhary, Luis Vidal and Jan-Jo Chen, “On the Use of
Simulation and Parallelization Tools in Computer Architecture and Programming
Courses,” <em>The Computers in Education Journal,</em> January/March, 2001,
pages 19-27.

<p>
</p></li>
<li>Insung Park, Michael J. Voss, Seon Wook Kim and Rudolf Eigenmann, “Parallel
Programming Environment for OpenMP,” <em>Scientific Programming</em>, 
2&amp;3, 2001, pages 143-161.

<p>
</p></li>
<li>Seon Wook Kim and Rudolf Eigenmann, “Where Does the Speedup Go: Quantitative
Modeling of Performance Losses in Shared-Memory Programs,” <em>Parallel
Processing Letters</em>, vol 10, no 2&amp;3, 2001, pages 227-238.

<p>
</p></li>
<li>Steve W. Bova, Clay P. Breshears, Henry Gabb, Rudolf Eigenmann, Greg Gaertner,
Bob Kuhn, Bill Magro and Stefano Salvini, “Parallel Programming with Message
Passing and Directives,” <em>IEEE Computation in Science and Engineering,</em>
September/October 2001, pages 22-37.

<p>
</p></li>
<li>Seon&nbsp;Wook Kim and Rudolf Eigenmann, “The structure of a compiler for <em>and</em>
implicit parallelism,” in <em>Proc. of the Workshop on Languages and
Compilers for Parallel Computing(LCPC'01)</em>. August 2001, 15 pages (on CDROM).

<p>
</p></li>
<li>Brian Armstrong and Rudolf Eigenmann, “Benchmarking and Performance Evaluation
with Realistic Applications,”chapter A Methodology for Scientific Benchmarking
with Large-Scale Applications, <em>MIT Press,</em> 2001, pages 109-127.

<p>
</p></li>
<li>Chong-Liang Ooi, Seon&nbsp;Wook Kim, Rudolf Eigenmann, Babak Falsafi, and T.&nbsp;N.
Vijaykumar, “Multiplex: Unifying conventional and speculative thread-level
parallelism on a chip multiprocessor,” in <em>Proc. of the International
Conference on Supercomputing, ICS'01</em>, ACM Press, June 2001, pages 368-380.

<p>
</p></li>
<li>Seon&nbsp;Wook Kim, Chong liang Ooi, Rudolf Eigenmann, Babak Falsafi, and T.&nbsp;N.
Vijaykumar, “Reference idempotency analysis: A framework for optimizing
speculative execution,” in <em>Proc. of the ACM Symposium on Principles and
Practice of Parallel Programming (PPOPP'01)</em>, ACM Press, June 2001, pages
2-11.

<p>
</p></li>
<li>Michael&nbsp;J. Voss and Rudolf Eigenmann,
<br>“High-level adaptive program optimization with ADAPT,”
<br>
in <em>Proc. of the ACM Symposium on Principles and Practice of
  Parallel Programming (PPOPP'01)</em>, ACM Press, June 2001, pages 93-102.

<p>
</p></li>
<li>Vishal Aslot, Max Domeika, Rudolf Eigenmann, Greg Gaertner, Wesley&nbsp;B. Jones,
and Bodo Parady, “SPEComp: A new benchmark suite for measuring parallel
computer performance,” in <em>OpenMP Shared-Memory Parallel Programming</em>,
Springer Verlag, Heidelberg, Germany, July 2001, Lecture Notes in Computer
Science #2104, pages 1-10.

<p>
</p></li>
<li>Seung-Jai Min, Seon&nbsp;Wook Kim, Michael Voss, Sang-Ik Lee, and Rudolf Eigenmann,
“Portable compilers for OpenMP,” in <em>OpenMP Shared-Memory Parallel
Programming</em>, Springer Verlag, Heidelberg, Germany, July 2001, Lecture Notes in
Computer Science #2104, pages 11-19.

<p>
</p></li>
<li>Vishal Aslot and Rudolf Eigenmann,
<br>“Performance characteristics of the SPEC OMP2001 benchmarks,”
<br>
in <em>Proc. of the Third European Workshop on OpenMP
  (EWOMP'2001)</em>, Barcelona, Spain, September 2001, 10 pages.

<p>
</p></li>
<li>Rudolf Eigenmann, Greg Gaertner, Faisal Saied, and Mark Straka, <em>Performance Evaluation and Benchmarking with Realistic Applications</em>, chapter
SPEC HPG Benchmarks: Performance Evaluation with Large-Scale Science and
Engineering Applications, MIT Press, Cambridge, Mass., 2001, pages 40-48.

<p>
</p></li>
<li>Renato&nbsp;J. Figueiredo, Josè A.&nbsp;B. Fortes, Rudolf Eigenmann, Nirav&nbsp;H.
Kapadia, Sumalatha Adabala, Jose Miguel-Alonso, Valerie Taylor, Luis Vidal, and
Jan-Jo Chen, “Network computer for computer architecture education: A progress
report. computer architecture and programming courses,” in <em>Proceeding of
2001 ASEE Annual Conference &amp; Exposition</em>, 2001, 16 pages.

<p>
</p></li>
<li>Rudolf Eigenmann and Michael Voss, “Toward a Compilation Paradigm for
Computational Applications on the Information Power Grid,” <em>Mathematics
and Computers in Simulation</em>, 2000, volume 54, number 4-5, pages 307-320.

<p>
</p></li>
<li>Michael. J. Voss and Rudolf Eigenmann, “A Framework for Remote Dynamic Program
Optimization,” <em>Proc. of the ACM SIGPLAN Workshop on Dynamic and Adaptive
Compilation and Optimization (Dynamo'00)</em>, January 2000, pages 32-40.

<p>
</p></li>
<li>Michael Voss and Rudolf Eigenmann, “Adapt: Automated De-Coupled Adaptive
Program Transformation,” <em>Proc. of the Int'l Conf. on Parallel
Processing</em>, August 2000, pages 163-170.

<p>
</p></li>
<li>Renato J. Figueiredo, José A. B. Fortes, Rudolf Eigenmann, Nirav Kapadia,
Sumalatha Adabala, Jose Miguel-Alonso, Valerie Taylor, Miron Livny, Luis Vidal
and Jan-Jo Chen, “A Network-Computing Infrastructure for Tool Experimentation
Applied to Computer Architecture Education,”<em>Workshop on Computer
Architecture Education held in conjunction with the 27th International
Symposium on Computer Architecture,</em> Vancouver, BC, June 10, 2000, 7 pages.

<p>
</p></li>
<li>José A. B. Fortes, Nirav H. Kapadia, Rudolf
Eigenmann, Renato J. Figueiredo, Valerie Taylor, Alok Choudhary, Luis Vidal and
Jan-Jo Chen, “On the Use of Simulation and Parallelization Tools in Computer
Architecture and Programming Courses,” <em>Proceeding of the 2000 ASEE Annual
Conference &amp; Exposition</em>, St. Louis, MO, June 18-21, 2000, 14 pages.

<p>
</p></li>
<li>Stefan Kortmann, Insung Park, Michael Voss and Rudolf Eigenmann,
“Interactive and Modular Optimization with InterPol,” <em>Proc. of the Int'l
Conference on Parallel and Distributed Processing Techniques and Applications</em>,
2000, 5 pages.

<p>
</p></li>
<li>Michael J. Voss, Kwok Wai Yau and Rudolf Eigenmann, “Interactive
Instrumentation and Tuning of OpenMP Programs,” <em>Proc. of the Int'l
Conference on Parallel and Distributed Processing Techniques and Applications</em>,
2000, 7 pages.

<p>
</p></li>
<li>Insung Park, Nirav H. Kapadia, Renato J. Figueiredo, Rudolf Eigenmann and
José A. B. Fortes, “Towards an Integrated, Web-executable Parallel
Programming Tool Environment", <em>Proc. of SC2000: High-Performance
Computing and Networking Conference</em>, 2000, 12 pages.

<p>
</p></li>
<li>Brian Armstrong, Seon Wook Kim and Rudolf Eigenmann, “Quantifying
Differences between OpenMP and MPI Using a Large-Scale Application Suite,”
<em>Proc. of the third International Symposium on High Performance Computing,
Lecture Notes in Computer Science #1940</em>, Springer Verlag, 2000, pages
482-493.

<p>
</p></li>
<li>Seon Wook Kim and Rudolf Eigenmann, “Compiler Techniques for Energy Saving
in Instruction Caches of Speculative Parallel Microarchitectures,” <em>Proc. of the Int'l Conference on Parallel Processing</em>, 2000, pages 77-84.

<p>
</p></li>
<li>Seon Wook Kim, Insung Park and Rudolf Eigenmann, “A Performance Advisor
Tool for Shared-Memory Parallel Programming,” <em>Proc. of the Workshop on
Languages and Compilers for Parallel Computing</em>, 2000, 15 pages.

<p>
</p></li>
<li>Insung Park and Rudolf Eigenmann, “Supporting Users' Reasoning in
Performance Evaluation and Tuning of Parallel Applications,” <em>Proc. of
the International Conference on Parallel and Distributed Computing Systems</em>,
2000, 6 pages.

<p>
</p></li>
<li>Valerie E. Taylor, José A. B. Fortes, and Rudolf Eigenmann,
“HPAM Petaflop Point Design: Identifying Critical Research Issues for Petaflop,”
Proceedings of the PetaFlop (TPF-3) Workshop, February 1999, 7 pages.

<p>
</p></li>
<li>Michael J. Voss and Rudolf Eigenmann, “Reducing Parallel Overheads Through
Dynamic Serialization,” <em>Proc. of the International Parallel Processing
Symposium</em>, 1999, pages 88-92.

<p>
</p></li>
<li>Thomas J. Downar, Rudolf Eigenmann, José A. B. Fortes, and Nirav H. Kapadia,
“Issues and Approaches in Parallel Multi-Component and Multi-Physics
Simulations,” <em>Proc. of the 1999 International Conference on Parallel and
Distributed Processing Techniques and Applications (PDPTA'99)</em>, pages 916-922.

<p>
</p></li>
<li>Seon Wook Kim and Rudolf Eigenmann,
“Compiling for Speculative Architectures,”
<em>Proc. of the 12th Int'l Workshop on Languages and Compilers for Parallel
Computing</em>, San Diago, Calif., August 1999, pages 464-467.

<p>
</p></li>
<li>Michael J. Voss and Rudolf Eigenmann, “Dynamically Adaptive Parallel
Programs,”<em>Proc. of Int'l Symp. on High-Performance Computing</em>, 1999,
Japan, pages 109-120.

<p>
</p></li>
<li>J. A. B. Fortes, N. H. Kapadia, R. Eigenmann, R. J. Figueiredo, V. Taylor,
A. Choudhary, L. Vidal, and J.-J. Chen, “On the Integration of Computer
Architecture and Parallel Programming Tools Into Computer Curricula,” <em>Proc. of the 1999 Annual Society for Engineering Education Conference</em>, 1999,
14 pages.

<p>
</p></li>
<li>Insung Park, Michael J. Voss, Brian Armstrong, and Rudolf Eigenmann, “Parallel
Programming and Performance Evaluation with The U<small>RSA</small> Tool Family,” <em>International Journal of Parallel Programming</em>, volume 26, number 5,
October 1998, pages 541-561.

<p>
</p></li>
<li>Z. Ben-Miled, J.A.B. Fortes, R. Eigenmann and V. Taylor, “On the Cost-Efficiency
of Hierarchical Heterogeneous Machines for Compiler- and Hand-Parallelized
Applications,” <em>International Journal of Parallel and Distributed Systems
and Networks</em>, volume 1, number 4, 1998, pages 193-203.

<p>
</p></li>
<li>William Blume and Rudolf Eigenmann, “Non-Linear and Symbolic Data
Dependence Testing,” <em>IEEE Transactions on Parallel and Distributed
Systems</em>, volume 9, number 12, December 1998, pages 1180-1194.

<p>
</p></li>
<li>Insung Park, Michael J. Voss, Brian Armstrong and Rudolf
Eigenmann, “Interactive Compilation and Performance Analysis with Ursa
Minor.” <em>Proceedings of the 10th Workshop on Languages and Compilers for
Parallel Computing, August 1997</em>, also in <em>Lecture
Notes in Computer Science,</em> volume 1366, Springer Verlag, 1998, pages 163-176.

<p>
</p></li>
<li>Z. Ben-Miled, J.A.B. Fortes, R. Eigenmann and V. Taylor, “On the
Implementation of Broadcast, Scatter and Gather in a Heterogeneous
Architecture,” <em>Hawaii International Conference on Systems Sciences</em>,
January 1998, pages 216-225.

<p>
</p></li>
<li>Insung Park and Rudolf Eigenmann, “U<small>RSA </small>M<small>AJOR</small>: Exploring Web Technology
for Design and Evaluation of High-Performance Systems,” <em>International
Conference on High-Performance Computing and Networking, HPCN Europe'98</em>,
Amsterdam, April 1998, pages 535-544.

<p>
</p></li>
<li>Richard L. Kennell and Rudolf Eigenmann, “Automatic Parallelization of C by
Means of Language Transcription,” <em>Proceedings of the 11th Int'l Workshop
on Languages and Compilers for Parallel Computing</em>, August 1998, pages
157-173.

<p>
</p></li>
<li>Brian Armstrong and Rudolf Eigenmann, Performance Forecasting: Towards a
Methodology for Characterizing Large Computational Applications,” <em>Proceedings of the International Conference on Parallel Processing</em>, August
1998, pages 518-525.

<p>
</p></li>
<li>Renato J. O. Figueiredo, José A. B. Fortes, Zina Ben Miled, Valerie Taylor,
and Rudolf Eigenmann, “Impact of Computing-in-Memory on the Performance of
Processor-and-Memory Hierarchies,” Proceedings of the 11th Int'l. Conference
on Parallel and Distributed Computing Systems (PDCS-98), September 1998, pages
43-50.

<p>
</p></li>
<li>Brian Armstrong, Seon Wook Kim, Insung Park, Michael Voss and Rudolf
Eigenmann, “Compiler-Based Tools for Analyzing Parallel Programs.” <em>Parallel Computing</em>, volume 24, 1998, pages 401-420.

<p>
</p></li>
<li>Rudolf Eigenmann, Laxmikant V. Kale, and David A. Padua, “Languages for
Computational Science and Engineering - Guest Editor's Introduction,” IEEE
Computational Science and Engineering, volume 5, number 2, April-June 1998,
pages 16-17.

<p>
</p></li>
<li>Rudolf Eigenmann, Jay Hoeflinger, and David Padua,  “On the Automatic
Parallelization of the Perfect Benchmarks.”  <em>IEEE Transactions on
Parallel and Distributed Systems</em>, volume 9, number 1, January 1997,
pages 5-23. 

<p>
</p></li>
<li>Sarita Adve, Doug Burger, Rudolf Eigenmann, Alasdair Rawsthorne, Michael
D. Smith, Catherine Gebotys, Mahmut Kandemir, David J. Lilja, Alok Choudhary,
Jesse Fang, and Pen-Chung Yew. “The Interaction of Architecture and Compilation
Technology for High-Performance Processor Design” <em>IEEE Computer,</em>
December 1997, pages 51-58.

<p>
</p></li>
<li>Rudolf Eigenmann, Insung Park, and Michael J. Voss, “Are Parallel
Workstations the Right Target for Parallelizing Compilers?” <em>Lecture Notes
in Computer Science, 1239: 10th International Workshop on Languages and
Compilers for Parallel Computing</em>, Springer-Verlag, August
1997, pages 300-314.

<p>
</p></li>
<li>Z. Ben-Miled, J. Fortes, R. Eigenmann, and V. Taylor, “Towards the Design of a
Heterogeneous Hierarchical Machine: a Simulation Approach.” <em>Proceedings of 30th
Simulation Symposium</em>, April 1997, pages 126-136. 

<p>
</p></li>
<li>M. A. Kandaswamy, V. Taylor, R. Eigenmann, J. Fortes, “Implicit Finite
Element Applications: A Case for Matching the Number of Processors to the
Dynamics of the Program Execution.” <em>Proceedings of the 8th SIAM
Conference on Parallel Processing for Scientific Computing</em>, April 1997, on
CD-ROM, 8 pages.

<p>
</p></li>
<li>Z. Ben-Miled, J.A.B. Fortes, R. Eigenmann and V. Taylor, “A
Simulation-based Cost-efficiency Study of Hierarchical Heterogeneous Machines
for Compiler and Hand-Parallelized Applications.” <em>Proceedings of the 9th
International Conference on Parallel and Distributed Computing and Systems</em>,
October 1997, pages 168-175.

<p>
</p></li>
<li>Rudolf Eigenmann and Siamak Hassanzadeh, “SPEC/High-Performance Group:
Benchmarking with Real Industrial Applications.” <em>IEEE Computational
Science and Engineering</em>, 3(1), Spring 1996, pages 18-23.

<p>
</p></li>
<li>William Blume, Ramon Doallo, Rudolf Eigenmann, John Grout, Jay Hoeflinger,
Thomas Lawrence, Jaejin Lee, David Padua, Yunheung Paek, Bill Pottenger,
Lawrence Rauchwerger, Peng Tu, “Parallel Programming with Polaris.” <em>IEEE
Computer</em>, December 1996, pages 78-82.

<p>
</p></li>
<li>Jose' A. B. Fortes, Rudolf Eigenmann, and Valerie Taylor,
“Hierarchical Processors-and-Memory Architecture for High Performance
Computing.” <em>Proceedings of the PetaFlops Systems Workshops</em>, Annapolis,
October 1996, pages 6.125-6.151.

<p>
</p></li>
<li>Michael J. Voss, Insung Park, and Rudolf Eigenmann, “On the
Machine-independent Target Language for Parallelizing Compilers.” <em>Proceedings of the 6th International Workshop on Compilers for Parallel
Computers (CPC'96)</em>, Aachen, Germany, December 1996, pages 207-218.

<p>
</p></li>
<li>Bill Blume and Rudolf Eigenmann, “Demand-driven, Symbolic Range
Propagation.”  <em>Lecture Notes in Computer Science, 1033: 9th
International Workshop on Languages and Compilers for Parallel Computing</em>,
Springer-Verlag, 1996, pages 141-160.

<p>
</p></li>
<li>Zina Ben Miled, Rudolf Eigenmann, Jose' A. B. Fortes, Valerie Taylor,
“Hierarchical Processors-and-Memory Architecture for High Performance
Computing.” <em>Proceedings of Frontiers'96 Conference</em>, Annapolis, October
1996, pages 355-362.

<p>
</p></li>
<li>Rudolf Eigenmann, “Portable Parallel Programming Languages.” <em>1996 ICPP
Workshop on Challenges for Parallel Processing</em>, August 1996, pages 125-131.

<p>
</p></li>
<li>W. Blume, R. Eigenmann, K. Faigin, J. Grout, J. Lee, T. Lawrence,
J. Hoeflinger, D. Padua, Y. Paek, P. Petersen, B. Pottenger, L.
Rauchwerger, P. Tu, and S. Weatherford, “Restructuring Programs for High-Speed
Computers with Polaris.” <em>1996 ICPP Workshop on Challenges for Parallel
Processing</em>, August 1996, pages 149-162.

<p>
</p></li>
<li>Rudolf Eigenmann and George Cybenko, “As Eniac Turns 50: Perspectives on
Computer Science Support for Science and Engineering - Theme Introduction.”
<em>IEEE Computational Science and Engineering</em>, Summer 1996, pages 16-18.

<p>
</p></li>
<li>William Blume and Rudolf Eigenmann,  “Symbolic Range Propagation.”  <em>Proceedings of the 9th International Parallel Processing Symposium, Santa
Barbara, CA</em>, April 1995, pages 357-363.

<p>
</p></li>
<li>David&nbsp;A. Padua, Rudolf Eigenmann, and Jay&nbsp;P. Hoeflinger, “Automatic Program
Restructuring for Parallel Computing and the Polaris Fortran Translator.”
<em>Proceedings of the 7th SIAM Conference on Parallel Processing for
Scientific Computing</em>, San Francisco, CA, February 1995, pages 647-649.

<p>
</p></li>
<li>Bill Pottenger and Rudolf Eigenmann, “Idiom Recognition in the Polaris
Parallelizing Compiler.”  <em>Proceedings of the 9th ACM International
Conference on Supercomputing</em>, 1995, pages 444-448.

<p>
</p></li>
<li>Gregg&nbsp;M. Skinner and Rudolf Eigenmann, “Parallelization and
Performance of a Combustion Chemistry Simulation.”  <em>Scientific
Programming, Special Issue: Applications Analysis</em>, 4(3), 1995, pages 127-139.

<p>
</p></li>
<li>Rudolf Eigenmann, “Parallel Architectures and How to Program Them.”  <em>Speedup</em>, 8(2), 1994, pages 39-44.

<p>
</p></li>
<li>William Blume, Rudolf Eigenmann, Jay Hoeflinger, David Padua, Paul
Petersen, Lawrence Rauchwerger, and Peng Tu, “Automatic Detection of
Parallelism: A Grand Challenge for High-Performance Computing.” <em>IEEE
Parallel and Distributed Technology</em>, 2(3), Fall 1994, pages 37-47.

<p>
</p></li>
<li>William Blume and Rudolf Eigenmann,  “The Range Test: A Dependence Test for
Symbolic, Non-linear Expressions.”  <em>Proceedings of Supercomputing '94,
Washington D.C.</em>, November 1994, pages 528-537.

<p>
</p></li>
<li>William Blume and Rudolf Eigenmann, “An Overview of Symbolic Analysis
Techniques Needed for the Effective Parallelization of the Perfect
Benchmarks.”  <em>Proceedings of the 1994 International Conference on
Parallel Processing</em>, August 1994, pages II233 - II238.

<p>
</p></li>
<li>William Blume, Rudolf Eigenmann, Keith Faigin, John Grout, Jay
Hoeflinger, David Padua, Paul Petersen, Bill Pottenger, Lawrence
Rauchwerger, Peng Tu, and Stephen Weatherford, “Polaris: Improving the
Effectiveness of Parallelizing Compilers.”  <em>Lecture Notes in Computer
Science, 892: 7th International Workshop on Languages and Compilers for
Parallel Computing</em>, Springer-Verlag, August 1994, pages 141-154.

<p>
</p></li>
<li>Utpal Banerjee, Rudolf Eigenmann, Alexandru Nicolau, and David Padua,
“Automatic Program Parallelization.”  <em>Proceedings of the IEEE</em>,
81(2), February 1993, pages 211-243.

<p>
</p></li>
<li>H.&nbsp;Burkhart, R.&nbsp;Eigenmann, H.&nbsp;Kindlimann, M.&nbsp;Moser, and H.&nbsp;Scholian,  “The
<span class="MATH"><img align="BOTTOM" border="0" src="img1.png" alt="$M^3$"></span> Multiprocessor Laboratory.”  <em>IEEE Trans. Parallel and Distributed
Syst.</em>, 4(5), May 1993, pages 507-519.

<p>
</p></li>
<li>Rudolf Eigenmann, Jay Hoeflinger, Greg Jaxon, Zhiyuan Li, and David Padua,
“Restructuring Fortran Programs for Cedar.”  <em>Concurrency: Practice and
Experience</em>, 5(7), October 1993, pages 553-573.

<p>
</p></li>
<li>Rudolf Eigenmann and Patrick McClaughry, “Practical Tools for Optimizing
Parallel Programs.”  <em>Proceedings of the 1993 Simulation Multiconference
on the High-Performance Computing Symposium</em>, Society for Computer Simulation,
San Diego, CA, 1993, pages 160-165.

<p>
</p></li>
<li>D.&nbsp;Kuck, E.&nbsp;Davidson, D.&nbsp;Lawrie, A.&nbsp;Sameh, C.-Q Zhu, A.&nbsp;Veidenbaum,
J.&nbsp;Konicek, P.&nbsp;Yew, K.&nbsp;Gallivan, W.&nbsp;Jalby, H.&nbsp;Wijshoff, R.&nbsp;Bramley, U.M. Yang,
P.&nbsp;Emrath, D.&nbsp;Padua, R.&nbsp;Eigenmann, J.&nbsp;Hoeflinger, G.&nbsp;Jaxon, Z.&nbsp;Li, T.&nbsp;Murphy,
J.&nbsp;Andrews, and S.&nbsp;Turner, “The Cedar System and an Initial Performance
Study.”  <em>Proceedings of the 20th International Symposium on Computer
Architecture, San Diego, CA</em>, May 1993, pages 213-224.

<p>
</p></li>
<li>G. Fox, S. Ranka, M. Scott, A. Malony, J. Browne, M. Chen, A. Choudhary,
T. Chetham, J. Cuny, R. Eigenmann, A. Fahmy, I. Foster, D. Gannon, T. Haupt,
M. Karr, et al., “ Common Runtime Support for High Performance Parallel
Languages: Parallel Compiler Runtime Consortium.”  <em>Proceedings of the
Supercomputing '93 Conference</em>, November 1993, pages 752-757.

<p>
</p></li>
<li>Rudolf Eigenmann, “Toward a Methodology of Optimizing Programs for
High-Performance Computers.”  <em>Proceedings of the International
Conference on Supercomputing, ICS'93, Tokyo, Japan</em>, July 1993, pages 27-36.

<p>
</p></li>
<li>William Blume and Rudolf Eigenmann,  “Performance Analysis of Parallelizing
Compilers on the Perfect Benchmarks Programs.”  <em>IEEE Transactions on
Parallel and Distributed Systems</em>, 3(6), November 1992, pages 643-656.

<p>
</p></li>
<li>R.&nbsp;Eigenmann, J.&nbsp;Hoeflinger, G.&nbsp;Jaxon, and D.&nbsp;Padua, “Cedar
Fortran and its Restructuring Compiler.”  In A.&nbsp;Nicolau D.&nbsp;Gelernter,
T.&nbsp;Gross and D.&nbsp;Padua, editors, <em>Advances in Languages and Compilers for
Parallel Processing: 3rd International Workshop on Languages and Compilers for
Parallel Computing</em>, MIT Press, 1991, pages 1-23.

<p>
</p></li>
<li>Ulrike Meier and Rudolf Eigenmann, “Parallelization and Performance of
Conjugate Gradient Algorithms on the Cedar Hierarchical-Memory
Multiprocessor.”  <em>Proceedings of the 3rd ACM SIGPLAN Symposium on
Principles and Practice of Parallel Programming, Williamsburg, VA</em>, April 1991,
pages 178-188.

<p>
</p></li>
<li>Rudolf Eigenmann and William Blume, “An Effectiveness Study of
Parallelizing Compiler Techniques.”  <em>Proceedings of the 1991
International Conference on Parallel Processing, St. Charles, IL</em>, August 1991,
pages II17-II25.

<p>
</p></li>
<li>Rudolf Eigenmann, Jay Hoeflinger, Zhiyuan Li, and David Padua,
“Experience in the Automatic Parallelization of Four Perfect-Benchmark
Programs.”  <em>Lecture Notes in Computer Science, 589: 4th International
Workshop on Languages and Compilers for Parallel Computing</em>, Springer-Verlag,
August 1991, pages 65-83.

<p>
</p></li>
<li>R.&nbsp;Eigenmann, J.&nbsp;Hoeflinger, G.&nbsp;Jaxon, and D.&nbsp;Padua, “Cedar
Fortran and Its Compiler.”  <em>Lecture Notes in Computer Science, 457:
Proceedings of the Joint Conference on Vector and Parallel Processing,
Zürich, Switzerland</em>, January 1990, pages 288-300.

<p>
</p></li>
<li>H.&nbsp;Burkhart, R.&nbsp;Eigenmann, H.&nbsp;Kindlimann, M.&nbsp;Moser, and
  H.&nbsp;Scholian, “The M3 Multiprocessor Programming Environment.”  <em>Proceedings of CONPAR `88 (ed. by C.R. Jesshope, K.D. Reinartz)</em>, Cambridge
Univ. Press, 1989, pages 446-455.

<p>
</p></li>
<li>Rudolf Eigenmann,  “Computer-aided software engineering in a multiprocessor
environment.”  In <em>3rd International Workshop on Computer-Aided Software
Engineering</em>, London, England, July 1989, pages II/208-219.

<p>
</p></li>
<li>E.&nbsp;Ballarin, H.&nbsp;Burkhart, R.&nbsp;Eigenmann, H.&nbsp;Kindlimann, and M.&nbsp;Moser,  “Making
a Compiler Easily Portable.”  <em>IEEE Software</em>, May 1988, pages 30-38.

<p>
</p></li>
<li>H.&nbsp;Burkhart and R.&nbsp;Eigenmann,  “On the Design of Multiprocessor Command
Languages.”  In K.&nbsp;Hopper and I.&nbsp;A. Newman, editors, <em>Foundation for
Human-Computer Communication</em>, IFIP Working Group 2.7,
North-Holland, September 1986, pages 470-487.

<p>
</p></li>
<li>Rudolf Eigenmann,  “ The M3 Multiprocessor Programming Environment (in German).”  <em>AGEN-Mitteilungen</em>,
number 45, June 1987, pages 47-54.

<p>
</p></li>
</ol>
</body>
</html>
<!-- {% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
 -->

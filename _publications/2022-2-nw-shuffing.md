---
title: "Network Shuffling: Privacy Amplification via Random Walks"
collection: publ_conferences
permalink: /publication/2022-2-nw-shuffing
# note: 'To appear'
# acceptance: 'Acceptance rate: 1349/9020 (15.0%)'
# rankCORE: 'CORE 2021: A*'
# rankGGS: 'GGS 2021: A++'
date: 2022-01-01
venue: 'International Conference on Management of Data (SIGMOD)'
# paperurl: 'https://doi.org/10.1145/3514221.3526162'
pubtype: 'conferences'
authors: ' 
Seng Pei Liew
,
Tsubasa Takahashi
,
Shun Takagi
,
Fumiyuki Kato
,
Yang Cao
,
Masatoshi Yoshikawa'
---
Abstract
 <br> 

Recently, it is shown that shuffling can amplify the central differential privacy guarantees of data randomized with local differential privacy. Within this setup, a centralized, trusted shuffler is responsible for shuffling by keeping the identities of data anonymous, which subsequently leads to stronger privacy guarantees for systems. However, introducing a centralized entity to the originally local privacy model loses some appeals of not having any centralized entity as in local differential privacy. Moreover, implementing a shuffler in a reliable way is not trivial due to known security issues and/or requirements of advanced hardware or secure computation technology.

Motivated by these practical considerations, we rethink the shuffle model to relax the assumption of requiring a centralized, trusted shuffler. We introduce network shuffling, a decentralized mechanism where users exchange data in a random-walk fashion on a network/graph, as an alternative of achieving privacy amplification via anonymity. We analyze the threat model under such a setting, and propose distributed protocols of network shuffling that is straightforward to implement in practice. Furthermore, we show that the privacy amplification rate is similar to other privacy amplification techniques such as uniform shuffling. To our best knowledge, among the recently studied intermediate trust models that leverage privacy amplification techniques, our work is the first that is not relying on any centralized entity to achieve privacy amplification.
 <br> 

 [[Link](https://doi.org/10.1145/3514221.3526162){:target="_blank"}][[Slide](/files/slides_sigmod2022.pdf){:target="_blank"}][[BibTeX](/files/bibtex/liew2022network.bib){:target="_blank"}]

<pre> @article{liew2022network,
  author    = {Seng Pei Liew and
               Tsubasa Takahashi and
               Shun Takagi and
               Fumiyuki Kato and
               Yang Cao and
               Masatoshi Yoshikawa},
  editor    = {Zachary Ives and
               Angela Bonifati and
               Amr El Abbadi},
  title     = {Network Shuffling: Privacy Amplification via Random Walks},
  booktitle = {SIGMOD '22: International Conference on Management of Data, Philadelphia,
               PA, USA, June 12 - 17, 2022},
  pages     = 773--787,
  publisher = ACM,
  year      = 2022,
  url       = https://doi.org/10.1145/3514221.3526162,
  doi       = 10.1145/3514221.3526162
  }
</pre>
---
title: What you think usearch does might not be what it does
author: ~
date: '2018-09-08'
slug: what-you-think-usearch-does-might-not-be-what-it-does
categories: []
tags: []
---

*I wrote this blog post in 2016 for the [MIT Microbiome Center](https://microbiome.mit.edu/).*

<img src="/img/usearch/Picture1.png" width="50%">

<div align="center">
<a href="#PartI">Part I</a> |
<a href="#PartII">Part II</a> |
<a href="#PartIII">Part III</a> |
<a href="#PartIV">Part IV</a> |
<a href="#PartV">Part V</a>
</div>

*One day in Athens, the microbiome scientist Everymeno
encounters 16Socrates.*

**Everymeno**: Hail, 16Socrates! I've been troubled by some results
from my 16S amplicon sequencing data, and I was hoping to hear your
wisdom.

**16Socrates**: I don't know that I can answer your questions, but we
can look for an answer together.

**E**: In a microbiome experiment, I collected samples, extracted the
DNA, and amplified the 16S gene. I'm converting the raw 16S sequences
into operational taxonomic units (OTUs). I know there's a lot of
[discussion](https://figshare.com/articles/2015_Poster_on_OTU_robustness_reproducibility_amp_ecological_consistency/1437744)
in the Microbiome
[Agora](https://en.wikipedia.org/wiki/Agora) about what
kinds of OTU-calling methods we should use, so I tried to avoid
controversy by using all of them and seeing what comes out.

I started calling OTUs using different strategies supported by
*usearch*, which seems to be a commonly-used program for microbiome
analysis. Many people use usearch [via
QIIME](http://qiime.org/install/install.html#installing-qiime-natively-with-a-full-install),
which calls usearch behind-the-scenes to cluster *de novo* or to do
reference-based searches against databases.

**16S**: I think I'm following you so far, but I'm a little
confused. When you say "usearch", do you mean the program
[usearch](http://www.drive5.com/usearch/), or do you mean
the proprietary heuristic
alignment algorithm [USEARCH](http://drive5.com/usearch/manual/usearch_algo.html)
that's implemented by the program usearch?

**E**: I see how that could be confusing. I'm mostly confused about
the behavior of the algorithm USEARCH. I will say usearch only I am
talking other things that the program usearch does---like call
*de novo* OTUs---or when we I am talking explicitly about using the program
to do USEARCH.

**16S**: We'll try to keep it straight.

<hr>

<h2 id="PartI">Part I</h2>

**In which Everymeno discovers that usearch
doesn't necessarily map similar sequences to the same database entry**

<i>In this first discussion, Everymeno is confused about his OTU calling
pipeline. He gets dramatically different numbers of OTUs depending on
whether he uses</i> de novo <i>or reference-based OTU-calling.
16Socrates suggests a small</i> in silico <i>experiment that shows that
usearch is not guaranteed to map similar sequences to the same reference
OTU, thus increasing the number of OTUs that result from reference-based
OTU-calling with usearch.</i>

**16S**: So what's been bugging you, Everymeno?

**E**: First, I found that I get a lot more OTUs if I call OTUs by
USEARCH-ing against the 97%-identity reference OTUs in the [Greengenes
database](http://greengenes.secondgenome.com/) than I do if
I call <i>de novo</i> 97%-identity OTUs using the program usearch. I thought
they should give the same results or, if anything, I would get more OTUs
by clustering *de novo*, since there might be sequences in my
samples that aren't in the database.

**16S**: It sounds like you expected that using *de novo* or
reference-based OTU-calling at a similar sequence-identity should lead
to similar results.

**E**: Yes, but it doesn't stop there. When I saw these results, I
wondered what was happening, so I looked for sequences that got put into
the same OTU in the *de novo* clustering but ended up in different OTUs
in the reference-based clustering. These set of sequences are similar to
one another, but the taxonomies assigned by using USEARCH and the
Greengenes database include a lot of different genera and species! Why
are these sequences not put into the similar OTUs when I cluster using
the two different methods? And why should similar sequences have such
different taxonomies assigned to them?

**16S**: That sounds like a difficult question. Maybe we can do a
little experiment on a much simpler system to get a sense of what's
going on. Let's look at the very first sequence from the [trimmed,
processed 16S data](http://hmpdacc.org/HM16STR/) in the
[Human Microbiome Project](http://hmpdacc.org/) data.
It's a 292-nucleotide sequence with header:

`F48MJBB01DZOWV_cs_nbp_rc cs_nbp=29-315 sample=700014956
rbarcode=TCACAC primer=V3-V5 subject=158822939 body_site=Stool
center=WUGSC`

Let's use USEARCH to find a 97% OTU in Greengenes that matches this
sequence.

**E**: I found an OTU (4351920) whose representative sequence is a
97.3% match for my HMP sequence. I'm going to draw it like this: I put
the OTU in the center and draw concentric circles indicating the sets of
sequences that are ever-less-similar to the OTU. I'll mark the HMP
sequence somewhere just inside the 97% identity line.

<img src="/img/usearch/Picture2.png" width="40%">

**16S**: Let's see what happens if we have another sequence very
similar to this one. Does it end up in the same OTU?

**E**: I expect it would! To my mind, this is the whole point of OTU
calling: it's a way to put similar sequences together into fewer,
more-easily-interpreted units. That's what I take the "T" in OTU to
mean.

**16S**: In other words, you expect that very closely-related
organisms will have very closely-related 16S sequences, so you want to
put those in the same taxonomic unit?

**E**: Yes, exactly.

**16S**: Well, let's check that our OTU calling method puts very
similar sequences into the same OTU. To generate very similar sequences,
let's enumerate all the sequences that are one nucleotide different
from the HMP sequence. For each nucleotide in the original sequence,
I'll make three new sequences, replacing that nucleotide with the three
other nucleotides. This will make 292 × 3 = 876 sequences that are each
one nucleotide different from the original sequence.

**E**: So, since the original sequence starts `GTG`, the first new
sequence will start `ATG`, the next `CTG`, the next `TTG`, and then the next
`GAG`, and so on?

**16S**: That's right. Let's use the
[`usearch_global`](http://drive5.com/usearch/manual/cmd_usearch_global.html)
command, which performs the USEARCH algorithm, to find which reference
OTUs in the database these sequences belong with.

**E**: What [sequence identity
cut-off](http://drive5.com/usearch/manual/opt_id.html)
should I use? The reference OTUs are at 97% identity, so I think I
should use a 97% identity cut-off.

**16S**: Why?

**E**: Well, "97% OTUs" means that every sequence in an OTU is
at least 97% similar to the OTU's representative sequence. I expect
that my query sequence is covered by this database, so my sequence
should be in some OTU, meaning that it's 97% similar to something.

**16S**: That sounds reasonable to me!

**E**: Then I'll run the usearch command:

`usearch -usearch_global my_hmp_sequence.fasta -db 97_otus.fasta -id
0.97 -blast6out output.b6`

*Everymeno runs the command, and a worried look comes over his face.*

The results are confusing!

The first thing that bothers me is that only 16% of the 876 sequences we
made even have matches with the database. I'll draw a table, where
I'll write which OTU was hit, that OTU's taxonomy, and the number of
our 876 sequences that hit that OTU.

counts OTU                      Taxonomy
------ ------------------------ ------------------------------------
53     1121270                  `g__Kaistobacter; s__`
21     4351920 (original match) `g__Sphingomonas; s__wittichii`
20     367995                   `g__Kaistobacter; s__`
16     654742                   `g__; s__`
8      1094453                  `g__Kaistobacter; s__`
5      989109                   `g__Kaistobacter; s__`
5      949062                   `g__Kaistobacter; s__`
3      4311513                  `g__Kaistobacter; s__`
3      331282                   `g__Kaistobacter; s__`
2      1130183                  `g__Kaistobacter; s__`
1      4476892                  `g__Kaistobacter; s__`
1      4319592                  `g__Kaistobacter; s__`
1      30355                    `g__Kaistobacter; s__`
1      137881                   `g__Sphingomonas; s__wittichii`

The second thing that bothers me is that the OTU that matched the
greatest number of the one-nucleotide-different sequences (1121270)
isn't the one (4351920) that matched the original sequence! The third
thing that bothers me is that, although all the OTUs in the table have
the same phylogeny down to family (Sphingomonadaceae), they have
different genus and species names. The sequences in this fake data set
we made are at most two nucleotides different from one another. That's
less than 1% different. How can sequences that are 1% different from one
another end up in different genera?

<h2 id="PartII">Part II</h2>

**In which Everymeno investigates usearch's heuristic controls**

<i>In Part I, Everymeno discovered that USEARCH isn't guaranteed to map
similar query sequences to the same database sequence. 16Socrates helps
Everymeno understand how this unintuitive mapping works by conducting
another in silico experiment on USEARCH, and he's able to formulate
an explanation for his results from Part I.</i>

**16S**: I can see why you're distressed by those results! You put in
many similar sequences and USEARCH told you they mapped to reference
OTUs, not all of which are even in the same genus. I have a hunch about
what's going on. To see if I'm right, I'll ask a crazy question: what
happens if you turn the minimum sequence identity requirement *down*?

**E**: You mean, allow *worse* matches between my query sequences and
the database? I'm not sure why that's a good idea, but I'll try it.
I'll run the same command I did before with only a 90% identity cutoff,
so I'll replace `-id 0.97` with `-id 0.90`.

*Everymeno runs the command.*

Now I'm even more confused! These hits are different than my first set
of hits. Most of these hits are to an OTU (3937304) that didn't even
appear in my first search. Also, the sequence identities I got with a
97% cut-off ranged from 97.3% to 99.3%, but all of these hits are
at *least* 99.3%! Why should allowing *worse* hits somehow produce only
*better* hits? And different ones?

**16S**: I think I can resolve some of your confusion. USEARCH is a
[heuristic](http://drive5.com/usearch/manual/aln_heuristics.html)
algorithm, meaning that it's not guaranteed to find the *best* hit, it
just finds *a* hit that matches your criteria.

**E**: So it sounds like, when we ran our first experiment with the
slightly different query sequences, USEARCH could have reported that all
those sequences mapped to the same OTU, since that would have met the
identity threshold we set?

**16S**: That sounds right.

**E**: Well, why didn't it? I suppose I should read some of
usearch's documentation to figure that out.

*He spends some time flipping through the manual.*

I have a little hypothesis: in usearch's documentation, it says that
usearch works by [somehow organizing the database
sequences](http://www.drive5.com/usearch/manual/usearch_algo.html)
by their [*k*-mer
content](https://en.wikipedia.org/wiki/K-mer). When we
changed the one nucleotide in our query sequences, we changed
many *k*-mers.

**16S**: I suppose that's possible, but I haven't heard a lot
about *k*-mers, so I'm not sure I can relate to how your thinking about
this problem. Is there another way we can get insight into how USEARCH
is making matches?

<hr>
<h2 id="PartIII">Part III</h2>

**In which Everymeno discovers that usearch can produce many "good" hits**

<i>In Part II, Everymeno showed how USEARCH's heuristics could lead to
the weird results he saw in Part I, where similar query sequences mapped
to different database sequences. At the end of Part II, 16Socrates
challenged Everymeno to formulate a simple way to investigate what kind
of mapping USEARCH is doing. Everymeno runs this experiment but runs
into problems when he tries to apply the approach he devises to OTU
calling.</i>

**E**: One way to see what kinds of hits USEARCH can make would be to
have it report *all* the matches it finds, not just the first one that
meets its accepting criteria. I read in the
[documentation](http://drive5.com/usearch/manual/termination_options.html)
that you can do that by setting `-maxaccepts 0 -maxrejects 0`. I expect
that this will give a lot of hits, so let's do something simple: I'll
use only the original HMP sequence and 97% identity cutoff, but I'll
have usearch show me all the hits. That command is:

`usearch -usearch_global my_hmp_sequence.fasta -db 97_otus.fasta -id 0.97 -maxaccepts 0 -maxrejects 0`

*Everymeno runs the command. For the first time, he looks less worried.*

Well, that makes me feel a little better. Of the 34 hits that are here,
one is the hit we got in the very first search (4351920) and one is the
best hit we got when we relaxed the sequence identity cutoff to 90%
(3937304). I'll write down the results in a table.

  **OTU**                                    **hit identity**  
  ------------------------------------------ ------------------
  3937304 (90% identity hit)                 99.7              
  4447334                                    99.3               
  4437581                                    99.3               
  4319592                                    99.3               
  113180                                     99.0
  1121270 (matched many one-different-HMP)   99.0                 
  1094453                                    99.0                 
  849863                                     98.6               
  654742                                     98.6               
  4465896                                    98.6               
  4358484                                    98.6               
  809715                                     98.3               
  4311513                                    98.3               
  367995                                     98.3               
  247509                                     98.3               
  137881                                     98.3               
  1130183                                    98.3               
  4476892                                    97.9
  4453972                                    97.9
  364155                                     97.9
  364155                                     97.9
  1136270                                    97.9
  838596                                     97.6
  4311514                                    97.6
  4258048                                    97.6
  3188693                                    97.6
  2294362                                    97.6
  1129668                                    97.6
  989109                                     97.3
  824146                                     97.3
  4351920 (original hit)                     97.3
  4305723                                    97.3
  1787355                                    97.3
  143386                                     97.3
  1125792                                    97.3


**16S**: Why don't you think people normally take this
show-me-everything approach?

**E**: Well, I know that showing all the hits is slower than just
taking the first hit, but it didn't seem that much slower: I think the
heuristic speedup in USEARCH comes mostly from efficient look-ups in the
reference database, not in the actual alignments, so reporting multiple
possible hits doesn't seem that bad.

I suppose it's also confusing if you have a tie among your good hits.
What should you do? Just assign that sequence randomly to one of the two
OTUs? Or should you pick the OTU that most of your other sequences have
fallen into? That sounds fraught.

But I think the worst part is the existential bellyache this is causing
me: if the heuristic search can give me so many sequences to which my
sequence is a good match, isn't something going wrong?

<hr>

<h2 id="PartIV">Part IV</h2>

**In which Everymeno learns how sequence identity can vary between query and database sequences.**

<i>At the end of Part III, Everymeno raised some questions about how to
apply the lessons he learned, namely, how to see all the sorts of hits
that usearch might report. He's troubled by the number of possible hits
usearch reports. In this part, 16Socrates challenges Everymeno to
explain how one query sequence can appear to map to so many reference
OTUs.</i>

**16S**: Everymeno, I'm also confused by the number of "acceptable"
hits usearch is giving us. I'm particularly troubled by one thing, and
maybe you can explain. We're using the 97% Greengenes OTUs, so I would
think, because these OTUs were called at 97% identity, that each OTU's
representative sequence is at least 3% different from any other OTU's
representative sequence. Correct?

**E**: I can see how you're trying to trick me! What you said might
not be true. We said before that "97% OTUs" means that each sequence
in an OTU is at most 3% different from the representative OTU sequence.
It's like this picture here: any sequence within the circle of at least
97% identity ---that is, at most 3% difference--- could be assigned to
the OTU.

<img src="/img/usearch/Picture3.png" width="30%">

This doesn't necessarily mean that every OTU is 3% different from every
other one. That's what this next picture shows.

<img src="/img/usearch/Picture4.png" width="40%">

I suppose it wouldn't be a very good OTU-calling algorithm if we had a
bunch of OTUs, all 1% different from one another, like in this third
picture. You would have too many choices about how to assign sequences
to OTUs while still keeping the 97% sequence-to-OTU identity rule: all
of the sequences that fall inside both circles could be assigned to
either OTU.

<img src="/img/usearch/Picture5.png" width="40%">

**16S**: I understand these pictures, but they've made me confused
about something else. You said that you would want your 97% OTU calling
algorithm to give OTUs who representative sequences are more like 6%
different rather than 1% different?

**E**: That's right. If OTUs are too similar to one another, you'll
have too many choices about how to assign sequences to them.

**16S**: So you're saying that, if the Greengenes 97% OTUs were
called according to this rule, then we would expect that most OTUs will
be more like 6% different rather 1% different from one another? That is,
that it's unlikely ---but not impossible--- to find two OTUs that are
99% similar to one another?

**E**: Yes, I think that's right, although I feel a little pedantic
for making you say it that way!

**16S**: Then here's my confusion: We said it's unlikely to find two
OTUs that are 99% similar, but in your last USEARCH, we saw that one
query sequence hit multiple OTUs with 99% identity. How can one sequence
be 1% different from two OTUs that should be around 6% different from
one another?

<img src="/img/usearch/Picture6.png" width="40%">

**E**: I can see how you're trying to trick me, 16Socrates, but I
know about the Greengenes database! The sequences in the database are
long ---1,400 nucleotides is typical--- while amplicon reads are short,
like our 292 nucleotide HMP sequence. The OTUs in the database are at
least 3% different across their *entire sequence*, so they could in
theory be identical over the region that our short sequence is matching.
Thus, our 292 nucleotide sequence is 1% different from a \~292
nucleotide subsequence in the Greengenes OTUs, while those OTUs may be
more different from one another over their entire \>1,000 nucleotide
length.

<img src="/img/usearch/Picture7.png" width="60%">

**16S**: *I'm not sure it was a trick, but that was tricky!

**E**: I guess this clears up what I was confused about in the very
beginning: my original HMP sequence was a good fit over its short length
to many reference OTUs, and USEARCH's heuristics meant that slightly
different query sequences got mapped to fairly dissimilar reference OTUs
that were nevertheless good matches to the query sequences over their
short length. When I did my OTU calling, I expected that USEARCH would
map similar sequences in my samples to the same reference OTU, but I can
see now that USEARCH isn't at all guaranteed to do that!

<hr>
<h2 id="PartV">Part V</h2>

**In which Everymeno applies what he's learned to OTU calling**

<i>In Part IV, Everymeno explained how a single, short query sequence can
hit many reference OTU sequences ---which are all fairly different from
one another--- with high identity, and he synthesizes the results of his
experiments about USEARCH's heuristic features to explain his original
search results. In this part, he and 16Socrates puzzle about how to
apply these lessons to their future OTU-calling efforts.</i>

**16S**: S*ince you like tricky questions, I'll ask, does all this
confusing mess mean that USEARCH is bad? Should we not use USEARCH?

**E**: What I learned from talking with you is that USEARCH is good at
what it does: it's a heuristic search algorithm. It finds approximate
matches for my sequences in the database. It's not designed to give the
single, best hit. I was expecting it to do that, and so I was
disappointed.

**16S**: Bravo! And a final follow-up: What does this mean for OTU
calling? How can we be sure that similar sequences in your experimental
data will end up in similar OTUs and be assigned the same taxonomies?

**E**: I suppose I can't rely on the USEARCH algorithm to do that,
necessarily. I suppose that, if I want to be sure that similar sequences
end up in the same OTU, I'll either have to use a much [slower,
non-heuristic reference-based
search](http://www.drive5.com/usearch/manual/cmd_search_global.html) or
just cluster *de novo* first.

A tool that doesn't rely as strongly on alignments might also work.
When I use
[RDP](http://rdp.cme.msu.edu/classifier/classifier.jsp) on
the 876 one-nucleotide-changed sequences, 868 of them are assigned one
taxonomy (genus *Sphingomonas*), and only 8 get a different taxonomy
(genus *Sphingosinicella* in the same family).

**16S**: Well, Everymeno, we worked through this idea so quickly,
maybe next time we should take up a more difficult problem, like the
[definition of
virtue](https://en.wikipedia.org/wiki/Meno)!

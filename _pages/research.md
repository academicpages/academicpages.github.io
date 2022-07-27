---
layout: archive
title: "Research Overview"
permalink: /research/
author_profile: true
redirect_from:
  - /research
---

My primary area of research is Programming Languages. These are the interface
between human problem solvers and actual computation: programming languages
provide the necessary abstractions for expressing an executable solution to a
computational problem and, as such, are also the medium for analyzing a given
solution (i.e., program) for qualities such as correctness, security, and
reliability.
{: style="text-align: justify;"}

Programming Languages is a broad area containing many interesting research
problems; it also is open to different approaches to those problems ranging from
formal and rigorous theoretical work to pragmatic implementations of complex
real-world systems. Within this area, my particular focus is on building tools
to help developers create quality solutions, particularly solutions that are
error-free and secure. To do so, I rely on programming language theory to
provide a principled approach and use that theory as a lever for building
practical systems that solve real-world problems.
{: style="text-align: justify;"}

My research has followed three distinct paths within my focus of interest:
{: style="text-align: justify;"}

1. Building tools for improving the quality of traditional software systems;

2. Applying programming language concepts and techniques to build tools for
hardware design; and

3. Applying the same concepts and techniques to build tools for Computer Science
Education.
{: style="text-align: justify;"}

## Tools for Software Quality

My graduate work focused on pointer analysis, a fundamental analysis for
understanding the behavior of programs and a critical component of any static
analysis tool for investigating program correctness and security. I created new,
innovative pointer analysis algorithms that significantly outperformed the
current state of the art. Once I started my own research lab I finished off some
remaining work on pointer analysis and then expanded my interests more broadly.
My new main focus was static analysis of JavaScript.
{: style="text-align:justify;"}

JavaScript is a dynamic language that is difficult to statically analyze while
remaining sound, reasonably precise, and practically useful. In fact, up to that
point no one had managed a sound JavaScript analysis; all existing JavaScript
analysis infrastructures explicitly gave up on soundness. Our basic research
question was whether a sound JavaScript analysis with useful precision and
performance was even possible. To tackle this question we turned to abstract
interpretation, a theoretical framework for provably sound static analysis. We
created a formal, executable concrete semantics for JavaScript (essentially a
formally-specified interpreter); we then lifted that semantics to an executable
abstract semantics specifying a static analysis that was provably a sound
over-approximation of the concrete semantics. We then used the resulting
analysis tool to build a security analysis for JavaScript-based browser addons,
demonstrating that we could soundly, precisely, and scalably derive important
information-flow properties of these addons in order to detect possible
malicious behavior.
{: style="text-align: justify;"}

While sound JavaScript static analysis was our main focus, we worked on
related projects as well:
{: style="text-align: justify;"}

-   An extension of abstract interpretation theory that showed control-flow
    sensitivity (e.g., flow- and context-sensitivity of various kinds), which
    previously was ignored by abstract interpretation frameworks, can be
    explained within the existing concept of *widening operators*. A practical
    outcome of this work was a method for implementing *tunable* control-flow
    sensitivity, i.e., being able to specify the sensitivity of an analysis
    after it has already been implemented, which we implemented and evaluated
    using our JavaScript analysis framework.
    {: style="text-align: justify;"}

-   A framework for automatically parallelizing certain types of static
    analysis, implemented and evaluated using our JavaScript analysis framework.
    {: style="text-align: justify;"}

-   A technique called *fixpoint reuse* for accelerating static analysis of
    dynamic languages like JavaScript when multiple versions of a program are
    being analyzed sequentially (e.g., as a browser addon is updated over time).
    {: style="text-align: justify;"}

-   A set of techniques for scalably implementing a JavaScript engine on top of
    a managed language runtime.
    {: style="text-align: justify;"}

Our research focus then shifted to problems in software testing. This may seem
like a significant departure from our static analysis work, but I view testing
as a form of *complete* program analysis---that is, rather than over-approximate
program behavior we under-approximate it. In this way, testing is complementary
to sound program analysis and provides a useful contrasting technique for
understanding program behavior. This shift was initially motivated by some
interesting problems that arose during our sound JavaScript analysis project
having to do with testing our formal semantics. How could we have confidence in
our formalization of such a complex language and our implementation of that
formalization? Testing seemed like a useful answer, but that led to another
problem: how to create large, comprehensive test suites of JavaScript programs
with which to test our work?
{: style="text-align: justify;"}

These questions led us to the area of *software fuzzing*, i.e., automatically
generating inputs for a system under test. However, our needs differed from the
majority of fuzzing work at the time: (1) our inputs were not simple types such
as bit-strings, but complex data structures with non-trivial invariants; and (2)
we weren't interested in detecting crashes but in detecting semantically
incorrect behavior of the system under test. We developed a novel technique for
generating these complex inputs using Constraint Logic Programming; the basic
idea is that we can specify the necessary invariants as logic programs and use
those programs to generate conforming inputs. Our first efforts were aimed at
generating JavaScript programs with non-trivial runtime behavior (e.g., that
didn't just terminate immediately with the value `undefined`). We then showed
that we can use the same technique to generate a number of interesting data
structures (e.g., splay trees, images, red-black trees, and more). Finally, we
collaborated with the Rust language development team to use our technique to
test the Rust type checker and help refine the Rust type system, by
automatically generating Rust programs that were guaranteed by construction to
be well-typed (or ill-typed). As an outgrowth of all of our fuzzing research, we
also created a new metric for comparing fuzzers against each other that does not
require any expert developer knowledge; this metric improves greatly on common
but methodologically flawed fuzzer comparison techniques.
{: style="text-align: justify;"}

As a side project unrelated to the above, we also worked on *cross-language
clone detection* (i.e., detecting repeated code across programs written in
different languages), which is relevant for applications written for multiple
platforms such as iOS and Android.
{: style="text-align: justify;"}

Our ongoing project in this space now is the problem of *Translating C to Safer
Rust*. Rust is explicitly designed to provide a safe alternative to systems
languages like C and C++ by statically guaranteeing memory- and thread-safety.
Our C-to-Rust project is motivated by the large amounts of existing C programs
comprising the world's critical computing infrastructure; our goal is to use
program analysis to automatically translate C programs into Rust programs such
that the Rust compiler can provide those guarantees (rather than falling back on
the `unsafe` code escape-hatch). We have done an extensive set of experiments
exploring this problem and potential avenues forward, and continue to work on
it.
{: style="text-align: justify;"}

## Tools for Hardware Design

This research path is motivated by my collaboration with the department's
Architecture Lab, consisting of Prof. Tim Sherwood and (for a time) Prof. Fred
Chong, and more recently adding Prof. Jonathan Balkind. Our first collaborative
effort targeted verifiably secure critical hardware systems. The Architecture
Lab was working in this space already, but had a number of issues they were
still trying to address. I brought a Programming Languages perspective to those
issues and offered some ideas, which led to our collaboration. We designed a
security-based type system and static analysis for Verilog which guaranteed that
a given hardware design has secure information flow, and implemented several
working processors with that guarantee.
{: style="text-align: justify;"}

An interesting question that arose during that project was about the primary
HW/SW interface, i.e., the ISA. This is the lowest level of abstraction for
which we can reason about a program's behavior, and requires the least amount of
Trusted Computing Base in order to do so. However, traditional existing ISAs
(such as x86) are extremely large, complex, and difficult to reason about. What
would an ISA look like if it was designed from scratch with verifiability in
mind? Our answer was an extremely novel, formally-specified ISA based on the
lambda calculus, and we showed: (1) that it could be reasonably implemented in
hardware; (2) that it could express critical software systems; and (3) that it
enabled much easier and more certain verification of safety and security
properties than traditional ISAs.
{: style="text-align: justify;"}

Our efforts and association with the Architecture Lab have led to four more
ongoing collaborative projects:
{: style="text-align: justify;"}

-   *Compositional Hardware Design.* Hardware is often broken into modules and
    designs are specified by composing those modules together. However, modules
    can have non-trivial (and non-obvious) restrictions and requirements for
    correct composition. We created a formal notion of "wire sorts" which can be
    used to annotate a module's interface, along with a provably correct set of
    restrictions on how modules are connected with respect to those annotations.
    Together, they guarantee that the resulting circuit is well-formed in a
    specific sense. Further work involves increasing the expressiveness of the
    annotations and the set of guarantees they can provide.
    {: style="text-align: justify;"}

-   *Hardware Decompilation.* We are investigating an entirely new problem
    called hardware decompilation, analogous to software decompilation. In this
    case, the goal is to take a netlist (a graph of wires and gates resulting
    from hardware synthesis) and reconstruct a higher-level program in an
    hardware description language (HDL). We have performed an initial step
    towards a solution called *loop rerolling*, the inverse of the traditional
    loop unrolling compiler optimization: we detect repeated logic in the
    netlist and restructure that logic as a loop in the higher-level HDL. The
    method leverages existing clone detection and program synthesis techniques.
    Further work involves reverse-engineering more programming abstractions,
    such as functions.
    {: style="text-align: justify;"}

-   *Designing Superconducting Circuits.* Superconducting circuits show a lot of
    promise as a possible next generation of digital circuits, however there
    are still a large number of unanswered questions and unsolved problems. We
    are tackling two related issues in this space: (1) designing a
    domain-specific language for describing, composing, simulating, and checking
    arbitrary superconducting gates and circuits; and (2) designing an algebraic
    formalism for describing the behaviors of superconducting circuits that
    enables us to verifiably safely transform circuits in order to optimize
    them. Further work involves iterating on the language and extending the
    formalisms.
    {: style="text-align: justify;"}

-   *Program Synthesis of Architectural Microcode.* Many modern processor
    microarchitectures dynamically translate ISA instructions into microcode
    (for example, to translate a CISC ISA into RISC-like micro-ops). Designing
    these microcoded architectures is complex and difficult; few academic groups
    explore this space due to this problem. We are exploring the idea of using
    program synthesis techniques to automatically synthesize a microcoded
    architecture, viewing the microcode as a form of "programming language". As
    a preliminary step, we have focused on automatically generating a
    processor's control logic given a description of its datapath and an ISA
    semantics.
    {: style="text-align: justify;"}

## Tools for Computer Science Education

I was motivated to begin this research path by a high-level problem that most
Computer Science departments face: a large population of students interested in
learning Computer Science coupled with a relative scarcity of instructors and
resources to help them do so. I experience this problem first-hand in the
undergraduate classes that I teach, and out of this experience came the thought
that I could apply my research on building tools for software developers and
hardware designers to the problem of building tools for students and instructors
in Computer Science courses in order to address this disparity.
{: style="text-align: justify;"}

We (meaning myself and those of my students who acted as my TAs) had already at
this point leveraged our research on language fuzzing (i.e., automatically
generating interesting programs in a given language) to create test suites for
grading various projects in our department's Compilers course and Programming
Languages course. We also adapted our work on cross-language clone detection to
target plagiarism detection (a problem distinct from clone detection due to its
adversarial nature). These were ad-hoc efforts, but planted the seed for a more
comprehensive ongoing project that I call *Mentor*.
{: style="text-align: justify;"}

Ultimately Mentor will provide assistance for a number of our courses, but at
the moment it targets our department's Automata and Formal Languages course. A
number of graduate and undergraduate students have worked and are working on
Mentor to continually expand its capabilities, and Mentor has been used in every
offering of this course since 2019. The main problem that I want Mentor to
address is automated student feedback. Studies show that students learn best
when they are provided fast and detailed feedback, however with so many students
and not enough instructors students often get assignments back weeks later and
with minimal commentary. Automated grading is a nice bonus that comes almost for
free with automated feedback. Currently, Mentor has the following capabilities:
{: style="text-align: justify;"}

-   Students can specify deterministic and nondeterministic finite automata,
    regular expressions, pushdown automata, context-free grammars, Turing
    machines, and hierarchical Turing machines in a simple domain-specific
    language and submit them online as problem solutions to get instantaneous
    feedback on correctness and hints about incorrect solutions;
    {: style="text-align: justify;"}

-   Instructors can automatically generate reasonable regular language
    construction problems (e.g., given a language provide a DFA/NFA/regular
    expression that describes that language) at various levels of difficulty.
    This capability is useful because the problems from most relevant textbooks
    have solutions available online.
    {: style="text-align: justify;"}

There is ongoing work to extend Mentor's capabilities for the Automata and
Formal Languages course (providing feedback on various types of proofs,
generating more kinds of problems, etc) and also to extend it beyond that course
(e.g., we are actively working on providing support for a course on Python
programming).
{: style="text-align: justify;"}

<hr>
Last Updated: July 2022

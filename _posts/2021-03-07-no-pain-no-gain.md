---
title: 'No pain no gain? Comparing 3 program analysis frameworks for C'
date: 2022-03-07
permalink: /posts/2022/03/no-pain-no-gain/
tags:
  - research
  - tooling
---

Program analysis methods often represent programs as graphs. These graphs should be automatically generated from the source code. There are many tools that have been implemented to do this, but they are often painful to set up. In this post, I will compare 3 program analysis frameworks which I have used to generate graph representations of C programs.

**TL;DR:** More powerful frameworks are more difficult to set up because they require compiler information or expose complex APIs.
- SrcML is great if all you need is the AST and you don't need 100% precision.
- Joern is great if you need the CFG or PDG for a large set of programs, and are OK with potentially parsing some programs incorrectly.
- LLVM is great if you want a rock-solid analysis and want to leverage complex program analysis passes used in the Clang compiler, and you can provide compiler information.

<figure>
  <img src="https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dkhrdd6e0293r9ledy0y.png">
  <figcaption>No pain ⇒ no gain. More pain ⇒ more gain???
(source: <a href="https://www.dreamstime.com/stock-illustration-gradual-development-muscle-building-weakling-to-steep-pitching-funny-cartoon-character-vector-illustration-isolated-image48375937">kharlamova</a>)
</figcaption>
</figure>

<!---
- LLVM is the fastest and most precise framework, but can be difficult to set up because it requires compiler information.
- Joern is the slowest framework and is not quite precise, but it does not require compiler information.
- SrcML is a great choice if all that is needed is the AST, but it does not provide the CFG.
--->

## Control flow what-now?

Different types of graphs are used for different analyses, depending on what information is needed [0]:
* Abstract Syntax Tree (AST): A tree representation of the tokens in a program which abstracts out details like parentheses, whitespace, and separators.
* Control Flow Graph (CFG): A graph representation where each node is a statement and each edge is a transition in control flow.
* Program Dependence Graph (PDG): A graph representation where each node is a statement and each edge is a control or data dependency. A variable is dependent on a statement if that statement affects the value of the variable.

I chose to study the relative benefits of 3 popular program analysis frameworks that I have used in my own research:
* [SrcML: an infrastructure for the exploration, analysis, and manipulation of source code](https://www.srcml.org/)
* [Joern: The Bug Hunter's Workbench](https://joern.io/)
* [LLVM: a collection of modular and reusable compiler and toolchain technologies](https://llvm.org/)

I evaluated the frameworks based on 3 criteria which we care about for any program analysis task.
* Speed: how fast is the framework?
* Precision: how precise is the resulting CFG?
* Ease of use: how much effort does it take to use the framework, esp. on a large set of programs?

All of these graph representations can be automatically generated from C source code, though the task is sometimes challenging.

## Challenges parsing C code

C programs are difficult to parse because the preprocessor allows arbitrary text substitution [1]. If preprocessor macros aren't defined, the parser can misinterpret the context of a certain chunk of code and parse it totally incorrectly. I call this _imprecision_ in my evaluation of the 3 frameworks.

C programs also require compiler information such as types and functions defined in header files in order to parse correctly [2]. These header files can be scattered all across the machine, and the standard library headers are are in different locations in different OS or distributions. The compiler information is usually passed to the parser by way of compiler flags such as `-I` or `-D`.

<figure>
  <img src="https://dev-to-uploads.s3.amazonaws.com/uploads/articles/yejf6uwhdglzftain6u9.png">
  <figcaption>Relative benefits of SrcML, Joern, and LLVM.
(source: original)
</figcaption>
</figure>

## SrcML

[SrcML](https://www.srcml.org/) is an XML format for source code.
It provides the AST in a language-independent format. It also preserves all characters, including whitespace, comments, and preprocessor macros.

SrcML can parse code with missing includes and libraries, which makes it a great fit for large-scale program analysis (on the order of millions of programs). However, this also means that the AST can be incorrect sometimes. The problem is worsened in the presence of preprocessor macros. The SrcML parser uses a set of heuristics to deal with these challenges, but it sometimes results in an incorrect AST.

The SrcML authors claim it is faster than a compiler (over 25KLOC/sec) [3]. I have observed that it does run very fast, and additionally can do all its processing in memory due to the fact that it outputs XML as text.

SrcML provides the AST but not the CFG or PDG. In order to obtain the CFG, then, we would have to implement an algorithm to generate the CFG based on the AST. Some projects have done this as part of their implementation (notably [srcSlice](https://github.com/srcML/srcSlice) and [srcPtr](https://github.com/srcML/srcPtr)), but I found it difficult to adapt these implementations for other uses.

The SrcML format is language-independent, so theoretically, you could write an analysis based on the XML format and apply it to all the languages supported (currently C, C++, C#, and Java).

Interestingly, SrcML is _reversible_, meaning a user can parse code into XML, edit the XML, then un-parse the XML back into code while preserving the edits. This allows some cool editing functionality, and I found it easier in some cases than editing the raw source code because I can locate the symbols I want to edit by traversing the XML tree.

The SrcML team was pretty responsive in my queries about their framework.

<!---
srcML
- Does not require compilation
- Faster than a compiler
  - “Lastly, the conversion to srcML is extremely efficient, running faster than a compiler (over 25KLOC/sec).” http://www.cs.kent.edu/~jmaletic/papers/ICSM13-srcML.pdf 
- No control/data flow implementation.
  - From Discord: “We do not have a specific tool to generate a control flow graph, but it should be pretty straight forward. We have a slicing tool srcSlice (see tools) - that computes control flow and data flow information on-the-fly as needed to compute a forward program slice.
  - Also, srcPtr does pointer analysis which also needs some control flow information. You can easily get conditionals and loop constructs using Xpath. Using srcSAX and just look for the branching events (if, while etc.) would be pretty easy. The code for all of these are in GitHub.”
  - https://github.com/srcML/srcSlice
  - https://github.com/srcML/srcPtr
- Multiple language support: C, C++, C#, Java
- Source-to-source translation approach. Validate the schema?
--->

## Joern

<!---
Does not require compilation
The implementation runs slower than srcML
Control/data-flow analysis available
Multiple language support: C/C++, x86/x64, JVM, LLVM Bitcode, Javascript
Manual rewriting
--->

[Joern](https://joern.io/) is a workbench which parses C/C++ code and generates a Code Property Graph (CPG). The CPG is a combination of AST, CFG, and PDG into one big graph, and it exposes information sufficient to perform a wide range of analyses. The main interface to the tool is a command-line interpreter which allows users to write custom queries in a DSL based on Scala.

Joern does not require compiler information, but uses a fuzzy parsing method known as _island grammars_ to parse the code as best as it can.

I found that the Joern implementation runs much slower than both SrcML and LLVM. This may be because of the choice of runtime platform: SrcML and LLVM are built with C++ and have narrow functionality, while Joern is built with Scala and is highly customizable/scriptable.

Multiple languages are supported: C/C++, x86/64 assembly, JVM, LLVM Bitcode, and Javascript. I've only tried C/C++, and these are the only languages marked as _high_ maturity on their [doc page](https://docs.joern.io/home#supported-languages).

Joern includes great utilities for analysis, but any modifications to the code must be manually pasted together. There is no support for rewriting or transformation.

The ShiftLeft team is very active in developing Joern, and they are helpful to users of their framework.

## LLVM

[LLVM](https://llvm.org/) is the granddaddy of all program analysis frameworks. It is a mature collection of tools designed for compiler development.

LLVM is the foundation of the Clang compiler, Clang Static Analyzer (CSA), klee, and many other well-known tools.
Because it's used in so many popular tools, it is optimized to be blazing fast.
LLVM exposes APIs for AST, CFG, and PDG information as well as [a whole host of other analyses](https://llvm.org/docs/Passes.html).
Basically, any information available to the compiler is available to the developer of an LLVM tool. As well, the information is 100% precise, as a compiler cannot tolerate incorrect information.

This power comes with a price - LLVM requires all types to be defined in order to parse the code correctly. Due to C's ambiguous grammar, if a type is not defined, then the compiler cannot tell the difference between a function definition and a variable definition, leading to errors in parsing (cite). If some definitions are missing, LLVM can produce a broken AST with large sections missing.

Usually, this information is provided by giving LLVM a set of compiler flags that would be used to compile the program. It can be difficult to get these flags if you want to analyze a lot of programs, since the flags are platform- and configuration-dependent.
This can introduce a lot of manual effort to obtain these flags, which can render LLVM infeasible for analyzing large-scale program datasets.

LLVM's analysis functionality only processes C/C++ at the source level. Additional utilities are available for LLVM IR, which is a low-level SSA assembly language which many other languages target.

LLVM provides the [Rewriter API](https://clang.llvm.org/doxygen/classclang_1_1Rewriter.html) for rewriting source code. I found these utilities to be very convenient in most cases, although in some cases when the location I want to rewrite was not exposed by the Clang AST, it was difficult to work around the rewriter API.

Finally, I found that the LLVM C++ API [LibTooling](https://clang.llvm.org/docs/LibTooling.html) can be intuitive and comfortable at times, but often the details are very complex and there are a lot of footguns.
I got better at using it from experience, but it still takes me a while to figure out [which ASTMatcher I should use](https://clang.llvm.org/docs/LibASTMatchersReference.html) or [whether to use the refactoring engine](https://clang.llvm.org/docs/RefactoringEngine.html).

<!---
Requires compilation, but has precise parsing; as good as a compiler
High-performance because it’s a compiler in widespread use (validate with benchmark)
Many analysis and transformation passes implemented
Only C/C++
Rewriting approach
--->

## Benchmark analysis

I implemented a simple refactoring tool with each framework in order to evaluate the speed of each tool.
The refactoring tool exchanges a `for` statement with a `while` statement. This can be done with AST only, though control-flow information is necessary in order to handle early `break`, `cont
inue`, or `return`. You can access the prototype's source code here: https://github.com/bstee615/pa_framework_examples.

Here is an example of the tool at work. When this program is input:

```c
int main()
{
    int x = 0;
    for (int i = 0; i < 10; i ++)
    {
        x += 1;
    }
    return x;
}
```

Then this program should be the output.

```c
int main()
{
    int x = 0;
    int i = 0;
    while (i < 10) {
      x += 1;
      i++;
    }
    return x;
}
```

I measured the runtime of my prototype tool in seconds on the example program, averaged over 5 runs.
The results are shown below. Format: Average ± std. deviation.

| LLVM | Joern | SrcML |
| --- | --- | --- |
| 0.0230s ± 0.0034s | 6.2906s ± 0.0034s | 0.0702s ± 0.0088s |

This evaluation shows the difference in startup times between the frameworks. In my research I have found that the startup time is a pretty large consideration, and the size of the program has a relatively small effect on the framework's performance.

LLVM and SrcML are pretty similar in performance for all practical matters. Notably, I used Python to invoke SrcML and parse the output XML. It may be slightly faster if I wrote it in C++ and linked with the SrcML library.

Joern was the slowest by far. This may be due to the overhead of starting up the Scala VM and Joern's interpreter.

<figure>
  <img src="https://dev-to-uploads.s3.amazonaws.com/uploads/articles/varxp2ea4y9zfxbjgrd5.png">
  <figcaption>Frameworks are multi-dimensional, not just lightweight/heavyweight.
(source: <a href="https://www.self.com/story/guide-to-navigating-free-weights-at-the-gym">Morgan Johnson</a>)
</figcaption>
</figure>

Each of these frameworks has its sweet spot in program analysis. In reality, analyzing real-world programs is difficult. There are many choices with different dimensions of pain/pleasure. I compared speed on a small example to highlight the differences between the frameworks. I suggest you do your own research into these 3 frameworks to figure out which one fits your application best. Most importantly, don't be dogmatic about using one approach over another - for example, supposing you are used to LLVM giving you compiler-level precision in your analyses, you may benefit from switching to Joern in order to speed up your development cycle.

## References
[0] F. Yamaguchi, N. Golde, D. Arp and K. Rieck, "Modeling and Discovering Vulnerabilities with Code Property Graphs," 2014 IEEE Symposium on Security and Privacy, 2014, pp. 590-604, DOI: https://doi.org/10.1109/SP.2014.44.

[1] Alejandra Garrido and Ralph Johnson. 2002. Challenges of refactoring C programs. In Proceedings of the International Workshop on Principles of Software Evolution (IWPSE '02). Association for Computing Machinery, New York, NY, USA, 6–14. DOI:https://doi.org/10.1145/512035.512039

[2] Bendersky, E. (2007, Nov). The context sensitivity of C's grammar. Eli Benderskys website ATOM. Retrieved March 3, 2022, from https://web.archive.org/web/20210713114717/https://eli.thegreenplace.net/2007/11/24/the-context-sensitivity-of-cs-grammar 

[3] M. L. Collard, M. J. Decker and J. I. Maletic, "srcML: An Infrastructure for the Exploration, Analysis, and Manipulation of Source Code: A Tool Demonstration," 2013 IEEE International Conference on Software Maintenance, 2013, pp. 516-519, DOI: https://doi.org/10.1109/ICSM.2013.85
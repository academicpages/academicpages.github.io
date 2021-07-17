---
title: "MIT OCW: Introduction to Computer Science and Programming in Python"
excerpt: "Introduction to Computer Science and Programming in Python from MIT Opencourseware"
collection: notes
date: 2021-07-17
permalink: /notes/MIT-OCW-CS-in-Python/
tags:
  - Course
  - MIT Opencourseware
  - Programming
  - Python
---

[Link to course](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)

### Goal 
Review computer science foundations and python fundamentals as I already took Software 1 and 2 using Java at Ohio State.  I anticipate being able to pick up on some nuances now that I'm not learning it for the first time and have professional programming experience.

## Lesson 1 - What is Computation

### Types of knowledge
- **declarative knowledge**: statements of facts (x = 16)
- **imparative knowledge**: recipe or how to do something (def sqrt(x): ...)

Recipes have steps, flow of control, termination criteria, etc. and therefore are algorithms

### Basic Machine Architecture:
- Memory: data & sequence of instructions
- Control unit: flow / interpreter (?)
- Arithmetic logic unit: does primitive instructions
- Input / output

### Basic primitives
- Turing showed you can compute anything using 6 primitives (move right, move left, read, write, scan, do nothing)
- therefore, anything computable in one programming language is computable in any other programming language

### Creating recipes:
- a programming language provides a set of primitive operations (words : float, bool, etc)
- expressions are complex but legal combinations of primitives (phrases, meaningful sentences : expressions operand operator)
- expressions have values and meanings in a programming language

### Languages
- static semantics: syntactically valid strings have meaning.  
  - "I are hungry" is *syntactically valid* (noun + verb + adjective), but has *static semantic error*
- semantics: meaning associated with syntactically correct string of symbols without semantic errors
  - English sentences can have many meanings (a *reading lamp* vs a *reading* lamp) but programming languages have only one meaning and it might not be what the programmer intended. 

### Languages & Errors
- syntactic errors are easily caught by the interpreter because the program can't run when it has them.
- static semantic errors are checked for by some programming languages before executing but may run and have unpredictable behavior.
- no semantic errors but poor logic could lead to crashes, won't stop, unexpected answer

### Python programs
- a program is a sequence of definitions and commands.
  - definitions are evaluated
  - commands are executed by the python interpreter in a shell
- commands (statements) instruct the interpreter to do something
- can be typed directly in a shell or stored in a file that is read into a shell

### Objects:
- programs manipulate **data objects**
- objects have a **type** that defines the kinds of things the program can do to them
- objects can be...
  - scalar (cannot be subdivided) 
    - In python, 4 scalar types: int, float, bool, NoneType
  - non-scalar (have internal structure that can be accessed) (list etc.)

### Expressions:
- expressions evaluate to a value, which has a type
- combine objects and operators to form expressions
- syntax for a simple expression could be <object> <operator> <object> or 1 + 2

### Operators on INTs and FLOATs
- sum + (result is float if at least one object is float)
- difference - 
- product *
- division / (result is always float)
- remainder % 
- power **

### Binding variables and values
- equal sign is an assignment of a value to a variable name
  - "variable = value"
- store in computer memory
- assignment binds name to value
- retrieve value by invoking the name

### Abstracting expressions
- using names rather than values in expressions allows you to run the code with different values by simply reassigning the variable rather than editing your expressions

### Programming vs Math
- in programming you need to provide expressions, you can't "solve for x"
- an assignment always has the expressions on the right evaluated to a value and a variable name on the left

### Changing bindings
- variable names can re-bind to new values by using a new assignment
- previous value may still by stored in memory but the handle for it is lost and left for the garbage collector


## Lesson 2 - 
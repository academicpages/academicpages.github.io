---
title: "CS61C Lab 3 (RISC-V Venus)"
excerpt: "This project will involve setting up and becoming familiar with Venus, the RISC-V simulator, while also learning the basics of the RISC-V assembly language, registers, memory access, and debugging. Using this lab I was able to understand how to write, execute, and troubleshoot simple RISC-V programs.<br/><img src='/images/risc/riscv1.png'>"
collection: portfolio
---
December 2024

Disclaimer: The content presented here reflects my understanding of materials from UC Berkeley's CS61C course "Great Ideas of Computer Architecture (Machine Structures)" Lab 3, and while it includes my own contributions, it is not entirely my original work.

For this project I plan to prepare working with RISC-V assembly and debugging tools such as Venus. Here's a summary of the steps and key concepts covered:
# Setup:
For this project I cloned into the git repository using GIT Bash.

```bash
$ git clone https://github.com/61c-teach/fa24-lab-starter.git
```

Thereafter, I installed tools necessary for this lab using the command:

```bash
$ bash tools/download_tools.sh
```

Also I did need to install the latest version of java.

And with that, my machine was practically ready.

# Exercise 1: Venus Basics
We use Venus so that any changes made on our local machine can replicate themselves to Venus web's frontend and vice versa.

In my cloned project labs folder I needed to expose my projects directory by using an open port and the command:

```bash
$ java -jar tools/venus.jar . -dm
```

![javalinLogo](/images/risc/riscv1.png)

Now if I open Venus on my local web browser, I can now see the web terminal and we can mount our local machines project folder to this website. This way if we apply any changes in either place, the changes will replicate respectively.

We can do this by performing the command in our Venus terminal:

```bash
$ mount local labs
```

![](/images/risc/riscv2.png)

As we can see it asks for an authentication key which we can see in our local machines terminal. Successfully providing this key to Venus will then link our files like we wish.

Navigating to our files tab, we can now see the success.

![](/images/risc/riscv3.png)

Now we're ready to really get to the fun!

# Exercise 2: Venus Basics

In this exercise we're asked to answer all eleven questions.
We will do so here,

### Walkthrough Exercise 2:

First though, we must open the respective file, "fib.s" in our project folder.
  + Question 1: What is the machine code of the highlighted instruction? The answer should be a 32 bit hexadecimal number, with the 0x prefix.
  ![](/images/risc/riscv4.png)
  >0x000002B3

  + Question 2: What is the machine code of the instruction at address 0x34? The answer should be a 32 bit hexadecimal number, with the 0x prefix.
  ![](/images/risc/riscv5.png)
  >0x00000073

On the right side of our screen we also have a "registers" tab, which we can use to see all 32 bit registers.
  + Question 3: What is the value of the sp register? The answer should be a 32 bit hexadecimal number, with the 0x prefix.
  ![](/images/risc/riscv6.png)
  >0x7FFFFFE0

We're asked to continue stepping until the value in the register 't1' changes. Our initial value is:
  ![](/images/risc/riscv7.png)
  >0x00000000

At offset 0x8 we see the change:
  + Question 4: What is the new value of the t1 register? The answer should be a 32 bit hexadecimal number, with the 0x prefix.
  ![](/images/risc/riscv8.png)
  >0x00000001

It's also asking for the machine code of the current instruction:
  + Question 5: What is the machine code of the current instruction? The answer should be a 32 bit hexadecimal number, with the 0x prefix.
  ![](/images/risc/riscv9.png)
  >0x10000E17

Stepping until offset 0x10, we're then asked:
  + Question 6: What is the value of the t3 register? The answer should be a 32 bit hexadecimal number, with the 0x prefix.
  ![](/images/risc/riscv10.png)
  >0x10000000

We're also asked what it points to, and we can see this instruction says "lw x28 0(x28)", the 0(x28) is key to me showing a dereference of an address. So lets take its address and find what it points to.
  + Question 7: What is the byte that t3 points to? The answer should be an 8 bit (1 byte) hexadecimal number, with the 0x prefix.
  ![](/images/risc/riscv11.png)
  >0C

Next, we're asked to set a breakpoint on offset 0x28, and find the value in the t0 register.
  + Question 8: What is the value of the t0 register? The answer should be a 32 bit hexadecimal number, with the 0x prefix.
  ![](/images/risc/riscv12.png)
  >0x00000001

Stepping into the loops breakpoint six more times like asked, we need to find the new value of the t0 register.
  + Question 8: What is the value of the t0 register? The answer should be a 32 bit hexadecimal number, with the 0x prefix.
  ![](/images/risc/riscv13.png)
  >0x0000000D

Now we're asked to change from hexadecimal and read the decimal value:
  + Question 10: What is the value of the t0 register in decimal? The answer should be a decimal number without a prefix.
  ![](/images/risc/riscv14.png)
  >13

Running the program until it finishes we're lastly asked:
  + Question 11: What is the output of the program? The answer should be a decimal number without a prefix.
  ![](/images/risc/riscv15.png)
  >144

# Exercise 3: Using Memcheck

In this exercise we're asked to answer seven new questions for exercise 3, using memcheck.

What is memcheck? These are basically two different modes for debugging our assembly level programs.
>Normal mode: shows our invalid reads or writes to memory, if there is unfreed memory at the end of the program it will notify us of this size.
>Verbose mode: this also prints out invalid reads and writes to memory, however it now includes a list of blocks of memory not freed upon finishing the program.

We will answer the questions again, here.

First things first, we need to open ex3_memcheck.s in our Venus online editor and get a general idea of it's behavior.
After running the program, it looks like we're running into an error message, and asked to:
  + Question 1: What address did the program try to access, but caused the error? The answer should be a 32 bit hexadecimal number, with the 0x prefix.
  ![](/images/risc/riscv16.png)
  >0x10008058

We're also asked:
  + Question 2: How many bytes was the program trying to access? The answer should be a decimal number without a prefix.
  >4 bytes

Seeming like a memory error, we go ahead and turn on memcheck in Venus editor to get more details.
  + Question 3: What address did the program try to access, but caused the error? The answer should be a 32 bit hexadecimal number, with the 0x prefix.
  ![](/images/risc/riscv17.png)
  >0x10008080

  + Question 4: How many bytes were allocated in the block related to the error? The answer should be a number without units.
  >40

  + Question 5: Which line of the source file caused this error? The answer should be a number.
  >Line 18

Trying to debug this error and recalling that register t1 contains the loop counter we're asked:
  + Question 6: What is the value of t1 based on the memcheck error message? The answer should be a decimal number.
  ![](/images/risc/riscv18.png)
  >11

We're asked to fix this error in the source code, and we know it was on line 18 so, lets try and find the bad actor:

<details>
<summary>Original Source Code (with errors)</summary>
  <pre>
  <code class="language-assembly">
  .import utils.s

  .text
  main:
      # This program will fill an array of size 10 with 0's

      # Allocate an array of size 10
      li a0 40   # 10 ints, 4 bytes each
      jal malloc # malloc is defined in utils.s
      mv t0 a0   # the pointer is returned in a0

      # Fill the array with 0's
      li t1 0  # t1 is the index
      li t2 10 # t2 is the size of the array

  loop:
      # Store 0 at the current index
      sw x0 0(t0)
      # Increment the index
      addi t1 t1 1
      # Increment the pointer
      addi t0 t0 4
      # Check if we are done
      # If not, loop
      bge t1 t2 loop

      # Exit the program
      li a0 0
      jal exit
  </code>
  </pre>
</details><br>

<details>
<summary>Fixed Source Code (for this step)</summary>
  <pre>
  <code class="language-assembly">
  .import utils.s

  .text
  main:
      # This program will fill an array of size 10 with 0's

      # Allocate an array of size 10
      li a0 40   # load immediate (const) 10 ints, 4 bytes each
      jal malloc # malloc is defined in utils.s
      mv t0 a0   # the pointer is returned in a0

      # Fill the array with 0's
      li t1 0  # t1 is the index
      li t2 10 # t2 is the size of the array

  loop:
      # Store 0 at the current index
      sw x0 0(t0)
      # Increment the index
      addi t1 t1 1
      # Increment the pointer
      addi t0 t0 4
      # Check if we are done
      # If not, loop
      bge t1 t2 loop              #swapped because we need t1 (the i'th element)to be greater than or equal to t2 (the size).

      # Exit the program
      li a0 0
      jal exit

    </code>
    </pre>
</details><br>

After running our program again, we're asked:
  + Question 7: How many bytes were not freed when the program exited? The answer should be a decimal number without units.
  ![](/images/risc/riscv19.png)
  >40

Now we're asked to run memcheck in verbose mode:
  + Question 8: What is the address of the block that was not freed? The answer should be a 32 bit hexadecimal number, with the 0x prefix.
  ![](/images/risc/riscv20.png)
  >0x10008030 is the starting address of this memory blocks

We're asked to fix This

<details>
<summary>Original Source Code (from this step)</summary>
  <pre>
  <code class="language-assembly">
  .import utils.s

  .text
  main:
      # This program will fill an array of size 10 with 0's

      # Allocate an array of size 10
      li a0 40   # load immediate (const) 10 ints, 4 bytes each
      jal malloc # malloc is defined in utils.s
      mv t0 a0   # the pointer is returned in a0

      # Fill the array with 0's
      li t1 0  # t1 is the index
      li t2 10 # t2 is the size of the array

  loop:
      # Store 0 at the current index
      sw x0 0(t0)
      # Increment the index
      addi t1 t1 1
      # Increment the pointer
      addi t0 t0 4
      # Check if we are done
      # If not, loop
      bge t1 t2 loop              #swapped because we need t1 (the i'th element)to be greater than or equal to t2 (the size).

      # Exit the program
      li a0 0
      jal exit

    </code>
    </pre>
</details><br>

<details>
<summary>Fixed Source Code (no errors)</summary>
  <pre>
  <code class="language-assembly">
  .import utils.s

  .text
  main:
      # This program will fill an array of size 10 with 0's

      # Allocate an array of size 10
      li a0 40   # load immediate (const) 10 ints, 4 bytes each
      jal malloc # malloc is defined in utils.s
      mv t0 a0   # the pointer is returned in a0

      # Fill the array with 0's
      li t1 0  # t1 is the index
      li t2 10 # t2 is the size of the array

  loop:
      # Store 0 at the current index
      sw x0 0(t0)
      # Increment the index
      addi t1 t1 1
      # Increment the pointer
      addi t0 t0 4
      # Check if we are done
      # If not, loop
      bge t1 t2 loop              #swapped because we need t1 (the i'th element)to be greater than or equal to t2 (the size).

      # Exit the program
      jal free                    #must place before setting a0 to 0 because this creates something like a dangling ptr. or a memory leak bc it's not freed.
      li a0 0
      jal exit

    </code>
    </pre>
</details><br>

This gives our code a successful run and zero bytes of memory in use at exit:
![](/images/risc/riscv21.png)

# Exercise 4: Array Practice

If we consider the discrete value function on integers in set {-3, -2, -1, 0, 1, 2, 3}. With the function definition:
```
f(-3) = 6
f(-2) = 61
f(-1) = 17
f(0) = -38
f(1) = 19
f(2) = 42
f(3) = 5
```

We can implement a function 'f:' such that all output values stored in the output array go through register a1, AND we can index into ths array and get the correct associated output.

<details>
<summary>Provided Code:</summary>
  <pre>
  <code class="language-assembly">
  .import ex4_discrete_fn.s

  .data
  # asciiz is a directive used to store strings
  # asciiz will automatically append a null terminator to the end of the string
  neg3:   .asciiz "f(-3) should be 6, and it is: "
  neg2:   .asciiz "f(-2) should be 61, and it is: "
  neg1:   .asciiz "f(-1) should be 17, and it is: "
  zero:   .asciiz "f(0) should be -38, and it is: "
  pos1:   .asciiz "f(1) should be 19, and it is: "
  pos2:   .asciiz "f(2) should be 42, and it is: "
  pos3:   .asciiz "f(3) should be 5, and it is: "

  output: .word   6, 61, 17, -38, 19, 42, 5

  .text
  main:
  	######### evaluate f(-3), should be 6 #########
      # load the address of the string located at neg3 into a0
      # this will serve as the argument to print_str
      la a0, neg3
      # print out the string located at neg3
      jal print_str
      # load the first argument to f into a0
      li a0, -3
      # load the second argument of f into a1
      # `output` is a pointer to an array that contains the possible output values of f
      la a1, output
      # execute f(-3)
      jal f
      # f will return the output of f(-3) into register a0
      # to print out the return value, we will call print_int
      # print_int expects the value that it's printing out to be in register a0
      # the output of the function is already in a0, so we don't need to move it
      jal print_int
      # print a new line
      jal print_newline

  	######### evaluate f(-2), should be 61 ########
      la a0, neg2
      jal print_str
      li a0, -2
      la a1, output
      jal f
      jal print_int
      jal print_newline

  	######### evaluate f(-1), should be 17 ########
      la a0, neg1
      jal print_str
      li a0, -1
      la a1, output
      jal f
      jal print_int
      jal print_newline

  	######### evaluate f(0), should be -38 ########
      la a0, zero
      jal print_str
      li a0, 0
      la a1, output
      jal f
      jal print_int
      jal print_newline

  	######### evaluate f(1), should be 19 #########
      la a0, pos1
      jal print_str
      li a0, 1
      la a1, output
      jal f
      jal print_int
      jal print_newline

  	######### evaluate f(2), should be 42 #########
      la a0, pos2
      jal print_str
      li a0, 2
      la a1, output
      jal f
      jal print_int
      jal print_newline

  	######### evaluate f(3), should be 5 #########
      la a0, pos3
      jal print_str
      li a0, 3
      la a1, output
      jal f
      jal print_int
      jal print_newline

  	# passing 10 to ecall will terminate the program
      li a0, 10
      ecall

  # prints out one integer
  # input values: a0: the integer to print
  # does not return anything
  print_int:
  	# to print an integer, we need to make an ecall with a0 set to 1
      # the thing that will be printed is stored in register a1
      # this line copies the integer to be printed into a1
      mv a1, a0
      # set register a0 to 1 so that the ecall will print
      li a0, 1
      # print the integer
      ecall
      # return to the calling function
      jr    ra

  # prints out a string
  print_str:
      mv a1, a0
      li a0, 4 # tells ecall to print the string that a1 points to
      ecall
      jr    ra

  print_newline:
      li a1, '\n'
      li a0, 11 # tells ecall to print the character in a1
      ecall
      jr    ra

      </code>
      </pre>
</details><br>

<details>
<summary>Expected Code (Starting Point)</summary>
  <pre>
  <code class="language-assembly">
  .globl f # this allows other files to find the function f

  # f takes in two arguments:
  # a0 is the value we want to evaluate f at
  # a1 is the address of the "output" array (read the lab spec for more information).
  # The return value should be stored in a0
  f:
      # Your code here

      # This is how you return from a function. You'll learn more about this later.
      # This should be the last line in your program.
      jr ra

  </code>
  </pre>
  </details><br>

<details>
<summary>Expected Code (Working)</summary>
  <pre>
  <code class="language-assembly">
  .globl f # this allows other files to find the function f

  # f takes in two arguments:
  # a0 is the value we want to evaluate f at
  # a1 is the address of the "output" array (read the lab spec for more information).
  # The return value should be stored in a0
  f:
      # Your code here

     addi t0 a0 3 #adding const 3 to index and storing in temp 0 (index = x + 3 in this case)
     slli t1 t0 2 #shifting left logical immediate (multiply by 2^n, 4 in this case) and store it in temp 1, multiplying index by size of each element in array
     add t1 t1 a1 #add this offset to address of array to get address of element we wish to read
     lw a0, 0(t1) #reading element

  #a0 index; a1 array base addy


      # This is how you return from a function. You'll learn more about this later.
      # This should be the last line in your program.
      jr ra
  </code>
  </pre>
</details><br>

Explanation:
>The thought process is added in comments in the code snippets but essentially we added an immediate value 3 to the register a0 which holds our index to get to the correct starting point and stored it in a temp register t0. Then to multiply by 4 (size of a word) we can shift the bits left two times which gives us a multiplication of 2^2 so 4, and store this value t1. This is what we'll add every time to register a1 (our base address for the values) to get to the next element. Then we load the element into memory so we can print it. This is essentially what we did here.

# Exercise 5: Factorial

In this exercise we are implementing a factorial function in risc-v. Taking a single integer parameter n, and returning n!.

<details>
<summary>Starting Code:</summary>
  <pre>
  <code class="language-assembly">
  .globl factorial

  .data
  n: .word 8

  .text
  # Don't worry about understanding the code in main
  # You'll learn more about function calls in lecture soon
  main:
      la t0, n
      lw a0, 0(t0)
      jal ra, factorial

      addi a1, a0, 0
      addi a0, x0, 1
      ecall # Print Result

      addi a1, x0, '\n'
      addi a0, x0, 11
      ecall # Print newline

      addi a0, x0, 10
      ecall # Exit

  # factorial takes one argument:
  # a0 contains the number which we want to compute the factorial of
  # The return value should be stored in a0
  factorial:
      # YOUR CODE HERE

      # This is how you return from a function. You'll learn more about this later.
      # This should be the last line in your program.
      jr ra
  </code>
  </pre>
</details><br>

<details>
<summary>Working Code:</summary>
  <pre>
  <code class="language-assembly">
  .globl factorial

  .data
  n: .word 5

  .text
  # Don't worry about understanding the code in main
  # You'll learn more about function calls in lecture soon
  main:
      la t0, n
      lw a0, 0(t0)
      jal ra, factorial

      addi a1, a0, 0
      addi a0, x0, 1
      ecall # Print Result

      addi a1, x0, '\n'
      addi a0, x0, 11
      ecall # Print newline

      addi a0, x0, 10
      ecall # Exit

  # factorial takes one argument:
  # a0 contains the number which we want to compute the factorial of
  # The return value should be stored in a0
  factorial:
      # YOUR CODE HERE
      #n! = n * (n-1)*(n-2)*...*1

      #base case if a0 == 0, we return 1
      beqz a0, return_one

      #initialize result to 1
      li t0, 1        #t0 = 1 (holding result)

  factorial_loop:
      #multiply t0 (result) by current value in a0 (n)
      mul t0, t0, a0 #t0 = t0 * a0

      #decrement a0 (n) by 1
      addi a0, a0, -1 #a0 = a0 - 1

      #If a0 > 0, continue (branch not equal zero)
      bnez a0, factorial_loop

      #return our result in register a0 before returning ()
      mv a0, t0
      jr ra

  return_one:
      li a0, 1
      jr ra

      #place return value in register a0 before returning ()

      # This is how you return from a function. You'll learn more about this later.
      # This should be the last line in your program.
      jr ra
  </code>
  </pre>
</details><br>

Explanation:
>Essentially, this exercise tailored me to learn about a base case, if n = 0 we just return 1. Otherwise we needed to create a loop in risc-v to continiously multiply n by (n-1) by (n-2) until our n reached zero, breaking out of the loop; giving us n!. Again, each of my thought processes are again explained in the comments of the code.

Testing 8!
![](/images/risc/riscv22.png)
>40320 :)

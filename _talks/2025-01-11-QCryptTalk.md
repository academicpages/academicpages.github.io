---
title: "Quantum Cryptography"
collection: talks
type: "Student talk"
permalink: /talks/2025-01-11-QCryptTalk
venue: "IISER-Mohali"
date: 2025-01-11
location: "Mohali, India"
---
Presented an in-house talk as part of a batch initiative (Catching Up With the Fields), in which I gave a brief introduction to quantum cryptography. Click to see transcript and slides.

**Slides:**

[PDF Version](https://github.com/ArnavMetrani/arnavmetrani.github.io/blob/master/_data/Quantum_Cryptography_Final.pdf)
(PDF previews below may take a minute and few reloads to appear.)
<iframe src="https://docs.google.com/gview?url=https://raw.githubusercontent.com/ArnavMetrani/arnavmetrani.github.io/refs/heads/master/_data/Quantum_Cryptography_Final.pdf&embedded=true" style="width:718px; height:700px;" frameborder="0"></iframe>

**Abstract:**
In this talk I will be introducing the field of quantum cryptography: what it is, why we need it, how do we implement it, and what are some of the open problems and challenges. I aim to make it interactive. The only prerequisites are basics of linear algebra and 1st year physics, but I hope there's something to take away for 3rd and 4th years as well. 
Formally, I will be covering one time pads, BB84, DPS-QKD, MDI-QKD, the 3 no-go theorems which led to QKD, and anything else which may seem appropriate.

**Transcript:**
(Some details and context for the transcript: It may read in an overtly verbose manner since I prepared it while preparing for the talk. The talk was meant for a mixed audience- first and second years who do not have an idea of linear algebra or QM, 3rd and 4th years who have taken a course in FQM (Foundational QM) or QCQI (Quantum Computing and Quantum Information), and maybe 1-2 PhDs who have covered the full formalism of QKD. As a result, the talk branches out slowly and moves onto more advanced topics once the basics have been laid out. I intended to structure it in a manner that everyone gained something from the talk, while making it interactive as well. I've added the transcript since I thought it was a nifty way to cover everying. Feel free to use the material here for your own presentations.)


Hey everyone, thank you for coming today. As the abstract states, I will be going through quantum cryptography, what it is, how it works, why it works, and how do we implement it.

I'll also explain the structure of the talk itself.
(Structure and pacing)
So before we start off, I just want to have a general understanding of what the crowd is like.

Just to make clear, I'm not here to come and talk on a stage. I will share the slides and there's nothing new in any of the information I'll be saying. So if you want to see it in YouTube video, you could very well do that. I'm pretty sure the person in the YouTube video will do a better job. What my advantage here is that I'm able to interact with you and vice versa. So there is no point if you aren't willing to interact. Hopefully a different person every time. And if you think they're any doubts that you have, no matter how bad or basic you may think them to be, be rest assured that I've struggled with it for a longer time. If you wish for me to elaborate on any point, please ask. I'll make it clear when I've just added something for illustration purposes here.

So how many of you have a basic understanding of linear algebra and quantum mechanics? How many of you are familiar with bracket notation? How many of you know what cryptography is? 
(Choose one person who raised for the last question and ask them to say what they think cryptography is.)
(Someone answers what it is. Ask the same person if they think that it always involves encryption and decryption.)

Fine, okay. In that case, can anyone give me an example of a cryptographic scheme in which we do not have the process of encryption and decryption? Even if the scheme is horrendously insecure, I don't mind it. I just want to see if you can think of an example.
(Give them a minute.) Take a minute. There's no hurry. I prefer if someone who doesn't already know it can do so but it's fine either way.
(Let's see if yes or no, and if yes then ask them to come on the board and show.)

I have two examples here. The first is what is called a zero-knowledge proof. So, a zero-knowledge proof is when you're trying to communicate to the other person reg. info about a particular statement. Namely, that the resulting statement is true or false without the other party learning anything else about the statement.

So for example, let's see the following:
(Slides for ZKP. Explain and ask through them.)

Sure, now this seems like quite a specific constraint to put, so could there possibly be any real-world applications?
(Show the Nature paper slide)

A different type of cryptographic protocol which does not involve encryption and decryption is the following. It's quite a basic and insecure one, but I think it does the job.
(Diagram consists of a straight horizontal line from A to C, the line has a large gap in the middle. Above the gap is a horizontal line that fits perfectly, below the gap is a NOT gate. The gap region + the above and below components are labelled as B.)
One party wishes to transfer to another some bit string of zeros and ones. And let's say the other party does not have any apparatus to measure it. But there is a third party which has the ability to measure it. So how does A communicate to B without C snooping? It can do in the following manner. A just sends it as it is, and B randomly decides to either let it pass as it is or apply a NOT gate. Let's say A is sending these bits one at a time and in some periodic manner it will. Then all that C has to do is declare the results. And C declares the results, A knows what B has done, and B knows what A has done. C has no info.
Believe it or not some of the protocols we will be looking at today are kind of based on this matter, even though this particular one is hopelessly insecure since any person can snoop on to the message being transmitted from A to B.


Lastly, we have the Diffie-Hellman key exchange as well, in which two parties are able to agree on a shared key without them passing the common secret key to each other.
This just serves for name dropping in case you're interested in checking it out later. I'll give a few moments just to stare at the screen.
(Show Diffie-Hellman slide)

So now we have seen two different processes in which there is no requirement for encryption and decryption, and one in which a key is obtained in an indirect manner.

Why is this important? Because quantum cryptography relies on this in an indirect manner. I have not explained as to what cryptography is, so a basic definition of cryptography is communication or any method of facilitating communication between two or more parties in a secure manner such that it eliminates any possible probability of eavesdropping and if there are eavesdroppers they cannot decipher.

Majority of the current work is focused towards the third approach in which you have parties sharing a key. And we'll come to see why shortly. So before that, let us talk about prime factorization. If you haven't heard about it already, there's a simple rundown.

Two primes p and q can be multiplied to get a larger number. That is easy to do. Trying to factorise any given number into these primes is tough to do. By easy it means it can be done polynomial time. By tough it means it cannot be done in polynomial time. So polynomial time is simply the number of steps for our understanding here. As numbers become bigger and bigger, we can simply choose a number which has a very low probability of being factorized even if, say, the entire Earth's computing power was used for thousands of years only for this purpose. The caveat here is that we have not found any classical solution which does not do it in non-polynomial time. It hasn't been a mathematical proof so far that there cannot exist a classical algorithm which is linear in time. Same problem with all other classical cryptographic protocols.

About 20 years ago you had Shor's algorithm which factors in polynomial time. So that led to huge flurry in quantum computers and quite recently you had Apple and Signal implement post quantum cryptography, It was a modified version of the Diffie-Hellman protocol mentioned earlier. So PQC are algorithms or cryptographic protocols which cannot be cracked in a reasonable time using quantum computers.

QKD does not answer the same question.

What I will be talking about today, that is QKD, will deal with none of these problems. In QKD, when testing a protocol, you might as well assume that the eavesdropper or snooper can perform 10^10^10^10 operations a second.

If your protocol cannot withstand the attacks of an infinitely powerful entity who follows the laws of physics so far as you know it, the protocol fails. That is the objective in QKD. The incredible part is that we do have algorithms which can withstand such attacks.

So QKD, unlike classical cryptography and PQC does not rely on any hardness problems. All it relies on is that quantum mechanics is valid.

Due to this approach, it also removes any possibility of backdoors. So some of you might have already heard about the dual encryption cryptography scandal in the mid 2000s. You have protocols which do not utilize QKD as well such as the Y-00 protocol but those are not unconditionally secure.

Now for the reason why it is called quantum cryptography. Quantum cryptography is just classical cryptography protocols with some minor tinkering in terms of the formalism or some quantum mechanical implementation. That is all. It's not inherently different. If that is the case, then we need to have some classical technique which is provably secure and we do have that it's called a one-time pad. One-time pad is quite simple in understanding actually.

(Show slide of OTP)
So this is what the procedure of one-time pads are. Now the question arises as to how do you prove its security.

(Show slide of security)
So this is how we're defining the condition for perfect security. And it makes intuitive sense as well. What we're trying to say is that just because we're trying to show that there is no correlation between the ciphertext and the message. If there is, then there is some way to maybe extract some information on what the message could possibly be, even if not completely.
It is a nice exercise to prove this. You already know everything which is required, which goes into proving it, which is just simple probability and simple conditional probability. There are no complicated expressions and all, but you still have to come up with a way to construct the proof. So that is left as an exercise.

(Show reuse of OTP slide)
A simple case where partial information is leaked is if we reuse the one-time bar. So, reusing the one-time bar would give you this. And this is because C1 XOR C2 is equal to M1 XOR M2. So, it is quite easy to make good guess as to what the first two messages were.

OTP is the only completely provably secure method of transmission which we have formed so far. We haven't even come across any other method which is provably secure. 

This now brings us to QKD. The entire purpose of QKD is to transmit this one time pad from one party to another party or come up with some schemes such that both of them can construct the same one time pad. That is all the goal.

(Cont.)


  











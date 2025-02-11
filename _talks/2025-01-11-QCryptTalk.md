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
In this talk I will be introducing the field of quantum cryptography: what it is, why we need it, how do we implement it, and what are some of the open problems and challenges. I aim to make it interactive. The only prerequisites are basics of linear algebra and 1st year physics, but I hope there's something to take away for 3rd and 4th years as well.\ 
Formally, I will be covering one time pads, BB84, DPS-QKD, MDI-QKD, the 3 no-go theorems which led to QKD, and anything else which may seem appropriate.

**Transcript:**
(Some details and context for the transcript: It may read in an overtly verbose manner since I prepared it while preparing for the talk. The talk was meant for a mixed audience- first and second years who do not have an idea of linear algebra or QM, 3rd and 4th years who have taken a course in FQM (Foundational QM) or QCQI (Quantum Computing and Quantum Information), and maybe 1-2 PhDs who have covered the full formalism of QKD. As a result, the talk branches out slowly and moves onto more advanced topics once the basics have been laid out. I intended to structure it in a manner that everyone gained something from the talk, while making it interactive as well. I've added the transcript since I thought it was a nifty way to cover everything. Feel free to use the material here for your presentations.\
PS. It's probably too long, and can be split into two talks.)


Hey everyone, thank you for coming today. As the abstract states, I will be going through quantum cryptography, what it is, how it works, why it works, and how we implement it.

I'll also explain the structure of the talk itself.\
(Structure and pacing)\
So before we start, I just want to have a general understanding of what the crowd is like.

Just to make clear, I'm not here to come and talk on a stage. I will share the slides and there's nothing new in any of the information I'll be saying. So if you want to see it in a YouTube video, you could very well do that. I'm pretty sure the person in the YouTube video will do a better job. My advantage here is that I'm able to interact with you and vice versa. So there is no point if you aren't willing to interact. Hopefully a different person every time. And if you think there are any doubts that you have, no matter how bad or basic you may think them to be, rest assured that I've struggled with it for a longer time. If you wish for me to elaborate on any point, please ask. I'll make it clear when I've just added something for illustration purposes here.

So how many of you have a basic understanding of linear algebra and quantum mechanics? How many of you are familiar with bracket notation? How many of you know what cryptography is?\
(Choose one person who raised for the last question and ask them to say what they think cryptography is.)\
(Someone answers what it is. Ask the same person if they think that it always involves encryption and decryption.)

Fine, okay. In that case, can anyone give me an example of a cryptographic scheme in which we do not have the process of encryption and decryption? Even if the scheme is horrendously insecure, I don't mind it. I just want to see if you can think of an example.\
(Give them a minute.) Take a minute. There's no hurry. I prefer if someone who doesn't already know it can do so but it's fine either way.\
(Let's see if yes or no, and if yes then ask them to come on the board and show.)

I have two examples here. The first is what is called a zero-knowledge proof. So, a zero-knowledge proof is when you're trying to communicate to the other person reg. info about a particular statement. Namely, that the resulting statement is true or false without the other party learning anything else about the statement.

So for example, let's see the following:\
(Slides for ZKP. Explain and ask through them.)

Sure, now this seems like quite a specific constraint to put, so could there possibly be any real-world applications?\
(Show the Nature paper slide)

A different type of cryptographic protocol which does not involve encryption and decryption is the following. It's quite a basic and insecure one, but I think it does the job.
(Diagram consists of a straight horizontal line from A to C, the line has a large gap in the middle. Above the gap is a horizontal line that fits perfectly, below the gap is a NOT gate. The gap region + the above and below components are labelled as B.)\
One party wishes to transfer to another some bit string of zeros and ones. And let's say the other party does not have any apparatus to measure it. But there is a third party that can measure it. So how does A communicate to B without C snooping? It can be done in the following manner. A just sends it as it is, and B randomly decides to either let it pass as it is or apply a NOT gate. Let's say A is sending these bits one at a time and in some periodic manner it will. Then all that C has to do is declare the results. And C declares the results, A knows what B has done, and B knows what A has done. C has no info.\
Believe it or not, some of the protocols we will be looking at today are kind of based on this matter, even though this particular one is hopelessly insecure since any person can snoop on the message being transmitted from A to B.


Lastly, we have the Diffie-Hellman key exchange as well, in which two parties can agree on a shared key without them passing the common secret key to each other.\
This just serves for name-dropping in case you're interested in checking it out later. I'll give a few moments just to stare at the screen.\
(Show Diffie-Hellman slide)

So now we have seen two different processes in which there is no requirement for encryption and decryption, and one in which a key is obtained indirectly.

Why is this important? Because quantum cryptography indirectly relies on this. I have not explained what cryptography is, so a basic definition of cryptography is communication or any method of facilitating communication between two or more parties in a secure manner such that it eliminates any possible probability of eavesdropping, and if there are eavesdroppers they cannot decipher.

Majority of the current work is focused on the third approach in which you have parties sharing a key. And we'll come to see why shortly. So before that, let us talk about prime factorization. If you haven't heard about it already, there's a simple rundown.

Two primes p and q can be multiplied to get a larger number. That is easy to do. Trying to factorise any given number into these primes is tough to do. By easy it means it can be done polynomial time. By tough it means it cannot be done in polynomial time. So polynomial time is simply the number of steps for our understanding here. As numbers become bigger and bigger, we can simply choose a number that has a very low probability of being factorized even if, say, the entire Earth's computing power was used for thousands of years only for this purpose. The caveat here is that we have not found any classical solution that does not do it in non-polynomial time. There hasn't been a mathematical proof so far that there cannot exist a classical algorithm that is linear in time. Same problem with all other classical cryptographic protocols.

About 20 years ago you had Shor's algorithm which factors in polynomial time. So that led to a huge flurry in quantum computers and quite recently you had Apple and Signal implement post-quantum cryptography, It was a modified version of the Diffie-Hellman protocol mentioned earlier. So PQC are algorithms or cryptographic protocols that cannot be cracked in a reasonable time using quantum computers.

QKD does not answer the same question.

What I will be talking about today, that is QKD, will deal with none of these problems. In QKD, when testing a protocol, you might as well assume that the eavesdropper or snooper can perform 10^10^10^10 operations a second.

If your protocol cannot withstand the attacks of an infinitely powerful entity that follows the laws of physics so far as you know it, the protocol fails. That is the objective of QKD. The incredible part is that we do have algorithms that can withstand such attacks.

So QKD, unlike classical cryptography and PQC does not rely on any hardness problems. All it relies on is that quantum mechanics is valid.

Due to this approach, it also removes any possibility of backdoors. So some of you might have already heard about the dual encryption cryptography scandal in the mid-2000s. You have protocols that do not utilize QKD as well such as the Y-00 protocol but those are not unconditionally secure.

Now for the reason why it is called quantum cryptography. Quantum cryptography is just a classical cryptography protocol with some minor tinkering in terms of formalism or some quantum mechanical implementation. That is all. It's not inherently different. If that is the case, then we need to have some classical technique that is provably secure and we do have that it's called a one-time pad. A one-time pad is quite simple to understand actually.

(Show slide of OTP)\
So this is what the procedure of one-time pads is. Now the question arises as to how you prove its security.

(Show slide of security)\
So this is how we're defining the condition for perfect security. And it makes intuitive sense as well. What we're trying to say is that just because we're trying to show that there is no correlation between the ciphertext and the message. If there is, then there is some way to maybe extract some information on what the message could possibly be, even if not completely.\
It is a nice exercise to prove this. You already know everything that is required, which goes into proving it, which is just simple probability and simple conditional probability. There are no complicated expressions and all, but you still have to come up with a way to construct the proof. So that is left as an exercise.

(Show reuse of OTP slide)\
A simple case where partial information is leaked is if we reuse the one-time bar. So, reusing the one-time bar would give you this. And this is because C1 XOR C2 is equal to M1 XOR M2. So, it is quite easy to make a good guess as to what the first two messages were.

OTP is the only completely provably secure method of transmission that we have formed so far. We haven't even come across any other method which is provably secure. 

This now brings us to QKD. The entire purpose of QKD is to transmit this one-time pad from one party to another party or come up with some schemes such that both of them can construct the same one-time pad. That is the goal.

(Show TEMPEST slide)\
This is a slight detour, but it would give an example of the kind of attacks you see in QKD as well. During WW2, the OTP and the plaintext were combined in an electromechanical manner. So these systems generated a considerable amount of electromagnetic waves. A few decades later, researchers were able to devise a system that extracted the plaintext just from the thermal radiation given off. This is similar to typing on a smartphone and logging the user's keyboard using the accelerometer. I have attached a link to this paper too.

Back on topic, the way we go about provable security is by establishing impossibility proofs or no-go theorems. There are three of them that I'll be looking at today, which seem to be the most important and coincidentally the most basic. The first is the no-cloning theorem.

(Show no-cloning slides)\
This is quite a simple proof that holds for pure states.\
However, you have to show that it's not possible at all within the formalism of quantum information.

We can extend it to mixed states via purification. What is purification? It is simply the method of converting a mixed state in a smaller space to a pure state in a larger space. So it can be done in the following manner.\
(Show purification slide)

Finally, we can show that no non-unitary operator can satisfy this as well. We do this via Stinespring Dilation.\
(Show Stinespring slide)

One thing to note is that this theorem does not hold if you have multiple copies of the same state. This will be important later, so just keep that in mind.

Great, so the next no-go theorem we are going to look at is called the indistinguishability of non-orthogonal states on measurement.\
(Show slide)\
This basically means that given two quantum states, if they are non-orthogonal, that is if their inner product is not zero (and not 1, trivially), then we cannot tell the state which we have received.

The proof of this is slightly complicated. I could go into it if someone is interested, but I'll have to do that at the end of the talk if I have enough time.
Those who already have taken the QCQI course would definitely know about the B92 protocol. The issue with B92 which depends on non-orthogonal states is that even though we cannot always be sure deterministically which state we have received or intercepted, we can always define an optimal set of POVMs that maximize our probability of guessing correctly. So it's called Helstrom measurement. I won't go into it but it is possible to do it with 93.3% probability for B92.

The third no-go theorem states that non-orthogonal states cannot be distinguished without disturbance. So not only can we not distinguish them deterministically in the first place, but if we were to even attempt to do so, that would bring about some changes in the output states. So in other words, there is no way of going about with the process of determination without affecting the states themselves.\
(Show proof slide)\
The proof is quite simple as well, which is why I put it here. If there exists some unitary operation such that it can transfer information of one state from one system to another state of another system, then it must affect the first state as well in the first system. If it does not affect it, then there is no way of extracting information.

So to summarize all of the no-go theorems in a very informal manner:\
(Show slide)


Now that we have all the basics in place, we can look at the first-ever QKD protocol and by far the most popular. It's called the BB84 protocol.\
(Show BB84 slide)\
Charles Bennett and Giles Brassard came up with the protocol and they presented it at a conference in IISc. Here, I'll be just referring to the states as polarization of light.  I can characterize them as horizontal, vertical, diagonal, and anti-diagonal.\
I will call anti-diagonal as H plus V and diagonal as H minus V. Normalized of course. So these are the four states that we have.

H and V mean Z basis,  A and D mean X basis. For our purposes here, it's just nomenclature. And within these bases, H means 0, V means 1, A means 0, D means 1. So the way the protocol works is quite simple. Alice randomly decides to send a pulse in one state. This could be H, V, A, or D.\
Bob randomly guesses the basis in which Alice has sent the state.\
Bob has access to two polarizing beamsplitters which work in the following manner.\
(Draw)
Bob also has access to two detectors. The detectors do not move. All that Bob is doing is switching in and out of the PBS. This is how Bob is guessing what basis the state sent by Alice in.\
We can also label the detectors in the following manner. "This" denotes one and the other detector denotes zero. So the detection results are kept secret and only Bob knows about it. Alice and Bob also share another classical channel. This is an insecure channel. So the way the protocol works is the following.

(Show sample run)\
The first step is that Alice randomly generates a bit string. How does it generate a completely random bit string? It uses a quantum random number generator. What is a quantum random number generator? I will not go into it, but it uses and relies on quantum mechanical phenomena to randomly generate numbers. So, this could be, for example, the shot noise of a very weak coherent force of light. I'll get back to this point shortly.\
So after you've generated the bit string, Alice generates another bit string. This time for deciding which basis to send the string in. So we can let z for this new basis, for this new bit string, we can choose z to 0 to denote, let's say, the z and x to denote, let's say, 1. So with this system, Alice starts sending light buses encoding accordingly and sends them in a periodic manner. Bob has also in the meantime generated randomly a bit string and uses this bit string to choose which PBS to place. So they also use this classical communication channel to synchronize the system such that if Alice is, let's say, sending the fifth bit or the fifth state, Bob accordingly should be applying its fifth guess corresponding to his own bit string, okay? So this process goes on, Bob receives, applies a PBS, some detection is made, and keeps recording this process, okay?

After this is done, Bob publicly declares what its basis choice selection sequence was, the sequence in which it applied the PBS. And Alice publicly declares which of the guesses by Bob was correct and not correct.\
And in this process, if their bases match, they keep this secret bit.\
This filtering process works because if the bases match, then whatever Bob has detected is exactly what Alice had sent. If it does not match, then through simple basis decomposition. So that is, you can write a state A as H plus V. It is a superposition of H and V, so you could have had either H click or V click. You did not know for sure. So you discard this. And the rest is kept.\
Now, Alice and Bob also want to figure out If there was an eavesdropper between the light pulse channel. This is verified by Bob randomly declaring some of the secret bits. If the secret bits do not match what Alice has sent even if the bases match, that means there has been some interference by attacker Eve due to the three no-go theorems which we have derived earlier.

A simple attack is called the intercept and resend. So you have Eve who intercepts this light pulse that is being sent. Randomly guesses which basis it was sent in and records the state. It assumes that it has guessed correctly and prepares the same state corresponding to its measurement and sends it to Bob. So if Eve follows this process then it gets away with the probability (3/4)^N. N is for the number of secured bits which are revealed above. However, as N gets large the probability of Eve not slipping up decreases exponentially and so with a high probability you can rule out the presence of Eve by this process.

I have a simple question for you. Why should Bob measure in the first place? Once Bob receives the collection of qubits or photon pulses from Alice, Bob could simply store them until Alice declares the basis used for encoding after which Bob can make the measurements. That way, there would be no guessing which Bob has to do in the first place. So what is the issue with that? Take a minute.

(Wait, see if anyone answers)

So the problem with this is that, since you have assumed Eve to be infinitely powerful, Eve can simply trap and store the light pulses sent when Alice sends the basis encoding through the classical channel. Eve immediately reads what is sent through the classical channel, applies the required measurement along the correct basis, on the light pulse, generates the desired photons matching the correct basis, and sends it to Bob, such that there is no indiscernible time delay between both channels.

One question you might have is how both of the parties rule out Eve intercepting the data being sent in the classical channel. The simple answer is that you don't because that is not what the protocol is concerned within the first place. No cryptographic protocol can prevent this. Let's say you have the most secure cryptographic protocol possible. Eve can simply intercept what both parties are sending and resend whatever it wants to do. The original authors of the paper suggested a method is called the Wegman-Carter Message Authentication Code to detect active eavesdropping in the classical channel, but it has some caveats such as both parties already sharing a secret key, so not useful here.

So far I've been referring to the states as light pulses. For the complete security of this protocol, we have to use single photons and single photons only to make sure it is provably secure. The reason is that if it is a multi-photon pulse, then Eve can simply use a beam splitter to extract some of the photons and store them. And when the basis declaration takes place, Eve can just measure in those bases.  

Now this is where the practical constraints come into place. Let's say we want to implement BB84. I think at best what we have is SPDC or quantum dots. Now the issue is, it takes around 10 to the power of 6 versus to have a high probability of getting one such process taking place for SPDC. As a result, since the conversion rate is very low, the corresponding key rates that we're generating are also very low.

Some terminology. Key rate or secure key rate is the number of secured bits generated per second, And this itself is derived from the ratio of secured bits generated per detected pulse. So we can get a rough estimate about the conversion rate if let's say our secured key rate is 1 bit per second and if our initial signal which was sent from Alice is let's say 1000 photons per second, or 1 per millisecond.

Now the issue is to generate 1000 photons per second, you'll have to have a source that is pumping in photons at a much higher rate just to generate 1000 photons per second from the SPDC source. So that is the issue with single photon generators currently. The conversion rates themselves are quite low. This is along the simple fact that our technology of optical fibers is not advanced enough such that a single photon can be transmitted over tens of kilometers without a high probability of it being absorbed. This means that if you already have a source that generates photons at a very low rate, it would make our secure keyrate extremely low.
  
We work around this by using sources that can already produce process at a high rate and then attenuating these pulses such that their intensities become very, very low. So in the end, we have a weak coherent pulse, WCP. The reason why we can still use this process is that weak coherent pulses can be modeled as a Poissonian source.\
(WCP slide)\
The way the intensity is modeled is by using number states. So number states for our purposes here is just the number of photons in each pulse and this is directly analogous to what you would have done in quantum harmonic oscillators with the raising and lowering operators. So 'a^dagger' is the creation operator, 'a' is the annihilation operator, and every analysis you do applies here. So number state operator is a^dagger a.\
The proof follows from coherent states being an eigenvector of the raising and lowering operators.

Just to give you a general scale of how weak the pulse has to be, the mean photon number is set to around 0.5 photons per pulse. This is done through some numerical simulations to decide what is the best possible mean photon number to set. 0.5 infers that roughly 90% of the time we do not see any pulse, in that time bin, 8% of the time we see one photon, and 2% of the time we see multi-photon pulses. The only reason why we can use weak coherent forces which have quite a decent probability of emitting multi-photon pulses is due to something called the decoy state technique, which I can get to in the very end if I have time.

This is the first practical problem we have seen so far. Another problem that we will be tackling now is the usage of polarization. The "ordinary" fibers used for telecom purposes are not polarization-maintaining. Polarization-maintaining fibers need to have birefringence modelled into their structure, making them much more expensive than telecom fibers. Since the goal is to use QKD over large distances, it becomes unfeasible to use pol-maintaining fibers. Also, it is currently a short-term goal to incorporate QKD signals into the existing telecom infrastructure, so polarization encoding will simply not do.

This gave rise to DPS QKD. DPS stands for differential phase shift.\
(Show T-12 slide)\
Here, we effectively send two pulses in quick succession (call it a pair) and the protocol involves Alice constantly sending such pair. Between the two pulses of a pair, we fix a certain phase shift. And similar to how we did in BB84, the phase shift is what can be considered as encoding the information. This here is the T-12 protocol mplementation.\
If both parties apply the phase shift corresponding to the correct bases, Bob can deduce Alice's intended bit. It follows the same BB84 protocol process in which the bases are declared, common classical channel, etc. 

(Show IM diagram)\
I don't know exactly how the intensity modulator works. It works on a principle called the Quantum Confined Stark Effect in which an electric field incident onto the material causes the materials absorption and emission spectrum to change. Alternatively, we can model it as an interferometer setup where the phase in one of the arms is set to 0 or π and we use one of the output ports of the interferometer for the signal generation.\
We can call the part which is in the front the early pulse, and the part which is in the end as the late pulse.\
Now through some clever engineering, we can choose any possible relationship between the early and the late pulse. So it basically becomes E + e^iθ L (normalized).\
(Write on the board the 4 states which are being used in T-12)\
The phase encoding is done using an EOPM (electro-optic phase modulator). The refractive index of the material changes when an electric field is applied to it.\
(Show slide of EOPM shift)\
This is a possible setup through which a phase shift of π/2 is encoded.

The final detection is obtained after Bob applies a random phase shift (corresponding to the 4 chosen shifts) and then the pulses are "combined" and the final detection is obtained via interference.\ 
(Show slide for interference)\
This is an example of when the shifts match. As we can see, in the "middle" time-bin we see constructive interference at one detector, and destructive at another.
There is a 50% probability that we'll get a detection in the first time bin or the third time bin and so we can't use those cases but if we get a detection in the second time bin then we know that it must be a resultant of guessing the basis correctly.  

If the bases do not match, then in the middle time bin we will see the faces of the pulses differing by pi by 2 and pi by 2. And so as a result, there is no complete constructive or destructive interference. So Bob cannot backtrack and determine what was the secret bit that Alice wanted to communicate.  

So that is it for DPS QKD. You also have entanglement-based protocols but I won't be getting into it because generating entangled photon pairs reliably is still problematic.  

So, then we should be done, right? Why do we need anything further?\
The issue is that detectors leak a lot of information and they are very costly.\ 
The attacks on detectors are quite interesting but I don't think I'll have time to get into it. I'll leave a link to the paper attached and if I have time I'll go back to it at the end of my talk.  

So it would be beneficial to have a setup in which we can give the detectors away to an untrusted third party and even then you can have Alice and Bob communicate with each other. This is what measurement device independent QKD, MDI-QKD gives.\  
(Show MDI slide)

So before this, just for completeness, I'll explain the other parts of a QKD protocol run. If I get more time I'll cover them at the end.\
(Show post-processing slide)

Going back to the MDI-QKD protocol.\
This protocol works based on the HOM effect, the Hong-Ou Mandel effect, in which if you have two indistinguishable photons sent through a beam splitter, both the photons will come out of the same port. They cannot come out of different ports. They do not come out of different ports.\  
(Show the HOM effect slide) 

If there are any variations in the parameters, they can be parametrized by a dip.\ 
(Show HOM dip slide)\
For coherent states, the visibility is 50% and not 100% as seen here. Visibility is the difference between the coincidence probabilities divided by the highest prob.  

Going back to the MDI slide, we can similarly split our photon pulse into "early" and "late" time bins, and we can see from calculations that if two parties send the same state, then there is a 100% probability that both the photons will be detected at the same detector.\
So Alice and Bob prepare the states, the pulse pairs are passed through a beamsplitter, and Charlie detects the results.\
The only way this protocol differs slightly is that Charlie only announces singlet states. That is, when both the detectors click and at different time-bins. If this happens, then Charlie declares and both of the parties declare their bases as well. And if their bases match, then Bob flips his selection.\ 
This can be shown by a simple example.\
(Show example via Z-basis matching on the board.)\
Because we have quantified their indistinguishability via the HOM dip, we know that Charlie cannot tell who sent which pulse/state.

We have now come to the end of the talk: current obstacles.\
Firstly, security proofs. So, the BB84 was proved by Lo and Chau, I think, around eight years after it was conceived. The proof did not actually prove using BB84 directly. It boiled down BB84 into another protocol and then showed that that protocol's proof implies this protocol's proof. Similarly, Shor and Preskill's proof involved CSS codes. So proving the security of these protocols was quite difficult, and still is. You have protocols such as the COW protocol, the coherent one-way protocol, whose unconditional security has still not been determined.

Next, there is no clear framework for analyzing the secure key rate as well as the security proofs for QKD protocols. No simplified or single framework has been determined so far. You have a lot of different approaches and their efficiency depends on protocol to protocol.\  
For example, Renato's Renner thesis was on the security of QKD protocols. It was published around the mid-2000s. That is one of the main frameworks that he used so far. And it is a 150-page tome. It dives headfirst into mathematics and cryptography, mainly.\  
(Show Renner slide)\
This is for analyzing finite key lengths in the basic BB84 portals.  

Until recently we did not even have good numerical methods to compute for arbitrary protocols. Those are still quite horrendous.\
(Show slide)\
As you can see.\ 
In the past few years, semi-definite programming has been touted as a tool for calculating key rates.

Next, there are attacks possible for each component. DI-QKD attempts to make the protocols device independent, and this is done by having criteria of making the components self-testable. I haven't covered it cause it's quite complex and I don't know much about it, but this is an active area of research as well. Unfortunately, the key rates are phenomenally low so far, something like 10^10 detections/pulses to generate one secure bit. So there is a long way to go here.

Next, there is the single photon restriction. As stated earlier, all the protocols described so far require single-photon pulses, which puts a severe restraint on speed.

There are also "hardware" problems. QKD is currently quite slow and expensive. Since it relies on OTP, for every message this process has to be followed.\ 
Also, since the current goal is to incorporate QKD into the telecom infra, several implementation problems are present. For example:\
(Show noise slide)\
This slide shows the optical loss VS distance for a typical telecom fiber. As we can see, the loss is minimum for 1550 nm and this is the wavelength that is currently used in telcom. Unfortunately, a lot of the detectors that we have currently (such as SPAD, QD) perform much better in the 800 nm range than at 1550 nm. SNSPDs perform well at 1550 nm but are very expensive. Even then, their efficiency (SNSPD has 98%) does not compare to the current telecom industry standards.

There you have it! We've gone through the motivation for QKD, covered the basics that enable it, covered protocols, and covered the current challenges as well. That's all I have for you. 

Questions?

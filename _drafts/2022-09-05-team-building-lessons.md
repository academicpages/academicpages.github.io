---
title:  "Early startup employee lessons learned, part 3: building a team"
permalink: /posts/2022/09/early-startup-team-building
date: 2022-06-26
---

A core function of being an early employee at a rapidly growing startup is helping it grow!
That means a lot of hiring, which I'll cover more in Part 4 of this series.
Along with hiring, learning how to build a successful team is also critical to growing with your startup with grace.
At my current job, I've helped the data science team grow from being just one person doing a little bit of everything (me!) to a team of over 15 people with three focused verticals, group leads for each vertical, and a director of data science fearlessly leading us all.
Growing the data science team has been one of the best parts of our current hyper-growth, and I've learned a lot of really useful lessons from our experience.

# Hiring strategy: junior vs. senior hires

How do you decide who to hire when?
Early on, you almost always need senior or experienced people.
You might think you just need an extra pair of hands, or that an intern will be able to pick up the extra workload you've taken on, or that a junior hire will be sufficient to get the work done under your supervision. 
Well, you're probably wrong.

At the beginning of our hyper growth, we focused on junior hires. 
To some extent, I think we were constrained to make junior hires because we hadn't yet raised additional money to keep up with our growth.
We also figured that hiring junior people would be way easier than senior folks, and that our junior hires would be enough to take the load off of me so that I could focus on other things.
Turns out that we were wrong.
The codebase I had written was poorly designed and almost entirely undocumented, which meant that the junior folks we hired could only barely debug it, let alone develop additional features on top of it.
And I wasn't an experienced enough mentor to know how to give them direction when building new features or where to focus my energy when reviewing their code.

We thought some extra pair of hands could at least take the load off of some of my daily operational tasks, but this too proved to be a little too good to be true.
Our junior hires were indeed able to take on a lot of the rote work I had been doing, alleviating a lot of the daily burden.
But when things went wrong, I had to be called in to troubleshoot, debug, and decide on a course of action.
The extra energy I spent supervising and firefighting was barely compensated for by the extra hands.

Similarly, the temptation of contractors is sweet but should be approached with extreme caution.
Early on, we also hired a team of software engineering contractors to try to take the load of maintaining and developing our codebase off of my poor data science shoulders.
But I wasn't experienced enough to know how to give the team direction (for example, by writing technical specifications), explain to them what I really needed, or even review the code they wrote particularly well.
What we ended up with set the stage for our tech debt: wrappers around my poorly designed and (still) undocumented code along with their new poorly designed and (also) undocumented code, all wrapped up and running in the cloud via a technology I was unfamiliar with.

In contrast, when we finally hired a full-time senior software engineer he was able to put the time and energy into understanding the ideas behind our software needs. He read through my codebase and started understanding its strengths and weaknesses.
And when we received a new contract that needed an entirely new pipeline written from scratch, he was able to stand that up quickly and relatively sustainably. 

Speaking of senior hires, the most important lesson I've learned is that if you're hiring for that team's leader but also semi-desperately need senior individual contributors, you should absolutely _not_ wait to hire the leader before hiring the IC's.
Luckily, the data science had a handful of opportunistic senior hires so we didn't run into this issue.
We hired our director of data science when we were already a fully-functional team of over 10 people, after an approximately year-long search.
If we had waited to find him before starting to fill out our ICs, we would have not succeeded.
In contrast, other teams at my company _have_ waited to hire a senior leader before filling out the team's ranks.
These teams really struggle with being overworked, not having clear processes or technical direction, and are generally falling behind the rest of the company's growth. 
In my opinion, senior ICs should be hired as soon as they are needed because they can provide an important bridge until the leader is hired without accumulating too much technical debt.

One pushback I've heard in favor of waiting to hire ICs until there is a leader is that the management chain rapidly becomes unmanageable, with individuals at the top having way too many direct reports.
I empathize with this situation, since nobody wants to manage more than 5 people (and nobody wants to be managed by someone with more than 5 reports).
But it shouldn't be a blocker to making the hires that you need - it should be addressed creatively and with open communication.
For example, restructuring teams so that not everybody is reporting to the same individual, breaking up job descriptions so that a leader or manager hire is easier to make, or simply being open and honest about the reality of the situation and working together to remedy it.
In my experience, as our data science team grew I ended up managing three individual contributors who were more senior than me for about a year.
It was a little strange and little lonely, but I treated them essentially like peers: I served as a honest conduit with our upper management and did my best to provide feedback on their performance, but as far as the actual work that they did, we were very much partners in figuring out what to do and how to do it.
It was a strange but fruitful relationship, and also meant that as they got promoted into more senior roles and as we fleshed out our management structure, the transition to being peers was extremely seamless.

Despite my energy and passion for senior hires, there are absolutely times when a junior hire is a great idea.
If the work you need to offload is repetitive or operational and fairly stable, you can almost certainly transition it to a junior hire.
I also learned this the hard way: our daily data review was done by PhD's for over a year, whereas now it's performed by a team of entry-level data analysts.
For a long time, we felt that the work we were doing was "too special" to be handed off to a junior hire.
But we were wrong - it was difficult to hand off, but it's not because it was special, it's becuase it wasn't documented.
Once we wrote down what we were actually doing, within three months we had almost completely offboarded it to our new entry-level team.

Finally, I am strong a believer in opportunistic hires.
I took a management training earlier this year which emphasized a quote from a management book: focus on getting the right people on the bus and the wrong people off the bus first, and _then_ figure out everybody's seats.
Some of our best hires were opportunistic - one applied to a stale position we'd forgotten to take down, another was a more senior candidate than we were originally intending to hire, and yet another was a former colleague who we knew had great potential despite having absolutely no idea where to place him. 

# Building the culture

As I mentioned in [Part 1](/posts/2022/11/early-startup-employee-change), building an open and collaborative team culture is one of my proudest achivements. 

- communicate about how you communicate
  - in remote environment
  - accountability: talk about it continuously, and enforce the norms when you start to deviate. (When someone asks "is this the right channel to post this in?" - answer their question!)
  - at biobot, we have fun things like "pulling a claire" or "pulling a scott"
- provide intentional tasks during onboarding
  - 30-60-90 is nice, but realistically you only need to plan for like 30 days. after a month, things will probably have changed enough that a new path has become clear
  - onboarding is the moment to create the culture! "make a plot!" is my favorite onboarding task, and we made sure that our director of DS did it too :D
- model the behavior you want from your colleagues, esp with your co-leaders (meh)
  - I want small talk when zoom meetings start, so I try to small talk!
  -
- give your rationale / explain the "why" behind what you're doing (to build an engaged team)
  - you'll probably feel like a broken record, but that's how it'll stick
  - nothing better than hearing one of your colleagues - especially someone junior! - connect the dots themselves, take that extra step because they understand the big picture behind what they're doing.

## Your changing role in the team

- you're still a leader, act like it
  - just by having been around a long time, you'll still be a leader - you know the context, you have all the scoops, you see the big picture. new folks will be excited to learn from you regardless of your actual role
  - your opinion will matter a lot, so be careful with it. as our company has grown larger and larger, i've made much more use of DMs - to share feedback  privately that in early days I would have put in a channel, to strategize a response to a tricky situation, to make sure i'm not overstepping on somebody else's work
- let go of your legos
  - obvi a post about a growing startup isn't complete without a "let go of your legos" reference
  - but really, it's so important to be intentional about giving other people space to take over things that used to be your job
  - importantly, it's very likely that they will do a worse job of it than you! they don't have the full context you do or the years of experience. but you *have* to let them take it, and make it their own. (1) there is often no "best" way to do something, and it's possible that they'll take your hacked-together solution and make it better, since it's their entire job to do that. also (2) whatever we lose by the mistakes or "less good" job they do, we gain by having a reduced bus factor. it's worth having a slightly less-accurate QC process, if it means we can hire junior data analysts to do it instead of a physics PhD...
- if this is one of your first jobs outside of school, don't be in a rush to get a "head of" or director title
  - give yourself space to discover what you actually like
  - i learned that i actually *don't* like (and am less effective at) a lot of the politics and relationship-leveraging needed to play an important strategic role. but because I was given the space to NOT be head of data science, i discovered that i DO love being a technical leader, and that's where i've been thriving. (it also meant that we got to hire a head of data science who i've learned so much from, from a career & personal growth perspective)
- inflection points
  - you're alone
  - you're not alone but you're in charge
  - someone else is in charge
  - your team is larger than you directly control

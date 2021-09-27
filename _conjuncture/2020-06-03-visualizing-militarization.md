---
title: Visualizing Police Militarization
output:
  md_document:
    variant: gfm
    preserve_yaml: TRUE
knit: (function(inputFile, encoding) {
  rmarkdown::render(inputFile, encoding = encoding, output_dir = "../_posts") })
date: 2020-06-03
permalink: /posts/2020/06/visualizing-militarization/
excerpt_separator: <!--more-->
header: 
  og_image: "posts/mrap/mrap-1.png"
tags:
  - data
  - policing
  - visualization
  - github
---

Much has been written lately about the increasing militarization of US
law enforcement. One of the most visible indicators of this shift in
recent decades is the increased frequency of tactical gear and equipment
worn and carried by police officers. However, this pales in comparison
to images of police departments bringing armored vehicles to peaceful
protests. <!--more--> People often criticize police departments or SWAT
teams for owning and deploying tanks in situations that don’t warrant
their use. In reality, these ‘tanks’ are typically [Mine-Resistant
Ambush Protected](https://en.wikipedia.org/wiki/MRAP) (MRAP) vehicles.
MRAPs were developed by the US military and produced by various
manufacturers from 2007-2009. As their name suggests, they are designed
to protect passengers from an improvised explosive device (IED) attack.

Given the extreme threat they were designed to survive, MRAPs are
emblematic of increasing police militarization in the US. But how did
police come to own these military-grade vehicles?

## Where have all the MRAPs gone?

Police departments, sheriff’s offices, and even school districts (the LA
Unified School District [briefly owned an
MRAP](https://www.lamag.com/citythinkblog/lausd-keys-mrap-tank/) in 2014
before [returning it to the Department of
Defense](https://www.dailynews.com/2014/11/21/lausd-school-police-return-armored-military-vehicle-which-is-now-in-barstow/))
that possess MRAPs typically acquire them through the little-known [1033
program](https://en.wikipedia.org/wiki/1033_program) which transfers
surplus military property to law enforcement agencies. The 1033 program
is separate from the [Department of Homeland
Security](https://www.theguardian.com/world/2014/aug/20/police-billions-homeland-security-military-equipment)
and [Department of
Justice](https://www.nytimes.com/interactive/2014/08/23/us/flow-of-money-and-equipment-to-local-police.html)
grants that agencies use to purchase equipment. In contrast, the 1033
program transfers surplus military equipment directly to law enforcement
agencies.

The 1033 program received increased [public
scrutiny](https://www.newsweek.com/how-americas-police-became-army-1033-program-264537)
after the highly militarized response to protests in Ferguson, MO after
the killing of Michael Brown by Darren Wilson in 2014. Scholars have
found a [positive
relationship](https://journals.sagepub.com/doi/full/10.1177/2053168017712885)
between 1033 transfers and police killings.

The National Defense Authorization Act of 1990 established a program to
transfer surplus Department of Defense property to “federal and state
agencies for use in counter-drug activities” and this was expanded to
the 1033 program in 1997 (see
[here](https://web.archive.org/web/20141202031945/http://www.dispositionservices.dla.mil/leso/pages/1033programfaqs.aspx#q1#q1)
for details). The program was [suspended by Obama
in 2014](https://www.usatoday.com/story/news/politics/2015/05/18/obama-police-military-equipment-sales-new-jersey/27521793/)
before being [restored by Trump
in 2017](https://www.nytimes.com/2017/08/28/us/politics/trump-police-military-surplus-equipment.html).

The [Marshall Project](https://www.themarshallproject.org/) has an
[online
database](https://www.themarshallproject.org/2014/12/03/the-pentagon-finally-details-its-weapons-for-cops-giveaway)
where you can look up all tactical equipment transferred to every law
enforcement agency in the US. However, the sheer scale of the data can
easily hinder understanding. MRAPs represent a tiny fraction of the
total property transferred to law enforcement agencies, but they are a
powerful symbol and can be very easily abused. In addition, their
presence can [lead peaceful protests to escalate to
violence](https://scholarship.law.slu.edu/cgi/viewcontent.cgi?article=1028&context=plr)
as protesters react to aggressive tactics, so it’s worth exploring how
many of them have made their way into the hands of state and local
agencies. To try and help illustrate the increasing level of police
militarization in the US, I’ve downloaded the
[data](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/)
from the Defense Logistics Agency (DLA), which administers the 1033
program.

Below I’ve plotted the total number of MRAPs transferred to law
enforcement agencies in each state from 1990 to 2020. It’s important to
note that this is *not* a reflection of the total number of MRAPs in
each state as this just count the transfers from DLA to local agencies.
It’s possible for agencies to return the vehicles, as LAUSD did, and
they may be rendered nonoperational over time as they are costly to
maintain.

![](/images/posts/mrap/mrap-1.png)<!-- -->

By 2020 only 3 states have not received a single MRAP (Hawaii is not
included in the data from DLA, although the Marshall Project’s database
records that the FBI has received 3). The grey band in each panel of the
plot marks the suspension of the 1033 program from 2014 to 2017. While
some states like Connecticut and New Mexico demonstrate a freeze in
transfers during this period, others like Tennessee and New Jersey
continued to receive multiple vehicles. To date, the state that has
received the most MRAPs is Texas with a whopping 116 vehicles.

## Thinking about the future

This isn’t a one-time issue limited to the current aggressive police
response to peaceful protest across the US; it’s a longer-running issue
and will continue to have consequences for marginalized people
throughout the US. The police chief of Camden New Jersey made headlines
when he [joined protestors and marched with
them](https://philadelphia.cbslocal.com/2020/05/31/members-of-camden-county-police-department-march-alongside-residents-to-honor-george-floyd/).
Prior to his tenure as chief, the city disbanded the existing police
force and built an entirely new one from the ground up. Without this
radical reconstruction, it’s doubtful whether the police would have
responded with such constructive engagement. Changing the culture of
police departments takes time, and we can’t lose track of that once the
current story fades from the public consciousness.

To that end, I’ve set up this post to automatically update whenever DLA
releases new data on transfers to civilian agencies. It will serve as a
way to continue to monitor the ongoing transfer of military hardware to
civilian law enforcement agencies.

## Coda

I like to think of myself as pretty in-the-know when it comes to police
militarization in the US. I study state-based violence and repression
around the world, and I’ve been aware of increasing militarization in US
police forces for over a decade now. I still learned something new while
writing this post. The US MRAP program was inspired by the
[Casspir](https://en.wikipedia.org/wiki/Casspir) (see Guardia, Mike. 20
November, 2013. *US Army and Marine Corps MRAPs: Mine Resistant Ambush
Protected Vehicles*. Osprey Publishing. ISBN 978-1-78096-255-9., p. 4),
a vehicle developed by Apartheid South Africa based on their experiences
in the [South African Border
War](https://en.wikipedia.org/wiki/South_African_Border_War) and
[Rhodesian Bush War](https://en.wikipedia.org/wiki/Rhodesian_Bush_War),
two anticolonial wars, making the MRAP a potent symbol of how [tools
used to police the empire abroad are eventually turned on a country’s
own citizens at
home](https://www.ucpress.edu/book/9780520295629/badges-without-borders).

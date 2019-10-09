---
title: "Paper Title Number 1"
collection: publications
permalink: /publication/2009-10-01-paper-title-number-1
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2009-10-01
venue: 'Journal 1'
paperurl: 'http://academicpages.github.io/files/paper1.pdf'
citation: 'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
---
This paper is about the number 1. The number 2 is left for future work.

[Download paper here](http://academicpages.github.io/files/paper1.pdf)

Recommended citation: Your Name, You. (2009). "Paper Title Number 1." <i>Journal 1</i>. 1(1).

import pandas as pd

prefs = pd.read_csv('/home/e7uemr/preferences_sanple.csv')
#mentormax = pd.read_csv('') for reading in the mentor max
#prevcounts = pd.read_csv('') for reading in the previous counts
#We should have a pdf that has a list of all the previous mentee's and whether or not they are participating in the rematching/staying with their current mentor
#We should use this to update counts, to update pairings, and to update preferences.
prefs = prefs.set_index(list(prefs)[0])

prefs.describe()

print(prefs)

pairings=[]
counts={}
maxvalues={}
mentormax={}
#pairings in the final list of pairings and their compatability scores. counts is the number of mentees per mentor
#maxvalues is the maximum compatability score per mentee, mentormax is the max number of mentees a mentor will take on
for i in range(len(prefs.index)):
    #this makes a counter for the number of mentee's per mentor.
    counts[prefs.index[i]] = 0
    
    #this makes a list of the max number of mentee's a mentor is willing to take on. It currently sets everyone to 2. When we have a survey, we can change this 
    #to an adaptive list
    mentormax[prefs.index[i]] = 2


#this is the number of mentee's in the list
count=len(list(prefs))

for i in range(count):
    alldata={}
    whatever={}
    for column in prefs:
        #we are going through each of the mentee's and sorting by each mentee's preferences. For the first round, we set the max value each mentee can have to 
        #compare to for the rest of the program. Then we take the difference between the max and the second highest.
        sorte = prefs.sort_values(by=column, ascending=False)
        if i == 0:
            maxvalues[column]=sorte[column][0]
            difference=sorte[column][0]-sorte[column][1]
            
        #for other iterations, we take the difference between the max value and the current highest value.
        else:
            difference=maxvalues[column]- sorte[column][0] 
        alldata[column] = [sorte[column], difference]
        whatever[column] = [alldata[column][0].keys()[0], alldata[column][0][0], difference]
    first=pd.DataFrame.transpose(pd.DataFrame(data=whatever)).sort_values(by=[2,1], ascending=False)
    pairings.append([first.index[0], first[0][0], first[1][0]])

    #in this section we up the counts, and we drop the mentee. We compare to the mentor max and drop the mentor when the counts are greater than or equal
    #to the current count. 
    counts[first[0][0]] += 1
    prefs=prefs.drop([first.index[0]], axis=1)
    if counts[first[0][0]] >= mentormax[first[0][0]]:
        prefs=prefs.drop([first[0][0]], axis=0)


print(pairings)

This method relies on the compatability calculation removing any bias from responses. For example: If someone were to say they care about everything and they have a preference for everything, we'd want their compatability scores scaled such that they don't have a compatability of 100 with everyone, whereas other mentee's only have a compatability of 50 I think a reasonable way to do this is to take the levels of importance and divide them by the sum of the levels of importance in the compatability score. We may need to work on the non-number line questions to ensure they are weighted well.

---
title: Road trip expense analysis, part 1
permalink: /posts/2019/07/road-trip-expenses-pt1
date: 2019-07-22
tags:
    - data-science
    - coding
    - portfolio
---

On my road trip, I kept track of (almost) all the money I spent. I was already fairly surprised with some of my [quick calculations](/2019/07/road-trip-stats) about how little I ended up spending (just around $4000!), and I also wanted to dive a bit more into how much I spent, where, and on what. So here we go!


```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
```

## The data

I tracked all my expenses in a notebook throughout my trip, and then entered them into an Excel spreadsheet.


```python
df = pd.read_excel('money.xlsx')
# Last column just has some notes, but no data
df = df.iloc[:, :5]
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>item</th>
      <th>price</th>
      <th>category</th>
      <th>ben_or_claire</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2019-02-17</td>
      <td>gas</td>
      <td>37.14</td>
      <td>car</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-02-17</td>
      <td>sonic</td>
      <td>4.90</td>
      <td>food</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019-02-18</td>
      <td>coffee</td>
      <td>2.50</td>
      <td>food</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019-02-18</td>
      <td>lunch</td>
      <td>12.00</td>
      <td>food</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2019-02-18</td>
      <td>dinner tacos</td>
      <td>8.15</td>
      <td>food</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



I tracked the date, the expense, and the price. I also manually assigned each expense a "category." And, for the parts of the trip where Ben joined me, I also tracked who paid for the expense. Unfortunately, I didn't do a great job of tracking expenses during these weekends, so I probably won't be able to dig into that split.

Anyway, let's see how much I spent on each category:


```python
(df.groupby('category')
    .sum()
    .sort_values(by='price', ascending=False)
    #.plot(kind='bar', rot=45)
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
    </tr>
    <tr>
      <th>category</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>car</th>
      <td>1721.53</td>
    </tr>
    <tr>
      <th>food</th>
      <td>1235.75</td>
    </tr>
    <tr>
      <th>gear</th>
      <td>659.79</td>
    </tr>
    <tr>
      <th>lodging</th>
      <td>569.02</td>
    </tr>
    <tr>
      <th>fun</th>
      <td>382.89</td>
    </tr>
    <tr>
      <th>dumb</th>
      <td>134.01</td>
    </tr>
    <tr>
      <th>postcards</th>
      <td>83.06</td>
    </tr>
    <tr>
      <th>misc</th>
      <td>59.70</td>
    </tr>
    <tr>
      <th>souvenirs</th>
      <td>29.00</td>
    </tr>
  </tbody>
</table>
</div>



Okay, nothing super wild here: as expected, car and food-related expenses were the largest part. Gear also ended up being a lot, mostly because I had to buy most of my camping-related gear at the beginning of the trip (a worthy investment, I hope!) Interestingly, lodging was pretty high too -- but I'm guessing this has to do with the parts of the trip where Ben joined me, and we paid for AirBnBs.

Let's look into a couple of the more dubious categories: "dumb" (this is when I locked myself out, I think), "gear" (which has a few confusing entries), "misc" (what does that even mean), and "souvenirs" (I think that was also only one purchase).


```python
check_cats = ['dumb', 'gear', 'misc', 'souvenirs']
df.query('category == @check_cats').sort_values(by='category')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>item</th>
      <th>price</th>
      <th>category</th>
      <th>ben_or_claire</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>22</th>
      <td>2019-02-25</td>
      <td>phone repair</td>
      <td>69.01</td>
      <td>dumb</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>203</th>
      <td>2019-04-27</td>
      <td>car lockout</td>
      <td>65.00</td>
      <td>dumb</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2019-02-25</td>
      <td>rei</td>
      <td>1.60</td>
      <td>gear</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>37</th>
      <td>2019-02-26</td>
      <td>knife</td>
      <td>8.09</td>
      <td>gear</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>77</th>
      <td>2019-04-17</td>
      <td>propane</td>
      <td>9.36</td>
      <td>gear</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>131</th>
      <td>2019-05-01</td>
      <td>home depot</td>
      <td>11.66</td>
      <td>gear</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>172</th>
      <td>2019-05-19</td>
      <td>propane</td>
      <td>6.38</td>
      <td>gear</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>188</th>
      <td>2019-05-24</td>
      <td>rei</td>
      <td>124.33</td>
      <td>gear</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>204</th>
      <td>2019-02-14</td>
      <td>rei</td>
      <td>352.40</td>
      <td>gear</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>205</th>
      <td>2019-02-16</td>
      <td>rei (parents paid)</td>
      <td>297.55</td>
      <td>gear</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>206</th>
      <td>2019-05-28</td>
      <td>air mattress reimbursement</td>
      <td>-151.58</td>
      <td>gear</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2019-02-26</td>
      <td>haircut</td>
      <td>50.00</td>
      <td>misc</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38</th>
      <td>2019-02-26</td>
      <td>cds/postcards</td>
      <td>9.70</td>
      <td>misc</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>95</th>
      <td>2019-05-02</td>
      <td>license plates</td>
      <td>29.00</td>
      <td>souvenirs</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



Oh, right! Not only did I lock myself out of my car at the Grand Canyon, but I also broke my phone on the first part of my trip and had to fix it. Okay, we'll leave these two "dumb" expenses in.

The gear category is a bit tough: I exchanged my air mattress a few times, and was eventually reimbursed for it, which explains the "negative" expense on 5/28. Also, my parents got me a lot of gear for the combination of Christmas, graduation, and my birthday -- that's the 2/16 trip for about $300. We'll leave that in here, though, since that's money that I was going to spend on this trip regardless.

Like I thought, there's only one souvenir expense (oops lol). I'll just lump that into the "misc" category.


```python
# Replace "souvenir" category with "misc"
df['category'] = df['category'].replace('souvenirs', 'misc')
```

## The road trip expenses

Ok, now I'm ready to dive in. I'll first look only at the parts of the trip that I spent on my own, since when Ben was visiting we stayed in AirBnB's and went out a lot -- lots of fun, definitely a great way to spend time and money, but not the road trip I was planning or intending for.

Let's look at how much I spent on each category during each part of the trip. I'll do a bit of pandas-fu to get the sum of all expenses in each category, one time for the whole dataset and one time just for the part where it was only me.

Coding notes: I [just learned](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_r.html) that you can use the `.assign()` to make a new column within a chain of pandas commands, like the R version of `mutate`. Cool!


```python
category_totals = pd.concat([
    df.groupby('category').sum().assign(trip='all_expenses').reset_index(),
    df[df['ben_or_claire'].isna()].groupby('category').sum().assign(trip='only_me').reset_index()
])

sns.barplot(data=category_totals, x='category', y='price', hue='trip')
```


![png](/images/2019/2019-07-18-road-trip-expenses-pt1_files/2019-07-18-road-trip-expenses-pt1_11_1.png)


Hm, it's pretty hard to tell how much I spent on the part of the trip with Ben. Let's directly calculate the difference...


```python
# Convert tidy data to wide data so I can subtract columns
wide_totals = category_totals.pivot(index='category', columns='trip', values='price')

wide_totals['all_expenses'] - wide_totals['only_me']
```




    category
    car          120.85
    dumb           0.00
    food          92.34
    fun           50.00
    gear           0.00
    lodging      382.65
    misc           0.00
    postcards      0.00
    dtype: float64



Hm. That's definitely not the whole picture. I'm pretty sure the food and fun expenses are way off, and that I spent way more than just $142 during the parts with Ben -- but that makes sense, given that I didn't really keep track of everything I spent during those days, let alone what Ben was spending. Also those parts involved much more alcohol and spontaneous purchases sooo... 😅

I also don't fully remember how I entered the lodging bills -- sometimes I think I put down the full cost (like when I paid for our AirBnBs on the first part of the trip), but other times I only put down my part (especially when Ben paid).  

Anyway, no need to dive into this because I *know* I have incomplete data. Let's move on with analyzing just the road trip part where I was alone! That said, I'll keep any car expenses that I encountered during our joint trip, because I would have needed to pay those anyway. I'll remove any food we split because that's just too complicated...


```python
# Keep only rows without anything in the ben/claire column,
# and keep all rows with the "car" category
df = df[ (df['category'] == "car") | (df['ben_or_claire'].isna()) ]

df['price'].sum()
```




    4349.76



Ok, so after all this cleaning and manipulation the total amount I spent looks a little different than what I [posted previously](/2019/07/road-trip-stats), but basically the same: on my ~3 month road trip, I spent about $4300!

I have a lot of questions that I could answer by combining this data with my other mileage and lodging datasets, but for now let's see what questions we can answer just from this data alone.

### Daily expenses

If we divide that by the total number of days I was on this trip for (105), that gives us an estimate of the daily cost* of my cross-country road trip!

_\*Of course, that's recognizing that there's a couple of high-expense weekends missing in this average, which would have been replaced by camping or crashing with friends -- so the daily average for a pure road trip should be a little higher than this._


```python
df.groupby('category').sum().sort_values(by='price', ascending=False) / 105
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
    </tr>
    <tr>
      <th>category</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>car</th>
      <td>16.395524</td>
    </tr>
    <tr>
      <th>food</th>
      <td>11.769048</td>
    </tr>
    <tr>
      <th>gear</th>
      <td>6.283714</td>
    </tr>
    <tr>
      <th>lodging</th>
      <td>5.419238</td>
    </tr>
    <tr>
      <th>fun</th>
      <td>3.646571</td>
    </tr>
    <tr>
      <th>dumb</th>
      <td>1.276286</td>
    </tr>
    <tr>
      <th>misc</th>
      <td>0.844762</td>
    </tr>
    <tr>
      <th>postcards</th>
      <td>0.791048</td>
    </tr>
  </tbody>
</table>
</div>



Hah! Glad to see my "dumb" mistakes averaged out to only costing me a little over a dollar a day! 😆 And not bad -- only $12 per day for food and $21 total for transportation and lodging. Also, I'll note that the daily gear cost will keep doing as time passes, since I own that stuff forever now!

Ok, that said we all know that the average isn't necessarily that informative. Especially on this trip, I think I tended to spend a lot of money for a few days and then go to the wilderness for a few days and not spend anything at all. Let's see if this impression is correct.


```python
df.groupby('date').sum().plot(kind='hist', bins=20)
```

![png](/images/2019/2019-07-18-road-trip-expenses-pt1_files/2019-07-18-road-trip-expenses-pt1_19_1.png)


At first, this histogram surprised me because there seem to be so _few_ days where I spent zero money. But actually, this data doesn't include those days! So this histogram just shows the money I spent, on days when I spent _some_ money.

Also, note that the one negative value is the day I got reimbursed for the sleeping pad I returned. It had sprung a leak twice, and the second time I went to REI to exchange it they told me I couldn't do that without being flagged in the system, so I had to return it. I also spent some money buying a new pad that same day, but the reimbursement wasn't processed till a few days after so it was on its own day.

Anyway, back to my questions about my spending habits. First up: how many days in a row would I spend money?


```python
days_btw_purchases = df.sort_values(by='date')['date'].drop_duplicates().diff().dt.days

# Remove the large value which represents the month I went to Malaysia
days_btw_purchases[days_btw_purchases < 30].value_counts()
```




    1.0    59
    2.0     6
    3.0     2
    Name: date, dtype: int64



So there were 55 days in a row where I made some sort of purchase, and only 2 days where I waited 3 days between purchases. I didn't ever wait more than 3 days (except the one-month break when I went to Malaysia, lol).

This is actually quite surprising! In my mind, I would go to the big city, buy a bunch of stuff, and then retreat to the wilderness. But now that I think about it, in actuality I would do that, but for big expenses only. I made small purchases almost every day, either stopping by a coffee shop or getting pie at Capitol Reef or other small joys.

Let's see how these numbers change as I increase the amount of money that I consider a "purchase":


```python
fig, ax = plt.subplots(1, 3, figsize=(10, 2))

prices = [10, 35, 50]
i = 0
for p in prices:

    days_btw_purchases = df.query('price > @p').sort_values(by='date')['date'].drop_duplicates().diff().dt.days
    days_btw_purchases[days_btw_purchases < 30].plot(kind='hist', ax=ax[i])

    ax[i].set_title('${}'.format(p))
    if i == 0:
        ax[i].set_ylabel('Frequency')
    else:
        ax[i].set_ylabel('')

    ax[i].set_xlabel('Days between purchase')
    i += 1
fig.tight_layout()
```


![png](/images/2019/2019-07-18-road-trip-expenses-pt1_files/2019-07-18-road-trip-expenses-pt1_23_0.png)


Damn. There were five times when I spent more than $50 two days in a row?? (That's what the left-most bar in the $50 panel tells me). And in general, there were only a few times when I went more than a week in between > $50 expenses.

On the flip side, there was only one time when I went like 5 days without spending more than $10. This was probably the week that I was hanging out in Utah, from Bryce to Moab.

The $35 price cutoff is intersting, because it kind of _de facto_ removes most of my gas fillups since they were usually about $30. Here the purchases are more varied: sometimes I spent more than $35 two days in a row, and other times I went about a week without spending that much on any given day. This jives much more with my feeling on how I spent money this trip.

Either way, I was maybe a less big spender than I expected ($4300 is so little for such a massive trip), but definitely a _more frequent_ spender than I thought.

### Gas, groceries, and camping

Now let's zoom in more specifically to the three big categories of expenses, and the ones you might be most interested in if you're planning your own trip.

The "car" category includes gas and other things, but for now I'm honestly only interested in looking at how often I paid for gas. Similarly, let's focus on my grocery shopping trips rather than eating out, since if you were trying to have the cheapest road trip possible then this would be the most important thing to look at.


```python
# Find all gas and grocery expenses, and put them in their own sub category
df['sub_category'] = df['category']
df.loc[df['item'].str.contains('gas'), 'sub_category'] = 'gas'
df.loc[df['item'].str.contains('groceries'), 'sub_category'] = 'groceries'
```

I'll do a similar analysis as above, looking at how many days in a row I spent money on each given thing. This time, though, I'll look within each category only. For example, this will let me answer "on average, how many days would I go between filling up my tank?"


```python
# Calculate days between spending on the same category
df['days_since_last_same_category'] = df.sort_values(by='date').groupby('category')['date'].diff().dt.days
df['days_since_last_same_subcategory'] = df.sort_values(by='date').groupby('sub_category')['date'].diff().dt.days

# Remove the large gap from Malaysia
df.loc[df['days_since_last_same_category'] > 30, 'days_since_last_same_category'] = np.nan
df.loc[df['days_since_last_same_subcategory'] > 30, 'days_since_last_same_subcategory'] = np.nan

df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>item</th>
      <th>price</th>
      <th>category</th>
      <th>ben_or_claire</th>
      <th>sub_category</th>
      <th>days_since_last_same_category</th>
      <th>days_since_last_same_subcategory</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2019-02-17</td>
      <td>gas</td>
      <td>37.14</td>
      <td>car</td>
      <td>NaN</td>
      <td>gas</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-02-17</td>
      <td>sonic</td>
      <td>4.90</td>
      <td>food</td>
      <td>NaN</td>
      <td>food</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2019-02-18</td>
      <td>coffee</td>
      <td>2.50</td>
      <td>food</td>
      <td>NaN</td>
      <td>food</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019-02-18</td>
      <td>lunch</td>
      <td>12.00</td>
      <td>food</td>
      <td>NaN</td>
      <td>food</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2019-02-18</td>
      <td>dinner tacos</td>
      <td>8.15</td>
      <td>food</td>
      <td>NaN</td>
      <td>food</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2019-02-18</td>
      <td>gas</td>
      <td>32.89</td>
      <td>car</td>
      <td>NaN</td>
      <td>gas</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2019-02-18</td>
      <td>groceries</td>
      <td>35.21</td>
      <td>food</td>
      <td>NaN</td>
      <td>groceries</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2019-02-19</td>
      <td>gas</td>
      <td>23.41</td>
      <td>car</td>
      <td>NaN</td>
      <td>gas</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2019-02-19</td>
      <td>guitar center</td>
      <td>68.17</td>
      <td>fun</td>
      <td>NaN</td>
      <td>fun</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2019-02-20</td>
      <td>gas</td>
      <td>8.66</td>
      <td>car</td>
      <td>NaN</td>
      <td>gas</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
keep_cats = ['food', 'car', 'lodging']
g = sns.FacetGrid(data=df.query('category == @keep_cats'), col='category',
                  sharey=False, col_order=keep_cats, sharex=False)
g.map(plt.hist, 'days_since_last_same_category')
```

![png](/images/2019/2019-07-18-road-trip-expenses-pt1_files/2019-07-18-road-trip-expenses-pt1_29_1.png)


Hm. This is also surprising, and tells me that I spent money on way more days than I thought. (I am seeing this in the fact that the "0" bar is quite large on all histograms, indicating that I frequently went zero days in between sequential purchases).

Specifically, I bought food two days in a row about 40 times. And then the majority of the rest of the times I bought food were just 1 day apart. In other words, for the majority of my trip I bought food either every day or every other day.

Looks like the story is pretty similar for car-related expenses: the majority of expenses had a lag of 0-2 days. So for the majority of my trip, I spent money on my car somewhere between every day and every 3 days. That makes sense -- I usually moved to a new spot every 2-3 days, which entailed a lot of driving, and I must have gotten gas basically every time I did that.

Now, lodging. Let's see: does this make sense? My impression is that I super rarely paid for housing... What this is saying is that yes, there were a few times when I went a week or more without paying for housing, but when I did pay for housing I paid for housing again within the next three days. I have a separate spreadsheet where I tracked the lodging expenses more cleanly, we'll have to come back to this when we analyze that one...

Let's zoom into the groceries and gas question, because I think these expenses are where I'm drawing my intuition from.


```python
keep_subcats = ['groceries', 'gas']
g = sns.FacetGrid(data=df.query('sub_category == @keep_subcats'), col='sub_category',
                  sharey=False, col_order=keep_subcats, sharex=False)
g.map(plt.hist, 'days_since_last_same_subcategory')
```

![png](/images/2019/2019-07-18-road-trip-expenses-pt1_files/2019-07-18-road-trip-expenses-pt1_31_1.png)


Yeah, I think this checks out. Of the 9 times I bought groceries, about 2/3 of them were at least 5 days apart (these are the bars on the right of the "groceries" plot). That makes sense -- I feel like I tended to buy groceries about once a week, and sometimes I'd have forgotten something so would need to swing back by the store the next day to get a bit more.

Similarly, most of my gas purchases were something like 2-3 days apart. This also makes sense, given my reasoning above about how often I was on the move.

## Coffee

Okay, I'm getting a bit tired of this deep dive but there is one more thing I want to know: how much money did I spend on caffeine?

As I was putting these data into the spreadsheet, I found myself often typing "coffee" or "tea." Ruh roh...


```python
# Get any items where I specified coffee or tea
df[df['item'].str.contains('coffee|tea')]['item'].value_counts()
```




    coffee                  15
    tea                      3
    coffee and lunch         2
    coffee and donuts        1
    tea and gatorade         1
    coffee and breakfast     1
    coffee and taters        1
    coffee and muffin        1
    pie and coffee           1
    iced tea                 1
    Name: item, dtype: int64



Hehe, can you tell that I liked to treat myself to coffee in a variety of ways? :)

I'll note here that I _also_ had instant coffee available, which isn't included in these expenses (I bought a super-pack at Costco). Pro-tip for all my fellow road tripping caffeine addicts: the Starbucks instant coffee is actually quite nice! There was even once where I treated myself to "real" coffee at some Bryce Canyon lodge, and it was _way worse_ than my usual instant. Good to know. But also I am weak and loved to treat myself to coffee and breakfast whenever I could reasonably justify it.

Okay but back to business: how much did I spend, and how often?


```python
caffeine = df[df['item'].str.contains('coffee|tea')]
caffeine['price'].sum()
```




    140.61



Hah! I spent $140 on caffeine (plus, at times, also food -- but let's be real the breakfast was just an excuse to buy coffee). That's about $1.30 a day, which is... not bad? (Though, again, this was _treat_ coffee, and I had instant most days of the trip.)

Okay. How many days did I go in between giving in to my desire for some non-instant coffee or other caffeine?


```python
days_btw_caffeine = caffeine.sort_values(by='date')['date'].drop_duplicates().diff().dt.days
days_btw_caffeine = days_btw_caffeine[days_btw_caffeine < 30]
days_btw_caffeine.plot(kind='hist')
plt.xlabel('Days between caffeine')
```


![png](/images/2019/2019-07-18-road-trip-expenses-pt1_files/2019-07-18-road-trip-expenses-pt1_38_1.png)


And therein, my friends, lies the histogram of an addict: I rarely went more than 5 days in between buying myself some form of caffeine.

So it goes. And it was all worth it.

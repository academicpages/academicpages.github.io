---
title: "kjbot"
excerpt: "A telegram bot for debt tracking between me and my housemates.<br/><img src='/images/korsan.jpg'><img src='/images/jaime.jpg'>"
collection: portfolio
---

kjbot (korsan-jaime-bot, named after two cats that lived with us for several months) is a telegram bot written in Python.
The source code lives on [furkan/korsan-jaime-bot](https://github.com/furkan/korsan-jaime-bot)

It has been our main debt tracking solution since the summer of 2019. It was initially hosted on [Python Anywhere](https://pythonanywhere.com) with Flask and webhooks. In late 2022, I moved it to a Raspberry Pi Zero W in our living room, along with removing webhooks and introducing containerization to the project. Ever since then, it has been running robustly as long as there is electricity and an Internet connection.

### Summary of commands

* **/start:** Starts the bot
* **/help:** Replies with command explanations.
* **/paid x y:** Use this when you gave **x** amount of money to **y**.
* **/spent x y:** Use this when the **x** amount of money you spent on **y** is for all members. (The bot sends a message about this purchase to all members. That's why **y**, the item, is mandatory.)
* **/status:** Display the current balance.

#### Commands that were added later

* **/add x:** Add **x** to chores/shopping list.
* **/list:** Display the chores/shopping items with their indices.
* **/remove x:** Remove the item with index **x** from the chores/shopping list.

### Korsan

![korsan](/images/korsan.jpg)

### Jaime

![jaime](/images/jaime.jpg)

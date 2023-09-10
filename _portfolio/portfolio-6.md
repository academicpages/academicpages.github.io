---
title: "RMP Extension"
excerpt: "Schedule Builder Extension for UC Davis students<br/>"
collection: portfolio
---
Developers: Shuaib Ahmed, Mark Soliman, Dave Nyugen


[Check it out on Github Here!](https://github.com/shuaibahmed01/RMP_extension)

## About

The RMP Extension provides UC Davis students with a streamlined and efficient method to checking professor ratings when signing up for classes. Through a simple installation of the chrome extension, students will see a display of professor names and their corresponding ratings according to the famous application, Rate My Professor. With the simple pressing of the search button on Schedule Builder, users will get a view of which professors have the best reputations.

## Behind the Scenes

We built our application using python libraries (bs4, pandas, numpy) to create various data frames to store professor full names then utilized Rate My Professor's api to grab each professors overall rating, level of difficulty, etc. When the search button on schedule builder is pressed, the extension we created correlates the information collected in out data frames to display all professors ratings according to the data frame.
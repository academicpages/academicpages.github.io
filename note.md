## Technical notes on making websites (for personal/projects/courses)


+ for course website, where we want quick edits of pages using MarkDown and no need for beauty, we should use Github + Jekeyll, like this:
    + https://github.com/cs231n/cs231n.github.io
    + this basically convert the markdown to html on the server side when you request a page
    + disadvantage: you will need to build the website to test it locally. But using a markdown viewer would be suffice
    + for local testing. It's just that you cannot get exactly what you see online

+ for personal page, I choose native html + jQuery + CSS (Bootstrap) for its local testability
    + we have to put duplicate header + sidebar html in multiple files since html does not have static "include" functionality
    + also, I use Google Analytics to track my viewer statistics
    + also, I use CNAME to point junweiliang.github.io to my custom domain junweiliang.me (and the files are still hosted on github)

+ for the more frequently updated content like blogs/awesome lists/letter/current openings, host them in a github repo and deliver embeded page through this guy
    + https://github.com/yusanshi/emgithub
    + basically a \<script\> to call a .js to get Github content in your page
    + you can overwrite the CSS as well

+ for showing a github link and number of star, use this
    + https://github.com/mdo/github-buttons
    + an \<iframe\> to put in your html

+ the style of my webpage (version 08/2022) is inspired by:
    + http://www.columbia.edu/~zs2262/index.html
    + https://viterbi-web.usc.edu/~feisha/

+ a visitor counter (and a badge to show it) is from this guy
    + https://visitor-badge.glitch.me/#docs
    + you can use it in markdowns as well as htmls

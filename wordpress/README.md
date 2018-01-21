I exported the Wordpress xml file from the wordpress dashboard
(`Tools > Export`).

I installed the `wp2md` tool from [the repo](https://github.com/dreikanter/wp2md)
and then ran:

```
wp2md -v -d cduvallet.github.io/wordpress/ claireduvallet.wordpress.2018-01-21.xml 
```

(from my main github folder, and then I moved the xml into this folder. It would
probably work from within here too, no biggie.)
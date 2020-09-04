---
title: "Password Checker with Python"
excerpt: "Online security is more important than ever. Research by Google in 2019  showed that thousands of people are using passwords that have [been hacked](https://thenextweb.com/security/2019/08/16/google-study-says-people-are-still-using-old-passwords-after-being-compromised/). More than 300, 000 users utilise credentials that have been previously compromised. [Read More...](/portfolio/2020-05-28-password-checker/)<br/><img src='/images/2020-05-28-password-checker/pass.jpg' style='max-width: 500px;'>"
collection: portfolio
---
### To download this application for your own use please check out the [repo](_portfolio/2020-07-12-covid-19-ct-scans.md)


Online security is more important than ever. With the advent of social media, block chain and many other new applications, we use authentication every day to carry our personal needs. 

A  report from the Identity Theft Resource Center found that there were 1,473 data breaches last year, a 17% increase over 2018's 1,257. The total number of sensitive records exposed, though was down 65%. Contrary to public assumption, hackers generally do not target specific individuals but rather large corporations. Hackers look for a security weakness to steal or copy as much personal information as possible in order to compile a list of leaked usernames and passwords to log in to different services. 

This has highlighted the need for services and websites to check the security of personal passwords and usernames. Websites like [have I been pwned](https://haveibeenpwned.com) to check whether your password or username has been compromised in a data breach. 

![png](/images/2020-05-28-password-checker/pwned.png)

However there is a more secure way of doing this rather than sending your personal information over the web for it to be intercepted. The pwned website operates using a database to check your information against. Knowing this we can use API requests with python directly.

The ```requests``` module  will allow us to make request, like having a browser but without the actual browser. 

```python 
import requests
url = 'https://api.pwnedpasswords.com/range/' + 'password123'
response = requests.get(url)
print(response)
```

### Hash Function

A function that generates a value of fixed length for each input that it gets. 

md5 - type of hash function, there are other such as SHA1.

A hash function generates some random pattern based on the input. There are some key features:

1. It's one way -  no one will know what the input is.
2. The output will always be the same. No matter how many times it's input.

This called idempotent. A function given an input always output the same thing. The one benefit is that we get really fast data access. 

Technically a hash function is going to take the input, translate it into gibberish and convert it to an index or addess space that is has based on this number.

Unlike arrays where we had ordered indexes, with hash tables, all we need to do is give it a key and we know exactly where that item is in our memory. But does the hash function slow things down? - we have to run it through the hash function, You don't want this process of storing data using the hash function to take a long time because every time you add a property to memory or  retrieve a property to memory we need this to be fast. Underneath the hood they are implemented with an optimum hashing function. Hash functions like SHA 256 take a really long time to generate a has and it is an overly complex hashing function use in places like cryptography.  When it comes to hashing functions you usually leave it to whichever frame work being used and we usually assume a time complexity or Big O notation of  01 because it happens really fast.


## Writing the program

Instead of giving the entire hash we only give the first 5 letters. [pwned.com](http://pwned.com) has close to 600 million passwords in their database, and the website now  just knows we're part of several 100 people that have the start hash. Now with the response we can check if our password has been hacked, by comparing our has with the list of password hashes that have been returned. 


```python
import requests
import hashlib

def request_api_data(query_char):
    """ requests data from an api and outputs a response"""
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {response.status_code}, check the API and try again')
    return response

def pwned_api_check(password):
    """check password if it exists in api response
    Have to run our password through the sha1 algorithm
    """
    print(hashlib.sha1(password.encode('utf-8')))
    # sha1password = hashlib.sha1(password.encode('utf-8'))

pwned_api_check('123')
```
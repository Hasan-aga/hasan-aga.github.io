---
title: Clean any NSFW content from you Reddit account
description: Using a simple Python script.
date: '2021-08-03T14:46:45.513Z'
categories: []
keywords: []
slug: /@hasan-alsulaiman/clean-any-nsfw-content-from-you-reddit-account-964174d7a83
comments: true
---

#### Before No Nut November

Using a simple Python script.

![](/assets/0__Us5f4J6HyUVQjNoA.jpg)
)
Social media giants such as Reddit and Twitter have been using NSFW content to promote their platforms, this turned these platforms into porn sites, which is sad since they have so much better content which is now being overshadowed by stupid porn, I didn’t ask for this since dedicated porn sites already exists and they are more than enough 😑

I wanted to clean up my Reddit from any NSFW content that I might have upvoted or saved (I do have a weakness for 🍰) and since doing so manually takes too long, I wrote a Python script to automate the boring task.

### How it works?!

I found out that what I need to do first is create a Reddit application (a bot), this way I can use Reddit’s API to retrieve a list of my saved items/ Upvotes, filter them for NSFW, then delete the filtered content, [creating an app](https://ssl.reddit.com/prefs/apps/) is simple

![](/assets/1__YXm__UbgzZWClFbT1lYS__Eg.jpeg)
)
make a note of the **_“personal use script”_** and **_“secret”_**, you will use these to authenticate you bot.

### The script

We can use Reddit API directly, or, we can make use of a Python library called [PRAW](https://praw.readthedocs.io/en/stable/getting_started/installation.html) which simplifies our communication with the API, so install PRAW by typing the following command into _Powershell_ in windows (or any terminal)

pip install praw

now go to the [Github repo](https://github.com/Hasan-Alsulaiman/Reddit/blob/main/savedReddit.py) and get a copy of the script

### Starting the script

To start, first fill in the required fields with your credentials, then you can use the methods inside **_MyReddit_** class to retrieve or delete your saved items or upvotes, note that you can delete all the items OR only the NSFW ones, so be careful!

\# user\_agent = name of your bot (can by anything)      
\# username, password = your reddit account creditentials      
\# the following info can be obtained by creating a reddit app      
\# Client\_id = personal use script      
\# client\_secret = secret

myReddit = MyReddit(client\_id="your own",  
        client\_secret="your own",  
        user\_agent="your own",  
        username="your own",  
        password="your own")      
myReddit.delete\_nsfw\_save()  
myReddit.delete\_nsfw\_upvote()

Note: deleting Upvotes will not work for old Upvotes because of Reddit’s spam policy, I found it only works with recent Upvotes

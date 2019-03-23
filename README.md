<h1 align="center">
  <br>
  <img src="https://raw.githubusercontent.com/tinyqubit/RedditBot_OnlineUsers/master/Images/Reddit_Logo.png" alt="Reddit" width="200">
  </br>
  RedditBot: Subreddit Online Users
  <br>
</h1>

<p align="center">
  <a href="#instructions">Instructions</a> •
  <a href="#libraries-used">Libraries Used</a> •
  <a href="#example-graph-output">Example Graph Output</a> •
  <a href="#future-features">Future Features</a>
</p>

<p align="center">
<img src="https://raw.githubusercontent.com/tinyqubit/RedditBot_OnlineUsers/master/Images/Example_Plot_1.png" alt="Reddit" width="700">
</p>

# Purpose
Track the amount of online users for a given subreddit you provide every time interval, and save that data to display on a graph.

## Instructions: Getting Started
First, you'll want to set up your credentials to use the Reddit API. You'll notice at the bottom of the script *subreddit_onlineusers_collector.py* you'll see:
```python
reddit = praw.Reddit(client_id = 'CLIENT_ID', client_secret = 'CLIENT_SECRET', username = 'USERNAME', password = 'PASSWORD', user_agent = 'USER_AGENT')
```
You can watch this video made by Sentdex to help you set this up!
https://www.youtube.com/watch?v=NRgfgtzIhBQ

<hr>

Once you've set up your credentials, you can run the program.
There are 2 scripts involved.
```
subreddit_onlineusers_collector.py
subreddit_onlineusers_grapher.py
```

## Instructions: Subreddit_OnlineUsers_Collector.py
This script will collect the online user count of the given subreddit you provide, and store the data in a text file. You will notice it'll create a directory on your desktop:
*Desktop/RedditBot_OnlineUsers/SUBREDDIT_subreddit_onlineusers*

It will create a file in this directory using this naming convention: 
*SUBREDDIT_DATE.txt*

This file stores all the data you've collected, and is used later by *subreddit_onlineusers_grapher.py*

In the *SUBREDDIT_DATE.txt* you will see the data:
```
13:15:43,2274
13:15:54,2274
13:16:04,2274
13:16:15,2283
```
It includes the time that the data was collected at, and the online user count at that time.

<hr>

You can edit these variables to your preference.
```python
# The name of the subreddit you want to use.
(string) subreddit_name

# The time in seconds between checking the online user count.
(int) sleep_time
```



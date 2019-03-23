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

# Purpose
Track the amount of online users for a given subreddit you choose every time interval, and save that data to display on a graph.

## Instructions: Getting Started
First, you'll want to set up your credentials to use the Reddit API. You'll notice at the bottom of the script *subreddit_onlineusers_collector.py* you'll see:
```python
reddit = praw.Reddit(client_id = 'CLIENT_ID', client_secret = 'CLIENT_SECRET', username = 'USERNAME', password = 'PASSWORD', user_agent = 'USER_AGENT')
```
You can watch this video made by Sentdex to help you set this up!
https://www.youtube.com/watch?v=NRgfgtzIhBQ

<hr>

There are 2 scripts involved.
```
subreddit_onlineusers_collector.py
subreddit_onlineusers_grapher.py
```

## Instructions: Subreddit_OnlineUsers_Collector.py
You'll want

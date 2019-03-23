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

# The time in seconds between checking the online user count. The default is 60 seconds.
(int) sleep_time
```

## Instructions: Subreddit_OnlineUsers_Grapher.py
This script will use the collected data in the text file *SUBREDDIT_DATE.txt* to display the data on a graph.

You can edit these variables to your preference.
```python
# The name of the subreddit you want to use.
(string) subreddit_name

# The date of data you want to collect. Use format MM-DD-YYYY
(string) date_to_collect
```

**Please note that these variables above are used to grab the text file, so make sure the names and dates are correct to what you have saved in the directory.**

## Example Graph Output
This displays the online user count over time. The time format is HOUR:MINUTE:SECOND
<p align="center">
<img src="https://raw.githubusercontent.com/tinyqubit/RedditBot_OnlineUsers/master/Images/Example_Plot_1.png" alt="Reddit" width="700">
</p>

## Libraries Used
subreddit_onlineusers_collector.py
```
praw
datetime
csv
os.path
```

subreddit_onlineusers_grapher.py
```
numpy
matplotlib
csv
os.path
```

## Future Features
- Ability to ask user for variable values through the console instead of going into the script to change them.
- Ability to track multiple subreddits at the same time.

## You May Also Like...
Reddit Bot: Posts Up Votes Grabber
https://github.com/TinyQubit/RedditBot_PostsUpVotesGrabber

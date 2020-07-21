import praw
import datetime as dt
import time
import csv
import os.path

# EDITABLE
subreddit_name = 'gamedev' # !!Must be exactly as written in Reddit.
sleep_time = 60 # How many seconds between checking?

# BE CAUTIOUS EDITING.
directory_path = "~/Desktop/RedditBot_OnlineUsers/" + str(subreddit_name) + "_subreddit_onlineusers/"

def CheckCurrentDate():
    global start_date

    current_date = dt.datetime.now().strftime("%m-%d-%Y")

    if current_date != start_date:
        start_date = current_date

def CheckForDirectory():
    global subreddit_name
    global directory_path

    print(directory_path)
    if not os.path.exists(os.path.expanduser(directory_path)):
        try:
            os.makedirs(os.path.expanduser(directory_path))
            print("Directory successfully created!\n")
        except:
            print("Directory could not be created, or it already exits.\n")

def WriteToFile(_online_users, _readable_time):
    global subreddit_name
    global start_date

    file_name = str(subreddit_name) + "_" + str(start_date)
    path = os.path.expanduser(directory_path + "/" + str(file_name) + ".txt")
    with open(path, "a") as csvFile:
        filewriter = csv.writer(csvFile)
        filewriter.writerow([_readable_time, _online_users])
        csvFile.close()

def RunProgram():
    global subreddit
    global subreddit_name

    CheckCurrentDate()

    readable_time = str(dt.datetime.now().time().strftime("%H:%M:%S"))
    subreddit = reddit.subreddit(subreddit_name)
    online_users = subreddit.active_user_count    

    WriteToFile(online_users, readable_time)

    print("\n" + str(subreddit_name) + " has " + str(online_users) + " users online as of " + str(readable_time))
    print("CURRENT CALLS: " + str(reddit.auth.limits) + "\n--------------------\n")
    time.sleep(sleep_time)
    RunProgram()

# PROGRAM EXECUTION STARTS HERE.
reddit = praw.Reddit(client_id = 'CLIENT_ID', client_secret = 'CLIENT_SECRET', username = 'USERNAME', password = 'PASSWORD', user_agent = 'USER_AGENT')
print("INITIAL CALLS: " + str(reddit.auth.limits))
subreddit = reddit.subreddit(subreddit_name)
start_date = dt.datetime.now().strftime("%m-%d-%Y")

CheckForDirectory()
RunProgram()

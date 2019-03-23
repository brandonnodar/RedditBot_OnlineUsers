import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import os.path
import csv

# EDITABLE
subreddit_name = "gamedev"
date_to_collect = "03-22-2019" # Make sure format is: MM-DD-YYYY

# BE CAUTIOUS EDITING
root_directory = "~/Desktop/Reddit_Bot/"

# Initializations. DO NOT EDIT UNLESS LAST RESORT.
data_x = []
data_y = []

def GrabDataFromTextFile():
    global root_directory
    global subreddit_name
    global date_to_collect
    global data_x
    global data_y

    file_path = os.path.expanduser(str(root_directory) + str(subreddit_name) + "_subreddit_onlineusers/" + str(subreddit_name) + "_" + str(date_to_collect + ".txt"))
    print(file_path)
    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            '''
            hours, minutes, seconds = map(int, row[0].split(":"))
            str_hours = str(hours) + "." + str(minutes)
            float_hours = float(str_hours)
            data_x.append(float_hours)
            '''
            data_x.append(row[0])
            online_count = int(row[1])
            data_y.append(online_count)

def GraphData():
    global data_x
    global data_y
    global subreddit_name

    print("Graphing data now...")

    '''
    x = np.array(data_x)
    test_y = [500, 1000, 1500, 2000, 2500, 3000]
    y = np.array(test_y)
    
    plt.xlabel('Time')
    plt.ylabel('Up Votes')
    plt.title("Subreddit: " + str(subreddit_name))
    '''
    
    '''
    plt.plot(data_x, data_y, c="#ff4400")
    
    plt.title("Subreddit: " + str(subreddit_name))
    plt.xlabel("Time")
    plt.ylabel("Up Votes")
    
    plt.xticks(rotation=90)
    
    
    plt.locator_params(numticks = 10)
    plt.show()
    '''
    
    
    x = data_x
    y = data_y
    plt.plot(x, y)

    ax = plt.subplot() 

    every_nth = 40
    for i, tick in enumerate(ax.xaxis.get_ticklabels()):
        if i % every_nth != 0:
            tick.set_visible(False)
        
    for i, line in enumerate(ax.xaxis.get_ticklines()):
            if i % every_nth != 0:
                line.set_visible(False)
        

    plt.xticks(fontsize=8, rotation=60)
    plt.show()



    

GrabDataFromTextFile()
GraphData()        
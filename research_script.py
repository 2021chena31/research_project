#Written by Angie Chen
#Based on https://www.geeksforgeeks.org/scraping-reddit-using-python/

import praw
import pandas as pd

NUM_POSTS = 100
SUBREDDIT_LIST = ["alcoholicsanonymous"] #list of subs to scrape

#pull api keys
def pull_keys(fileName):
    f = open(fileName,'r')
    ls = f.readlines()

    for i in range(len(ls)):
        ls[i] = ls[i].strip("\n")
    
    f.close()
    return ls

#write information to csv, given the subreddit name
def to_csv(subreddit_name, amount):
    subreddit = reddit_read_only.subreddit(subreddit_name)
    fileName = subreddit.display_name + ".csv"
    
    f = open(fileName,'w')
    f.write("title,description,author,score,number of comments,url\n")

    for post in subreddit.new(limit=amount):
        try:
            f.write('"'+str(post.title)+'"' + ",")
            f.write('"'+str(post.selftext)+'"' + ",")
            f.write("u/"+str(post.author) + ",")
            f.write(str(post.score) + ",")
            f.write(str(post.num_comments) + ",")
            f.write(post.url + ",")
            f.write('\n')
        except:
            f.write("parse error.")
            f.write('\n')

    f.close()
    print(subreddit.display_name + ".csv file complete.")
    
    

if __name__ == '__main__':
    keys = pull_keys("research_script_keys.txt")
    
    reddit_read_only = praw.Reddit(client_id=keys[0],         # your client id
                                   client_secret=keys[1],      # your client secret
                                   user_agent=keys[2])        # your user agent

    for sub in SUBREDDIT_LIST:
        to_csv(sub, NUM_POSTS)
    

    print("Script finished.")
    #use regex to pull related subreddits?
     
    # Display the name of the Subreddit
    #print("Display Name:", subreddit.display_name)
     
    # Display the title of the Subreddit
    #print("Title:", subreddit.title)
     
    # Display the description of the Subreddit
    #print("Description:", subreddit.description)

    #subreddit = reddit_read_only.subreddit("Python")
 
    #for post in subreddit.hot(limit=5):
    #    print(post.title)
    #    print()

    

import praw
import pandas as pd


def pull_keys(fileName):
    f = open(fileName,'r')
    ls = f.readlines()

    for i in range(len(ls)):
        ls[i] = ls[i].strip("\n")
    
    f.close()
    return ls


def to_csv(subreddit_name):
    subreddit = reddit_read_only.subreddit(subreddit_name)
    fileName = subreddit.display_name + ".csv"
    
    f = open(fileName,'w')
    #f.write(subreddit.display_name + "\n")

    f.close()
    
    


if __name__ == '__main__':
    keys = pull_keys("research_script_keys.txt")
    
    reddit_read_only = praw.Reddit(client_id=keys[0],         # your client id
                                   client_secret=keys[1],      # your client secret
                                   user_agent=keys[2])        # your user agent


    #use regex to pull related subreddits?
     
    # Display the name of the Subreddit
    #print("Display Name:", subreddit.display_name)
     
    # Display the title of the Subreddit
    #print("Title:", subreddit.title)
     
    # Display the description of the Subreddit
    #print("Description:", subreddit.description)

    subreddit = reddit_read_only.subreddit("Python")
 
    for post in subreddit.hot(limit=5):
        print(post.title)
        print()

    

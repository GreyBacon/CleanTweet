from tkinter import ttk
import tweepy
import tkinter as tk
import twitauth
from cleanup import cleanup
import re

# Consumer key and secret referred to in twitauth.py
# If using this code you will need to make a twitauth.py file with consumer_key and consumer_secret
consumer_key = twitauth.consumer_key
consumer_secret = twitauth.consumer_secret

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def run_tweets(event='', msg_counter=[]):
    # Reset output
    reset_counter = 0
    for msg in msg_counter:
        msg_counter[reset_counter].destroy()
        reset_counter += 1
    msg_counter.clear()

    # Catch any errors that might come from the input
    try:
        # Check if the entry is a twitter url and post specific tweet if so
        if re.search('^(https:\/\/twitter\.com\/)', user_input.get()) and re.search('\/(\d+)$', user_input.get()):
            # Pulls the tweet ID out of the url
            url = re.search('(\d+)$', user_input.get()).group(0)

            # Output original tweet
            valid_text = api.get_status(url, tweet_mode="extended").full_text
            valid_text = ''.join(c for c in valid_text if c <= '\uFFFF')
            orig_message = tk.Message(root, text=valid_text, background='antiquewhite1', width='400')
            orig_message.grid(column=0, row=3, sticky='W' + 'E')
            msg_counter.append(orig_message)

            #Post changed tweet only if there were changes
            if valid_text == cleanup(valid_text):
                clean_message = tk.Message(root, text="No changes were made", background='antiquewhite1', width='400')
                clean_message.grid(column=1, row=3, sticky='W' + 'E')
                msg_counter.append(clean_message)
            else:
                clean_message = tk.Message(root, text=cleanup(valid_text), background='antiquewhite1', width='400')
                clean_message.grid(column=1, row=3, sticky='W' + 'E')
                msg_counter.append(clean_message)

        # Search up to 10 tweets matching inputted term
        else:
            loop_pos = 0
            for status in tweepy.Cursor(api.search, q=user_input.get() + ' -filter:retweets', tweet_mode='extended',
                                        result_type='mixed').items(100):
                if loop_pos < 10:
                    # Clean up emoji and other invalid characters
                    valid_text = status.full_text
                    valid_text = ''.join(c for c in valid_text if c <= '\uFFFF')

                    # Check if there were any changes to each post
                    # Alternate colors per line and output original/changed text
                    if cleanup(valid_text) != valid_text:
                        if (loop_pos % 2) == 0:
                            alternate_colors = 'antiquewhite1'
                        else:
                            alternate_colors = root.cget('bg')

                        # Output original and cleaned up tweets into two columns
                        orig_message = tk.Message(root, text=valid_text, background=alternate_colors, width='400')
                        orig_message.grid(column=0, row=loop_pos + 3, sticky='W' + 'E')
                        msg_counter.append(orig_message)
                        clean_message = tk.Message(root, text=cleanup(valid_text), background=alternate_colors, width='400')
                        clean_message.grid(column=1, row=loop_pos + 3, sticky='W' + 'E')
                        msg_counter.append(clean_message)
                        loop_pos += 1
            if loop_pos == 0:
                orig_message = tk.Message(root, text="No fitting messages were found", background='antiquewhite1', width='400')
                orig_message.grid(column=0, row=loop_pos + 3, sticky='W' + 'E')
                msg_counter.append(orig_message)
    except:
        clean_message = tk.Message(root, text=cleanup(valid_text), background=alternate_colors, width='400')
        clean_message.grid(column=1, row=loop_pos + 3, sticky='W' + 'E')
        msg_counter.append(clean_message)

# Set up window
root = tk.Tk()
root.title("Twitter Cleaner")
root.geometry("800x800")
tk.Grid.columnconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 1, weight=1)
input_label = tk.Label(root, height=1, text="Search term or post URL").grid(column=0, row=0, sticky='W', padx=(15,0))
user_input = tk.Entry(root)
user_input.grid(column=0, row=1, sticky='W' + 'E', padx=(15, 15))
button_run = tk.Button(root, text="Search", command=run_tweets).grid(column=1, row=1, sticky='W')
user_input.bind('<Return>', run_tweets)
orig_label = tk.Label(root, height=1, text="Original tweet", font='size=16').grid(column=0, row=2, sticky='W' + 'E')
clean_label = tk.Label(root, height=1, text="Cleaned up tweet", font='size=16').grid(column=1, row=2, sticky='W' + 'E')

root.mainloop()

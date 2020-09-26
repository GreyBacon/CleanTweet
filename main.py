import tweepy
import tkinter as tk
import twitauth
import cleanup

# Consumer key and secret referred to in twitauth.py
consumer_key = twitauth.consumer_key
consumer_secret = twitauth.consumer_secret


''' Old method needing access token/secret, not needed since there this is read-only
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)'''

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def run_tweets(event=''):
    # Reset textboxes
    original_text.delete('1.0', 'end')
    new_text.delete('1.0', 'end')

    # TODO limit results by total results instead of searches
    # Search all tweets
    for status in tweepy.Cursor(api.search, q=user_input.get() + ' -filter:retweets', tweet_mode='extended',
                                result_type='mixed').items(20):
        # Clean up emoji and other invalid characters
        valid_text = status.full_text
        valid_text = ''.join(c for c in valid_text if c <= '\uFFFF')

        # Checks if there was anything changed
        if cleanup(valid_text) != valid_text:
            # print(cleanup(valid_text) + '\n' + '------------------------------------------' + '\n')
            original_text.insert('end', valid_text + '\n' + '------------------------------------------' + '\n')
            new_text.insert('end', cleanup(valid_text) + '\n' + '------------------------------------------' + '\n')
    original_text.insert('end', 'Sorry, no tweets were immediately found matching that term')


# TODO Make this prettier,
# TODO Maybe output into a grid
# TODO Make both outputs scroll at the same time
# Set up window
window = tk.Tk()
input_frame = tk.Frame(window)
input_frame.pack()
original_text = tk.Text()
new_text = tk.Text()
input_label = tk.Label(input_frame, height=1, text="Search term or post URL")
input_label.pack(side=tk.LEFT)
user_input = tk.Entry(input_frame)
# user_input.config(wrap="none")
user_input.pack(side=tk.LEFT)
user_input.bind('<Return>', run_tweets)
button_run = tk.Button(input_frame, text="Search", command=run_tweets)
button_run.pack(side=tk.RIGHT)

original_text.pack(side=tk.LEFT)
new_text.pack(side=tk.RIGHT)
window.mainloop()

import re

# Clear hashtags
'''
def clearhash(tweet):
    tweet = re.sub('@.*([ ])', '', tweet)
    return tweet
'''


def cleanup(tweet):
    # politics
    tweet = re.sub(r'(republican|republicans|repubs|GOP|the right)', 'silly willies', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(democrat|democrats|dems|the left|leftist)', 'teletubbies', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(\belection|elections|reelection|re-election)', 'big ol party', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(president|presidency)', 'cool dude', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(\bimpeach\b)', 'hug', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(impeached)', 'tickled', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(vote)', 'dance', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(voting)', 'dancing', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(maga\b)', 'friendship', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(rigged)', 'wonderful', tweet, flags=re.IGNORECASE)

    tweet = re.sub(r'(trump)', 'Duck', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(biden)', 'Bro', tweet, flags=re.IGNORECASE)

    tweet = re.sub(r'(coronavirus|covid-19|covid19|\bvirus\b)', 'snuffles', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(dead)', 'sleeping', tweet, flags=re.IGNORECASE)
    # badwords
    tweet = re.sub(r'(idiot|idiots|morons|dumbass|dumbasses)', 'goobers', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(\bhell\b)', 'heckin heck', tweet, flags=re.IGNORECASE)

    return tweet

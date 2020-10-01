import re

# Holds the dictionary of words to change
def cleanup(tweet):
    # politics
    tweet = re.sub(r'(republicans|repubs|GOP|the right)', 'silly willies', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(republican|conservative)', 'clown', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(democrats|dems|the left|leftist)', 'teletubbies', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(democrat|liberal)', 'mime', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(\belection|elections|reelection|re-election)', 'big ol party', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(president|presidency)', 'cool dude', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(\bimpeach\b)', 'hug', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(impeached)', 'tickled', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(vote)', 'dance', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(voting)', 'dancing', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(maga\b)', 'friendship', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(rigged)', 'wonderful', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(blm|black lives matter)', 'free icecream for everyone', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(white supremacists)', 'pineapple pizza-eaters', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(white supremacist|racist|sexist)', 'pineapple pizza-eater', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(white supremacy|racism|sexism)', 'pineapple pizza-eating', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(\bcorrupt\b)', 'smelly', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(corruption)', 'tomfoolery', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(antifa)', 'fairies', tweet, flags=re.IGNORECASE)

    tweet = re.sub(r'(trump)', 'Duck', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(biden)', 'Bro', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(obama)', 'banana', tweet, flags=re.IGNORECASE)

    tweet = re.sub(r'(coronavirus|covid-19|covid19|\bvirus\b|plague)', 'snuffles', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(dead)', 'sleeping', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(deaths)', 'sneezes', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(kill)', 'encourage', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(terrorists)', 'goblins', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(terrorism)', 'candy-stealing', tweet, flags=re.IGNORECASE)


    # badwords
    tweet = re.sub(r'(idiot|idiots|morons|dumbass|dumbasses|losers)', 'goobers', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(\bhell\b)', 'heckin heck', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(\bass\b|asshole)', 'bum', tweet, flags=re.IGNORECASE)
    tweet = re.sub(r'(dick)', 'stick', tweet, flags=re.IGNORECASE)

    # & symbol since it comes in as &amp:
    tweet = re.sub(r'(&amp;)', '&', tweet, flags=re.IGNORECASE)
    return tweet

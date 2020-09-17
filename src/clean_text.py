import numpy as np 
import pandas as pd 
import re

tweet_corpus = []

def abstract_tweets(df):
    '''Create list of tweets from DF 'content' field'''
    for i in range(len(df)):
        tweet_corpus.append(df['content'][i])
    return tweet_corpus


regex_url = '(http:\/\/([\/]*[\w|-]*[.|\/][\w]*)+)'
regex_splitter = '(.+)\(..:.+\)'
url_cleaned_tweet_corpus = []

def clean_tweets(tweets):
    '''Take in a corpus of words and removes URL'''
    for tweet in tweet_corpus:
        new_tweet_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet)
        url_cleaned_tweet_corpus.append(new_tweet_string)

    return url_cleaned_tweet_corpus


header_list = ['President Donald Trump: ', 'Donald Trump: ', 'President Donald J. Trump: ', 'President Trump: ',]

speeches_filepath_list = ['data/speeches/atlanta.txt', 'data/speeches/battle_creek.txt',
                          'data/speeches/charleston.txt', 'data/speeches/charlotte.txt',
                          'data/speeches/china.txt', 'data/speeches/cincinati.txt',
                          'data/speeches/citydeploy.txt', 'data/speeches/colorado_springs.txt',
                          'data/speeches/dallas.txt', 'data/speeches/diabetes.txt',
                          'data/speeches/environment.txt', 'data/speeches/farmers.txt',
                          'data/speeches/ford.txt', 'data/speeches/fourthofjuly.txt',
                          'data/speeches/governors.txt', 'data/speeches/houston_modi.txt',
                          'data/speeches/ice.txt', 'data/speeches/iowa.txt',
                          'data/speeches/iran.txt', 'data/speeches/israel.txt',
                          'data/speeches/jamestown.txt', 'data/speeches/kentucky.txt',
                          'data/speeches/Las_vegas.txt', 'data/speeches/marchforlife.txt',
                          'data/speeches/memorial.txt', 'data/speeches/michigan.txt',
                          'data/speeches/michigan2.txt', 'data/speeches/milwaukee.txt',
                          'data/speeches/minneapolis.txt', 'data/speeches/mississippi.txt',
                          'data/speeches/nasa.txt', 'data/speeches/new_hampshire.txt',
                          'data/speeches/new_jersey.txt', 'data/speeches/new_mexico.txt',
                          'data/speeches/north_carolina.txt', 'data/speeches/oklahoma_tulsa.txt',
                          'data/speeches/pennsylvania.txt', 'data/speeches/pennsylvania2.txt',
                          'data/speeches/prayerbreakfast.txt', 'data/speeches/raid.txt',
                          'data/speeches/rnc.txt', 'data/speeches/rushmore.txt',
                          'data/speeches/shootings.txt', 'data/speeches/stateofunion.txt',
                          'data/speeches/teens.txt', 'data/speeches/toledo.txt',
                          'data/speeches/veterans.txt', 'data/speeches/westpoint.txt',
                          'data/speeches/Yuma.txt']


corona_briefing_filepath_list = ['data/corona_briefings/corona1.txt','data/corona_briefings/corona2.txt',
                                'data/corona_briefings/corona3.txt', 'data/corona_briefings/corona4.txt',
                                'data/corona_briefings/corona5.txt', 'data/corona_briefings/corona6.txt',
                                'data/corona_briefings/corona7.txt', 'data/corona_briefings/corona8.txt',
                                'data/corona_briefings/corona9.txt', 'data/corona_briefings/corona10.txt',
                                'data/corona_briefings/corona11.txt', 'data/corona_briefings/corona12.txt',
                                'data/corona_briefings/corona13.txt', 'data/corona_briefings/corona14.txt',
                                'data/corona_briefings/corona15.txt', 'data/corona_briefings/corona16.txt',
                                'data/corona_briefings/corona17.txt', 'data/corona_briefings/corona18.txt',
                                'data/corona_briefings/corona19.txt', 'data/corona_briefings/corona20.txt',
                                'data/corona_briefings/corona21.txt', 'data/corona_briefings/corona22.txt',
                                'data/corona_briefings/corona23.txt', 'data/corona_briefings/corona24.txt',
                                'data/corona_briefings/corona25.txt', 'data/corona_briefings/corona26.txt',
                                'data/corona_briefings/corona27.txt', 'data/corona_briefings/corona28.txt',
                                'data/corona_briefings/corona29.txt', 'data/corona_briefings/corona30.txt',
                                'data/corona_briefings/corona31.txt', 'data/corona_briefings/corona32.txt',
                                'data/corona_briefings/corona33.txt', 'data/corona_briefings/corona34.txt',
                                'data/corona_briefings/corona35.txt', 'data/corona_briefings/corona36.txt',
                                'data/corona_briefings/corona37.txt', 'data/corona_briefings/corona38.txt',
                                'data/corona_briefings/corona39.txt', 'data/corona_briefings/corona40.txt',
                                'data/corona_briefings/corona41.txt', 'data/corona_briefings/corona42.txt',
                                'data/corona_briefings/corona43.txt', 'data/corona_briefings/corona44.txt',
                                'data/corona_briefings/corona45.txt', 'data/corona_briefings/corona46.txt',
                                'data/corona_briefings/corona47.txt', 'data/corona_briefings/corona48.txt',
                                'data/corona_briefings/corona49.txt', 'data/corona_briefings/corona50.txt']

trump_text_only_corona_briefing_dict = {}
trump_text_only_speeches_dict = {}


def abstract_trump_talk(file_path_list, dict):
    '''Takes in files with multiple speakers and abstracts Trumps lines'''
    for file in file_path_list:
        with open(file, "r") as f:
            text_str = ''.join(f.readlines())
            split_content = re.split(regex_splitter, text_str)
            trump_text_only = []
            for idx, item in enumerate(split_content):
                if item in header_list:
                    trump_text_only.append(split_content[idx+1])
                else:
                    pass
            dict[file] = trump_text_only
    return dict


corona_briefing_corpus = [] 

def create_corpus(dict, list_):
    ''' Turns dictionary into corpus list'''
    for value in dict.values():
        for sent in value:
            list_.append(sent)
    return list_
        


def combine_corpus():
    